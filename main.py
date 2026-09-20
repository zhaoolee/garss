import time
import os
import re
import json
import shutil
import email.utils
import calendar
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from urllib.parse import quote, urljoin, urlparse
from zoneinfo import ZoneInfo
from multiprocessing import Pool,  Manager

try:
    import feedparser
except ImportError:
    feedparser = None

try:
    import markdown
except ImportError:
    markdown = None

try:
    import requests
except ImportError:
    requests = None

try:
    import yagmail
except ImportError:
    yagmail = None


GARSS_STUDIO_ACCESS_TOKEN = ""
SHANGHAI_TZ = ZoneInfo("Asia/Shanghai")
RECENT_WINDOW_SECONDS = 24 * 60 * 60


def get_garss_studio_base_url():
    return os.environ.get("GARSS_STUDIO_BASE_URL", "http://127.0.0.1:25173").rstrip("/")


def get_garss_studio_access_code():
    return os.environ.get("GARSS_STUDIO_ACCESS_CODE") or os.environ.get("ACCESS_CODE") or "banana"


def is_garss_studio_rsshub_url(feed_url):
    parse_result = urlparse(feed_url)
    return parse_result.scheme in ["http", "https"] and parse_result.netloc in ["rsshub:1200", "rsshub.v2fy.com"]


def get_rsshub_route_path(feed_url):
    parse_result = urlparse(feed_url)
    route_path = parse_result.path or "/"

    if parse_result.query:
        route_path = route_path + "?" + parse_result.query

    return route_path


def get_garss_studio_access_token():
    global GARSS_STUDIO_ACCESS_TOKEN

    if GARSS_STUDIO_ACCESS_TOKEN:
        return GARSS_STUDIO_ACCESS_TOKEN

    login_url = urljoin(get_garss_studio_base_url() + "/", "api/auth/login")
    response_data = http_post_json(login_url, {"accessCode": get_garss_studio_access_code()}, 8)
    GARSS_STUDIO_ACCESS_TOKEN = response_data["token"]
    return GARSS_STUDIO_ACCESS_TOKEN


def http_get_content(url, timeout, headers):
    if requests:
        response = requests.get(url, timeout=timeout, headers=headers)
        response.raise_for_status()
        return response.content

    request = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def http_post_json(url, body, timeout):
    encoded_body = json.dumps(body).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=encoded_body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def get_feed_url_content(feed_url, timeout, headers):
    if not is_garss_studio_rsshub_url(feed_url):
        return http_get_content(feed_url, timeout, headers)

    route_path = get_rsshub_route_path(feed_url)
    fetch_url = urljoin(get_garss_studio_base_url() + "/", "api/rsshub/fetch") + "?routePath=" + quote(route_path, safe="")
    return http_get_content(
        fetch_url,
        timeout,
        {
            **headers,
            "Authorization": "Bearer " + get_garss_studio_access_token(),
        },
    )


def parse_entry_datetime(value="", parsed_time=None):
    """Return an aware datetime without inventing a date when a feed omits one."""
    parsed_date = None

    if value:
        try:
            parsed_date = email.utils.parsedate_to_datetime(value)
        except (TypeError, ValueError):
            try:
                parsed_date = datetime.fromisoformat(value.replace("Z", "+00:00"))
            except (TypeError, ValueError):
                pass

    if parsed_date is None and parsed_time:
        try:
            parsed_date = datetime.fromtimestamp(calendar.timegm(parsed_time), ZoneInfo("UTC"))
        except (TypeError, ValueError, OverflowError):
            pass

    if parsed_date is None:
        return None
    if parsed_date.tzinfo is None:
        parsed_date = parsed_date.replace(tzinfo=ZoneInfo("UTC"))
    return parsed_date.astimezone(SHANGHAI_TZ)


def make_feed_entry(title, link, published="", parsed_time=None):
    published_at = parse_entry_datetime(published, parsed_time)
    return {
        "title": title or "",
        "link": link or "",
        "date": published_at.strftime("%Y-%m-%d") if published_at else "",
        "published_at": published_at.isoformat() if published_at else "",
    }


def is_recent_entry(entry, now=None):
    now = now or datetime.now(SHANGHAI_TZ)
    published_at = parse_entry_datetime(entry.get("published_at", ""))
    if published_at is None:
        return False
    age_seconds = (now - published_at).total_seconds()
    return -300 <= age_seconds <= RECENT_WINDOW_SECONDS


