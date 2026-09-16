# 《嘎!RSS》🐣为打破信息茧房而生, 让古老的RSS在AI时代再次伟大 Github Actions Rss (garss, 嘎RSS! 已收集281个RSS源, 生成时间: 2026-09-16 08:05:15)

信息茧房是指人们关注的信息领域会习惯性地被自己的兴趣所引导，从而将自己的生活桎梏于像蚕茧一般的「茧房」中的现象。

![](https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/ga-rss.png)

这个名为**嘎!RSS**的项目会利用免费的Github Actions服务, 提供一个内容全面的信息流, 让现代人的知识体系更广泛, 减弱信息茧房对现代人的影响, 让**非茧房信息流**造福人类~
[《嘎!RSS》永久开源页面: https://github.com/zhaoolee/garss](https://github.com/zhaoolee/garss)

## 适合谁

![](./EditREADME.assets/d1f1e682f729dd6ef337987999f0649e3b7272ca4ceae026ce524783cfdb92c3.png)


## 项目优势（米氏对比法）

| 项目  | garss |  新闻APP  |  商业化RSS工具 |
| --- | --- | --- | --- |
|  | ![](./EditREADME.assets/81c848887aae715af60abf018a7162da2dd04a638be84cdc2d6caf278a5d225b.gif) |  ![](./EditREADME.assets/70583b524a17989de539b0abcb82acc8a852cf822c36af6fdb781b12f393cf2e.png)  | ![](./EditREADME.assets/cd830e307ec2077063af97ca516ff18409c15c332689b008c6a146d4d71b48f1.png) |
| 不上传浏览记录  |   ✅  |  ❌  |  ✅  |
| 信息茧房  |   ❌  |  ✅   |  ✅  |
| 私有化部署  |   ✅  |  ❌  |  ❌   |
| 付费订阅  |   ❌ |  ✅   |  ✅    |
| 开放API  |   ✅  |  ❌   |  ❌    |
| 支持二次开发  |   ✅  |  ❌   |  ❌    |
| 代码开源  |   ✅  |  ❌   |  ❌   |
| 接入 AI Skill | ✅  |  ❌   |  ❌  |
| RSSHub社区支持 | ✅  |  ❌   |  ❌  |
| 广告插入  |   ❌ |  ✅   |  ✅    |
| URL看图增强 | ✅  |  ✅（需安装插件）   |  ❌  |
| 突破IP限制 | ✅  |  ❌  |  ❌  |
| Github Action抓取 | ✅  |  ❌  |  ❌  |


## 快速启动

## 快速启动和关闭

仓库根目录提供跨平台控制台入口：

| 平台 | 统一入口 |
| --- | --- |
| macOS | `GARSS-MACOS.command` |
| Linux | `GARSS-LINUX.sh` |
| Windows | `GARSS-WINDOWS.bat` |

双击后文件后，可选择启动、关闭、升级、查看状态或退出控制台。启动和升级会自动打开浏览器；关闭控制台窗口不会停止服务，只有选择“关闭”才会停止容器。

![](./EditREADME.assets/4a32e72cf86a22133683a74fc5d43c0508e76fe7401e01a5d82ceac582c9587d.png)

## 锤子便签风格的GARSS阅读器

- 首次启动

```
cd garss-studio
cp .env.example .env
docker compose -f docker-compose.dev.yml up --build
```

![](./EditREADME.assets/3296e8bba846baf1a9237db41dabc98d34c275f4739e81ff95c4bbf1cf46ebc4.png)

- 简单快速的分类阅读交互

![](./EditREADME.assets/81c848887aae715af60abf018a7162da2dd04a638be84cdc2d6caf278a5d225b.gif)

- 锤子便签风格的阅读体验

![](./EditREADME.assets/d343d47183e5514679102b11941468007747d8a82ddfaddf03841f176e497648.gif)

- 简单的订阅管理

![](./EditREADME.assets/917fe70142126e4fb1862b539b4b6da47ed52bc5a69fe3fe7549f920d8ddce28.png)

- 集成RSSHUB

![](./EditREADME.assets/df8266f29d5fb35e9ae8df54b216ca0d83bc48172b8ee755ca2cacf130a52cfc.png)


- 完善的二开文档

![](./EditREADME.assets/49e2a0713a83ae59b8ca5564aa55435d1eac47b898e9a3188a973a622fe85c10.png)

- AI SKILL支持

![](./EditREADME.assets/d6f2c60f6062dff2c4ea252c31b5547332ab69122aaf7788c37748ca24104b3d.gif)

![](./EditREADME.assets/2294b9387de7a633dbbb3aca7dfc7aad09eae624dbf53e3014dbbb3d8f4de5d5.png)

- 自动拉取，保证新闻时效

![](./EditREADME.assets/7f7c8f96cc5406b61a981fe0f9b62a4c6f496fca0feaa0bb95c0d059a2d3a46c.png)

- 常用页面

```
阅读页：http://127.0.0.1:25173/reader?pw=banana
订阅源：http://127.0.0.1:25173/sources?pw=banana
设置页：http://127.0.0.1:25173/settings?pw=banana
API 文档：http://127.0.0.1:25173/api/docs
```

CLAWHUB的SKILL调用GARSS后端：https://clawhub.ai/zhaoolee/garss-studio-rss-api

## 推荐使用什么软件订阅RSS？
我推荐一款免费的浏览器扩展程序Feedbro ，使用教程[Chrome插件英雄榜第96期《Feedbro》在Chrome中订阅RSS信息流](https://www.v2fy.com/p/096-feedbro-2021-02-27/)

## 主要功能
1. 收集RSS, 打造无广告内容优质的 **头版头条** 超赞新闻页
2. 利用Github Actions, 搜集全部RSS的头版头条新闻标题和超链接, 并自动更新到首页,当天最新发布的文章会出现🌈 标志

## 今日值得看 🕶️

邮件内容区开始>
<h2>新蒸熟23个小蛋糕🍰(文章) 生产时间 2026-09-16 08:05:15 保质期24小时</h2>

<div style='line-height:3;background-color:#FAF6EA;' ><a href='https://36kr.com/p/3985321952115717?f=rss' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ 8点1氪丨8月一线城市房价上涨；携程上架510万一张的太空旅行船票；字节跳动上半年净利润出现下滑，但海外收入占比再创新高 | 第1篇</a></div><div style='line-height:3;' ><a href='https://36kr.com/newsflashes/3985327791471369?f=rss' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ 24只高股息绩优股估值跌至历史底部，机构预期8股上涨空间超50% | 第2篇</a></div><div style='line-height:3;background-color:#FAF6EA;' ><a href='https://36kr.com/newsflashes/3985326027569926?f=rss' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ 贝森特支持向美国人发放5000美元支票的提议，称可以不影响财政赤字 | 第3篇</a></div><div style='line-height:3;' ><a href='https://36kr.com/newsflashes/3985323997985799?f=rss' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ OpenAI据报正与Anthropic、谷歌DeepMind合作推进AI安全 | 第4篇</a></div><div style='line-height:3;background-color:#FAF6EA;' ><a href='https://www.ainvest.com/news/current-mortgage-rates-hit-7-oil-prices-fed-hikes-push-yields-higher-2609/' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ Current Mortgage Rates Hit 7% As Oil Prices And Fed Hikes Push Yields Higher | 第5篇</a></div><div style='line-height:3;' ><a href='https://www.ainvest.com/news/rackspace-jumps-11-5-wall-street-stays-neutral-2609/' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ Rackspace Jumps 11.5% as Wall Street Stays Neutral | 第6篇</a></div><div style='line-height:3;background-color:#FAF6EA;' ><a href='https://www.ainvest.com/news/apecoin-ape-trades-0-13-apechain-arbos-51-upgrade-99-drawdown-finally-2609/' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ ApeCoin (APE) Trades Near $0.13 After ApeChain ArbOS 51 Upgrade -- Is the 99% Drawdown Finally Over? | 第7篇</a></div><div style='line-height:3;' ><a href='https://www.ainvest.com/news/binc-5-9-yield-cuts-stack-375k-credit-risk-pays-2609/' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ BINC's 5.9% Yield Cuts the Stack You Need by ~$375k. The Credit Risk Pays For It. | 第8篇</a></div><div style='line-height:3;background-color:#FAF6EA;' ><a href='https://www.ainvest.com/news/qcom-retook-zone-capped-2026-comeback-168-ai-bid-breaks-2609/' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ QCOM Just Retook the Zone That Capped Its 2026 Comeback—Below $168 the Whole AI Bid Breaks | 第9篇</a></div><div style='line-height:3;' ><a href='https://www.ainvest.com/news/apecoin-ape-trading-time-0-13-catalyst-sight-2609/' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ ApeCoin (APE) | Trading Near All-Time Low at $0.13 -- Is There a Catalyst in Sight? | 第10篇</a></div><div style='line-height:3;background-color:#FAF6EA;' ><a href='https://www.ainvest.com/news/current-mortgage-rates-hit-7-oil-prices-fed-hikes-push-yields-higher-2609/' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ Current Mortgage Rates Hit 7% As Oil Prices And Fed Hikes Push Yields Higher | 第11篇</a></div><div style='line-height:3;' ><a href='https://www.ainvest.com/news/rackspace-jumps-11-5-wall-street-stays-neutral-2609/' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ Rackspace Jumps 11.5% as Wall Street Stays Neutral | 第12篇</a></div><div style='line-height:3;background-color:#FAF6EA;' ><a href='https://www.ainvest.com/news/apecoin-ape-trades-0-13-apechain-arbos-51-upgrade-99-drawdown-finally-2609/' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ ApeCoin (APE) Trades Near $0.13 After ApeChain ArbOS 51 Upgrade -- Is the 99% Drawdown Finally Over? | 第13篇</a></div><div style='line-height:3;' ><a href='https://www.ainvest.com/news/binc-5-9-yield-cuts-stack-375k-credit-risk-pays-2609/' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ BINC's 5.9% Yield Cuts the Stack You Need by ~$375k. The Credit Risk Pays For It. | 第14篇</a></div><div style='line-height:3;background-color:#FAF6EA;' ><a href='https://www.ainvest.com/news/video-jacobsen-tentative-rate-hike-symbolism-substance-2609/' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ Jacobsen: Tentative Rate Hike About "Symbolism" Over "Substance" | 第15篇</a></div><div style='line-height:3;' ><a href='https://www.ainvest.com/news/video-swarmer-swmr-president-ratel-robotics-acquisition-saving-lives-combat-2609/' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ Swarmer (SWMR) President on Ratel Robotics Acquisition, Saving Lives in Combat | 第16篇</a></div><div style='line-height:3;background-color:#FAF6EA;' ><a href='https://www.ainvest.com/news/qcom-retook-zone-capped-2026-comeback-168-ai-bid-breaks-2609/' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ QCOM Just Retook the Zone That Capped Its 2026 Comeback—Below $168 the Whole AI Bid Breaks | 第17篇</a></div><div style='line-height:3;' ><a href='https://www.ainvest.com/news/apecoin-ape-trading-time-0-13-catalyst-sight-2609/' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ ApeCoin (APE) | Trading Near All-Time Low at $0.13 -- Is There a Catalyst in Sight? | 第18篇</a></div><div style='line-height:3;background-color:#FAF6EA;' ><a href='https://www.infoq.cn/article/foEzSr8xfG0STQ1wgbti' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ 129亿美元卖身英伟达之后，是时候重新理解Hugging Face了 | 第19篇</a></div><div style='line-height:3;' ><a href='https://event.baai.ac.cn/activities/1084' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ 实现个人电脑Token自由，端侧推理引擎 FreeToken | 第20篇</a></div><div style='line-height:3;background-color:#FAF6EA;' ><a href='https://www.ithome.com/1/002/850.htm' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ EA《双人成行》10 月 15 日登陆任天堂 Switch 2：新增好友通行证跨平台功能，部分地区老玩家可免费升级 | 第21篇</a></div><div style='line-height:3;' ><a href='https://www.ithome.com/1/002/849.htm' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ 苹果 M6 Mac mini 跑分曝光：单核较 M4 款高 24%、多核高 48% | 第22篇</a></div><div style='line-height:3;background-color:#FAF6EA;' ><a href='https://www.nodeseek.com/post-930980-1' style="line-height:2;text-decoration:none;display:block;color:#584D49;">🌈 ‣ 内存要涨到什么时候噶 | 第23篇</a></div>

<邮件内容区结束

## 已收集RSS列表

| 编号 | 名称 | 描述 | RSS  |  最新内容 |
| --- | --- | --- | --- |  --- |
| <h2 id="软件工具">软件工具</h2> |  |   |  |
| <div id="S001" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/S001.png" width="30px" style="width:30px;height: auto;"/><br><span>S001</span></div> |  不死鸟 | 不死鸟:专注分享优质资源 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://iao.su) |  [订阅地址](https://iao.su/feed) | 
| <div id="S002" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/S002.png" width="30px" style="width:30px;height: auto;"/><br><span>S002</span></div> | 精品MAC应用分享 | 精品MAC应用分享，每天分享大量mac软件，为您提供优质的mac软件,免费软件下载服务 |  [‣ Things 3.24.0 一款优秀的GTD任务管理工具 \| 2026-09-15](https://xclient.info/s/things.html)<br/>[‣ System Dashboard Pro 4.3.1 系统监测 \| 2026-09-15](https://xclient.info/s/system-dashboard-pro.html) | [订阅地址](https://xclient.info/feed) | 
| <div id="S003" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/S003.png" width="30px" style="width:30px;height: auto;"/><br><span>S003</span></div> | 老殁 | 免费推荐优秀软件 |  [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.mpyit.com) | [订阅地址](https://www.mpyit.com/feed) |
| <div id="S004" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/S004.png" width="30px" style="width:30px;height: auto;"/><br><span>S004</span></div> | 鹏少资源网 | 专注于精品软件收录分享 |   [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.jokerps.com) | [订阅地址](https://www.jokerps.com/feed) |
| <div id="S005" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/S005.png" width="30px" style="width:30px;height: auto;"/><br><span>S005</span></div> | 小众软件 | 分享免费、小巧、实用、有趣、绿色的软件 | [‣ 高性价比（廉价）SSD VPS 提供商 CloudCone，最低 96 元人民币/年｜再次补货 \| 2026-09-15](https://www.appinn.com/cloudcone-ssd-vps/)<br/>[‣ 限免：DearMob iPhone Manager – iPhone/iPad 照片、视频传输，应用安装、整机备份恢复、换机工具\[Win/macOS\] \| 2026-09-15](https://www.appinn.com/5kplayer-iphone-manager/) | [订阅地址](https://www.appinn.com/feed/) | 
| <div id="S006" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/S006.png" width="30px" style="width:30px;height: auto;"/><br><span>S006</span></div> | 懒得勤快的博客 | 懒得勤快，互联网分享精神，勤于发现，乐于分享 |  [暂无法通过爬虫获取信息, 点击进入源网站主页](https://masuit.com) | [订阅地址](https://masuit.com/rss) |
| <div id="S007" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/S007.png" width="30px" style="width:30px;height: auto;"/><br><span>S007</span></div> | 反斗限免 | 反斗软件旗下软件限免资讯网站 |  [‣ 限时免费获取育碧游戏 For Honor Standard Edition 荣耀战魂标准版\[Windows\]\[￥148→0\] \| 2026-09-15](https://free.apprcn.com/limited-time-get-ubisoft-game-for-honor-standard-edition-for-free/)<br/>[‣ Geekersoft Video Converter - 视频格式转换工具\[1年授权\]\[Windows\]\[$29.99→0\] \| 2026-09-15](https://free.apprcn.com/geekersoft-video-converter-5/) | [订阅地址](https://free.apprcn.com/feed/) | 
| S008 | 异次元软件世界  | 极具人气和特色的软件网站！专注于推荐优秀软件、APP应用和互联网资源，每篇图文评测都极其用心，并提供大量软件资源下载。 | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://rsshub:1200)  |  [订阅地址](http://rsshub:1200/iplay/home) |  
| RH028 | Amazon Kindle Software Updates | Kindle E-Reader Software Updates | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://rsshub:1200) | [订阅地址](http://rsshub:1200/amazon/kindle/software-updates) |
| RH029 | App Store 限免/促销 | 每日精品限免和促销应用 | [‣ 「降价」Tape \| 2023-07-17](https://itunes.apple.com/cn/app/tape/id537766208?mt=8&at=1001l9Jj)<br/>[‣ 「免费」Lock Notes Pro \| 2023-07-17](https://itunes.apple.com/us/app/lock-notes-pro-protect-your/id1052612947?mt=8&uo=4) | [订阅地址](http://rsshub:1200/appstore/xianmian) |
| RH030 | Android Security Bulletins | Android Security Bulletins | [‣ Bulletin September 2026 \| 2026-09-07](https://source.android.com/docs/security/bulletin/2026/2026-09-01)<br/>[‣ Bulletin August 2026 \| 2026-09-07](https://source.android.com/docs/security/bulletin/2026/2026-08-01) | [订阅地址](http://rsshub:1200/android/security-bulletin) |
| RH031 | OpenAI - ChatGPT Release Notes | ChatGPT Release Notes | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://rsshub:1200) | [订阅地址](http://rsshub:1200/openai/chatgpt/release-notes) |
| <h2 id="活着的个人独立博客">活着的个人独立博客</h2> |  |   |  |
| <div id="B001" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B001.png" width="30px" style="width:30px;height: auto;"/><br><span>B001</span></div> |  阮一峰的网络日志 | 一个科技博客，讲解的知识通俗易懂 |  [‣ 科技爱好者周刊（第 412 期）：禁止 issue，只用 PR \| 2026-09-11](http://www.ruanyifeng.com/blog/2026/09/weekly-issue-412.html)<br/>[‣ 科技爱好者周刊（第 411 期）：OpenClaw 2.0 是一个缩影 \| 2026-09-11](http://www.ruanyifeng.com/blog/2026/09/weekly-issue-411.html) | [订阅地址](http://www.ruanyifeng.com/blog/atom.xml) |
| <div id="B002" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B002.png" width="30px" style="width:30px;height: auto;"/><br><span>B002</span></div> | 当我在扯淡 | 王垠的博客，观点奇妙有趣 |  [‣ 从 wordpress 转移到 substack \| 2022-11-20](https://yinwang1.wordpress.com/2022/11/20/%e4%bb%8e-wordpress-%e8%bd%ac%e7%a7%bb%e5%88%b0-substack/)<br/>[‣ 计算机科学进阶班招生 \| 2022-11-20](https://yinwang1.wordpress.com/2022/02/22/advanced-cs-course/) | [订阅地址](https://yinwang1.wordpress.com/feed/) |
| <div id="B003" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B003.png" width="30px" style="width:30px;height: auto;"/><br><span>B003</span></div> | 黑果小兵的部落阁 | Hackintosh安装镜像、教程及经验分享|  [‣ 利用CFGLOCK.efi解锁MSR 0xE2 \| 2026-07-10](https://blog.daliansky.net/undefined.html)<br/>[‣ FEVM FN60G黑苹果兼Sequoia安装教程 \| 2026-07-10](https://blog.daliansky.net/FEVM-FN60G-Hackintosh-and-Sequoia-Installation-Tutorial.html) | [订阅地址](https://blog.daliansky.net/atom.xml) |
| <div id="B004" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B004.png" width="30px" style="width:30px;height: auto;"/><br><span>B004</span></div> | 张鑫旭的博客 | 张鑫旭-鑫空间-鑫生活 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.zhangxinxu.com) | [订阅地址](https://www.zhangxinxu.com/wordpress/feed/) | 
| <div id="B005" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B005.png" width="30px" style="width:30px;height: auto;"/><br><span>B005</span></div> | 方圆小站 | zhaoolee的杂谈博客  | [‣ 用AI打磨软件 \| 2026-09-14](https://fangyuanxiaozhan.com/p/2026-06-16-11-38-56-use-ai-polish-the-software/)<br/>[‣ A除最畜生的一代模型 Claude 5 发布后… \| 2026-09-14](https://fangyuanxiaozhan.com/p/2026-06-10-14-25-36-anthropic-fable-5/) | [订阅地址](https://fangyuanxiaozhan.com/feed/) |
| <div id="B006" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B006.png" width="30px" style="width:30px;height: auto;"/><br><span>B006</span></div> | V2方圆 | 防加班办公工具技能宝典  | [‣ StickMe 隐私政策 \| 2026-09-05](https://v2fy.com/p/2026-09-05-stickme-privacy/)<br/>[‣ 109_Opossum_负鼠_BQB \| 2026-09-05](https://v2fy.com/p/109_opossum_%e8%b4%9f%e9%bc%a0_bqb/) | [订阅地址](https://v2fy.com/feed/) |
| <div id="B007" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B007.png" width="30px" style="width:30px;height: auto;"/><br><span>B007</span></div> | 老左笔记 | 记录云主机商活动和建站运维教程  | [‣ 2026年轻云互联优惠码和云服务器优惠套餐整理（国内国外多机房CN2线路） \| 2026-09-14](https://www.laozuo.org/33479.html)<br/>[‣ 2026年丽萨主机优惠码和多机房家庭网络VPS套餐整理（原生IP和住宅IP VPS推荐） \| 2026-09-14](https://www.laozuo.org/27770.html) | [订阅地址](https://www.laozuo.org/feed) |
| <div id="B008" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B008.png" width="30px" style="width:30px;height: auto;"/><br><span>B008</span></div> | FLiNG Trainer | 修改器大神风灵月影 | [‣ Star Wars Zero Company Trainer \| 2026-09-06](https://flingtrainer.com/trainer/star-wars-zero-company-trainer/?utm_source=rss&utm_medium=rss&utm_campaign=star-wars-zero-company-trainer)<br/>[‣ Onimusha: Way of the Sword Trainer \| 2026-09-06](https://flingtrainer.com/trainer/onimusha-way-of-the-sword-trainer/?utm_source=rss&utm_medium=rss&utm_campaign=onimusha-way-of-the-sword-trainer) | [订阅地址](https://flingtrainer.com/feed/) |
| <div id="B009" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B009.png" width="30px" style="width:30px;height: auto;"/><br><span>B009</span></div> | 奔跑中的奶酪 | 有智，有趣，有爱 | [‣ 奶酪清单 \| 2026-03-10](https://www.runningcheese.com/a)<br/>[‣ 奶酪资源 \| 2026-03-10](https://www.runningcheese.com/b) | [订阅地址](https://www.runningcheese.com/feed) |
| <div id="B010" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B010.png" width="30px" style="width:30px;height: auto;"/><br><span>B010</span></div> | 唐巧的博客 | 记录下自己学习的点滴 | [‣ 404 Not Found \| 2026-09-08](https://blog.devtang.com/2026/09/08/404-not-found/)<br/>[‣ 《估值原理》读书笔记：价格背后的游戏、责任与社会秩序 \| 2026-09-08](https://blog.devtang.com/2026/08/30/valuation-principles-note/) | [订阅地址](https://blog.devtang.com/atom.xml) |
| <div id="B011" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B011.png" width="30px" style="width:30px;height: auto;"/><br><span>B011</span></div> | I'M TUALATRIX | Hello! This is TualatriX's blog | [‣ 记「乾坤大挪移」式使用双系统 \| 2025-07-23](https://imtx.me/blog/macos-dual-boot/)<br/>[‣ Now \| 2025-07-23](https://imtx.me/now/) | [订阅地址](https://imtx.me/feed/latest/) |
| <div id="B012" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B012.png" width="30px" style="width:30px;height: auto;"/><br><span>B012</span></div> | 云风的 BLOG | 思绪来得快去得也快，偶尔会在这里停留 | [‣ 暑假的英语补习 \| 2026-09-09](https://blog.codingnow.com/2026/09/summer.html)<br/>[‣ 银河竞逐的乐趣和策略 \| 2026-09-09](https://blog.codingnow.com/2026/08/rftg_strategy.html) | [订阅地址](https://blog.codingnow.com/atom.xml) |
| <div id="B013" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B013.png" width="30px" style="width:30px;height: auto;"/><br><span>B013</span></div> | 透明创业实验 | timqian的博客  | [‣ like-history.ai \| 2023-12-01](https://blog.t9t.io/like-history-ai-2023-12-01/)<br/>[‣ 我如何帮助 GPT-4 在 1 小时内自主解决 LeetCode 上 100 个编程问题 \| 2023-12-01](https://blog.t9t.io/leetcode-gpt-4-2023-11-20/) | [订阅地址](https://blog.t9t.io/atom.xml) |
| <div id="B014" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B014.png" width="30px" style="width:30px;height: auto;"/><br><span>B014</span></div> | 扯氮集 | 多歧为贵 不取苟同 | [‣ AI的说服 靠的不是懂你 是把你淹没 \| 2026-09-10](http://weiwuhui.com/11101.html)<br/>[‣ 阿里发了100亿刀股票 字节则选择贷300亿刀 \| 2026-09-10](http://weiwuhui.com/11096.html) | [订阅地址](http://weiwuhui.com/feed) |
| <div id="B015" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B015.png" width="30px" style="width:30px;height: auto;"/><br><span>B015</span></div> | wenzi | 蚊子在前端开发工作中的总结  | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.xiabingbao.com) | [订阅地址](https://www.xiabingbao.com/atom.xml) |
| <div id="B016" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B016.png" width="30px" style="width:30px;height: auto;"/><br><span>B016</span></div> | DIYgod | 人气网红,前端萌新,有猫,开源  | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://diygod.me)  |  [订阅地址](https://diygod.me/atom.xml) | 
| <div id="B017" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B017.png" width="30px" style="width:30px;height: auto;"/><br><span>B017</span></div> | MacTalk-池建强的随想录 | 关注技术和人文 | [‣ 两小时用智谱 glm 5.2 实现了 CatReader 的移动微信版 \| 2026-06-15](https://macshuo.com/?p=2069)<br/>[‣ 谁说 ChatGPT 和 Codex 合体了？ \| 2026-06-15](https://macshuo.com/?p=2063)  |  [订阅地址](http://macshuo.com/?feed=rss2) | 
| <div id="B018" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B018.png" width="30px" style="width:30px;height: auto;"/><br><span>B018</span></div> | ShrekShao | ShrekShao's Blog | [‣ 更新了吴健雄院队和健雄杯的网站 \| 2021-02-24](http://shrekshao.github.io/2021/02/24/wjxfootball/)<br/>[‣ shrekshao.com \| 2021-02-24](http://shrekshao.github.io/2021/01/01/shrekshao-com/)  |  [订阅地址](http://shrekshao.github.io/feed.xml) | 
| <div id="B019" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B019.png" width="30px" style="width:30px;height: auto;"/><br><span>B019</span></div> | Phodal | Phodal - A Growth Engineer | [‣ 从生成动画到可编程产物：在 Harness 中构建 Lottie 创作运行时 \| 2026-08-30](http://www.phodal.com/blog/agentic-programming-artifact/)<br/>[‣ 面向人机交互设计 Harness：构建以产物为中心的 Agent Loop \| 2026-08-30](http://www.phodal.com/blog/artifact-centered-agent-harness/)  |  [订阅地址](https://www.phodal.com/blog/feeds/rss/) |
| B020 | 追梦人物 | 追梦人物的博客 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.zmrenwu.com)  |  [订阅地址](https://www.zmrenwu.com/all/rss/) | 
| B021 | 小明明s à domicile | 小明明s à domicile | [‣ 关于本博客 \| 2019-04-23](https://www.dongwm.com/page/about-blog)<br/>[‣ Stable Diffusion高级教程 - Controlnet \| 2019-04-23](https://www.dongwm.com/post/stable-diffusion-controlnet/)  |  [订阅地址](https://www.dongwm.com/atom.xml) | 
| <div id="B022" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B022.png" width="30px" style="width:30px;height: auto;"/><br><span>B022</span></div> | 但行好事，莫问前程 | Windard's simple blog web  | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://windard.com)  |  [订阅地址](https://windard.com/feed.xml) | 
| <div id="B023" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B023.png" width="30px" style="width:30px;height: auto;"/><br><span>B023</span></div> | 罗磊的独立博客 | 前端工程师，ZUOLUOTV制作人  | [‣ 开启我的「人生 AI」计划 \| 2026-03-10](https://luolei.org/life-ai)<br/>[‣ 2026 年，我把自己做成了一个 AI \| 2026-03-10](https://luolei.org/luolei-ai)  |  [订阅地址](https://luolei.org/feed/) | 
| B024 | 阁子 | Newdee's Blog  | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://newdee.cf)  |  [订阅地址](https://newdee.cf/atom.xml) | 
| <div id="B025" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B025.png" width="30px" style="width:30px;height: auto;"/><br><span>B025</span></div> | RidiQulous | RidiQulous's Blog  | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://ridiqulous.com)  |  [订阅地址](https://ridiqulous.com/feed/) | 
| <div id="B026" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B026.png" width="30px" style="width:30px;height: auto;"/><br><span>B026</span></div> | 代码家 | 善存于心，世界和平 | [‣ 定在原地，回头和远望 \| 2025-12-18](https://daimajia.com/2025/12/18/three-years-off-work-living-with-pain-and-finding-life/)<br/>[‣ AIGC – 图片与文字分享 \| 2025-12-18](https://daimajia.com/2023/01/03/aigc/)  |  [订阅地址](https://daimajia.com/feed) | 
| <div id="B027" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B027.png" width="30px" style="width:30px;height: auto;"/><br><span>B027</span></div> | 开源实验室 | 张涛的开源实验室 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.kymjs.com)  |  [订阅地址](https://www.kymjs.com/feed.xml) | 
| <div id="B028" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B028.png" width="30px" style="width:30px;height: auto;"/><br><span>B028</span></div> | 技术小黑屋 | 一个Android 工程师 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://droidyue.com)  |  [订阅地址](https://droidyue.com/atom.xml) | 
| <div id="B029" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B029.png" width="30px" style="width:30px;height: auto;"/><br><span>B029</span></div> | 依云 | 依云's Blog | [‣ 通过字幕总结YouTube视频内容 \| 2026-06-09](https://blog.lilydjwg.me/posts/217033.html)<br/>[‣ 自定义系统默认中文字体 \| 2026-06-09](https://blog.lilydjwg.me/posts/217026.html)  |  [订阅地址](https://blog.lilydjwg.me/posts.rss) | 
| <div id="B030" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B030.png" width="30px" style="width:30px;height: auto;"/><br><span>B030</span></div> | INTJer | Armin Li（李钊） | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://arminli.com)  |  [订阅地址](https://arminli.com/feed/) | 
| <div id="B031" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B031.png" width="30px" style="width:30px;height: auto;"/><br><span>B031</span></div> | 思圆笔记 | 促成良性循环 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://hintsnet.com)  |  [订阅地址](https://hintsnet.com/pimgeek/feed/) | 
| <div id="B032" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B032.png" width="30px" style="width:30px;height: auto;"/><br><span>B032</span></div> | 老周快救我 | Life Is Fantastic | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://zxx.im)  |  [订阅地址](https://zxx.im/feed) | 
| <div id="B033" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B033.png" width="30px" style="width:30px;height: auto;"/><br><span>B033</span></div> | MouT.me | 给生活打个草稿 | [‣ 终于补完了《汪达与巨像》 \| 2020-07-24](https://ghost.mout.me/shadow-of-the-colossus/)<br/>[‣ 微信群接龙表格功能的思考 \| 2020-07-24](https://ghost.mout.me/product-note-of-wechat-chain-of-sign-form/)  |  [订阅地址](https://ghost.mout.me/rss/) | 
| <div id="B034" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B034.png" width="30px" style="width:30px;height: auto;"/><br><span>B034</span></div> | diss带码 | 码动人生 | [‣ datart系列04：基于threejs自定义插件3D-MAP \| 2023-01-11](https://dumplingbao.github.io/2023/01/11/datart-bi-04/)<br/>[‣ datart系列03：图表插件开发 \| 2023-01-11](https://dumplingbao.github.io/2022/04/15/datart-bi-03/)  |  [订阅地址](https://dumplingbao.github.io/atom.xml) | 
| <div id="B035" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B035.png" width="30px" style="width:30px;height: auto;"/><br><span>B035</span></div> | 王登科-DK博客 | 布洛芬爱好者 | [‣ 庄子不会喜欢 AI：效率，机心，伯乐之罪 \| 2026-07-02](https://greatdk.com/2144.html)<br/>[‣ 3 天 100 万注册用户，日烧千亿 token，一次意外的里程碑 \| 2026-07-02](https://greatdk.com/2149.html)  |  [订阅地址](https://greatdk.com/feed) | 
| <div id="B036" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B036.png" width="30px" style="width:30px;height: auto;"/><br><span>B036</span></div> | 笨方法学写作 | 笨方法学写作,这一次彻底学会写作 | [‣  \| 2026-07-23](https://cnfeat.com/posts/2026/07/23/2026-07-10-%E5%A6%82%E4%BD%95%E4%BB%8E%E8%87%AA%E5%B7%B1%E5%8F%98%E5%BC%BA%E5%88%87%E6%8D%A2%E5%88%B0%E8%AE%A9%E5%88%AB%E4%BA%BA%E5%8F%98%E5%BC%BA/)<br/>[‣ 为什么你那么努力，却依然不赚钱？看懂这个底层逻辑，少走3年弯路 \| 2026-07-23](https://cnfeat.com/posts/2026/07/16/%E4%B8%BA%E4%BB%80%E4%B9%88%E4%BD%A0%E9%82%A3%E4%B9%88%E5%8A%AA%E5%8A%9B%E5%8D%B4%E4%BE%9D%E7%84%B6%E4%B8%8D%E8%B5%9A%E9%92%B1%E7%9C%8B%E6%87%82%E8%BF%99%E4%B8%AA%E5%BA%95%E5%B1%82%E9%80%BB%E8%BE%91%E5%B0%91%E8%B5%B03%E5%B9%B4%E5%BC%AF%E8%B7%AF/)  |  [订阅地址](https://www.cnfeat.com/feed.xml) | 
| <div id="B037" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B037.png" width="30px" style="width:30px;height: auto;"/><br><span>B037</span></div> | 风雪之隅 | 左手代码右手诗 | [‣ Yac 2.4.0发布 - 小值读取性能提升64% \| 2026-08-26](https://www.laruence.com/2026/08/26/6566.html)<br/>[‣ 用Yac给WordPress做缓存：比Memcached快19% \| 2026-08-26](https://www.laruence.com/2026/08/20/6420.html)  |  [订阅地址](https://www.laruence.com/feed) | 
| <div id="B038" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B038.png" width="30px" style="width:30px;height: auto;"/><br><span>B038</span></div> | Hawstein's Blog | 这里是 Hawstein 的个人博客，记录生活点滴。 | [‣ 从一期播客说起 \| 2025-08-13](https://hawstein.com/2025/08/13/starting-from-a-podcast/)<br/>[‣ 写给 YF：自由生活与创造 \| 2025-08-13](https://hawstein.com/2025/07/14/freedom-and-creation/)  |  [订阅地址](https://hawstein.com/feed.xml) | 
| <div id="B039" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B039.png" width="30px" style="width:30px;height: auto;"/><br><span>B039</span></div> | DeveWork | WordPress极客一枚 | [‣ 一键将 DeepSeek 集成到 Alfred App 中 \| 2025-02-15](https://devework.com/deepseek-alfred-workflow.html)<br/>[‣ 借助云函数SCF实现Let’s Encrypt SSL证书自动更新 \| 2025-02-15](https://devework.com/acme-qcloud-scf.html)  |  [订阅地址](https://devework.com/feed) | 
| <div id="B040" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B040.png" width="30px" style="width:30px;height: auto;"/><br><span>B040</span></div> | 海交史 | 东亚文史研究动态网 | [‣ 全明笔记整理与研究中期检查报告 \| 2026-09-15](https://www.haijiaoshi.com/archives/17466?utm_source=rss&utm_medium=rss&utm_campaign=%25e5%2585%25a8%25e6%2598%258e%25e7%25ac%2594%25e8%25ae%25b0%25e6%2595%25b4%25e7%2590%2586%25e4%25b8%258e%25e7%25a0%2594%25e7%25a9%25b6%25e4%25b8%25ad%25e6%259c%259f%25e6%25a3%2580%25e6%259f%25a5%25e6%258a%25a5%25e5%2591%258a)<br/>[‣ 《全宋笔记》历时十九载全十编出齐 \| 2026-09-15](https://www.haijiaoshi.com/archives/17464?utm_source=rss&utm_medium=rss&utm_campaign=%25e3%2580%258a%25e5%2585%25a8%25e5%25ae%258b%25e7%25ac%2594%25e8%25ae%25b0%25e3%2580%258b%25e5%258e%2586%25e6%2597%25b6%25e5%258d%2581%25e4%25b9%259d%25e8%25bd%25bd%25e5%2585%25a8%25e5%258d%2581%25e7%25bc%2596%25e5%2587%25ba%25e9%25bd%2590)  |  [订阅地址](https://www.haijiaoshi.com/feed) | 
| <div id="B041" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B041.png" width="30px" style="width:30px;height: auto;"/><br><span>B041</span></div> | 四季书评 | 四季书评 | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://www.4sbooks.com)  |  [订阅地址](http://www.4sbooks.com/feed) | 
| <div id="B042" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B042.png" width="30px" style="width:30px;height: auto;"/><br><span>B042</span></div> | 文三娃| 网络上甘岭战区候任参谋长 | [‣ 环球节律赏析 \| 2019-08-19](https://wentommy.wordpress.com/2019/08/19/%e7%8e%af%e7%90%83%e8%8a%82%e5%be%8b%e8%b5%8f%e6%9e%90/)<br/>[‣ 胡侃偶记之『推特篇』 \| 2019-08-19](https://wentommy.wordpress.com/2019/06/01/%e8%83%a1%e4%be%83%e5%81%b6%e8%ae%b0%e4%b9%8b%e3%80%8e%e6%8e%a8%e7%89%b9%e7%af%87%e3%80%8f/)  |  [订阅地址](https://wentommy.wordpress.com/feed/) | 
| <div id="B043" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B043.png" width="30px" style="width:30px;height: auto;"/><br><span>B043</span></div> | 我的小角落 | 点击文章标题可评论哦 | [‣  \| 2026-06-19](https://micheer.net/archives/1101.html)<br/>[‣ 要被GPT笑死 \| 2026-06-19](https://micheer.net/archives/1083.html)  |  [订阅地址](http://micheer.net/?feed=rss2) | 
| <div id="B044" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B044.png" width="30px" style="width:30px;height: auto;"/><br><span>B044</span></div> | 木遥 | 木遥的窗子 | [‣ 小写的牧歌 \| 2023-07-13](https://blog.farmostwood.net/1256.html)<br/>[‣ Braess 悖论 \| 2023-07-13](https://blog.farmostwood.net/1287.html)  |  [订阅地址](http://blog.farmostwood.net/feed) | 
| <div id="B045" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B045.png" width="30px" style="width:30px;height: auto;"/><br><span>B045</span></div> | Limboy's HQ | Limboy's HQ | [‣ 捷径 \| 2026-08-12](https://limboy.me/posts/shortcut)<br/>[‣ 注意力 \| 2026-08-12](https://limboy.me/posts/attention)  |  [订阅地址](https://limboy.me/index.xml) | 
| <div id="B046" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B046.png" width="30px" style="width:30px;height: auto;"/><br><span>B046</span></div> | 人人都是产品经理——iamsujie | 成长中的产品经理，期待和同学们一起，用好产品改变世界~ | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://iamsujie.com)  |  [订阅地址](http://iamsujie.com/feed/) | 
| <div id="B047" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B047.png" width="30px" style="width:30px;height: auto;"/><br><span>B047</span></div> | 土木坛子 | 和光同尘，与时舒卷 | [‣ 人生经营的终极目标 \| 2026-09-13](https://tumutanzi.com/archives/17629)<br/>[‣ 众安银行股票投资功能试用 \| 2026-09-13](https://tumutanzi.com/archives/17628)  |  [订阅地址](https://tumutanzi.com/feed) | 
| <div id="B048" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B048.png" width="30px" style="width:30px;height: auto;"/><br><span>B048</span></div> | 火丁笔记 | 多研究些问题，少谈些主义。 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://blog.huoding.com)  |  [订阅地址](https://blog.huoding.com/feed) | 
| B049 | 產品經理 x 成長駭客 - Mr. PM下午先生 | PM可以是產品經理、下午、Pig Man，但絕對不是Poor Man | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://mrpm.cc)  |  [订阅地址](http://mrpm.cc/?feed=rss2) | 
| B050 | Matrix67 | Matrix67: The Aha Moments  | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://www.matrix67.com)  |  [订阅地址](http://www.matrix67.com/blog/feed) | 
| <div id="B051" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B051.png" width="30px" style="width:30px;height: auto;"/><br><span>B051</span></div> | 我爱自然语言处理 | I Love Natural Language Processing  | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.52nlp.cn)  |  [订阅地址](https://www.52nlp.cn/feed) | 
| <div id="B052" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B052.png" width="30px" style="width:30px;height: auto;"/><br><span>B052</span></div> | sunnyxx | sunnyxx的技术博客  | [‣ 重识 Objective-C Runtime - 看透 Type 与 Value \| 2016-08-13](http://blog.sunnyxx.com/2016/08/13/reunderstanding-runtime-1/)<br/>[‣ 重识 Objective-C Runtime - Smalltalk 与 C 的融合 \| 2016-08-13](http://blog.sunnyxx.com/2016/08/13/reunderstanding-runtime-0/)  |  [订阅地址](http://blog.sunnyxx.com/atom.xml) | 
| <div id="B053" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B053.png" width="30px" style="width:30px;height: auto;"/><br><span>B053</span></div> | 搞笑談軟工 | 敏捷開發，設計模式，精實開發，Scrum，軟體設計，軟體架構  | [‣ 學習總在課堂後 \| 2025-06-08](https://teddy-chen-tw.blogspot.com/2025/06/blog-post.html)<br/>[‣ 重構既有系統，邁向整潔架構 （6）：第三回合，在使用案例層讀寫分離 \| 2025-06-08](https://teddy-chen-tw.blogspot.com/2024/09/6.html)  |  [订阅地址](http://teddy-chen-tw.blogspot.com/feeds/posts/default) | 
| <div id="B054" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B054.png" width="30px" style="width:30px;height: auto;"/><br><span>B054</span></div> | Beyond the Void | 遊記、語言學、經濟學、信息學競賽/ACM經驗、算法講解、技術知識  | [‣ 我的遊記 \| 2016-09-30](https://byvoid.com/zht/travel/)<br/>[‣ 關於 \| 2016-09-30](https://byvoid.com/zht/about/)  |  [订阅地址](https://byvoid.com/zht/feed.xml) | 
| B055 | Est's Blog | This blog is rated  R, viewer discretion is advised  | [‣ 海南之行后记 \| 2026-09-03](https://blog.est.im/2026/stderr-28)<br/>[‣ The httpx 1.0 situation \| 2026-09-03](https://blog.est.im/2026/stdout-35)  |  [订阅地址](https://blog.est.im/rss) | 
| <div id="B056" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B056.png" width="30px" style="width:30px;height: auto;"/><br><span>B056</span></div> | 卢昌海个人主页 | Changhai Lu's Homepage  | [‣ 最新微博：2026 年 9 月 13 日 \| 2026-09-13](https://www.changhai.org/articles/miscellaneous/blog/202609.php#latest)<br/>[‣ Latest post on Threads：2026.09.11 \| 2026-09-13](https://www.changhai.org/articles/miscellaneous/eblog/202609.php#latest)  |  [订阅地址](https://www.changhai.org//feed.xml) | 
| <div id="B057" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B057.png" width="30px" style="width:30px;height: auto;"/><br><span>B057</span></div> | 程序师 | 程序员、编程语言、软件开发、编程技术 | [‣ 问题解决：在 Android 上的 Ubuntu chroot 环境中运行 apt-get update 失败 \| 2026-05-20](https://www.techug.com/post/apt-get-update-fails-on-chroot-ubuntu-on-android/)<br/>[‣ 耶鲁大学：中国风电与太阳能建设令人惊叹 \| 2026-05-20](https://www.techug.com/post/china-renewable-photo-essay/)  |  [订阅地址](https://www.techug.com/feed) | 
| B058 | bang's blog | 我的世界 | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://blog.cnbang.net)  |  [订阅地址](http://blog.cnbang.net/feed/) | 
| B059 | 白宦成 | 思无邪 | [‣ Claude Tag 产品分析 \| 2026-09-10](https://www.ixiqin.com/2026/09/10/claude-tag-product-analysis/)<br/>[‣ 如何选择 DeepSeekHarnes / Claude Code/Codex/ Pi \| 2026-09-10](https://www.ixiqin.com/2026/08/26/how-to-choose-depseekharnes-claude-code-codex-pi/)  |  [订阅地址](https://www.ixiqin.com/feed/) | 
| <div id="B060" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B060.png" width="30px" style="width:30px;height: auto;"/><br><span>B060</span></div> | Jason 独立开发，自由职业 | 记录一位独立开发者的精进之路，分享自由职业者的生存方式。 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://atjason.com)  |  [订阅地址](https://atjason.com/atom.xml/) | 
| <div id="B061" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B061.png" width="30px" style="width:30px;height: auto;"/><br><span>B061</span></div> | Randy's Blog | Randy is blogging about life, tech and music. | [‣ 高考随想 \| 2026-06-10](https://lutaonan.com/blog/undefined)<br/>[‣ 让 AI 戴着镣铐跳舞 \| 2026-06-10](https://lutaonan.com/blog/undefined)  |  [订阅地址](https://lutaonan.com/rss.xml) | 
| <div id="B062" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B062.png" width="30px" style="width:30px;height: auto;"/><br><span>B062</span></div> | 木木木木木 | 林小沐的博客 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://immmmm.com)  |  [订阅地址](https://immmmm.com/atom.xml) | 
| B063 | Skywind Inside | 写自己的代码，让别人猜去吧 | [‣ 在 Vim 里实现可定制表单对话框 \| 2026-05-02](https://skywind.me/blog/archives/3676)<br/>[‣ 单头文件 C++ 游戏开发库（GameLib.h） \| 2026-05-02](https://skywind.me/blog/archives/3666)  |  [订阅地址](http://www.skywind.me/blog/feed) | 
| B064 | 轉個彎日誌 | by 阿川先生 | [‣ 網路創業：與其當成在做生意，不如當成在做實驗 \| 2020-10-13](https://blog.turn.tw/?p=3787&utm_source=rss&utm_medium=rss&utm_campaign=%25e7%25b6%25b2%25e8%25b7%25af%25e5%2589%25b5%25e6%25a5%25ad%25ef%25bc%259a%25e8%2588%2587%25e5%2585%25b6%25e7%2595%25b6%25e6%2588%2590%25e5%259c%25a8%25e5%2581%259a%25e7%2594%259f%25e6%2584%258f%25ef%25bc%258c%25e4%25b8%258d%25e5%25a6%2582%25e7%2595%25b6%25e6%2588%2590%25e5%259c%25a8%25e5%2581%259a%25e5%25af%25a6%25e9%25a9%2597)<br/>[‣ 遠端（在家）工作的4個技巧：批次溝通、過度溝通、被動溝通、多層溝通 \| 2020-10-13](https://blog.turn.tw/?p=3768&utm_source=rss&utm_medium=rss&utm_campaign=%25e9%2581%25a0%25e7%25ab%25af%25ef%25bc%2588%25e5%259c%25a8%25e5%25ae%25b6%25ef%25bc%2589%25e5%25b7%25a5%25e4%25bd%259c%25e7%259a%25844%25e5%2580%258b%25e6%258a%2580%25e5%25b7%25a7%25ef%25bc%259a%25e6%2589%25b9%25e6%25ac%25a1%25e6%25ba%259d%25e9%2580%259a%25e3%2580%2581%25e9%2581%258e%25e5%25ba%25a6%25e6%25ba%259d%25e9%2580%259a)  |  [订阅地址](https://blog.turn.tw/?feed=rss2) | 
| <div id="B065" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B065.png" width="30px" style="width:30px;height: auto;"/><br><span>B065</span></div> | 余果的博客 | 公众号：余果专栏 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://yuguo.us)  |  [订阅地址](https://yuguo.us/feed.xml) | 
| <div id="B066" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B066.png" width="30px" style="width:30px;height: auto;"/><br><span>B066</span></div> | 陈沙克日志 | 把我的过程记录下来，以免以后忘了 | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://www.chenshake.com)  |  [订阅地址](http://www.chenshake.com/feed/) | 
| B067 | 透明思考 Transparent Thoughts | 就，觉得自己还挺有洞察力的…… | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://gigix.thoughtworkers.org)  |  [订阅地址](http://gigix.thoughtworkers.org/atom.xml) | 
| <div id="B068" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B068.png" width="30px" style="width:30px;height: auto;"/><br><span>B068</span></div> | 依云's Blog | Happy coding, happy living! | [‣ 通过字幕总结YouTube视频内容 \| 2026-06-09](https://blog.lilydjwg.me/posts/217033.html)<br/>[‣ 自定义系统默认中文字体 \| 2026-06-09](https://blog.lilydjwg.me/posts/217026.html)  |  [订阅地址](https://blog.lilydjwg.me/feed) | 
| <div id="B069" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B069.png" width="30px" style="width:30px;height: auto;"/><br><span>B069</span></div> | 王子亭的博客 | 精子真名叫「王子亭」，生于 1995.11.25，英文ID是jysperm.  精子是一名独立博客作者 | [‣ 2023 年度小结 \| 2023-12-30](https://jysperm.me/2023/12/summary-of-2023/)<br/>[‣ HostedBeans: 基于 Beancount 的协作托管服务 \| 2023-12-30](https://jysperm.me/2023/11/introducing-hostedbeans/)  |  [订阅地址](https://jysperm.me/atom.xml) | 
| <div id="B070" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B070.png" width="30px" style="width:30px;height: auto;"/><br><span>B070</span></div> | 谢益辉 | 中文日志 - Yihui Xie  | [‣ 我心似海洋 \| 2026-01-12](https://yihui.org/cn/2026/01/heart-sea/)<br/>[‣ Bressanone \| 2026-01-12](https://yihui.org/cn/2026/01/bressanone/)  |  [订阅地址](https://yihui.org/cn/index.xml) | 
| <div id="B071" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B071.png" width="30px" style="width:30px;height: auto;"/><br><span>B071</span></div> | 褪墨・时间管理，个人提升，生活健康与习惯 | 褪墨・时间管理是一个关注时间管理、GTD、个人提升、生活健康与习惯、学习方法和演讲技巧的网站。我们的目标是：把事情做到更好！| [‣ 《Getting Things Done》读书笔记 \| 2019-02-26](https://www.mifengtd.cn/articles/gtd-book-summary.html)<br/>[‣ 我的时间管理道与术（三） \| 2019-02-26](https://www.mifengtd.cn/articles/time-management-dao-shu-3.html)  |  [订阅地址](https://www.mifengtd.cn/feed.xml) | 
| <div id="B072" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B072.png" width="30px" style="width:30px;height: auto;"/><br><span>B072</span></div> | 数字移民 | 数字移民是一种生活方式 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://blog.shuziyimin.org)  |  [订阅地址](https://blog.shuziyimin.org/feed) | 
| <div id="B073" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B073.png" width="30px" style="width:30px;height: auto;"/><br><span>B073</span></div> | Just lepture | Love its people, but never trust its government. | [‣ 我用 AI 造新語 \| 2026-01-17](https://lepture.com/zh/2026/new-language-by-ai)<br/>[‣ 丟失的表達欲 \| 2026-01-17](https://lepture.com/zh/2025/loss-of-self-expression)  |  [订阅地址](https://lepture.com/feed.xml) | 
| B074 | 1 Byte | Articles about life, technology, and startups. | [‣ 我在 2025 年看完的书 \| 2026-01-14](https://1byte.io/articles/2025-books/)<br/>[‣ 西班牙之行 \| 2026-01-14](https://1byte.io/articles/spain-trip-2025/)  |  [订阅地址](https://1byte.io/rss.xml) | 
| <div id="B075" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B075.png" width="30px" style="width:30px;height: auto;"/><br><span>B075</span></div> | 庭说 | 保持蓬勃的好奇心 | [‣ Windows 10 电脑：使用技巧、佳软推荐以及系统重装教程 \| 2017-12-17](https://tingtalk.me/windows/)<br/>[‣ Telegram（电报）：新手指南、使用教程及频道推荐 \| 2017-12-17](https://tingtalk.me/telegram/)  |  [订阅地址](https://tingtalk.me/atom.xml) | 
| <div id="B076" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B076.png" width="30px" style="width:30px;height: auto;"/><br><span>B076</span></div> | KAIX.IN | 杂文、随笔、感悟、记录 | [‣ 骆驼、狮子、孩子、路飞、大笑 \| 2026-09-15](https://kaix.in/2026/0915/)<br/>[‣ 那时候，贾母也才十来岁 \| 2026-09-15](https://kaix.in/2026/0829/)  |  [订阅地址](https://kaix.in/feed/) | 
| <div id="B077" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B077.png" width="30px" style="width:30px;height: auto;"/><br><span>B077</span></div> | 硕鼠的博客站 | 范路的博客主站，时而会发些东西。 | [‣ 第五次扫黑除恶为何剑指差评黑产 \| 2026-09-15](https://lukefan.com/2026/09/15/negative-review-black-market-anti-crime-campaign/)<br/>[‣ OpenAI破解数学题之后，热情怎么办 \| 2026-09-15](https://lukefan.com/2026/09/14/openai-navier-stokes-ai-agents-controversy/)  |  [订阅地址](http://lukefan.com/?feed=rss2) | 
| <div id="B078" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B078.png" width="30px" style="width:30px;height: auto;"/><br><span>B078</span></div> | 构建我的被动收入 | Lifelong Learner | [‣ 置身 Agent 时代：当软件开始不再需要软件工程师 \| 2026-09-15](https://www.bmpi.dev/dev/agent-era-software-engineering/)<br/>[‣ 给 Agent 造一个 Domain Harness \| 2026-09-15](https://www.bmpi.dev/dev/agent-native-system-paradigm/)  |  [订阅地址](https://www.bmpi.dev/index.xml) | 
|  <div id="B079" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B079.png" width="30px" style="width:30px;height: auto;"/><br><span>B079</span></div> | Livid | Beautifully Advance | [‣ Installing Jekyll on macOS Ventura \| 2023-01-03](https://livid.v2ex.com/guides/2023/01/03/jekyll-macos-ventura.html)<br/>[‣ 20210531 \| 2023-01-03](https://livid.v2ex.com/diaries/2021/05/31/20210531.html)  |  [订阅地址](https://livid.v2ex.com/feed.xml) | 
| <div id="B080" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B080.png" width="30px" style="width:30px;height: auto;"/><br><span>B080</span></div> | 胡涂说 | hutusi.com | [‣ AI Naive: 用 AI 做“无用之用”的独立软件作品集 \| 2026-08-30](https://hutusi.com/flows/2026/08/30)<br/>[‣ Jeff Dean 离开 Google，以及关于他的传说 \| 2026-08-30](https://hutusi.com/flows/2026/08/08)  |  [订阅地址](https://hutusi.com/feed.xml) | 
| B081 | 鸟窝 | 万物之始，大道至简，衍化至繁 | [‣ 代码在发臭：一个能"闻"出坏味道的 AI 技能，我拿它扫了最新的开源代码 \| 2026-07-04](https://colobu.com/2026/07/04/ai-skill-sniffs-out-code-smells/)<br/>[‣ 百度网络监控工具开源第四弹：evr — 构造 VXLAN 探测 \| 2026-07-04](https://colobu.com/2026/06/30/baidu-network-monitor-evr-vxlan-probe/)  |  [订阅地址](https://colobu.com/atom.xml) |
| <div id="B082" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B082.png" width="30px" style="width:30px;height: auto;"/><br><span>B082</span></div> | 卡瓦邦噶！ | 无法自制的人得不到自由。 | [‣ BPG 连接建立失败问题的答案和解析 \| 2026-09-09](https://www.kawabangga.com/posts/7413)<br/>[‣ BGP 连接建立失败问题 \| 2026-09-09](https://www.kawabangga.com/posts/7397) | [订阅地址](https://www.kawabangga.com/feed) |
| <div id="B083" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B083.png" width="30px" style="width:30px;height: auto;"/><br><span>B083</span></div> | 方圆STU | 天是方的，地是圆的。 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://fangyuanstu.com) | [订阅地址](https://fangyuanstu.com/feed/) |
| <div id="B084" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B084.png" width="30px" style="width:30px;height: auto;"/><br><span>B084</span></div> | 折影轻梦 | 崇尚自由、热爱科学与艺术 | [‣ Viora 招聘：AI Design Engineer / AI Growth Engineer \| 2026-05-26](https://nexmoe.com/posts/viora-hire-ai-design-growth)<br/>[‣ 我做了个 VS Code 小工具，用来看本机和远程服务器的资源占用 \| 2026-05-26](https://nexmoe.com/%E4%BA%A7%E5%93%81/20260525-vscode-monitor-pro-0-7) | [订阅地址](https://nexmoe.com/atom.xml) |
| <div id="B085" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B085.png" width="30px" style="width:30px;height: auto;"/><br><span>B085</span></div> | 不羁阁 | 行走少年郎 不羁，谓才行高远，不可羁系也 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://bujige.net) | [订阅地址](https://bujige.net/atom.xml) |
| <div id="B086" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/B086.png" width="30px" style="width:30px;height: auto;"/><br><span>B086</span></div> | Cal Paterson | Cal Paterson's articles | [‣ Agent memory as a file format \| 2026-08-31](https://calpaterson.com/memoryfields.html)<br/>[‣ Dependency cooldowns turn you into a free-rider \| 2026-08-31](https://calpaterson.com/deps.html) | [订阅地址](https://calpaterson.com/calpaterson.rss) |
| B087 | 3号实验室 | 树莓派; 开发板; 编程; 折腾 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.labno3.com) | [订阅地址](https://www.labno3.com/feed/) |
| <div id="B088" style="text-align: center;"><span>B088</span></div> | ZMonster's Blog | 巧者劳而智者忧，无能者无所求，饱食而遨游，泛若不系之舟 | [‣ 我给自己建了一个数据库 \| 2026-07-30](http://www.zmonster.me/2026/07/30/build-self-db.html)<br/>[‣ 找工作啦 \| 2026-07-30](http://www.zmonster.me/2024/05/13/ready-to-work.html) | [订阅地址](https://www.zmonster.me/atom.xml) |
| <div id="B089" style="text-align: center;"><span>B089</span></div> | 十年老程网 | 推荐各种VPS主机 | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://snlcw.com) | [订阅地址](http://snlcw.com/feed) |
| <div id="B090" style="text-align: center;"><span>B090</span></div> | 小明明 domicile | 前豆瓣工程师，现在家带娃，远程工作机会联系我哟 | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://snlcw.com) | [订阅地址](http://snlcw.com/feed) |
| <div id="B091" style="text-align: center;"><span>B091</span></div> | LFhacks.com | 读万卷书，行万里路 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.lfhacks.com) | [订阅地址](https://www.lfhacks.com/rss/) |
| <div id="B092" style="text-align: center;"><span>B092</span></div> | 三省吾身 | 兴趣遍地都是，专注和持之以恒才是真正稀缺的 | [‣ 从一个简单功能的实现，谈谈 react 中的逻辑复用进化过程 \| 2019-09-17](http://guowenfh.github.io/2019/09/17/2019/react-reuse/)<br/>[‣ 在 vue 中使用 jsx 与 class component 的各种姿势 \| 2019-09-17](http://guowenfh.github.io/2019/09/17/2019/vue-jsx-class-component/) | [订阅地址](https://blog.guowenfh.com/atom.xml) |
| <div id="B093" style="text-align: center;"><span>B093</span></div> | 夏海比比 | 关于设计与摄影，一个95后的个人博客 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://huiweishijie.com) | [订阅地址](https://huiweishijie.com/feed.xml) |
| <div id="B094" style="text-align: center;"><span>B094</span></div> | TRHX'S BLOG | 一入 IT 深似海 从此学习无绝期 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.itrhx.com) | [订阅地址](https://www.itrhx.com/atom.xml) |
| <div id="B095" style="text-align: center;"><span>B095</span></div> | CallMeSoul | callmesoul前端开发者 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://callmesoul.cn) | [订阅地址](https://callmesoul.cn/rss.xml) |
| <div id="B096" style="text-align: center;"><span>B096</span></div> | 龚成博客 |  不高大但是威猛，不英俊但是潇洒 | [‣ 2020-07-02-培养渴望 \| 2020-07-01](https://laogongshuo.com/archives/420)<br/>[‣ 2020-06-18-关于皇帝 \| 2020-07-01](https://laogongshuo.com/archives/445) | [订阅地址](https://laogongshuo.com/feed) |
| <div id="B097" style="text-align: center;"><span>B097</span></div> | Seven's blog |  你不会找到路，除非你敢于迷路 | [‣ 运维笔记：NetworkManager shared 模式给共享客户端固定 IP \| 2026-08-07](https://blog.diqigan.cn/posts/coding/linux/networkmanager-shared-dhcp-static-ip.html)<br/>[‣ 运维踩坑：nginx 缓存上游容器旧 IP，请求转发到了错误的服务 \| 2026-08-07](https://blog.diqigan.cn/posts/coding/maintenance/nginx-cached-stale-upstream-ip-trap.html) | [订阅地址](https://blog.diqigan.cn/atom.xml) |
| <div id="B098" style="text-align: center;"><span>B098</span></div> | 治部少辅 |  你晚来天雨雪，能饮一杯无？ | [‣ Emscripten Fetch 接口的一个潜在内存泄漏问题 \| 2025-05-07](https://www.codewoody.com/posts/45916/)<br/>[‣ 在 VPN 场景下的跨子网通信防火墙配置方法 \| 2025-05-07](https://www.codewoody.com/posts/18417/) | [订阅地址](https://www.codewoody.com/atom.xml) |
| <div id="B099" style="text-align: center;"><span>B099</span></div> | CRIMX BLOG |  CRIMX 的博客，主要记录 Web 前端相关的一些内容，偶尔涉及其它方面。 | [‣ 如何在 Sass 中方便引用祖先选择器 \| 2020-07-14](https://blog.crimx.com/2020/07/14/如何在-sass-中方便引用祖先选择器/)<br/>[‣ Web Extension Live Reloading \| 2020-07-14](https://blog.crimx.com/2020/07/08/web-extension-live-reloading/) | [订阅地址](https://blog.crimx.com/rss.xml) |
| <div id="B100" style="text-align: center;"><span>B100</span></div> | 小非的物理小站 |  信仰共产主义，后现代主义者，结构主义者，奇妙发现世界～～ | [‣ 开放研究之所以可能(三) \| 2021-06-13](https://xiaophy.com/2021/06/14/thinking11.html)<br/>[‣ 开放研究是如何直面命题 \| 2021-06-13](https://xiaophy.com/2019/02/22/thinking10.html) | [订阅地址](https://xiaophy.com/feed.xml) |
| <div id="B101" style="text-align: center;"><span>B101</span></div> | Michael翔 |  因上努力，果上随缘！ | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://michael728.github.io) | [订阅地址](https://michael728.github.io/atom.xml) |
| <div id="B102" style="text-align: center;"><span>B102</span></div> | Dosk 技术站 | SpringHack 的无名技术小站 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.dosk.win) | [订阅地址](https://www.dosk.win/feed.xml) |
| <div id="B103" style="text-align: center;"><span>B103</span></div> | Lu Shuyu's NoteBook | 你好呀，我是一个准大学生，曾经是一个信息学奥林匹克竞赛（OI）选手，ID 为AquaRio。 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://blog.lushuyu.site) | [订阅地址](https://blog.lushuyu.site/about-me/feed) |
| <div id="B104" style="text-align: center;"><span>B104</span></div> | Xieisabug | 吃饭学家，复制学家，偷懒学家。 | [‣ 用js写卡牌游戏（十） \| 2026-01-06](https://www.xiejingyang.com/2026/01/06/%e7%94%a8js%e5%86%99%e5%8d%a1%e7%89%8c%e6%b8%b8%e6%88%8f%ef%bc%88%e5%8d%81%ef%bc%89/)<br/>[‣ 2025.12 AI使用有感 \| 2026-01-06](https://www.xiejingyang.com/2025/12/21/2025-12-ai%e4%bd%bf%e7%94%a8%e6%9c%89%e6%84%9f/) | [订阅地址](https://www.xiejingyang.com/feed/) |
| <div id="B105" style="text-align: center;"><span>B105</span></div> | Ryu Zheng 郑泽鑫的博客 |   一个生信工作者的独立博客 | [‣ 使用 Github Actions 自动更新 ANNOVAR 的 Clinvar 数据库 \| 2021-06-14](https://zhengzexin.com/archives/automatic_update_Clinvar_db_for_ANNOVAR/)<br/>[‣ 2020 年终总结 \| 2021-06-14](https://zhengzexin.com/archives/Summary_of_2020/) | [订阅地址](https://zhengzexin.com/feed/index.xml) |
| <div id="B106" style="text-align: center;"><span>B106</span></div> | 轶哥 |   妄图改变世界的全栈程序员。 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.wyr.me) | [订阅地址](https://www.wyr.me/rss.xml) |
| <div id="B107" style="text-align: center;"><span>B107</span></div> | 清竹茶馆 |  技术分享,前端开发,生活杂谈 | [‣ 读完 DeepSeek-V4 技术报告：这次最值得看的，不是“更大”，而是“更省” \| 2026-04-24](https://blog.vadxq.com/article/deepseek-v4-report-read/)<br/>[‣ Codex Skills 不是 Prompt 的升级版，而是写给 AI 的岗位 SOP \| 2026-04-24](https://blog.vadxq.com/article/codex-skills-are-ai-sops/) | [订阅地址](https://blog.vadxq.com/atom.xml) |
| <div id="B108" style="text-align: center;"><span>B108</span></div> | 隋堤倦客 |  我挥舞着键盘和本子，发誓要把这世界写个明明白白！！！ | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://fengxu.ink) | [订阅地址](https://fengxu.ink/atom.xml) |
| <div id="B109" style="text-align: center;"><span>B109</span></div> | 维基萌  |  萌即是正义！一名热爱acg的前端设计师的小站！  | [‣ Steam Frame 突然就发售了 \| 2026-09-15](https://www.wikimoe.com/post/t-tles4wwa)<br/>[‣ 今日的农家乐体验 \| 2026-09-15](https://www.wikimoe.com/post/t-tlaxi45t) | [订阅地址](https://www.wikimoe.com/rss.php) |
| <div id="B110" style="text-align: center;"><span>B110</span></div> | StrongWong  |  Embedded Software Engineer. Blogging about tech and life.  | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://blog.strongwong.top) | [订阅地址](https://blog.strongwong.top/atom.xml) |
| <div id="B111" style="text-align: center;"><span>B111</span></div> | 保罗的小宇宙  |  Still single, still lonely.  | [‣ 奇趣影棚项目 Vibe Coding 第一天问题记录 \| 2026-06-18](https://paugram.com/coding/vibe-coding-day-1.html)<br/>[‣ 失业后的一次前端面试经历 \| 2026-06-18](https://paugram.com/coding/tech-interview-2026-1.html) | [订阅地址](https://paugram.com/feed/) |
| <div id="B112" style="text-align: center;"><span>B112</span></div> | Mobility  |  聚沙成塔  | [‣ Flint：让 skill 成为个人资产 \| 2026-09-14](https://lichuanyang.top/posts/29684/)<br/>[‣ 从薅 token 到管 skill：我的 pks 工具落地实践 \| 2026-09-14](https://lichuanyang.top/posts/34689/) | [订阅地址](https://lichuanyang.top/atom.xml) |
| <div id="B113" style="text-align: center;"><span>B113</span></div> | Not LSD  |  A man cannot be described. He is not LSD.  | [‣ MacOS Solution - External Drive Cannot Mount After Plug Off without Eject \| 2020-08-31](http://notlsd.com/2020/09/01/macos-external-drive-renew/)<br/>[‣ 汝之图非吾之骥-「俞军产品方法论」书摘兼书评 \| 2020-08-31](http://notlsd.com/2020/09/01/yu-jun-product-methodology/) | [订阅地址](https://notlsd.github.io/atom.xml) |
| <div id="B114" style="text-align: center;"><span>B114</span></div> |  MikeoPerfect's Diary  |  故事太多，需要找个地方记录一下  | [‣ 值得纪念的一天 \| 2026-03-30](https://blog.mikeoperfect.com/posts/44605/)<br/>[‣ 关于结婚、生娃和育娃 \| 2026-03-30](https://blog.mikeoperfect.com/posts/25211/) | [订阅地址](https://blog.mikeoperfect.com/atom.xml) |
| <div id="B115" style="text-align: center;"><span>B115</span></div> |  爪哇堂 JavaTang  |  荣辱不惊闲看庭前花开花谢，去留无意漫随天外云卷云舒  | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.javatang.com) | [订阅地址](https://www.javatang.com/feed) |
| <div id="B116" style="text-align: center;"><span>B116</span></div> |  暗无天日  |  DarkSun的个人博客  | [‣ Emacs 31.1 发布速览：没有大功能，但你的配置可以变短了 \| 2026-08-26](https://lujun9972.github.io/blog/2026/08/25/emacs-31.1-发布速览：没有大功能，但你的配置可以变短了/index.html)<br/>[‣ 用 /proc/pid/fd 追踪进程网络连接 \| 2026-08-26](https://lujun9972.github.io/blog/2026/07/22/用-proc-pid-fd-追踪进程网络连接/index.html) | [订阅地址](https://www.lujun9972.win/rss.xml) |
| <div id="B117" style="text-align: center;"><span>B117</span></div> |  Grayson's Blog  |  Grayson's Blog   | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://blog.grayson.org.cn) | [订阅地址](http://blog.grayson.org.cn/feed.xml) |
| <div id="B118" style="text-align: center;"><span>B118</span></div> |  格物致知  |  专注于分享后端相关的技术以及设计架构思想，偶尔写一些生活和前端相关的东西   | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://liqiang.io) | [订阅地址](https://liqiang.io/atom.xml) |
| <div id="B119" style="text-align: center;"><span>B119</span></div> |  黄琦雲的博客  |  心中本没有路，用双手敲写康庄大道。知之甚少，学之甚多，生命不休，求索不止。   | [‣ SSH协议中隧道与代理的用法详解 \| 2022-07-17](https://knightyun.github.io/2022/07/17/tools-ssh-tunnel)<br/>[‣ 后记：菠菜站点的攻克之旅 \| 2022-07-17](https://knightyun.github.io/2021/12/06/exploit-penetrate-bocai-website) | [订阅地址](https://knightyun.github.io/feed.xml) |
| <div id="B120" style="text-align: center;"><span>B120</span></div> |  阳志平的网志 |  致力于认知科学的产品开发、课程设计与科学传播。   | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.yangzhiping.com) | [订阅地址](https://www.yangzhiping.com/feed.xml) |
| <div id="B121" style="text-align: center;"><span>B121</span></div> |  落园 |  专注经济视角下的互联网   | [‣ 二十而已 \| 2026-08-21](https://loyhome.com/%e4%ba%8c%e5%8d%81%e8%80%8c%e5%b7%b2/)<br/>[‣ 夏日见闻 \| 2026-08-21](https://loyhome.com/%e5%a4%8f%e6%97%a5%e8%a7%81%e9%97%bb/) | [订阅地址](https://www.loyhome.com/feed/) |
| <div id="B122" style="text-align: center;"><span>B122</span></div> |  Her Blue |  一个摄影博主，设立了自己的摄影品牌「她的蓝」有没有那么一首诗篇，找不到句点   | [‣ 照片，究竟是留给自己，还是展示给别人 \| 2026-07-13](https://her.blue/zhao-pian-jiu-jing-shi-liu-gei-zi-ji-huan-shi-zhan-shi-gei-bie-ren/)<br/>[‣ 当 S-Log3 不再稀缺，我还需要留着相机吗？ \| 2026-07-13](https://her.blue/dang-s-log3-bu-zai-xi-que-wo-huan-xu-yao-liu-zhao-xiang-ji-ma/) | [订阅地址](https://her.blue/rss/) |
| <div id="B123" style="text-align: center;"><span>B123</span></div> |  伪医生律师的博客 |  记录、生活、思考   | [‣ 野生菌真是大自然的绝佳馈赠 \| 2026-08-25](https://chidd.net/2026/08/25/ye-sheng-jun.html)<br/>[‣ 一场互联网的狂欢——“走个面儿”的问题 \| 2026-08-25](https://chidd.net/2026/08/20/niu-lai.html) | [订阅地址](https://chidd.net/feed) |
| <div id="B124" style="text-align: center;"><span>B124</span></div> |  ZWWoOoOo |   一个折腾WordPress多年的开发者, 博客里有众多 WordPress技术教程分享   | [‣ 非球迷看世界杯方式竟然不给了 \| 2026-06-17](https://zww.me/28279.zsay)<br/>[‣ 更新到 WordPress 7.0，都 7.0 了……眼睛都出问题了 \| 2026-06-17](https://zww.me/28274.zsay) | [订阅地址](https://zww.me/feed) |
| <div id="B125" style="text-align: center;"><span>B125</span></div> |  水八口的冥想盆 |   一位居住在日本的女开发者   | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://blog.shuiba.co) | [订阅地址](https://blog.shuiba.co/feed) |
| <div id="B126" style="text-align: center;"><span>B126</span></div> |  失眠海峡 |   我要与你坦诚相见   | [‣ 熊猫小A: 人生呐，就是关关难过关关过！ \| 2026-05-27](https://blog.imalan.cn/archives/memo-20260528-0000/)<br/>[‣ 音浪太强不晃会被撞到地上 \| 2026-05-27](https://blog.imalan.cn/archives/dance-to-the-music/) | [订阅地址](https://blog.imalan.cn/feed/index.xml) |
| <div id="B127" style="text-align: center;"><span>B127</span></div> |  千古壹号的博客 |   一个京东前端工程师   | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://qianguyihao.com) | [订阅地址](https://qianguyihao.com/atom.xml) |
| <div id="B128" style="text-align: center;"><span>B128</span></div> |  涛叔 |   互联网从业者，专注效率工具和思维方法   | [‣ 友链可能导致网站掉备案 \| 2026-09-06](https://tao.zz.ac/beian-2.html)<br/>[‣ 基于 Nginx + GeoLite2 搭建简易 IP 查询工具 \| 2026-09-06](https://tao.zz.ac/zz/ip.html) | [订阅地址](https://taoshu.in/feed.xml) |
| <div id="B129" style="text-align: center;"><span>B129</span></div> |  可能吧 |   有趣有用的互联网趋势   | [‣ 那么，我是如何使用 ChatGPT 的 \| 2024-01-24](https://kenengba.com/post/3800.html)<br/>[‣ 阿禅与摩托车，没有维修艺术 \| 2024-01-24](https://kenengba.com/post/3781.html) | [订阅地址](https://feeds.feedburner.com/kenengbarss) |
| <h2 id="数码">数码</h2> |  |   |  |
| D001 | 少数派 | 少数派致力于更好地运用数字产品或科学方法，帮助用户提升工作效率和生活品质 | [‣ 社区速递 158 \| 便宜耐造的副厂手柄与大学宿舍里那些相见恨晚的装备 \| 2026-09-15](https://sspai.com/post/114613)<br/>[‣ 具透 \| 精心优化， 体验感愉悦升华：iOS 27 中值得关注的新特性 \| 2026-09-15](https://sspai.com/post/114565)  |  [订阅地址](https://sspai.com/feed) | 
| D002 | 数字尾巴 | 分享美好数字生活 | [‣ 赴一场出行的科技漫游 \| 比亚迪&数字尾巴活动回顾 \| 2026-08-19](http://www.dgtle.com/article-1734270-1.html)<br/>[‣ 【回顾】一起 "Glow"！WWDC26 尾巴分享会 \| 2026-08-19](http://www.dgtle.com/article-1730623-1.html)  |  [订阅地址](https://www.dgtle.com/rss/dgtle.xml) | 
| D003 | Chiphell  | 分享与交流用户体验 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.chiphell.com)  |  [订阅地址](https://www.chiphell.com/portal.php?mod=rss)  | 
| <h2 id="IT团队博客">IT团队博客</h2> |  |   |  |
| I001 | AlloyTeam | 腾讯全端AlloyTeam团队的技术博客 | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://www.alloyteam.com)  |  [订阅地址](http://www.alloyteam.com/feed/) | 
| I002 | 奇舞周刊 | 360前端团队博客，领略前端技术，阅读奇舞周刊  | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://weekly.75.team)  |  [订阅地址](https://weekly.75.team/rss) | 
| I004 | 淘系前端团队 | 淘宝团队技术博客 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://fed.taobao.org)  |  [订阅地址](https://fed.taobao.org/atom.xml) | 
| I005 | 字节跳动团队技术博客 | 字节跳动团队技术博客 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://blog.csdn.net)  |  [订阅地址](https://blog.csdn.net/ByteDanceTech/rss/list) | 
| I006 | 美团技术团队博客 | 美团技术团队博客 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://tech.meituan.com)  |  [订阅地址](https://tech.meituan.com/feed/)  | 
| I007 | 云音乐大前端专栏 | 网易云音乐大前端专栏 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://musicfe.dev)  |  [订阅地址](https://musicfe.dev/rss)  | 
| I008 | 百度 FEX 团队 | FEX 技术周刊 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://fex.baidu.com)  |  [订阅地址](https://fex.baidu.com/feed.xml)  | 
| I009 | JDC  | 京东设计中心 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://jdc.jd.com)  |  [订阅地址](https://jdc.jd.com/feed)  | 
| I010 | 凹凸实验室  | 凹凸技术揭秘 · 技术精进与业务发展两不误 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://aotu.io)  |  [订阅地址](https://aotu.io/atom.xml)  | 
| RH001 | Augment Code - Blog | AI Development Blog | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://rsshub:1200) | [订阅地址](http://rsshub:1200/augmentcode/blog) |
| RH002 | Anthropic - Engineering | Anthropic Engineering | [‣ How we contain Claude across products \| 2026-05-24](https://www.anthropic.com/engineering/how-we-contain-claude)<br/>[‣ An update on recent Claude Code quality reports \| 2026-05-24](https://www.anthropic.com/engineering/april-23-postmortem) | [订阅地址](http://rsshub:1200/anthropic/engineering) |
| RH003 | Apache APISIX 博客 | Blog | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://rsshub:1200) | [订阅地址](http://rsshub:1200/apache/apisix/blog) |
| RH004 | 30 Seconds of code | New and popular code snippets | [‣ Cherry-pick an unreachable GitHub commit \| 2026-04-02](https://www.30secondsofcode.org/git/s/cherry-pick-unreachable-github-commit)<br/>[‣ A better alternative to force pushing \| 2026-04-02](https://www.30secondsofcode.org/git/s/force-push-better-alternative) | [订阅地址](http://rsshub:1200/30secondsofcode/latest) |
| <h2 id="公司官方新闻">公司官方新闻</h2> |  |   |  |
| C001 | Apple新闻 | Apple官方消息 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.apple.com)  |  [订阅地址](https://www.apple.com/newsroom/rss-feed.rss) |  
| <h2 id="互联网类">互联网类</h2> |  |   |  |
| H001 | 虎嗅 | 虎嗅网新闻 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.huxiu.com)  |  [订阅地址](https://www.huxiu.com/rss/0.xml) |  
| H002 | 36kr | 36氪 | [‣ 8点1氪丨8月一线城市房价上涨；携程上架510万一张的太空旅行船票；字节跳动上半年净利润出现下滑，但海外收入占比再创新高 🌈 2026-09-16](https://36kr.com/p/3985321952115717?f=rss)<br/>[‣ 科氪｜荣耀发布行业首个系统级Agent Harness架构操作系统MagicOS 11  Magic9首发搭载 🌈 2026-09-16](https://36kr.com/p/3984824416467976?f=rss)  |  [订阅地址](https://www.36kr.com/feed) |  
| H003 | 微软亚洲研究院 | 微软亚洲研究院技术博客 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.msra.cn)  |  [订阅地址](https://www.msra.cn/feed) | 
| H004 | 极客公园 | 极客公园  | [‣ 对话小宇宙 kyth：播客的护城河是真实，AI 无法取代的是人的立场 \| 2026-09-15](http://www.geekpark.net/news/370345)<br/>[‣ 给 AI 发外设，戴森派摄像头进嘴、绿联给充电宝开了扇窗 \| 2026-09-15](http://www.geekpark.net/news/370328)  |  [订阅地址](https://www.geekpark.net/rss) | 
| RH005 | 白鲸出海 - 资讯 | 白鲸出海资讯 | [‣ 恺英斥资20亿元参股娱美德，约定促成传奇IP独家授权协议 \| 2026-09-15](https://www.baijing.cn/article/56704)<br/>[‣ “电子挂件”出海爆单，5周狂揽400万元 \| 2026-09-15](https://www.baijing.cn/article/56705) | [订阅地址](http://rsshub:1200/baijing/article) |
| <h2 id="金融类">金融类</h2> |  |   |  |
| F001 | 雪球 | 聪明的投资者都在这里,雪球每日精华 | [‣ 以未来股价为导向的投资方式 \| 2026-09-15](http://xueqiu.com/1553799558/409306793)<br/>[‣ 中远海控2026年三季报业绩前瞻 \| 2026-09-15](http://xueqiu.com/5742821612/409277558)  |  [订阅地址](https://xueqiu.com/hots/topic/rss) |  
| RH006 | 百度 - 首页指数 | 百度股市通 | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://rsshub:1200) | [订阅地址](http://rsshub:1200/baidu/gushitong/index) |
| RH007 | AInvest - Latest Article | AInvest latest articles | [‣ Current Mortgage Rates Hit 7% As Oil Prices And Fed Hikes Push Yields Higher 🌈 2026-09-16](https://www.ainvest.com/news/current-mortgage-rates-hit-7-oil-prices-fed-hikes-push-yields-higher-2609/)<br/>[‣ Rackspace Jumps 11.5% as Wall Street Stays Neutral 🌈 2026-09-16](https://www.ainvest.com/news/rackspace-jumps-11-5-wall-street-stays-neutral-2609/) | [订阅地址](http://rsshub:1200/ainvest/article) |
| RH008 | AInvest - Latest News | AInvest latest news | [‣ Current Mortgage Rates Hit 7% As Oil Prices And Fed Hikes Push Yields Higher 🌈 2026-09-16](https://www.ainvest.com/news/current-mortgage-rates-hit-7-oil-prices-fed-hikes-push-yields-higher-2609/)<br/>[‣ Rackspace Jumps 11.5% as Wall Street Stays Neutral 🌈 2026-09-16](https://www.ainvest.com/news/rackspace-jumps-11-5-wall-street-stays-neutral-2609/) | [订阅地址](http://rsshub:1200/ainvest/news) |
| RH009 | 财新 - 财新数据通 | 财新数据通专享资讯 | [‣ 【权益周观察】市场成交连续缩量 机构寄望“预防性加息”落地减扰 \| 2026-09-15](https://database.caixin.com/2026-09-15/102485061.html)<br/>[‣ 【市场动态】10年期美债收益率三年来首次升破5% 通胀和融资担忧双重夹击 \| 2026-09-15](https://database.caixin.com/2026-09-15/102484936.html) | [订阅地址](http://rsshub:1200/caixin/database) |
| RH010 | 财新 - 财新周刊 | 财新周刊 | [‣ 《财新周刊》第1223期 \| 2026-09-13](https://weekly.caixin.com/2026/cw1223/)<br/>[‣ 《财新周刊》第1222期 \| 2026-09-13](https://weekly.caixin.com/2026/cw1222/) | [订阅地址](http://rsshub:1200/caixin/weekly) |
| RH011 | 财新 - 首页新闻 | 财新网首页 | [‣ 8月经济运行图景 \| 2026-09-15](https://opinion.caixin.com/2026-09-16/102485264.html)<br/>[‣ 清仓万物云股票套现逾2亿港元 58同城董事长姚劲波涉违规售股 \| 2026-09-15](https://www.caixin.com/2026-09-15/102485235.html) | [订阅地址](http://rsshub:1200/caixin/article) |
| RH012 | 链新闻 ABMedia | ABMedia 最新消息 | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://rsshub:1200) | [订阅地址](http://rsshub:1200/abmedia/index) |
| <h2 id="科技类">科技类</h2> |  |   |  |
| T001 | Hack News | 极其优质的极客新闻 | [‣ Introducing System One Models and Jev \| 2026-09-15](https://typesafe.ai/blog/introducing-system-one-models-and-jev)<br/>[‣ Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations \| 2026-09-15](https://github.com/arnegiacomo/fugleramme)  |  [订阅地址](https://news.ycombinator.com/rss) |  
| T002 | 奇客Solidot–传递最新科技情报 | 奇客的资讯，重要的东西 | [‣ 夜晚睡眠光照太亮可能会损伤心脏 \| 2026-09-15](https://www.solidot.org/story?sid=85388)<br/>[‣ 出于兴趣阅读有助于促进终身的身心健康 \| 2026-09-15](https://www.solidot.org/story?sid=85387)  |  [订阅地址](https://www.solidot.org/index.rss) |  
| T003 | 环球科学 | 科学美国人中文版，一些科普文章 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://feedx.net)  |  [订阅地址](https://feedx.net/rss/huanqiukexue.xml) |
| T004 | MIT 科技评论 | MIT 科技评论 本周热榜 | [‣ 真能戴出门的脑机接口来了？长得像普通毛线帽，戴上就能意念打字 \| 2026-09-15](https://www.mittrchina.com/news/detail/16957)<br/>[‣ 听“上帝”的话发币，这对夫妻把500多人带进了加密深坑 \| 2026-09-15](https://www.mittrchina.com/news/detail/16952)  |  [订阅地址](http://rsshub:1200/mittrchina/hot) |  
| T005 | 产品运营 | 产品运营 - 人人都是产品经理 | [‣ 从”边卖边补”到”准备好再卖”：产品商品化的四步闭环 \| 2026-09-15](https://www.woshipm.com/operate/6464859.html)<br/>[‣ 业务系统里，你的“用户”真的是用户吗？ \| 2026-09-15](https://www.woshipm.com/operate/6464313.html)  |  [订阅地址](http://www.woshipm.com/category/operate/feed) |  
| T006 | 产品经理  | 产品经理 – 人人都是产品经理 | [‣ 深度：产品经理要守住产品边界！为什么会这么难？ \| 2026-09-08](https://www.woshipm.com/pmd/6461254.html)<br/>[‣ 产品经理的三思之道：思危、思退、思变 \| 2026-09-08](https://www.woshipm.com/pmd/6459338.html)  |  [订阅地址](http://www.woshipm.com/category/pmd/feed) |  
| T007 | 产品100  | 产品人学习成长社区 | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://www.chanpin100.com)  |  [订阅地址](http://www.chanpin100.com/feed) |  
| T008 | 蓝卡  | 美好科技生活方式 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.lanka.cn)  |  [订阅地址](https://www.lanka.cn/feed) |  
| T009 | APPDO数字生活指南  | Simon的自留地_数码_App_羊毛_相机_数字指南 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://simonword.com)  |  [订阅地址](https://simonword.com/feed) |  
| RH013 | InfoQ 中文 - 推荐 | InfoQ 推荐 | [‣ 129亿美元卖身英伟达之后，是时候重新理解Hugging Face了 🌈 2026-09-16](https://www.infoq.cn/article/foEzSr8xfG0STQ1wgbti)<br/>[‣ 缓存不该困在一台服务器里 🌈 2026-09-16](https://www.infoq.cn/article/zfjt89uVj0EGxf6aeaw4) | [订阅地址](http://rsshub:1200/infoq/recommend) |
| RH014 | Anthropic - News | Anthropic News | [‣ Developing Enterprise Frontier Safeguards with our customers \| 2026-08-31](https://www.anthropic.com/news/enterprise-frontier-safeguards)<br/>[‣ Improving our alignment and security efforts \| 2026-08-31](https://www.anthropic.com/news/improving-alignment-security-efforts) | [订阅地址](http://rsshub:1200/anthropic/news) |
| RH015 | OpenAI - Research | OpenAI Research | [‣ On the Navier–Stokes Millennium Prize Problem \| 2026-09-08](https://openai.com/index/navier-stokes-solution/)<br/>[‣ Research acceleration: The view inside OpenAI \| 2026-09-08](https://openai.com/index/research-acceleration-view-inside-openai/) | [订阅地址](http://rsshub:1200/openai/research) |
| RH016 | OpenAI - News | OpenAI News | [‣ How Fyxer built an AI executive assistant people trust \| 2026-09-14](https://openai.com/index/fyxer/)<br/>[‣ Perplexity trusts GPT-6 Astra with end-to-end systems \| 2026-09-14](https://openai.com/index/perplexity-improving-accuracy-with-astra/) | [订阅地址](http://rsshub:1200/openai/news) |
| RH017 | AI工具集 - 每日AI资讯 | 每日 AI 资讯 | [‣ 上海 AI Lab 开源多模态基础大模型「书生-S2」 \| 2026-09-14](https://mp.weixin.qq.com/s/EZghVJB13rJTRfBv2_U0Xw)<br/>[‣ 宇树开源通用人形基础模型UnifoLM-WLA-1.0 \| 2026-09-14](https://mp.weixin.qq.com/s/TkbZMqKTIS5FVqBdzO2a7A) | [订阅地址](http://rsshub:1200/ai-bot/daily-ai-news) |
| RH018 | AIbase - 资讯 | AI 新闻资讯 | [‣ 阶跃星辰王炸发布 StepAudio 3 系列语音大模型，强势斩获多项全球第一！ \| 2026-09-15](https://www.aibase.com/zh/news/31066)<br/>[‣ ​加拿大研究员呼吁无限期暂停前沿 AI 研发：否则人类灭绝“只是时间问题” \| 2026-09-15](https://www.aibase.com/zh/news/31065) | [订阅地址](http://rsshub:1200/aibase/news) |
| RH019 | AIbase - AI日报 | AI 日报 | [‣ AI日报：Claude Opus 5.2 灰测；苹果正式推送 iOS27；微信回应小微AI隐私争议 \| 2026-09-15](https://www.aibase.com/zh/news/31064)<br/>[‣ AI日报：豆包手机助手消费者版发布；Suno发布v6音乐模型；ElevenLabs发布Music v2.5音频模型 \| 2026-09-15](https://www.aibase.com/zh/news/31034) | [订阅地址](http://rsshub:1200/aibase/daily) |
| RH020 | 少数派 - Matrix | 少数派 Matrix | [‣ 如何用飞书多维表格搭建一套小巧智能的 CRM \| 2026-09-14](https://sspai.com/post/114582)<br/>[‣ 让安卓系统日历支持 CalDAV 双向同步：DAVx5 + 钉钉、飞书日历实践 \| 2026-09-14](https://sspai.com/post/114520) | [订阅地址](http://rsshub:1200/sspai/matrix) |
| RH021 | 少数派 - 首页 | 少数派首页 | [‣ 社区速递 158 \| 便宜耐造的副厂手柄与大学宿舍里那些相见恨晚的装备 \| 2026-09-15](https://sspai.com/post/114613)<br/>[‣ 具透 \| 精心优化， 体验感愉悦升华：iOS 27 中值得关注的新特性 \| 2026-09-15](https://sspai.com/post/114565) | [订阅地址](http://rsshub:1200/sspai/index) |
| RH022 | 北京智源人工智能研究院 - 活动 | 智源社区活动 | [‣ 从个体智能到系统智能：多智能体时代的Graph Engineering技术全景解读 \| 2026-09-23](https://event.baai.ac.cn/activities/1086)<br/>[‣ 聚焦OPD mechanism，如何实现OPD高效工作 \| 2026-09-23](https://event.baai.ac.cn/activities/1085) | [订阅地址](http://rsshub:1200/baai/hub/events) |
| <h2 id="学习类">学习类</h2> |  |   |  |
| L001 | 扔物线 | 帮助 Android 工程师进阶成长 | [‣ 【性能优化】真有那么慢？Java 和 Kotlin 的反射 \| 2024-12-27](https://rengwuxian.com/reflection/)<br/>[‣ 【泛型 Plus】Kotlin 的加强版类型推断：@BuilderInference \| 2024-12-27](https://rengwuxian.com/fan-xing-plus-kotlin-de-jia-qiang-ban-lei-xing-tui-duan-builderinference/)  |  [订阅地址](https://rengwuxian.com/feed) |  
| L002 | MOOC中国 | 慕课改变你，你改变世界  | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.mooc.cn)  |  [订阅地址](https://www.mooc.cn/feed) |  
| <h2 id="学术类">学术类</h2> |  |   |  |
| A001 | 青柠学术 | 每个科研小白都有成为大神的潜力 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://iseex.github.io)  |  [订阅地址](https://iseex.github.io/feed) |  
| <h2 id="生活类">生活类</h2> |  |   |  |
| L001 | 李子柒 | 李子柒的微博 | [‣ 2024微博之夜线下奖项 \| 2025-01-11](https://weibo.com/2970452952/P96zzyizF)<br/>[‣ 2024#微博焕新非遗盛典# 多彩非遗，共生共享。在微博，让我们一起探索#蜀不尽的非遗#，感受那些在历史长河中熠熠生辉的千年瑰宝，传承东方魅力！#天府非遗周# \| 2025-01-11](https://weibo.com/2970452952/P09BmgMwb)  |  [订阅地址](http://rsshub:1200/weibo/user/2970452952) |  
| L002 | 理想生活实验室 | 为更理想的生活 | [‣ 初秋在成都麓湖 CPI，和 BIRKENSTOCK 一起“自然行走” \| 2026-09-14](http://www.toodaylab.com/84206)<br/>[‣ 在《是枝裕和》里，从采访、对谈、别人的视角来认识一位“完整的导演” \| 2026-09-14](http://www.toodaylab.com/84205)  |  [订阅地址](https://www.toodaylab.com/rss) |  
| L003 | 一兜糖 | 家的主理人社区 | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://rsshub:1200)  |  [订阅地址](http://rsshub:1200/yidoutang/index) |
| RH023 | Bandcamp - Weekly | Bandcamp Weekly | [‣ Bandcamp Selects \| 2026-09-14](https://bandcamp.com/?show=999)<br/>[‣ The Metal Show \| 2026-09-14](https://bandcamp.com/?show=998) | [订阅地址](http://rsshub:1200/bandcamp/weekly) |
| RH024 | 深圳台风网 - 深圳天气直播 | 深圳天气直播 | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://rsshub:1200) | [订阅地址](http://rsshub:1200/121/weatherLive) |
| <h2 id="设计类">设计类</h2> |  |   |  |
| D001 | Behance |  Adobe旗下设计网站Behance | [‣ Editorial illustrations \| 2026-09-15](https://www.behance.net/gallery/255742367/Editorial-illustrations)<br/>[‣ Misty mornings in Kraków \| 2026-09-15](https://www.behance.net/gallery/255684893/Misty-mornings-in-Krakow)  |  [订阅地址](https://www.behance.net/feeds/projects) |  
| D002 | Behance官方博客 |  Behance官方博客 | [‣ How to Recover From Burnout \| 2022-07-01](https://medium.com/behance-blog/how-to-recover-from-burnout-d9d783a09c68?source=rss-f5272b7f3182------2)<br/>[‣ Meet This Month’s Guest Curator: AJ Jefferies \| 2022-07-01](https://medium.com/behance-blog/meet-this-months-guest-curator-aj-jeffries-df95220b780f?source=rss-f5272b7f3182------2)  |  [订阅地址](https://medium.com/feed/@behance) |  
| D003 | Pinterest |  图片设计社交 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://newsroom.pinterest.com)  |  [订阅地址](https://newsroom.pinterest.com/en/feed/posts.xml) |  
| D004 | 优设 |  优秀设计联盟-优设网-设计师交流学习平台-看设计文章，学软件教程，找灵感素材，尽在优设网！ | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.uisdc.com)  |  [订阅地址](https://www.uisdc.com/feed) |  
| D005 | 腾讯CDC | 腾讯用户研究与体验设计部 | [‣ 一篇不是很枯燥的ChatGPT闲谈 \| 2023-04-17](https://cdc.tencent.com/2023/04/17/%e4%b8%80%e7%af%87%e4%b8%8d%e6%98%af%e5%be%88%e6%9e%af%e7%87%a5%e7%9a%84chatgpt%e9%97%b2%e8%b0%88/)<br/>[‣ 聚合类工具产品设计指南 – 交互篇 \| 2023-04-17](https://cdc.tencent.com/2023/03/08/%e8%81%9a%e5%90%88%e7%b1%bb%e5%b7%a5%e5%85%b7%e4%ba%a7%e5%93%81%e8%ae%be%e8%ae%a1%e6%8c%87%e5%8d%97-%e4%ba%a4%e4%ba%92%e7%af%87/)  |  [订阅地址](https://cdc.tencent.com/feed/) | 
| D006 | ID公社 | 发现有意味的设计 | [‣ 在知乎想法上的一些即时分享 \| 2018-04-12](https://www.hi-id.com/?p=4340)<br/>[‣ 即食 13/18 \| 2018-04-12](https://www.hi-id.com/?p=4241)  |  [订阅地址](http://feeds.feedburner.com/ID) | 
| D007 | 摄影世界 | 你的随身摄影杂志 | [‣ “国社之镜·世纪光影——人民城市·幸福图景” 城市主题展征稿启事 \| 2026-09-10](https://www.photoworld.com.cn/post/181505)<br/>[‣ 索尼发布电影摄影机遥控单元 RM-DP7、DP5 操控更高效 \| 2026-09-10](https://www.photoworld.com.cn/post/181538)  |  [订阅地址](https://feedx.net/rss/photoworld.xml) | 
| D008 | Design Milk | Design Milk 是一个分享现代设计与生活方式灵感的网站 | [‣ 7 South African Designers to Know From Maison&Objet 2026 \| 2026-09-15](https://design-milk.com/south-african-designers-maison-objet-2026/)<br/>[‣ Venus Williams Serves Up a New Collection With Crate & Barrel \| 2026-09-15](https://design-milk.com/venus-williams-crate-barrel-grand-slam-collection/)  |  [订阅地址](https://design-milk.com/feed/) |
| D009 | Smashing Magazine | Magazine on CSS, JavaScript, front-end, accessibility, UX and design. For developers, designers and front-end engineers.s | [‣ Building A UX ROI Case That Survives The Boardroom \| 2026-09-11](https://smashingmagazine.com/2026/09/building-ux-roi-case-survives-boardroom/)<br/>[‣ The Death Of The Button: Why The Best Interface Is No Interface \| 2026-09-11](https://smashingmagazine.com/2026/09/death-button-why-best-interface-is-no-interface/)  |  [订阅地址](https://www.smashingmagazine.com/feed/) |
| RH025 | Apple - Design updates | Apple design updates | [‣ Designing for iPhone Duo \| 2026-09-08](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)<br/>[‣ Layout \| 2026-09-08](https://developer.apple.com/design/human-interface-guidelines/layout) | [订阅地址](http://rsshub:1200/apple/design) |
| <h2 id="内容平台">内容平台</h2> |  |   |  |
| C001 | 知乎 | 知乎每日精选 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.zhihu.com)  |  [订阅地址](https://www.zhihu.com/rss) |  
| C002 | 湾区日报 | 关注创业与技术，每天推送3到5篇优质英文文章 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://wanqu.co)  |  [订阅地址](https://wanqu.co/feed/) |  
| C003 | 爱范儿 | 让未来触手可及 | [‣ 19.98 万元起，吉利银河战舰 700 开启预售，最高 1129 匹马力，还有三电机四驱 \| 2026-09-15](https://www.ifanr.com/1680277?utm_source=rss&utm_medium=rss&utm_campaign=)<br/>[‣ 号称人类造的最后一个 AI 要来了，刷屏全网的 RSI 是什么 \| 2026-09-15](https://www.ifanr.com/1679813?utm_source=rss&utm_medium=rss&utm_campaign=)  |  [订阅地址](https://www.ifanr.com/feed) |  
| C004 | 小众软件 | 小众软件RSS | [‣ 高性价比（廉价）SSD VPS 提供商 CloudCone，最低 96 元人民币/年｜再次补货 \| 2026-09-15](https://www.appinn.com/cloudcone-ssd-vps/)<br/>[‣ 限免：DearMob iPhone Manager – iPhone/iPad 照片、视频传输，应用安装、整机备份恢复、换机工具\[Win/macOS\] \| 2026-09-15](https://www.appinn.com/5kplayer-iphone-manager/)  |  [订阅地址](https://www.appinn.com/feed/) |  
| C005 | 199IT | 互联网数据资讯网 | [‣ IEA：2026年全球能源投资报告 \| 2026-09-15](http://www.199it.com/archives/1833203.html)<br/>[‣ AI重塑劳动力培训：技能革命与终身学习新时代 \| 2026-09-15](http://www.199it.com/archives/1840858.html)  |  [订阅地址](https://www.199it.com/feed) |  
| C006 | IT之家 | IT之家 - 软媒旗下网站 | [‣ EA《双人成行》10 月 15 日登陆任天堂 Switch 2：新增好友通行证跨平台功能，部分地区老玩家可免费升级 🌈 2026-09-16](https://www.ithome.com/1/002/850.htm)<br/>[‣ 苹果 M6 Mac mini 跑分曝光：单核较 M4 款高 24%、多核高 48% 🌈 2026-09-16](https://www.ithome.com/1/002/849.htm)  |  [订阅地址](https://www.ithome.com/rss) |  
| C007 | HelloGitHub 月刊 | 一切出于兴趣。兴趣是最好的老师，HelloGitHub 就是帮你找到编程的兴趣。 | [‣ HelloGitHub 第 125 期 \| 2026-08-28](https://hellogithub.com/periodical/volume/125)<br/>[‣ HelloGitHub 第 124 期 \| 2026-08-28](https://hellogithub.com/periodical/volume/124)  |  [订阅地址](https://hellogithub.com/rss) |  
| C008 | 蠎周刊 | Python各种Weekly中译版。 | [‣ 上周蠎超赞 26w36 #537 \| 2026-09-13](https://weekly.pychina.org/awesomepw/awesome-pw-537.html)<br/>[‣ 上周蠎超赞 26w35 #536 \| 2026-09-13](https://weekly.pychina.org/awesomepw/awesome-pw-536.html)  |  [订阅地址](https://weekly.pychina.org/feeds/all.atom.xml) |  
| C009 | WordPress大学 | WordPress建站资源平台 | [‣ 说说无聊的 WordPress 浏览器扩展 \| 2026-08-18](https://www.wpdaxue.com/wordpress-browser-extension.html)<br/>[‣ WordPress 惊爆 wp2shell 重磅漏洞，请马上升级！ \| 2026-08-18](https://www.wpdaxue.com/wordpress-wp2shell.html)  |  [订阅地址](https://www.wpdaxue.com/feed) |  
| C010 | Linux中国 | Linux中文开源社区 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://linux.cn)  |  [订阅地址](https://linux.cn/rss.xml) |  
| C011 | V2EX | 创意工作者的社区 | [‣ \[Apple\] 解决 b 站 iPad 应用发烫卡顿的终极方案 \| 2026-09-15](https://www.v2ex.com/t/1242287#reply6)<br/>[‣ \[职场话题\] 坐标深圳，在 boss 上打了招呼，几乎没人回，已读都没几个 \| 2026-09-15](https://www.v2ex.com/t/1242286#reply0)  |  [订阅地址](https://www.v2ex.com/index.xml) |  
| C012 | 酷壳(左耳朵耗子) | 酷 壳RSS | [‣ 是微服务架构不香还是云不香？ \| 2023-05-08](https://coolshell.cn/articles/22422.html)<br/>[‣ 我看ChatGPT: 为啥谷歌掉了千亿美金 \| 2023-05-08](https://coolshell.cn/articles/22398.html)  |  [订阅地址](https://coolshell.cn/feed) |  
| C013 | 豆瓣 | 豆瓣最受欢迎的影评 | [‣ 反类型游戏 (评论: 杀死比尔：血色全传) \| 2026-09-15](https://movie.douban.com/review/17816882/)<br/>[‣ 不是风骨是封建 (评论: 兰香如故) \| 2026-09-15](https://movie.douban.com/review/17812711/)  |  [订阅地址](https://www.douban.com/feed/review/movie) |  
| C014 | 豆瓣 | 豆瓣最受欢迎的书评 | [‣ 他只是脚痛，不是脚臭 (评论: 走在蓝色的田野上) \| 2026-09-15](https://book.douban.com/review/17816791/)<br/>[‣ 译校序——1804知识学二轮讲课已译校完毕并制作PDF (评论: Philosophische Bibliothek, Bd.284, Die Wissenschaftslehre, Zweiter Vortrag im Jahre 1804 vom 16. April - 8. Juni.) \| 2026-09-15](https://book.douban.com/review/17816365/)  |  [订阅地址](https://www.douban.com/feed/review/book) |  
| C015 | 豆瓣 | 豆瓣最受欢迎的乐评 | [‣ 邪·道 (评论: 不信邪) \| 2026-09-15](https://music.douban.com/review/17817390/)<br/>[‣ linernotes (评论: Action) \| 2026-09-15](https://music.douban.com/review/17817381/)  |  [订阅地址](https://www.douban.com/feed/review/music) |  
| C016 | 开源中国 | 开源中国社区推荐文章 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.oschina.net)  |  [订阅地址](https://www.oschina.net/blog/rss) |  
| C017 | 博客园 | 博客园精华区 | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://feed.cnblogs.com)  |  [订阅地址](http://feed.cnblogs.com/blog/picked/rss) |  
| C018 | 博客园 | 博客园首页 | [‣ Git 提交代码：从报错到 SSH 免密推送 - AlfredZhao \| 2026-09-15](https://www.cnblogs.com/jyzhao/p/22990250)<br/>[‣ 模型聪明了 10 倍，为什么你的 Agent 每天还在过《土拨鼠之日》？ - Swizard \| 2026-09-15](https://www.cnblogs.com/swizard/p/22990047)  |  [订阅地址](http://feed.cnblogs.com/blog/sitehome/rss) |  
| C019 | PTT(台湾论坛) | PTT电影专题 | [‣ \[新聞\] 網紅老爸3週票房逼近7000萬 演員基隆廟口參拜催票人氣旺 \| 2026-09-15](https://www.ptt.cc/bbs/movie/M.1789487848.A.8FA.html)<br/>[‣ \[新聞\] 粽邪4請鍾馗巡迴戲院 鐵粉刷片20次 \| 2026-09-15](https://www.ptt.cc/bbs/movie/M.1789487518.A.928.html)  |  [订阅地址](https://www.ptt.cc/atom/movie.xml) |  
| <div id="C021" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/C021.png" width="30px" style="width:30px;height: auto;"/><br><span>C021</span></div> | 吾爱破解 | 吾爱破解精品软件区 | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://rsshub:1200)  |  [订阅地址](http://rsshub:1200/discuz/x/https%3a%2f%2fwww.52pojie.cn%2fforum-16-1.html) |  
| <div id="C022" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/C022.png" width="30px" style="width:30px;height: auto;"/><br><span>C022</span></div> | cnBeta.COM 精彩优秀评论 | 从cnBeta每天数千评论中精选出来的优秀评论 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.cnbeta.com)  |  [订阅地址](https://www.cnbeta.com/commentrss.php) |  
| <div id="C023" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/C023.png" width="30px" style="width:30px;height: auto;"/><br><span>C023</span></div> | 比特客栈的文艺复兴 | We do not choose who we are, but we do choose who we become. | [‣ 次世代动画的狂想曲 \| 2026-07-05](https://bitinn.net/11829/)<br/>[‣ 在加速世界里，寻找永恒浪漫 \| 2026-07-05](https://bitinn.net/11808/)  |  [订阅地址](https://bitinn.net/feed/) |  
| C024 | Pixiv(艺术家社区) | 男性向作品排行 - 前20 | [‣ 突撃！ヒナ委員長のあさごはん！（スミカ担当） \| 2026-09-13](https://www.pixiv.net/artworks/149649297)<br/>[‣ とある楽園 \| 2026-09-13](https://www.pixiv.net/artworks/149656755)  |  [订阅地址](https://rakuen.thec.me/PixivRss/male-20) |
| C025 | Pixiv(艺术家社区) | 女性向作品排行 - 前20 | [‣ 松本透はゴリラ妻とプリティ娘とツンデレ息子を愛しすぎてる㉔ \| 2026-09-14](https://www.pixiv.net/artworks/149666606)<br/>[‣ 【ニンゲンの飼い方】新シーズン　第3話『さぁ出発だ』 \| 2026-09-14](https://www.pixiv.net/artworks/149652152)  |  [订阅地址](https://rakuen.thec.me/PixivRss/female-20) |
| C026 | Pixiv(艺术家社区) | Pixiv每日排行 - 前20 | [‣ 🌹ガールズ×ヴァンパイア🌹 \| 2026-09-12](https://www.pixiv.net/artworks/149596619)<br/>[‣ ロード・ログレス \| 2026-09-12](https://www.pixiv.net/artworks/149594560)  |  [订阅地址](http://rakuen.thec.me/PixivRss/daily-20) |  
| C027 | Pixiv(艺术家社区) | Pixiv每月排行 - 前20 | [‣ そのピッチリインナーは非常に素晴らしかった \| 2026-08-18](https://www.pixiv.net/artworks/148597100)<br/>[‣ Ronova \| 2026-08-18](https://www.pixiv.net/artworks/148574137)  |  [订阅地址](http://rakuen.thec.me/PixivRss/monthly-20) |  
| C028 | cnBeta | 中文业界资讯 | [‣ 1024：程序员的“青春饭”还稳吗？ \| 2022-10-26](https://m.cnbeta.com/view/1330241.htm)<br/>[‣ 这趟绿皮慢火车开了52年：26.5元从没涨过价 \| 2022-10-26](https://m.cnbeta.com/view/1329189.htm)  |  [订阅地址](https://feedx.net/rss/cnbetatop.xml) |  
| C029 | China Daily News | 中国每日新闻 | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://www.chinadaily.com.cn)  |  [订阅地址](http://www.chinadaily.com.cn/rss/cndy_rss.xml) |  
| C030 | MM范 | 妹子热门图 | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://rsshub:1200)  |  [订阅地址](http://rsshub:1200/95mm/tab/热门) |  
| C031 | CNU视觉联盟 | 每日精选 | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://rsshub:1200)  |  [订阅地址](http://rsshub:1200/cnu/selected) | 
| C032 | 香水时代 | 最新香水评论-发现香水圈的新鲜事 | [‣ ★★★★☆ 蔻依 仙境花园系列-北国雪松 Chloe Atelier des Fleurs Cedrus, 2019 \| 2026-09-15](https://www.nosetime.com/xiangshui/235939-atelier-des-fleurs-chloe-cedrus.html)<br/>[‣ ★★★★☆ 恺芮得 拿破仑之水（成功） Creed Aventus, 2010 \| 2026-09-15](https://www.nosetime.com/xiangshui/503110-xinyang-chenggong-creed-aventus.html)  |  [订阅地址](http://rsshub:1200/nosetime/home) |  
| C033 | 恩山无线论坛  | 无线路由器爱好者的乐园 | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://rsshub:1200)  |  [订阅地址](http://rsshub:1200/right/forum/31) |  
| C034 | xLog | An open-source creative community written on the blockchain. | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://xlog.app)  |  [订阅地址](https://xlog.app/feed/hottest?interval=1) |  
| C035 | NodeSeek | 一个面向Web开发、主机托管、VPS/服务器等技术话题的极客社区 | [‣ 内存要涨到什么时候噶 🌈 2026-09-16](https://www.nodeseek.com/post-930980-1)<br/>[‣ 溢120+剩余价值 有的PM 再收台白丝4837 159款回来 🌈 2026-09-16](https://www.nodeseek.com/post-930979-1)  |  [订阅地址](https://rss.nodeseek.com/) |  
| N013 | 一亩三分地 - 分区-世界公民 | 分区 分区 id 留学申请 257 世界公民 379 投资理财 400 生活干货 31 职场达人 345 人际关系 391 海外求职 38 签证移民 265 分类 热门帖子 最新帖子 hot new 排序方式 最新回复 最新发布 post &#124; 示例：/1point3acres/section/345 &#124; 参数：id: 分区 id，见下表，默认为全部；type: 帖子分类, 见下表，默认为 hot，即热门帖子；order: 排序方式，见下表，默认为空，即最新回复 &#124; 源码：section.ts | [‣ 国内真是人间地狱 \| 2026-09-15](https://instant.1point3acres.com/thread/1189512)<br/>[‣ Troll大叔回国感悟 \| 2026-09-15](https://instant.1point3acres.com/thread/1189584) | [订阅地址](http://rsshub:1200/1point3acres/section/379/hot) |
| <h2 id="影视资源">影视资源</h2> |  |   |  |
| <div id="M001" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/M001.png" width="30px" style="width:30px;height: auto;"/><br><span>M001</span></div> | VIP影院 |  666影院 - 全网VIP电影免费看！ | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://bukaivip.com)  |  [订阅地址](https://bukaivip.com/rss) |  
| M002 | LimeTorrents |  Latest Torrents RSS | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.limetorrents.pro)  |  [订阅地址](https://www.limetorrents.pro/rss/) |
| M003 | Torlock |  种子站Torlock | [‣ \[SubsPlease\] BanG Dream! Yumemita (01-13) (1080p) \[Batch\] \| 2026-09-15](https://www.torlock.com/torrent/67856883/bang-dream%21-yumemita-%2801-13%29-%281080p%29-%5Bbatch%5D.html)<br/>[‣ The.Dog.Bite.Murders.2025.1080p.WEB-DL.H264-PlayfulDarkness.mkv \| 2026-09-15](https://www.torlock.com/torrent/67856882/the-dog-bite-murders-2025-1080p-web-dl-h264-playfuldarkness.html)  |  [订阅地址](https://www.torlock.com/rss.xml) | 
| M004 | YTS |  Most popular Torrents in the smallest file size | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://yts.mx)  |  [订阅地址](https://yts.mx/rss) | 
| M005 | RARBG |  种子站RARBG | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://rarbg.to)  |  [订阅地址](https://rarbg.to/rss.php) | 
| RH026 | 6v电影 - 最新电影 | 6v电影最新电影 | [‣ 2026动作《惩罚者》1080p.HD国语中字 \| 2026-09-14](https://www.hao6v.cc/dy/2026-09-15/50436.html)<br/>[‣ 2026科幻剧情《盒子里的羊》1080p.HD中字 \| 2026-09-14](https://www.hao6v.cc/dy/2026-09-14/50425.html) | [订阅地址](http://rsshub:1200/6v123/latestMovies) |
| <h2 id="游戏">游戏</h2> |  |   |  |
| <div id="G001" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/G001.png" width="30px" style="width:30px;height: auto;"/><br><span>G001</span></div> | 机核网 |  不止是游戏 | [‣ 宇宙，在此刻变得完整｜《无人深空》「宇宙」大更新 \| 2026-09-15](https://www.gcores.com/articles/219757)<br/>[‣ 【传言】英伟达60系显卡2027年上半年发售 \| 2026-09-15](https://www.gcores.com/articles/219756)  |  [订阅地址](https://www.gcores.com/rss) |  
| <div id="G002" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/G002.png" width="30px" style="width:30px;height: auto;"/><br><span>G002</span></div> | 游研社 |  无论你是游戏死忠，还是轻度的休闲玩家，在这里都能找到感兴趣的东西。 | [‣ 完美世界电竞再度于上海主办2027反恐精英世界锦标赛！ \| 2026-09-15](https://www.yystv.cn/p/14394)<br/>[‣ 天津光荣首度操刀，《三国志14》时隔6年推出“威力加强传承版” \| 2026-09-15](https://www.yystv.cn/p/14388)  |  [订阅地址](https://www.yystv.cn/rss/feed) |  
| G003 | 游戏葡萄 |  深度解读游戏  | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://rsshub:1200)  |  [订阅地址](http://rsshub:1200/gamegrape/13) |  
| RH027 | 5EPLAY - 新闻列表 | 5EPLAY 新闻 | [‣ FISSURE裂变天地3：气运在手！Legacy 2-1 MIBR \| 2026-09-17](https://csgo.5eplay.com/article/260912ixzo1s)<br/>[‣ dastan谈PV裂变天地3出局：我们好像缺了一些精气神 \| 2026-09-17](https://csgo.5eplay.com/article/260916cmbyjx) | [订阅地址](http://rsshub:1200/5eplay/article) |
| <h2 id="资源类">资源类</h2> |  |   |  |
| <div id="R001" style="text-align: center;"><img src="https://cdn.jsdelivr.net/gh/zhaoolee/garss/_media/favicon/R001.png" width="30px" style="width:30px;height: auto;"/><br><span>R001</span></div> | 书格 |  有品格的数字古籍图书馆 | [‣ 自警编 \| 2026-09-11](https://www.shuge.org/view/zi_jing_bian/)<br/>[‣ 祭侄文稿 \| 2026-09-11](https://www.shuge.org/view/ji_zhi_wen_gao/)  |  [订阅地址](https://www.shuge.org/feed/) |  
| R002 | 书伴 |  为静心阅读而生 | [‣ Kindle Scribe Colorsoft 上手测评：色彩生动，响应快速 \| 2025-10-04](https://bookfere.com/post/1173.html)<br/>[‣ \[2025.10.01\] Kindle 阅读器固件升级至 5.18.5.0.1 \| 2025-10-04](https://bookfere.com/post/1172.html)  |  [订阅地址](https://feeds.feedburner.com/bookfere) |  
| R003 | kindle吧 |  海量书单阅读分享者 | [暂无法通过爬虫获取信息, 点击进入源网站主页](https://www.kindle8.cc)  |  [订阅地址](https://www.kindle8.cc/feed) | 
| R004 | 起点中文网 |  限时免费清单 | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://rsshub:1200)  |  [订阅地址](http://rsshub:1200/qidian/free) | 
| N002 | 豆瓣 - 豆瓣电影分类 | 排序方式可选值如下 近期热门 标记最多 评分最高 最近上映 U T S R &#124; 示例：/douban/movie/classification/R/7.5/Netflix,2020 &#124; 参数：sort: 排序方式，默认为U；score: 最低评分，默认不限制；tags: 分类标签，多个标签之间用英文逗号分隔，常见的标签到豆瓣电影的分类页面查看，支持自定义标签 &#124; 源码：other/classification.ts | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://rsshub:1200) | [订阅地址](http://rsshub:1200/douban/movie/classification) |
| <h2 id="Telegram优质频道RSS订阅">Telegram优质频道RSS订阅</h2> |  |   |  |
| TG001 | 4K影视屋 |  蓝光无损电影 | [‣ 🎬 📺 暴力成人动画《极道寿司次郎》HBO上线预告 \| 2026-09-15](https://t.me/dianying4K/1455)<br/>[‣ 🎬 📺 俄罗斯科幻剧集《正午》终极预告 \| 2026-09-15](https://t.me/dianying4K/1454)  |  [订阅地址](http://rsshub:1200/telegram/channel/dianying4K) |  
| TG002 | 编程笑话 |  程序员编程笑话 | [‣ 🖼 \| 2026-09-14](https://t.me/programmerjokes/3896)<br/>[‣ 🖼 \| 2026-09-14](https://t.me/programmerjokes/3895)  |  [订阅地址](http://rsshub:1200/telegram/channel/programmerjokes) |  
| TG003 | 薅羊毛 |  各种购物平台的优惠信息 | [‣ 支付宝搜索”一分钱通骑“ 7天5次通骑，0.01元。单次最高抵3元，7天可省15元，哈啰、青桔、美团单车/助力车都能用。 \| 2023-09-23](https://t.me/yangmaoshare/32)<br/>[‣ ↩️ 更新了十几家有试用的机场：博客地址，方便收藏：https://jichanggo.com/%e6%9c%80%e6%96%b0%e5%85%8d%e8%b4%b9%e6%9c%ba%e5%9c%ba%e5%85%8d%e8%b4%b9%e4%b... \| 2023-09-23](https://t.me/yangmaoshare/31)  |  [订阅地址](http://rsshub:1200/telegram/channel/yangmaoshare) |  
| TG004 | 竹新社 |  7×24不定时编译国内外媒体的即时新闻报道。 | [‣ ↩️ 中国8月社会商品零售35280亿元、同比增0.3%，餐饮收入4544亿元、同比增1.1%。坏于预期。除汽车外的零售额同比增2.5%。 \| 2026-09-15](https://t.me/tnews365/35606)<br/>[‣ ↩️ 2026年“东京·中国电影周”决定取消举办，主办方NPO法人“日中电影节实行委员会”近日发布了这一消息。 \| 2026-09-15](https://t.me/tnews365/35605)  |  [订阅地址](http://rsshub:1200/telegram/channel/tnews365) |  
| TG005 | 书和读书 |  好书推荐。 | [‣ ↩️ 我这条信息有多少人跟了？是不是应该请吃一个🍗😄 \| 2026-07-29](https://t.me/GoReading/10319)<br/>[‣ 🖼 昨天清空了所有 AI 和数据中心的股票🤣 \| 2026-07-29](https://t.me/GoReading/10318)  |  [订阅地址](http://rsshub:1200/telegram/channel/GoReading) |  
| TG006 | 阿里云盘资源分享 |  分享资源完成阿里云盘任务，收获精品资源保存到不限速网盘 | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://rsshub:1200)  |  [订阅地址](http://rsshub:1200/telegram/channel/YunPanPan) |
| TG007 | Google Drive | 资源共享-软件-电影-纪录片-科学上网 | [暂无法通过爬虫获取信息, 点击进入源网站主页](http://rsshub:1200)  |  [订阅地址](http://rsshub:1200/telegram/channel/YunPanPan) |
| TG008 | 扫地僧笔记 | 扫地僧树洞 | [‣ 🔁🖼 原来网速跑慢能这么爽 \| 2026-09-15](https://t.me/lover_links/9553)<br/>[‣ ↩️🖼 晚安 \| 2026-09-15](https://t.me/lover_links/9552)  |  [订阅地址](http://rsshub:1200/telegram/channel/lover_links) |
| TG009 | 树莓派家用云服务器 | 树莓派家用云服务器交流  | [‣ 《树莓派不吃灰》035：使用树莓派5B运行openclaw，快速领取麦当劳优惠券，使用skill刷推 https://v2fy.com/p/2026-02-03-09-09-04-openclaw-pi/ \| 2026-03-09](https://t.me/zhaoolee_pi/51)<br/>[‣ \[《树莓派不吃灰》034：使用qemu在树莓派运行x86镜像，以大模型二道贩子x86镜像new api为例\](https://v2fy.com/p/2025-10-16-22-25-01-x86/) \| 2026-03-09](https://t.me/zhaoolee_pi/50)  |  [订阅地址](http://rsshub:1200/telegram/channel/zhaoolee_pi) |
| TG010 | 快乐星球 | 美女图片  | [‣ 🖼 \| 2026-09-15](https://t.me/botmzt/22404)<br/>[‣ 🖼 \| 2026-09-15](https://t.me/botmzt/22400)  |  [订阅地址](http://rsshub:1200/telegram/channel/botmzt) |
| TG011 | Newlearnerの自留地 | 不定期推送 IT 相关资讯 | [‣ 🖼 #News \| 2026-09-15](https://t.me/NewlearnerChannel/15961)<br/>[‣ 🎬 #macOS #APP #AI #独立开发 \| 2026-09-15](https://t.me/NewlearnerChannel/15960)  |  [订阅地址](http://rsshub:1200/telegram/channel/NewlearnerChannel) |
| N008 | 小破不入渠 |  | [‣ 这集很好。2015 年《Inside Out》上映的时候，它的设定就是「Gen Z 这代人的思想行为模式，反应了计算机控制和数据驱动的文化」。我们当时很容易识别这一点，因... \| 2026-09-07](https://t.me/forwardlikehell/2932)<br/>[‣ 上周在 B 站看到有 UP 采访了一个杨百翰大学的留学生，后者读的本科项目学费便宜，但要遵守一些「奇葩」的摩门校规，包括不能喝咖啡、茶，不能留胡子。 \| 2026-09-07](https://t.me/forwardlikehell/2931) | [订阅地址](http://rsshub:1200/telegram/channel/forwardlikehell) |
| N009 | 小声读书 |  | [‣ 🖼 专为 monk.party 打造的 macOS 极致体验菜单栏用量与限流监控小工具。纯原生 Swift + SwiftUI 打造。 \| 2026-09-15](https://t.me/weekly_books/2571)<br/>[‣ 🖼 上海人工智能实验室 Atria 团队发布 Atria Dawn Preview，一款面向科学研究、工程开发与专业工作流的智能体基础模型。 \| 2026-09-15](https://t.me/weekly_books/2570) | [订阅地址](http://rsshub:1200/telegram/channel/weekly_books) |
| N010 | 小道消息 |  | [‣ 🖼 涨价了 \| 2026-09-07](https://t.me/WebNoteslah/635)<br/>[‣ 媒体报道的猝死案例中，过度劳累、熬夜、剧烈运动、情绪激动和饮酒经常被描述为事发前的诱因。但媒体报道不能代替流行病学统计，也很容易误导人。 \| 2026-09-07](https://t.me/WebNoteslah/634) | [订阅地址](http://rsshub:1200/telegram/channel/WebNoteslah) |
| N011 | 每日消费电子观察 |  | [‣ 伊朗多家银行遭遇TLS证书风波：被美国制裁后无法申请证书或证书被撤销 \| 2026-09-15](https://t.me/CE_Observe/44136)<br/>[‣ 零点击入侵！新型微信蠕虫可无感知盗号，无需接打电话 \| 2026-09-15](https://t.me/CE_Observe/44135) | [订阅地址](http://rsshub:1200/telegram/channel/CE_Observe) |
| N012 | Alan的小纸箱 |  | [‣ 🔁 为加强首都地区空域安全管理，维护空中飞行秩序，保障地面重要目标和人民生命财产安全，依据有关法律法规，参照国际通行做法，我国将在首都及周边地区划设... \| 2026-09-15](https://t.me/alansbox/4822)<br/>[‣ 🖼 恭喜 Dario 成为第一个被中美欧三地政府集体驳斥/怒喷的 SOTA 模型机构创始人。 \| 2026-09-15](https://t.me/alansbox/4821) | [订阅地址](http://rsshub:1200/telegram/channel/alansbox) |
| <h2 id="摄影">摄影</h2> |  |   |  |
| C020 | PTT(台湾论坛) | PTT正妹专题 | [‣ \[正妹\] 睦那京 \| 2026-09-15](https://www.ptt.cc/bbs/Beauty/M.1789513965.A.7B4.html)<br/>[‣ \[正妹\] 宛郿 \| 2026-09-15](https://www.ptt.cc/bbs/Beauty/M.1789513795.A.3F9.html)  |  [订阅地址](https://www.ptt.cc/atom/beauty.xml) |  
| N003 | 热点影像模特约拍频道 |  | [‣ 🖼 近期可約拍人體model: 悠悠，Gigi，婉雯，川純，金金，研研，朱思莉，頭4位可約香港拍🇭🇰 \| 2026-09-01](https://t.me/hotspotimage88/622)<br/>[‣ https://hotspotimage.com/bbs/viewthread.php?tid=25682 \| 2026-09-01](https://t.me/hotspotimage88/621) | [订阅地址](http://rsshub:1200/telegram/channel/hotspotimage88) |
| N004 | R21JP |  | [‣ 🎬 天天枯坐盯盘，不得犒劳自己一番？ \| 2026-09-15](https://t.me/m81plus/17001)<br/>[‣ 🖼 精緻不是刻意 是我喜歡的生活方式✨ \| 2026-09-15](https://t.me/m81plus/17000) | [订阅地址](http://rsshub:1200/telegram/channel/m81plus) |
| N005 | Analog Photography |  | [‣ 🖼 \[Ga645, Kodak gold 200\] source \| 2026-09-15](https://t.me/anallog/12605)<br/>[‣ 🖼 Some double exposures from the last roll \[Pentax LX, Super Takumar 50mm f/1.4, Fujilfilm 400\] #nsfw source \| 2026-09-15](https://t.me/anallog/12601) | [订阅地址](http://rsshub:1200/telegram/channel/anallog) |
| N006 | photography |  | [‣ 🔧 photography pinned «SHARE YOUR STORY WITH FOLKFRAME Every photograph can show us something. Some photographs have something to tell. At FolkFram... \| 2026-09-15](https://t.me/photography/490)<br/>[‣ 🖼 \| 2026-09-15](https://t.me/photography/489) | [订阅地址](http://rsshub:1200/telegram/channel/photography) |
| N007 | Photography Poses |  | [‣ 🖼 \| 2025-08-29](https://t.me/photography_poses/2604)<br/>[‣ 🖼 \| 2025-08-29](https://t.me/photography_poses/2603) | [订阅地址](http://rsshub:1200/telegram/channel/photography_poses) |
| <h2 id="未分类">未分类</h2> |  |   |  |
| N001 | 共产党员网 - 最新发布 | 最新发布 : : zxfb &#124; 示例：/12371/zxfb &#124; 参数：category: 新闻分类名，预设 zxfb &#124; 来源：www.12371.cn &#124; 源码：zxfb.ts | [‣ 石泰峰会见新加坡公共服务统筹部长兼国防部长陈振声 \| 2026-09-15](https://www.12371.cn/2026/09/15/ARTI1789462213280361.shtml)<br/>[‣ 基础研究为何重要、怎样加强 \| 2026-09-15](https://www.12371.cn/2026/09/15/ARTI1789456398468680.shtml) | [订阅地址](http://rsshub:1200/12371/zxfb) |



## 批量导入所有RSS订阅

OPML V2.0:  [https://raw.githubusercontent.com/zhaoolee/garss/main/zhaoolee_github_garss_subscription_list_v2.opml](https://raw.githubusercontent.com/zhaoolee/garss/main/zhaoolee_github_garss_subscription_list_v2.opml) 

OPML V2.0 备用CDN地址: [https://cdn.jsdelivr.net/gh/zhaoolee/garss/zhaoolee_github_garss_subscription_list_v2.opml](https://cdn.jsdelivr.net/gh/zhaoolee/garss/zhaoolee_github_garss_subscription_list_v2.opml)



> 如果RSS软件版本较老无法识别以上订阅,请使用[V1.0版本的OPML订阅信息](https://raw.githubusercontent.com/zhaoolee/garss/main/zhaoolee_github_garss_subscription_list_v1.opml) [V1.0版本的OPML订阅信息备用CDN地址](https://cdn.jsdelivr.net/gh/zhaoolee/garss/zhaoolee_github_garss_subscription_list_v1.opml)


## 如何定制自己的私人简报?

从 github.com/zhaoolee/garss.git 仓库, fork一份程序到自己的仓库

允许运行actions

![允许运行actions](https://cdn.fangyuanxiaozhan.com/assets/1630216112533FANcC1QY.jpeg)

在EditREADME.md中, 展示了zhaoolee已收集的RSS列表, 你可以参考每行的格式, 按行增删自己订阅的RSS

然后按照下图设置发件邮箱相关内容即可!

![](https://cdn.fangyuanxiaozhan.com/assets/1629970189283arACkBKe.png)

在根目录, tasks.json中配置收件人, 收件人是一个对象数组, 数组中的邮箱, 都会收到邮件, 后续会扩展更多功能~

```
{
    "tasks": [
        {
            "email": "zhaoolee@gmail.com"
        },
        {
            "email": "zhaoolee@foxmail.com"
        }
    ]
}
```

设置完成后 在README.md文件的底部加个空格，并push，即可触发更新！

## 无法收到邮件怎么办

可以按照以下代码，自测一下自己的HOST, PASSWORD，USER 是否能顺利发邮件

```
!pip install yagmail

import yagmail

# 连接邮箱服务器
yag = yagmail.SMTP(user="填USER参数", password="填PASSWORD参数", host='填HOST参数')

# 邮箱正文
contents = ['今天是周末,我要学习, 学习使我快乐;', '<a href="https://www.python.org/">python官网的超链接</a>']

# 发送邮件
yag.send('填收件人邮箱', '主题:学习使我快乐', contents)
```

在线自测地址 [Colab： https://colab.research.google.com/](https://colab.research.google.com/)

![在线自测](https://i.v2ex.co/zQWM0V6b.png)

## 发送邮件的效果

![手机端优化后的邮件效果](https://cdn.fangyuanxiaozhan.com/assets/163039979740967wCT8RQ.jpeg)

![PC端优化后的邮件效果](https://cdn.fangyuanxiaozhan.com/assets/1630399693988c2tk8n7k.png)

## 微信交流群

[https://frp.v2fy.com/dynamic-picture/%E5%BE%AE%E4%BF%A1%E4%BA%A4%E6%B5%81%E7%BE%A4/qr.png](https://frp.v2fy.com/dynamic-picture/%E5%BE%AE%E4%BF%A1%E4%BA%A4%E6%B5%81%E7%BE%A4/qr.png)


## 广告位招租

![广告位招租](https://raw.githubusercontent.com/zhaoolee/ChineseBQB/master/README/zhaoolee-link.png)
