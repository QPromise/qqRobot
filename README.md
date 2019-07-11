# qqRobot

这是一个基于[QQLight](https://www.52chat.cc/download.php)的Python机器人框架。

## 使用方法

### 1、运行机器人客户端
 - 运行机器人客户端这个目录下的QQLight.exe启动登录qq，使用Air就行，可以满足一般的需求，不用购买Pro版。

### 2、Python自定义各种机器人接口
 - 将下载的master文件夹用IDE打开，如PyCharm。
 - 安装所需依赖包 `pip install -r requirements.txt`
 - 在terminal运行 `python QQLightBot.py -H 127.0.0.1 -P 49632 -U / -L INFO example:ExampleProtocol`
## 各模块主要功能
 - 主要模块为example.py,在其中导入了其它功能模块
 - generate_wordcloud.py:群备注词云生成
 - get_weiboContent.py:获取指定id第一条微博
 - realTime_notification.py:指定网站的更新通知获取
 - test_direction.py:考试目标方向的比例统计
 - time_judge.py:白天三个时间段的判断
## 功能实现
 - 考研倒计时回复。
 - 微博、网站内容爬取，群中关键字推送。
 - 群备注词云推送，以及各部分比例统计。
 - 白天分三个时间段表情包变换。
 - 群成员进群退群监控。
 - 里面example.py的代码内容根据自己的需求修改即可，记得把群号改为自己QQLight登录的qq加入的群，这是前提。
 - 内容有一些针对性，不明白的地方可以联系邮箱：qcs@stu.ouc.edu.cn
## 接口功能列表
 -   Air版（免费，适用于非营利性个人用户）
        
        好友消息 √  
        群消息 √  
        群私聊消息 √  
        讨论组消息 √  
        讨论组私聊消息 √  
        在线状态私聊消息 √  
        文字消息 √  
        小黄豆、emoji、动态表情、魔法表情、小表情 √  
        QQ点歌、网易云点歌、JSON点歌 √  
        图片 √ 
        群名片监控 √  
        踢人 √  
        禁言 √  
        退群 √  
        退出讨论组 √  
        修改讨论组名称 √  
        修改群名片 √  
        修改个性签名 √  
        长文本解析 √  
        修改好友备注 √  
        取群列表、好友列表、群成员列表 √  
        取Cookies √
        语音消息 ×  
        XML卡片，JSON卡片消息 ×  
        红包消息 ×  
        财付通转账消息 ×  
        撤回群成员消息 ×  
        领取红包功能 ×  
        抖动好友窗口 ×  
        邀请好友入群 ×  
        （主动）添加好友 ×  
        （主动）添加群 ×  
        厘米秀 ×  
        QQ闪照 ×  
        QQ秀图 ×  
        QQ名片赞 ×  
        框架配套的群管功能 ×