def get_entry_dedup_key(entry):
    link = (entry.get("link") or "").strip().rstrip("/")
    if link:
        return "link:" + link
    title = re.sub(r"\s+", " ", (entry.get("title") or "").strip().lower())
    return "title:" + title if title else ""


def parse_feed_entries_with_stdlib(feed_url_content):
    root = ET.fromstring(feed_url_content)
    entries = []

    if root.tag.endswith("rss") or root.find("./channel") is not None:
        for item in root.findall("./channel/item"):
            title = item.findtext("title", default="")
            link = item.findtext("link", default="")
            published = item.findtext("pubDate", default="") or item.findtext("date", default="")
            entries.append(make_feed_entry(title, link, published))
        return entries

    namespaces = {"atom": "http://www.w3.org/2005/Atom"}
    for entry in root.findall("./atom:entry", namespaces):
        title = entry.findtext("atom:title", default="", namespaces=namespaces)
        link_element = entry.find("atom:link", namespaces)
        link = link_element.get("href", "") if link_element is not None else ""
        published = entry.findtext("atom:published", default="", namespaces=namespaces) or entry.findtext(
            "atom:updated",
            default="",
            namespaces=namespaces,
        )
        entries.append(make_feed_entry(title, link, published))

    return entries


def parse_feed_entries(feed_url_content):
    if not feedparser:
        return parse_feed_entries_with_stdlib(feed_url_content)

    feed = feedparser.parse(feed_url_content)
    feed_entries = feed["entries"]
    result = []

    for entry in feed_entries:
        published = entry.get("published") or entry.get("updated") or ""
        parsed_time = entry.get("published_parsed") or entry.get("updated_parsed")
        result.append(make_feed_entry(entry.get("title", ""), entry.get("link", ""), published, parsed_time))

    return result


def get_rss_info(feed_url, index, rss_info_list):
    result = {"result": []}
    request_success = False
    # 如果请求出错，则重新请求，最多三次
    for i in range(3):
        if(request_success == False):
            try:
                headers = {
                    # 设置用户代理头(为狼披上羊皮)
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
                    "Content-Encoding": "gzip"
                }
                # 三次分别设置8, 16, 24秒钟超时
                feed_url_content = get_feed_url_content(feed_url, (i+1)*8, headers)
                feed_entries = parse_feed_entries(feed_url_content)
                feed_entries_length = len(feed_entries)
                print("==feed_url=>>", feed_url, "==len=>>", feed_entries_length)
                for entrie in feed_entries:
                    title = entrie["title"]
                    link = entrie["link"]
                    date = entrie["date"]
                    published_at = entrie["published_at"]

                    title = title.replace("\n", "")
                    title = title.replace("\r", "")

                    result["result"].append({
                        "title": title,
                        "link": link,
                        "date": date,
                        "published_at": published_at,
                    })
                request_success = True
            except Exception as e:
                print(feed_url+"第+"+str(i)+"+次请求出错==>>",e)
                pass
        else:
            pass

    rss_info_list[index] = result["result"]
    print("本次爬取==》》", feed_url, "<<<===", index, result["result"])
    # 剩余数量
    remaining_amount = 0

    for tmp_rss_info_atom in rss_info_list:
        if(isinstance(tmp_rss_info_atom, int)):
            remaining_amount = remaining_amount + 1
            
    print("当前进度 | 剩余数量", remaining_amount, "已完成==>>", len(rss_info_list)-remaining_amount)
    return result["result"]
    


def send_mail(email, title, contents):
    if os.environ.get("GARSS_SKIP_MAIL", "") == "1":
        print("已设置 GARSS_SKIP_MAIL=1，跳过邮件发送")
        return

    if not yagmail:
        print("当前环境没有 yagmail，跳过邮件发送")
        return

    # 判断secret.json是否存在
    user = ""
    password = ""
    host = ""
    try:
        if(os.environ["USER"]):
            user = os.environ["USER"]
        if(os.environ["PASSWORD"]):
            password = os.environ["PASSWORD"]
        if(os.environ["HOST"]):
            host = os.environ["HOST"]
    except:
        print("无法获取github的secrets配置信息,开始使用本地变量")
        if(os.path.exists(os.path.join(os.getcwd(),"secret.json"))):
            with open(os.path.join(os.getcwd(),"secret.json"),'r') as load_f:
                load_dict = json.load(load_f)
                user = load_dict["user"]
                password = load_dict["password"]
                host = load_dict["host"]
                # print(load_dict)
        else:
            print("无法获取发件人信息")
    
    # 连接邮箱服务器
    # yag = yagmail.SMTP(user=user, password=password, host=host)
    yag = yagmail.SMTP(user = user, password = password, host=host)
    # 发送邮件
    yag.send(email, title, contents)

