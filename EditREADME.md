# Github Actions Rss (garss, 嘎RSS! 已收集{{rss_num}}个RSS源, 生成时间: {{ga_rss_datetime}})

信息茧房是指人们关注的信息领域会习惯性地被自己的兴趣所引导，从而将自己的生活桎梏于像蚕茧一般的“茧房”中的现象。由于信息技术提供了更自我的思想空间和任何领域的巨量知识，一些人还可能进一步逃避社会中的种种矛盾，成为与世隔绝的孤立者。在社群内的交流更加高效的同时，社群之间的沟通并不见得一定会比信息匮乏的时代更加顺畅和有效。

这个名为**嘎!RSS**的项目会利用免费的Github Actions服务, 提供一个内容全面的信息流, 让现代人的知识体系更广泛, 减弱信息茧房对现代人的影响, 让**非茧房信息流**造福人类~


[《嘎!RSS》永久开源页面: https://github.com/zhaoolee/garss](https://github.com/zhaoolee/garss)


## 主要功能

- 收集RSS, 打造无广告内容优质的 **头版头条** 超赞新闻页

- 利用Github Actions, 搜集全部RSS的头版头条(已完成)

- 开发支持邮件订阅Rss邮件发送服务(开发进度50%)


| 名称 | 描述 | <div style="width: 100px!important">RSS</div>  |  最新内容 |
| --- | --- | --- |  --- |
| <h2 id="软件工具">软件工具</h2> |  |   |  |
| 反斗限免 | 反斗软件旗下软件限免资讯网站 | [订阅地址](https://free.apprcn.com/feed/) |  {{latest_content}} |
| 不死鸟 | 不死鸟:专注分享优质资源 | [订阅地址](https://iao.su/feed) |  {{latest_content}} |
| 精品MAC应用分享 | 精品MAC应用分享，每天分享大量mac软件，为您提供优质的mac软件,免费软件下载服务 | [订阅地址](https://xclient.info/feed) |  {{latest_content}} |
| 老殁 | 免费推荐优秀软件 | [订阅地址](https://www.mpyit.com/feed) |  {{latest_content}} |
| 鹏少资源网 | 专注于精品软件收录分享 | [订阅地址](https://www.jokerps.com/feed) |  {{latest_content}} |
| <h2 id="个人博客">个人博客</h2> |  |   |  |
| 阮一峰的网络日志 | 一个科技博客，讲解的知识通俗易懂 | [订阅地址](http://www.ruanyifeng.com/blog/atom.xml) | {{latest_content}} |
| 当我在扯淡 | 王垠的博客，观点奇妙有趣 | [订阅地址](https://yinwang1.wordpress.com/feed/) | {{latest_content}} |
| 黑果小兵的部落阁 | Hackintosh安装镜像、教程及经验分享| [订阅地址](https://blog.daliansky.net/atom.xml) | {{latest_content}} |
| 张鑫旭的博客 | 张鑫旭-鑫空间-鑫生活 | [订阅地址](https://www.zhangxinxu.com/wordpress/feed/) | {{latest_content}} |
| V2方圆 | zhaoolee的博客  | [订阅地址](https://www.v2fy.com/feed/) | {{latest_content}} |
| <h2 id="团队博客">团队博客</h2> |  |   |  |
| AlloyTeam | 腾讯全端AlloyTeam团队的技术博客 | [订阅地址](http://www.alloyteam.com/feed/) | {{latest_content}} |
| 微软亚洲研究院 | 微软亚洲研究院技术博客 | [订阅地址](https://www.msra.cn/feed) | {{latest_content}} |
| 极客公园 | 极客公园  | [订阅地址](https://www.geekpark.net/rss) | {{latest_content}} |
| 奇舞周刊 | 360前端团队博客，领略前端技术，阅读奇舞周刊  | [订阅地址](https://weekly.75.team/rss) | {{latest_content}} |
| 淘系前端团队 | 淘宝团队技术博客 | [订阅地址](https://weekly.75.team/rss) | {{latest_content}} |
| 字节跳动团队技术博客 | 字节跳动团队技术博客 | [订阅地址](https://blog.csdn.net/ByteDanceTech/rss/list) | {{latest_content}} |
| 美团技术团队博客 | 美团技术团队博客 | [订阅地址](https://tech.meituan.com/feed/)  | {{latest_content}} |
| <h2 id="公司官方新闻">公司官方新闻</h2> |  |   |  |
| Apple新闻 | Apple官方消息 | [订阅地址](https://www.apple.com/newsroom/rss-feed.rss) |  {{latest_content}} |
| <h2 id="互联网类">互联网类</h2> |  |   |  |
| 虎嗅 | 虎嗅网新闻 | [订阅地址](https://www.huxiu.com/rss/0.xml) |  {{latest_content}} |
| 36kr | 36氪 | [订阅地址](https://www.36kr.com/feed) |  {{latest_content}} |
| <h2 id="金融类">金融类</h2> |  |   |  |
| 雪球 | 聪明的投资者都在这里,雪球每日精华 | [订阅地址](https://xueqiu.com/hots/topic/rss) |  {{latest_content}} |
| <h2 id="学习类">学习类</h2> |  |   |  |
| 扔物线 | 帮助 Android 工程师进阶成长 | [订阅地址](https://rengwuxian.com/feed) |  {{latest_content}} |
| MOOC中国 | 慕课改变你，你改变世界  | [订阅地址](https://www.mooc.cn/feed) |  {{latest_content}} |
| <h2 id="学术类">学术类</h2> |  |   |  |
| 青柠学术 | 每个科研小白都有成为大神的潜力 | [订阅地址](https://iseex.github.io/feed) |  {{latest_content}} |
| <h2 id="生活类">生活类</h2> |  |   |  |
| 李子柒 | 李子柒的微博 | [订阅地址](https://rsshub.app/weibo/user/2970452952) |  {{latest_content}} |
| 理想生活实验室 | 为更理想的生活 | [订阅地址](https://www.toodaylab.com/rss) |  {{latest_content}} |
| <h2 id="设计类">设计类</h2> |  |   |  |
| Behance |  Adobe旗下设计网站Behance | [订阅地址](https://www.behance.net/feeds/projects) |  {{latest_content}} |
| Pinterest |  图片设计社交 | [订阅地址](https://newsroom.pinterest.com/en/feed/posts.xml) |  {{latest_content}} |
| 优设 |  优秀设计联盟-优设网-设计师交流学习平台-看设计文章，学软件教程，找灵感素材，尽在优设网！ | [订阅地址](https://www.uisdc.com/feed) |  {{latest_content}} |
| <h2 id="内容平台">内容平台</h2> |  |   |  |
| 知乎 | 知乎每日精选 | [订阅地址](https://www.zhihu.com/rss) |  {{latest_content}} |
| 小众软件 | 小众软件RSS | [订阅地址](https://www.appinn.com/feed/) |  {{latest_content}} |
| V2EX | 创意工作者的社区 | [订阅地址](https://www.v2ex.com/index.xml) |  {{latest_content}} |
| 酷 壳 | 酷 壳RSS | [订阅地址](https://coolshell.cn/feed) |  {{latest_content}} |
| 豆瓣 | 豆瓣最受欢迎的影评 | [订阅地址](https://www.douban.com/feed/review/movie) |  {{latest_content}} |
| 豆瓣 | 豆瓣最受欢迎的书评 | [订阅地址](https://www.douban.com/feed/review/book) |  {{latest_content}} |
| 豆瓣 | 豆瓣最受欢迎的乐评 | [订阅地址](https://www.douban.com/feed/review/music) |  {{latest_content}} |
| 开源中国 | 开源中国社区推荐文章 | [订阅地址](https://www.oschina.net/blog/rss) |  {{latest_content}} |
| 博客园 | 博客园精华区 | [订阅地址](http://feed.cnblogs.com/blog/picked/rss) |  {{latest_content}} |
| 博客园 | 博客园首页 | [订阅地址](http://feed.cnblogs.com/blog/sitehome/rss) |  {{latest_content}} |
| 吾爱破解 | 吾爱破解 - LCG - LSG 安卓破解 病毒分析 - 最新精华 | [订阅地址](https://www.52pojie.cn/forum.php?mod=guide&view=digest&rss=1) |  {{latest_content}} |
