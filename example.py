# -*- coding: utf-8 -*-
import time
import logging
import re
from urllib.parse import quote
import random
from QQLightBot import ApiProtocol,MsgDict
from datetime import datetime
from realTime_notification import prase_web,check_info
from get_weiboContent import *
from test_direction import *
from generate_wordcloud import *
logger = logging.getLogger('QQLightBot')
from time_judge import  time_judge


class ExampleProtocol(ApiProtocol):
    # @classmethod
    # async def send_intime(cls):
    #     if time.strptime(time.strftime("%H%M%S"), "%H%M%S") == time.strptime('170920', "%H%M%S"):
    #             await cls.sendMessage(2, '605565297', '', '[QQ:pic=cbef2ca7-b5bd-d1be-1e15-a35e630d0fa6.jpg]')
    @classmethod
    async def onConnect(cls):
        """连接成功
        """
        logger.info('connect succeed')
        # print(await cls.getQQInfo('815221919'))
        # sched = BlockingScheduler()
        # sched.add_job(cls.sendMessage(2, '605565297', '', '[QQ:pic=cbef2ca7-b5bd-d1be-1e15-a35e630d0fa6.jpg]'), 'cron', day_of_week='1-5', hour=17, minute=17)
        # sched.start()
    @classmethod
    async def getGroupMemberList(cls, group):
        """接口.获取群成员列表
        :param cls:
        :param group:       群号或讨论组号
        """
        await cls._ws.send_json(cls._makeData(
            'getGroupMemberList', group=group))
        result = await cls._ws.receive()
        # print(json.loads(result.data))
        return MsgDict(json.loads(result.data))['result']['members']

    @classmethod
    async def message(cls, type=0, qq='', group='', msgid='', content=''):  # @ReservedAssignment
        """事件.收到消息
        :param cls:
        :param type:        1=好友消息、2=群消息、3=群临时消息、4=讨论组消息、5=讨论组临时消息、6=QQ临时消息
        :param qq:          消息来源QQ号，"10000"都是来自系统的消息（比如某人被禁言或某人撤回消息等）
        :param group:       类型为1或6的时候，此参数为空字符串，其余情况下为群号或讨论组号
        :param msgid:       消息id，撤回消息的时候会用到，群消息会存在，其余情况下为空
        :param content:     消息内容
        """
        logger.info(
            str(dict(type=type, qq=qq, group=group, msgid=msgid, content=content)))
        """
        测试模块
        """
        # if group == '605565297' and weibo_content(content):
        #     await cls.sendMessage(2, group, '',weibo_content(content))

        #曲阜师范大学考研群
        if group == '88145363':
            if content == '倒计时' or re.search('倒计时', content) and re.search('考研', content) or re.search('多少天',
                                                                                                       content) and re.search(
                    '考研', content) or re.search('几天', content) and re.search('考研', content):
                # 构造一个将来的时间
                future = datetime.strptime('2019-12-22 00:00:00', '%Y-%m-%d %H:%M:%S')
                # 当前时间
                now = datetime.now()
                # 求时间差
                delta = future - now
                hour = delta.seconds / 60 / 60
                minute = (delta.seconds - hour * 60 * 60) / 60
                seconds = delta.seconds - hour * 60 * 60 - minute * 60
                print_now = now.strftime('%Y-%m-%d %H:%M:%S')
                await cls.sendMessage(2, group, '',
                                "[QQ:face="+time_judge()+"]距离 2019-12-21 考研还有%d天" % delta.days)
            elif weibo_content(content):
                await cls.sendMessage(2, group, '', weibo_content(content))

        """
        功能使用模块
        """
        #考研群,测试群
        if group == '681882220' or group == '699188599' or group == '778577978':
            if content == '倒计时' or re.search('倒计时', content) and re.search('考研', content) or re.search('多少天',
                                                                                                       content) and re.search(
                    '考研', content) or re.search('几天', content) and re.search('考研', content):
                # 构造一个将来的时间
                future = datetime.strptime('2019-12-22 00:00:00', '%Y-%m-%d %H:%M:%S')
                # 当前时间
                now = datetime.now()
                # 求时间差
                delta = future - now
                hour = delta.seconds / 60 / 60
                minute = (delta.seconds - hour * 60 * 60) / 60
                seconds = delta.seconds - hour * 60 * 60 - minute * 60
                print_now = now.strftime('%Y-%m-%d %H:%M:%S')
                await cls.sendMessage(2, group, '',
                                "[QQ:face="+time_judge()+"]距离 2019-12-21 考研还有%d天" % delta.days)
            elif weibo_content(content):
                await cls.sendMessage(2, group, '', weibo_content(content))
            elif content == '研招网':
                 news = check_info()
                 if  news['flag']:
                     await cls.sendMessage(2, group, '',
                                             "中国海洋大学研究生招生信息网有新发布的内容，主题为：《"+news.get('info_text')+'》\n点击网址进入查看：'+news.get('url'))
                 elif not news['flag']:
                             await cls.sendMessage(2, group, '',
                                             "中国海洋大学研究生招生信息网最新发布的主题为：《"+news.get('info_text')+'》\n点击网址进入查看：'+news.get('url'))
            elif re.search('院',content) and re.search('网',content):
                await cls.sendMessage(2, group, '',
                                "中国海洋大学信息学院网站:\nhttp://it.ouc.edu.cn/")
            elif re.search('系',content) and re.search('网',content):
                await cls.sendMessage(2, group, '',
                                      "中国海洋大学计算机科学与技术系网站:\nhttp://cs.ouc.edu.cn/")
            elif re.search('免费',content) and re.search('资料',content):
                await  cls.silence(qq, group, duration = 2592000)
                await  cls.withdrawMessage(group, msgid)
            elif qq =='815221919' and re.search('禁言\[QQ:',content):
                regex = r'=([\s\S]*)]'
                silences_qq = re.findall(regex, content)
                for silence_qq in silences_qq:
                    await  cls.silence(silence_qq, group, duration=2592000)
            elif content == '群备注比例':
                if group == '699188599':
                    members = await cls.getGroupMemberList('681882220')
                else:
                    members = await cls.getGroupMemberList(group)
                end_ratio = test_direction(members)
                await cls.sendMessage(2, group, '',
                                      "当前修改备注人数为{0}人\n".format(end_ratio[7])+
                                      "专硕参考报录比910,911,940,农信分别为{0},{1},{2},{3}\n".format(end_ratio[0], round(end_ratio[1],1),
                                                                             end_ratio[2],end_ratio[9]) +
                                      "学硕参考报录比912,940,954分别为{0},{1},{2}\n".format(end_ratio[3], end_ratio[4], end_ratio[5]) +
                                      "专硕:学硕为{}:1".format(end_ratio[6]))
            elif content == '本群词云':
                png_path = cls.formatImage('D:\Chrome浏览器下载\QQLightBot-master\worldcloud.png')
                await cls.sendMessage(2, group,'',png_path)
                members = await cls.getGroupMemberList(group)
                print(members)
                generate_world(members)
            elif content == '参考书':
                await cls.sendMessage(2, group, '','[QQ:pic=c3d25b8e-cb17-221d-514f-9dfd5e6934d9.png]')
            if time.strptime(time.strftime("%H%M%S"), "%H%M%S") == time.strptime('220000',"%H%M%S"):
                await cls.sendMessage(2, '605565297', '', '[QQ:pic=cbef2ca7-b5bd-d1be-1e15-a35e630d0fa6.jpg]')
    @classmethod
    async def friendRequest(cls, qq='', message=''):
        """事件.收到好友请求
        :param cls:
        :param qq:          QQ
        :param message:     验证消息
        """
        logger.info(
            str(dict(type=type, qq=qq, message=message)))

    @classmethod
    async def becomeFriends(cls, qq=''):
        """事件.成为好友
        :param cls:
        :param qq:          QQ
        """
        logger.info(
            str(dict(type=type, qq=qq)))

    @classmethod
    async def groupMemberIncrease(cls, type='', qq='',  # @ReservedAssignment
                                  group='', operator=''):
        """事件.群成员增加
        :param cls:
        :param type:        1=主动加群、2=被管理员邀请
        :param qq:          QQ
        :param group:       QQ群
        :param operator:    操作者QQ
        """
        logger.info(
            str(dict(type=type, qq=qq, group=group, operator=operator)))
        # 先判断是否是黑名单用户,感觉进群禁言比直接拒绝更好玩。
        black_list = ['1371087907','1093780350','884355421','1151039635','394354735','3457219093','2375514923']  # 黑名单列表
        if group == '681882220' or group == '699188599' or group == '778577978':
            if str(qq) in black_list:
                await cls.sendMessage(2, group, '',
                                      "恭喜新进群的黑名单用户[QQ:face=144]，你将享受秒执行的无限期一个月禁言套餐哦，开心吧[QQ:face=14]" + "[QQ:at={0}]".format(
                                          qq))
                await cls.silence(qq, group, duration=2592000)
            else:
                await cls.sendMessage(2, group, '',
                                      "进群请改备注，如：20-软工专-张三[QQ:face=144]记得看群文件和群公告，可以解决大多数疑惑[QQ:face=183]不要发广告[QQ:face=181]" + "[QQ:at={0}]".format(
                                          qq))
        if group == '88145363':
            await cls.sendMessage(2, group, '',
                              "进群请改备注，如：20-计算机-张三[QQ:face=144]记得看群文件，有今年的录取情况，不要发广告[QQ:face=181][QQ:emoji=14912151][QQ:emoji=15710351]一战成研\n" + "[QQ:at={0}]".format(
                                  qq))
    @classmethod
    async def groupMemberDecrease(cls, type='', qq='',  # @ReservedAssignment
                                  group='', operator=''):
        """事件.群成员减少
        :param cls:
        :param type:        1=主动退群、2=被管理员踢出
        :param qq:          QQ
        :param group:       QQ群
        :param operator:    操作者QQ，仅在被管理员踢出时存在
        """
        logger.info(
            str(dict(type=type, qq=qq, group=group, operator=operator)))
        if group == '681882220' or group == '699188599' or group == '778577978':
            fight_words = ['He laughs best who laughs last.', 'Talk is cheap,make the move.','Push yourself until the end.',
                           'Sticking to the end is the best.', 'Everything happens for a resaon.',
                           'Have faith in yourself.', 'I have got your back.','All things come to those who wait.',
                           'The shortest way to do many things is to only one thing at a time.','Nothing seek, nothing find.',
                           'If you are doing your best,you will not have to worry about failure.','Energy and persistence conquer all things.',
                           'Keep trying no matter how hard it seems. it will get easier.','Suffering is the most powerful teacher of life.',
                           'Constant dropping wears the stone.','Adversity is the midwife of genius.','If you are doing your best,you will not have to worry about failure.',
                           'Pain past is pleasure.','Our greatest glory consists not in never falling but in rising every time we fall.',
                           'When we start with a positive attitude and view themselves as successful when we start a success.',"Don't aim for success if you want it; just do what you love and believe in, and it will come naturally."]
            random_num = random.randint(0, len(fight_words) - 1)
            await cls.sendMessage(2, group, '',
                                          "groupMembers--;\nsuccessRate++;\n[QQ:face=144]"+fight_words[random_num]+"[QQ:face=120]")
    @classmethod
    async def adminChange(cls, type=1, qq='', group=''):  # @ReservedAssignment
        """事件.群管理员变动
        :param cls:
        :param type:        1=成为管理 2=被解除管理
        :param qq:          QQ
        :param group:       QQ群
        """
        logger.info(
            str(dict(type=type, qq=qq, group=group)))

    @classmethod
    async def groupRequest(cls, type=1, qq='', group='',  # @ReservedAssignment
                           seq='', operator='', message=''):
        """事件.加群请求
        :param cls:
        :param type:        1=主动加群、2=被邀请进群、3=机器人被邀请进群
        :param qq:          QQ
        :param group:       QQ群
        :param seq:         序列号，处理加群请求时需要用到
        :param operator:    邀请者QQ，主动加群时不存在
        :param message:     加群附加消息，只有主动加群时存在
        """
        logger.info(
            str(dict(type=type, qq=qq, group=group,
                     seq=seq, operator=operator, message=message)))

    @classmethod
    async def receiveMoney(cls, type=1, qq='', group='',  # @ReservedAssignment
                           amount='', id='', message=''):  # @ReservedAssignment
        """事件.收款
        :param cls:
        :param type:        1=好友转账、2=群临时会话转账、3=讨论组临时会话转账
        :param qq:          转账者QQ
        :param group:       type为1时此参数为空，type为2、3时分别为群号或讨论组号
        :param amount:      转账金额
        :param id:          转账订单号
        :param message:     转账备注消息
        """
        logger.info(
            str(dict(type=type, qq=qq, group=group,
                     amount=amount, id=id, message=message)))

    @classmethod
    async def updateCookies(cls, *args, **kwargs):
        """事件.Cookies更新
        :param cls:
        """
        logger.info('args: {}, kwargs: {}'.format(str(args), str(kwargs)))