def replace_readme():
    new_edit_readme_md = ["", ""]
    current_date_news_index = [""]


    
    # 读取EditREADME.md
    print("replace_readme")
    new_num = 0
    recent_article_keys = set()
    generated_at = datetime.now(SHANGHAI_TZ)
    with open(os.path.join(os.getcwd(),"EditREADME.md"),'r') as load_f:
        edit_readme_md = load_f.read();



        new_edit_readme_md[0] = edit_readme_md
        before_info_list =  re.findall(r'\{\{latest_content\}\}.*\[订阅地址\]\(.*\)' ,edit_readme_md);
        # 填充统计RSS数量
        new_edit_readme_md[0] = new_edit_readme_md[0].replace("{{rss_num}}", str(len(before_info_list)))
        # 填充统计时间
        ga_rss_datetime = generated_at.strftime('%Y-%m-%d %H:%M:%S')
        new_edit_readme_md[0] = new_edit_readme_md[0].replace("{{ga_rss_datetime}}", str(ga_rss_datetime))

        # 使用进程池进行数据获取，获得rss_info_list
        before_info_list_len = len(before_info_list)
        rss_info_list = Manager().list(range(before_info_list_len))
        print('初始化完毕==》', rss_info_list)

        

        # 创建一个最多开启8进程的进程池
        po = Pool(8)

        for index, before_info in enumerate(before_info_list):
            # 获取link
            link = re.findall(r'\[订阅地址\]\((.*)\)', before_info)[0]
            po.apply_async(get_rss_info,(link, index, rss_info_list))


        # 关闭进程池,不再接收新的任务,开始执行任务
        po.close()

        # 主进程等待所有子进程结束
        po.join()
        print("----结束----", rss_info_list)


        for index, before_info in enumerate(before_info_list):
            # 获取link
            link = re.findall(r'\[订阅地址\]\((.*)\)', before_info)[0]
            # 生成超链接
            rss_info = rss_info_list[index]
            latest_content = ""
            parse_result = urlparse(link)
            scheme_netloc_url = str(parse_result.scheme)+"://"+str(parse_result.netloc)
            latest_content = "[暂无法通过爬虫获取信息, 点击进入源网站主页]("+ scheme_netloc_url +")"

            # 加入到索引
            try:
                for rss_info_atom in rss_info:
                    dedup_key = get_entry_dedup_key(rss_info_atom)
                    if is_recent_entry(rss_info_atom, generated_at) and dedup_key and dedup_key not in recent_article_keys:
                        recent_article_keys.add(dedup_key)
                        new_num = new_num + 1
                        if (new_num % 2) == 0:
                            current_date_news_index[0] = current_date_news_index[0] + "<div style='line-height:3;' ><a href='" + rss_info_atom["link"] + "' " + 'style="line-height:2;text-decoration:none;display:block;color:#584D49;">' + "🌈 ‣ " + rss_info_atom["title"] + " | 第" + str(new_num) +"篇" + "</a></div>"
                        else:
                            current_date_news_index[0] = current_date_news_index[0] + "<div style='line-height:3;background-color:#FAF6EA;' ><a href='" + rss_info_atom["link"] + "' " + 'style="line-height:2;text-decoration:none;display:block;color:#584D49;">' + "🌈 ‣ " + rss_info_atom["title"] + " | 第" + str(new_num) +"篇" + "</a></div>"

            except:
                print("An exception occurred")
            

                
            if(len(rss_info) > 0):
                rss_info[0]["title"] = rss_info[0]["title"].replace("|", "\|")
                rss_info[0]["title"] = rss_info[0]["title"].replace("[", "\[")
                rss_info[0]["title"] = rss_info[0]["title"].replace("]", "\]")

                latest_date = rss_info[0]["date"] or "日期未知"
                latest_content = "[" + "‣ " + rss_info[0]["title"] + ( " 🌈 " + latest_date if is_recent_entry(rss_info[0], generated_at) else " \| " + latest_date ) +"](" + rss_info[0]["link"] + ")"

            if(len(rss_info) > 1):
                rss_info[1]["title"] = rss_info[1]["title"].replace("|", "\|")
                rss_info[1]["title"] = rss_info[1]["title"].replace("[", "\[")
                rss_info[1]["title"] = rss_info[1]["title"].replace("]", "\]")

                second_date = rss_info[1]["date"] or "日期未知"
                latest_content = latest_content + "<br/>[" + "‣ " +  rss_info[1]["title"] + ( " 🌈 " + second_date if is_recent_entry(rss_info[1], generated_at) else " \| " + second_date ) +"](" + rss_info[1]["link"] + ")"

            # 生成after_info
            after_info = before_info.replace("{{latest_content}}", latest_content)
            print("====latest_content==>", latest_content)
            # 替换edit_readme_md中的内容
            new_edit_readme_md[0] = new_edit_readme_md[0].replace(before_info, after_info)
    
    # 替换EditREADME中的索引
    new_edit_readme_md[0] = new_edit_readme_md[0].replace("{{news}}", current_date_news_index[0])
    # 替换EditREADME中的新文章数量索引
    new_edit_readme_md[0] = new_edit_readme_md[0].replace("{{new_num}}", str(new_num))
    # 添加CDN
    new_edit_readme_md[0] = new_edit_readme_md[0].replace("./_media", "https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media")
        
    # 将新内容
    with open(os.path.join(os.getcwd(),"README.md"),'w') as load_f:
        load_f.write(new_edit_readme_md[0])
    

    mail_re = r'邮件内容区开始>([.\S\s]*)<邮件内容区结束'
    reResult = re.findall(mail_re, new_edit_readme_md[0])
    new_edit_readme_md[1] = reResult

    
    return new_edit_readme_md

