#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import logging
import re
from urllib.parse import quote

from QQLightBot import ApiProtocol
from datetime import datetime
from realTime_notification import prase_web,check_info
from get_weiboContent import *
logger = logging.getLogger('QQLightBot')
BaiduMatch = re.compile('^百度 (.*)', re.M | re.S)

#可以设置定时发消息
        # while 1 :
        #     try:
        #          news = check_info()
        #          if  news['flag']:
        #             await cls.sendMessage(2, '605565297', '',
        #                            "中国海洋大学研究生招生信息网有新发布的内容，\n主题为：《"+news.get('info_text')+'》\n点击网址进入查看：'+news.get('url'))
        #          elif not news['flag']:
        #             await cls.sendMessage(2, '605565297', '',
        #                            "中国海洋大学研究生招生信息网暂时没有新发布的内容，\n最新发布的主题为：《"+news.get('info_text')+'》\n点击网址进入查看：'+news.get('url'))
        #     except:
        #         print('遇到了异常')
        #         break
class ExampleProtocol(ApiProtocol):

    @classmethod
    async def onConnect(cls):
        """连接成功
        """
        logger.info('connect succeed')

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
#         if group == '794510765':
#         # 测试群
#         if BaiduMatch.search(content):
#             await cls.sendMessage(2, group, '', '{}\nhttps://pyqt5.com/search.php?m=baidu&w={}'
#                                   .format(cls.formatAt(qq), quote(content[3:])))
#         else:
#             # 复读机
#             await cls.sendMessage(2, group, '', '我是复读机：' + content)

        if group == '605565297':
            if content == '倒计时' or re.search('倒计时', content) and re.search('考研', content) or re.search('多少天',
                                                                                                       content) and re.search(
                    '考研', content) or re.search('几天', content) and re.search('考研', content):
                # 构造一个将来的时间
                future = datetime.strptime('2019-12-21 00:00:00', '%Y-%m-%d %H:%M:%S')
                # 当前时间
                now = datetime.now()
                # 求时间差
                delta = future - now
                hour = delta.seconds / 60 / 60
                minute = (delta.seconds - hour * 60 * 60) / 60
                seconds = delta.seconds - hour * 60 * 60 - minute * 60
                print_now = now.strftime('%Y-%m-%d %H:%M:%S')
                print("今天是：", print_now)
                print("距离 2019-12-21 \"work\" 还剩下：%d天" % delta.days)
                print(delta.days, hour, minute, seconds)
                # 复读机
                await cls.sendMessage(2, group, '',
                                "[QQ:face=175]距离 2019-12-21 考研还有%d天" % delta.days)
            elif content == '张宇':
                id = '2058586920'
                data = get_weibo(id)
                await cls.sendMessage(2, group, '',
                                      "[QQ:face=175]张宇在"+str(data['created_at'])+"更新了微博，快来点击查看吧->"+str(data['scheme']))
            elif content == '汤家凤':
                id = '2644595644'
                data = get_weibo(id)
                await cls.sendMessage(2, group, '',
                                      "[QQ:face=175]汤家凤在" + str(data['created_at']) + "更新了微博，快来点击查看吧->" + str(
                                          data['scheme']))
            elif content == '肖秀荣':
                id = '1227078145'
                data = get_weibo(id)
                await cls.sendMessage(2, group, '',
                                      "[QQ:face=175]肖秀荣在" + str(data['created_at']) + "更新了微博，快来点击查看吧->" + str(
                                          data['scheme']))
            elif content == '李永乐':
                id ='2440693053'
                data = get_weibo(id)
                await cls.sendMessage(2, group, '',
                                      "[QQ:face=175]李永乐在" + str(data['created_at']) + "更新了微博，快来点击查看吧->" + str(
                                          data['scheme']))
            elif content == '李林':
                id= '6444289173'
                data = get_weibo(id)
                await cls.sendMessage(2, group, '',
                                      "[QQ:face=175]李林在" + str(data['created_at']) + "更新了微博，快来点击查看吧->" + str(
                                          data['scheme']))

            elif content == '唐迟':
                id = '1491569192'
                data = get_weibo(id)
                await cls.sendMessage(2, group, '',
                                      "[QQ:face=175]唐迟在" + str(data['created_at']) + "更新了微博，快来点击查看吧->" + str(
                                          data['scheme']))
            if re.search('免费资料',content):
                await  cls.silence(qq, group, duration = 2592000)
                await  cls.withdrawMessage(group, msgid)
        if group == '681882220' or group == '739538831':
            if content == '倒计时' or re.search('倒计时', content) and re.search('考研', content) or re.search('多少天',
                                                                                                       content) and re.search(
                    '考研', content) or re.search('几天', content) and re.search('考研', content):
                # 构造一个将来的时间
                future = datetime.strptime('2019-12-21 00:00:00', '%Y-%m-%d %H:%M:%S')
                # 当前时间
                now = datetime.now()
                # 求时间差
                delta = future - now
                hour = delta.seconds / 60 / 60
                minute = (delta.seconds - hour * 60 * 60) / 60
                seconds = delta.seconds - hour * 60 * 60 - minute * 60
                print_now = now.strftime('%Y-%m-%d %H:%M:%S')
                print("今天是：", print_now)
                print("距离 2019-12-21 \"work\" 还剩下：%d天" % delta.days)
                print(delta.days, hour, minute, seconds)
                # 复读机
                await cls.sendMessage(2, group, '',
                                "[QQ:face=175]距离 2019-12-21 考研还有%d天" % delta.days)
            elif content == '张宇':
                id = '2058586920'
                data = get_weibo(id)
                await cls.sendMessage(2, group, '',
                                      "[QQ:face=175]张宇在"+str(data['created_at'])+"更新了微博，快来点击查看吧->"+str(data['scheme']))
            elif content == '汤家凤':
                id = '2644595644'
                data = get_weibo(id)
                await cls.sendMessage(2, group, '',
                                      "[QQ:face=175]汤家凤在" + str(data['created_at']) + "更新了微博，快来点击查看吧->" + str(
                                          data['scheme']))
            elif content == '肖秀荣':
                id = '1227078145'
                data = get_weibo(id)
                await cls.sendMessage(2, group, '',
                                      "[QQ:face=175]肖秀荣在" + str(data['created_at']) + "更新了微博，快来点击查看吧->" + str(
                                          data['scheme']))
            elif content == '李永乐':
                id ='2440693053'
                data = get_weibo(id)
                await cls.sendMessage(2, group, '',
                                      "[QQ:face=175]李永乐在" + str(data['created_at']) + "更新了微博，快来点击查看吧->" + str(
                                          data['scheme']))
            elif content == '李林':
                id= '6444289173'
                data = get_weibo(id)
                await cls.sendMessage(2, group, '',
                                      "[QQ:face=175]李林在" + str(data['created_at']) + "更新了微博，快来点击查看吧->" + str(
                                          data['scheme']))
            # elif content == '徐涛':
            #     id = '2140522467'
            #     data = get_weibo(id)
            #     await cls.sendMessage(2, group, '',
            #                           "[QQ:face=175]徐涛在" + str(data['created_at']) + "更新了微博，快来点击查看吧->" + str(
            #                               data['scheme']))
            elif content == '唐迟':
                id = '1491569192'
                data = get_weibo(id)
                await cls.sendMessage(2, group, '',
                                      "[QQ:face=175]唐迟在" + str(data['created_at']) + "更新了微博，快来点击查看吧->" + str(
                                          data['scheme']))
            # elif content == '海大研招网':
            #     news = check_info()
            #     if  news['flag']:
            #         await cls.sendMessage(2, '605565297', '',
            #                                 "中国海洋大学研究生招生信息网有新发布的内容，\n主题为：《"+news.get('info_text')+'》\n点击网址进入查看：'+news.get('url'))
            #     elif not news['flag']:
            #                 await cls.sendMessage(2, '605565297', '',
            #                                 "中国海洋大学研究生招生信息网暂时没有新发布的内容，\n最新发布的主题为：《"+news.get('info_text')+'》\n点击网址进入查看：'+news.get('url'))
            if re.search('免费资料',content):
                await  cls.silence(qq, group, duration = 2592000)
                await  cls.withdrawMessage(group, msgid)
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
    async def groupMemberIncrease(cls, type=1, qq='',  # @ReservedAssignment
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
        if group == '605565297':
            # await cls.getGroupMemberList(group)
            # print(cls.getGroupMemberList(group))
            # print(str(dict(cls.getGroupMemberList(group))))
            await cls.sendMessage(2, group, '',
                                          "进群请改备注，如：20-软工专-张三[QQ:face=144]记得看群文件和群公告，可以解决大多数疑惑[QQ:face=183]不要发广告[QQ:face=181]\n"+"[QQ:at={0}]".format(qq))
        if group == '681882220':
            await cls.sendMessage(2, group, '',
                                          "进群请改备注，如：20-软工专-张三[QQ:face=144]记得看群文件和群公告，可以解决大多数疑惑[QQ:face=183]不要发广告[QQ:face=181]\n"+"[QQ:at={0}]".format(qq))
    @classmethod
    async def groupMemberDecrease(cls, type=1, qq='',  # @ReservedAssignment
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