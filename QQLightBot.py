#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
import asyncio
import binascii
from importlib import import_module
import json
import logging
import os
import sys
from typing import List
import aiohttp

"""
QQLight接口实现
"""
class MsgDict(dict):

    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        if key in self:
            value = self[key]
            if isinstance(value, dict):
                value = MsgDict(value)
            return value
        return None


class ApiProtocol:

    _ws = None
    _session = None

    @classmethod
    def _init(cls, ws, session):
        """初始化协议设置ws连接对象和网络请求对象
        :param cls:
        :param ws:
        :param session:
        """
        cls._ws = ws
        cls._session = session

    @classmethod
    def _makeData(cls, method, **kwargs):
        """封装成json数据发送
        :param cls:
        :param method:        方法
        """
        data = {
            'id': binascii.hexlify(os.urandom(6)).decode(),
            'method': method,
            'params': kwargs
        }
        if len(kwargs) == 0:
            data.pop('params')
        return data

    @classmethod
    def getImageUrl(cls, guid):
        """通过guid拼接图片的url地址
        :param cls:
        :param guid:
        """
        return 'http://gchat.qpic.cn/gchatpic_new/0/0-0-{}/0'.format(
            guid.replace('-', '').upper().split('.')[0])

    @classmethod
    def formatAt(cls, qq):
        """at某个人
        :param cls:
        :param qq:            qq或者all
        """
        return '[QQ:at={}]'.format(qq)

    @classmethod
    def formatFace(cls, fid):
        """QQ表情
        :param cls:
        :param fid:           表情代码，旧表情范围（0-170）
        """
        return '[QQ:face={}]'.format(fid)

    @classmethod
    def formatEmoji(cls, eid):
        """Emoji表情
        :param cls:
        :param eid:           表情代码
        """
        return '[QQ:emoji={}]'.format(eid)

    @classmethod
    def formatImage(cls, path, flash=False):
        """图片
        :param cls:
        :param path:          图片GUID或者URL
        :param flash:         True表示闪照
        """
        return '[QQ:{0}pic={1}]'.format('flash,' if flash else '', path)

    @classmethod
    async def onConnect(cls):
        """连接成功
        """

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

    @classmethod
    async def friendRequest(cls, qq='', message=''):
        """事件.收到好友请求
        :param cls:
        :param qq:          QQ
        :param message:     验证消息
        """

    @classmethod
    async def becomeFriends(cls, qq=''):
        """事件.成为好友
        :param cls:
        :param qq:          QQ
        """

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

    @classmethod
    async def adminChange(cls, type=1, qq='', group=''):  # @ReservedAssignment
        """事件.群管理员变动
        :param cls:
        :param type:        1=成为管理 2=被解除管理
        :param qq:          QQ
        :param group:       QQ群
        """

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

    @classmethod
    async def updateCookies(cls):
        """事件.Cookies更新
        :param cls:
        """

    @classmethod
    async def sendMessage(cls, type, group, qq, content):  # @ReservedAssignment
        """接口.发送消息
        :param cls:
        :param type:        1=好友消息、2=群消息、3=群临时消息、4=讨论组消息、5=讨论组临时消息、6=QQ临时消息
        :param group:       群号或讨论组号，发送消息给好友的情况下忽略
        :param qq:          QQ号，发送消息给群或讨论组的情况下忽略
        :param content:     消息内容
        """
        await cls._ws.send_json(cls._makeData(
            'sendMessage', type=type, group=group,
            qq=qq, content=content))

    @classmethod
    async def withdrawMessage(cls, group = '', msgid = ''):
        """接口.撤回消息
        :param cls:
        :param group:       群号或讨论组号
        :param msgid:       消息ID，群消息会存在，其余情况下为空
        """
        await cls._ws.send_json(cls._makeData(
            'withdrawMessage', group=group, msgid=msgid))

    @classmethod
    async def getFriendList(cls):
        """接口.获取好友列表
        :param cls:
        """
        await cls._ws.send_json(cls._makeData('getFriendList'))
        result = await cls._ws.receive()
        return MsgDict(json.loads(result.data))

    @classmethod
    async def addFriend(cls, qq, message):
        """接口.添加好友
        :param cls:
        :param qq:          QQ号
        :param message:     验证消息，可选
        """
        await cls._ws.send_json(cls._makeData(
            'addFriend', qq=qq, message=message))

    @classmethod
    async def deleteFriend(cls, qq):
        """接口.删除好友
        :param cls:
        :param qq:          QQ号
        """
        await cls._ws.send_json(cls._makeData(
            'deleteFriend', qq=qq))

    @classmethod
    async def getGroupList(cls):
        """接口.获取群列表
        :param cls:
        """
        await cls._ws.send_json(cls._makeData('getGroupList'))
        result = await cls._ws.receive()
        return MsgDict(json.loads(result.data))

    @classmethod
    async def getGroupMemberList(cls, group):
        """接口.获取群成员列表
        :param cls:
        :param group:       群号或讨论组号
        """
        await cls._ws.send_json(cls._makeData(
            'getGroupMemberList', group=group))
        result = await cls._ws.receive()
        return MsgDict(json.loads(result.data))

    @classmethod
    async def addGroup(cls, group, message):
        """接口.添加群
        :param cls:
        :param group:       群号或讨论组号
        :param message:     验证消息，可选
        """
        await cls._ws.send_json(cls._makeData(
            'addGroup', group=group, message=message))

    @classmethod
    async def quitGroup(cls, group):
        """接口.退出群
        :param cls:
        :param group:       群号或讨论组号
        """
        await cls._ws.send_json(cls._makeData(
            'quitGroup', group=group))

    @classmethod
    async def getGroupCard(cls, qq, group):
        """接口.获取群名片
        :param cls:
        :param qq:          QQ号
        :param group:       群号或讨论组号
        """
        await cls._ws.send_json(cls._makeData(
            'getGroupCard', qq=qq, group=group))
        result = await cls._ws.receive()
        print(result.data)
        return MsgDict(json.loads(result.data))

    @classmethod
    async def uploadImage(cls, type, object, data):  # @ReservedAssignment
        """接口.上传图片
        # 该接口并不发送图片，而是将图片上传到QQ服务器，并返回GUID
        # 所获得的GUID只能对type和object指定的对象使用，否则图片可能无法显示
        :param cls:
        :param type:        1=私聊类型的图片、2=群组类型的图片
        :param object:      图片准备发送到的QQ号或群组号
        :param data:        图像数据转换的十六进制字符串
        :return: GUID
        """
        await cls._ws.send_json(cls._makeData(
            'uploadImage', type=type, object=object, data=data))
        result = await cls._ws.receive()
        return MsgDict(json.loads(result.data))

    @classmethod
    async def getQQInfo(cls, qq):
        """接口.获取QQ资料
        :param cls:
        :param qq:          QQ号
        """
        await cls._ws.send_json(cls._makeData(
            'getQQInfo', qq=qq))
        result = await cls._ws.receive()
        return MsgDict(json.loads(result.data))

    @classmethod
    async def getGroupInfo(cls, qq, group):
        """接口.获取群资料
        :param cls:
        :param qq:          QQ号
        :param group:       群组号
        """
        await cls._ws.send_json(cls._makeData(
            'getQQInfo', qq=qq, group=group))
        result = await cls._ws.receive()
        return MsgDict(json.loads(result.data))

    @classmethod
    async def inviteIntoGroup(cls, qq, group):
        """接口.邀请好友入群
        :param cls:
        :param qq:          QQ
        :param group:       群号或讨论组号
        """
        await cls._ws.send_json(cls._makeData(
            'inviteIntoGroup', group=group))

    @classmethod
    async def setGroupCard(cls, qq, group, name):
        """接口.设置群名片
        :param cls:
        :param qq:          QQ
        :param group:       群号或讨论组号
        :param name:        群名片
        """
        await cls._ws.send_json(cls._makeData(
            'setGroupCard', qq=qq, group=group, name=name))

    @classmethod
    async def getLoginAccount(cls):
        """接口.获取当前登录账号
        """
        await cls._ws.send_json(cls._makeData('getLoginAccount'))

    @classmethod
    async def setSignature(cls, content):
        """接口.设置个性签名
        :param cls:
        :param content:     个性签名
        """
        await cls._ws.send_json(cls._makeData(
            'setSignature', content=content))

    @classmethod
    async def getNickname(cls, qq):
        """接口.获取QQ昵称
        :param cls:
        :param qq:          QQ
        """
        await cls._ws.send_json(cls._makeData(
            'getNickname', qq=qq))
        result = await cls._ws.receive()
        return MsgDict(json.loads(result.data))

    @classmethod
    async def getPraiseCount(cls, qq):
        """接口.获取名片点赞数量
        :param cls:
        :param qq:          QQ
        """
        await cls._ws.send_json(cls._makeData(
            'getPraiseCount', qq=qq))
        result = await cls._ws.receive()
        return MsgDict(json.loads(result.data))

    @classmethod
    async def givePraise(cls, qq):
        """接口.点赞名片
        :param cls:
        :param qq:          QQ
        """
        await cls._ws.send_json(cls._makeData(
            'givePraise', qq=qq))

    @classmethod
    async def handleFriendRequest(cls, qq, type, message):  # @ReservedAssignment
        """接口.处理好友请求
        :param cls:
        :param qq:          QQ
        :param type:        1=同意、2=拒绝、3=忽略
        :param message:     拒绝理由，仅在拒绝请求时有效
        """
        await cls._ws.send_json(cls._makeData(
            'handleFriendRequest', qq=qq, type=type, message=message))

    @classmethod
    async def setState(cls, type):  # @ReservedAssignment
        """接口.处理好友请求
        :param cls:
        :param type:        1=我在线上、2=Q我吧、3=离开、4=忙碌、5=请勿打扰、6=隐身
        """
        await cls._ws.send_json(cls._makeData(
            'setState', type=type))

    @classmethod
    async def handleGroupRequest(cls, qq, group, seq,
                                 type, message):  # @ReservedAssignment
        """接口.处理好友请求
        :param cls:
        :param qq:          QQ
        :param group:       群号
        :param seq:         加群请求事件提供的序列号
        :param type:        1=同意、2=拒绝、3=忽略
        :param message:     拒绝时的拒绝理由，其它情况忽略
        """
        await cls._ws.send_json(cls._makeData(
            'handleGroupRequest', qq=qq, group=group, seq=seq,
            type=type, message=message))

    @classmethod
    async def kickGroupMember(cls, qq, group):
        """接口.移除群成员
        :param cls:
        :param qq:          QQ
        :param group:       群号
        """
        await cls._ws.send_json(cls._makeData(
            'kickGroupMember', qq=qq, group=group))

    @classmethod
    async def silence(cls, qq, group, duration):
        """接口.禁言
        :param cls:
        :param qq:          QQ
        :param group:       群号
        :param duration:    禁言时间，单位为秒，为0时解除禁言
        """
        await cls._ws.send_json(cls._makeData(
            'silence', qq=qq, group=group, duration=duration))

    @classmethod
    async def globalSilence(cls, group, enable):
        """接口.全体禁言
        :param cls:
        :param group:       群号
        :param enable:      True为全体禁言,False为取消全体禁言
        """
        await cls._ws.send_json(cls._makeData(
            'globalSilence', group=group, enable=enable))

    @classmethod
    async def getCookies(cls):
        """接口.获取Cookies
        :param cls:
        """
        await cls._ws.send_json(cls._makeData('getCookies'))
        result = await cls._ws.receive()
        return MsgDict(json.loads(result.data))

    @classmethod
    async def getBkn(cls):
        """接口.获取Bkn
        :param cls:
        """
        await cls._ws.send_json(cls._makeData('getBkn'))
        result = await cls._ws.receive()
        return MsgDict(json.loads(result.data))

    @classmethod
    async def getClientKey(cls):
        """接口.获取ClientKey
        :param cls:
        """
        await cls._ws.send_json(cls._makeData('getClientKey'))
        result = await cls._ws.receive()
        return MsgDict(json.loads(result.data))