# 将README.md复制到docs中

def cp_readme_md_to_docs():
    shutil.copyfile(os.path.join(os.getcwd(),"README.md"), os.path.join(os.getcwd(), "docs","README.md"))
    
def cp_media_to_docs():
    if os.path.exists(os.path.join(os.getcwd(), "docs","_media")):
        shutil.rmtree(os.path.join(os.getcwd(), "docs","_media"))	
    shutil.copytree(os.path.join(os.getcwd(),"_media"), os.path.join(os.getcwd(), "docs","_media"))

def get_email_list():
    email_list = []
    with open(os.path.join(os.getcwd(),"tasks.json"),'r') as load_f:
        load_dic = json.load(load_f)
        for task in load_dic["tasks"]:
            email_list.append(task["email"])
    return email_list

# 创建opml订阅文件

def create_opml():

    result = "";
    result_v1 = "";

    # <outline text="CNET News.com" description="Tech news and business reports by CNET News.com. Focused on information technology, core topics include computers, hardware, software, networking, and Internet media." htmlUrl="http://news.com.com/" language="unknown" title="CNET News.com" type="rss" version="RSS2" xmlUrl="http://news.com.com/2547-1_3-0-5.xml"/>

    with open(os.path.join(os.getcwd(),"EditREADME.md"),'r') as load_f:
        edit_readme_md = load_f.read();

        ## 将信息填充到opml_info_list
        opml_info_text_list =  re.findall(r'.*\{\{latest_content\}\}.*\[订阅地址\]\(.*\).*' ,edit_readme_md);

        for opml_info_text in opml_info_text_list:


            # print('==', opml_info_text)

            opml_info_text_format_data = re.match(r'\|(.*)\|(.*)\|(.*)\|(.*)\|.*\[订阅地址\]\((.*)\).*\|',opml_info_text)

            # print("data==>>", opml_info_text_format_data)

            # print("总信息", opml_info_text_format_data[0].strip())
            # print("编号==>>", opml_info_text_format_data[1].strip())
            # print("text==>>", opml_info_text_format_data[2].strip())
            # print("description==>>", opml_info_text_format_data[3].strip())
            # print("data004==>>", opml_info_text_format_data[4].strip())
            print('##',opml_info_text_format_data[2].strip())
            print(opml_info_text_format_data[3].strip())
            print(opml_info_text_format_data[5].strip())
            

            opml_info = {}
            opml_info["text"] = opml_info_text_format_data[2].strip()
            opml_info["description"] = opml_info_text_format_data[3].strip()
            opml_info["htmlUrl"] = opml_info_text_format_data[5].strip()
            opml_info["title"] = opml_info_text_format_data[2].strip()
            opml_info["xmlUrl"] = opml_info_text_format_data[5].strip()

            # print('opml_info==>>', opml_info);
            


            opml_info_text = '<outline  text="{text}" description="{description}" htmlUrl="{htmlUrl}" language="unknown" title="{title}" type="rss" version="RSS2" xmlUrl="{xmlUrl}"/>'

            opml_info_text_v1 = '      <outline text="{title}" title="{title}" type="rss"  \n            xmlUrl="{xmlUrl}" htmlUrl="{htmlUrl}"/>'

            opml_info_text =  opml_info_text.format(
                text=opml_info["text"], 
                description=opml_info["description"], 
                htmlUrl = opml_info["htmlUrl"],
                title=opml_info["title"],
                xmlUrl=opml_info["xmlUrl"]
            )

            opml_info_text_v1 =  opml_info_text_v1.format(
                htmlUrl = opml_info["htmlUrl"],
                title=opml_info["title"],
                xmlUrl=opml_info["xmlUrl"]
            )

            result = result + opml_info_text + "\n"

            result_v1 = result_v1 + opml_info_text_v1 + "\n"
    
    zhaoolee_github_garss_subscription_list = "";
    with open(os.path.join(os.getcwd(),"rss-template-v2.txt"),'r') as load_f:
        zhaoolee_github_garss_subscription_list_template = load_f.read();
        GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
        date_created = datetime.utcnow().strftime(GMT_FORMAT);
        date_modified = datetime.utcnow().strftime(GMT_FORMAT);
        zhaoolee_github_garss_subscription_list = zhaoolee_github_garss_subscription_list_template.format(result=result, date_created=date_created, date_modified=date_modified);
        # print(zhaoolee_github_garss_subscription_list);

    # 将内容写入
    with open(os.path.join(os.getcwd(),"zhaoolee_github_garss_subscription_list_v2.opml"),'w') as load_f:
        load_f.write(zhaoolee_github_garss_subscription_list)

    zhaoolee_github_garss_subscription_list_v1 = ""
    with open(os.path.join(os.getcwd(),"rss-template-v1.txt"),'r') as load_f:
        zhaoolee_github_garss_subscription_list_template = load_f.read();
        zhaoolee_github_garss_subscription_list_v1 = zhaoolee_github_garss_subscription_list_template.format(result=result_v1);
        # print(zhaoolee_github_garss_subscription_list_v1);

    # 将内容写入
    with open(os.path.join(os.getcwd(),"zhaoolee_github_garss_subscription_list_v1.opml"),'w') as load_f:
        load_f.write(zhaoolee_github_garss_subscription_list_v1)




        
    # print(result)

def create_json():
    result = {"garssInfo": []}
    with open(os.path.join(os.getcwd(),"EditREADME.md"),'r') as load_f:
        edit_readme_md = load_f.read();
        ## 将信息填充到opml_info_list
        opml_info_text_list =  re.findall(r'.*\{\{latest_content\}\}.*\[订阅地址\]\(.*\).*' ,edit_readme_md);
        for opml_info_text in opml_info_text_list:
            opml_info_text_format_data = re.match(r'\|(.*)\|(.*)\|(.*)\|(.*)\|.*\[订阅地址\]\((.*)\).*\|',opml_info_text)
            opml_info = {}
            opml_info["description"] = opml_info_text_format_data[3].strip()
            opml_info["title"] = opml_info_text_format_data[2].strip()
            opml_info["xmlUrl"] = opml_info_text_format_data[5].strip()
            result["garssInfo"].append(opml_info)
    with open("./garssInfo.json","w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

def main():
    create_json()
    create_opml()
    readme_md = replace_readme()
    content = markdown.markdown(readme_md[0], extensions=['tables', 'fenced_code']) if markdown else readme_md[0]
    email_list = get_email_list()

    mail_re = r'邮件内容区开始>([.\S\s]*)<邮件内容区结束'
    reResult = re.findall(mail_re, readme_md[0])

    try:
        send_mail(email_list, "嘎!RSS订阅", reResult)
    except Exception as e:
        print("==邮件设信息置错误===》》", e)


if __name__ == "__main__":
    main()