async def _run(args, entity):
    logger = logging.getLogger('QQLightBot')
    # 创建session
    async with aiohttp.client.ClientSession(timeout=aiohttp.client.ClientTimeout(total=60)) as session:
        logger.info(
            'connect to ws://{0}:{1}{2}'.format(args.hostname, args.port, args.path))
        # 连接服务器
        async with session.ws_connect('ws://{0}:{1}{2}'.format(args.hostname, args.port, args.path)) as ws:
            logger.info('connect succeed')
            try:
                logger.info('entity _init')
                entity._init(ws, session)
            except AttributeError:
                logger.error('class %r has no method %r' % (entity, '_init'))
            await entity.onConnect()
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    logger.debug('received data: {}'.format(msg.data))
                    try:
                        # 解析json数据
                        msg = MsgDict(json.loads(msg.data))
                        if 'error' in msg:
                            logger.warn(msg.error)
                        if msg.event != None:
                            # 调用函数并传递参数
                            try:
                                if msg.params != None:
                                    await getattr(entity, msg.event)(**msg.params)
                                else:
                                    await getattr(entity, msg.event)()
                            except Exception as e:
                                logger.exception(e)
                    except Exception as e:
                        logger.exception(e)
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    logger.error('connection lost')
                    break


def main(argv: List[str]) -> None:
    arg_parser = ArgumentParser(
        description='QQLightBot WebSocket Client',
        prog='QQLightBot'
    )
    # 功能代码文件
    arg_parser.add_argument(
        'entry_func',
        help=('Should be specified in the module:class'),
        metavar='entry-func'
    )
    # 连接地址
    arg_parser.add_argument(
        '-H', '--hostname',
        help='connect to server on (default: %(default)r)',
        default='127.0.0.1'
    )
    # 端口
    arg_parser.add_argument(
        '-P', '--port',
        help='connect port to server on (default: %(default)r)',
        type=int,
        default='49632'
    )
    # 路径
    arg_parser.add_argument(
        '-U', '--path',
        help='connect to server url on (default: %(default)r)',
        default='/'
    )
    # 日志级别
    arg_parser.add_argument(
        '-L', '--level',
        help='log level (default: %(default)r), all is: DEBUG INFO WARN ERROR',
        default='DEBUG'
    )

    # 解析命令行参数
    args, _ = arg_parser.parse_known_args(argv)

    mod_str, _, class_str = args.entry_func.partition(':')
    if not mod_str or not class_str:
        arg_parser.error(
            "'entry-func' not in 'module:class' syntax"
        )
    if mod_str.startswith('.'):
        arg_parser.error('relative module names not supported')
    try:
        module = import_module(mod_str)
    except ImportError as e:
        arg_parser.error('unable to import %s: %s' % (mod_str, e))
    try:
        entity = getattr(module, class_str)
    except AttributeError:
        arg_parser.error('module %r has no class %r' % (mod_str, class_str))

    # 配置日志格式
    formatter = logging.Formatter(
        '[%(asctime)s %(module)s:%(funcName)s:%(lineno)s] %(levelname)-8s %(message)s')
    logger = logging.getLogger('QQLightBot')
    logger.setLevel(getattr(logging, args.level) if args.level in (
        'DEBUG', 'INFO', 'WARN', 'ERROR') else logging.DEBUG)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # 开始连接
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_run(args, entity))


if __name__ == '__main__':
    main(sys.argv[1:])