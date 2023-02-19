import uuid
import requests
import traceback
from revChatGPT.V1 import Chatbot
from log import logger
from config import openai

# {
#     "email": "",
#     "password": "",
#     "session_token": "",
#     "conversation_id": "UUID...",
#     "parent_id": "UUID...",
#     "proxy": "...",
#     "paid": false
# }

config = {
    "email": openai.email,
    "password": openai.password,
    "session_token": openai.session_token,
    "proxy": openai.proxy
}

chatbot = Chatbot(config, conversation_id=None)
sessions = {}


def chat(msg):
    message = ""
    for data in chatbot.ask(
            prompt=msg
    ):
        message = data["message"]

    logger.debug("message: " + message)
    return message


# def chat(msg, sessionid=""):
#     try:
#         if msg.strip() == '':
#             return '您好，我是人工智能助手，如果您有任何问题，请随时告诉我，我将尽力回答。\n如果您需要重置我们的会话，请回复`重置会话`'
#         # 获得对话session
#         session = get_chat_session(sessionid)
#         if '重置会话' == msg.strip():
#             session.reset_conversation()
#             return "会话已重置"
#         # 与ChatGPT交互获得对话内容
#         message = session.get_chat_response(msg)
#         print("会话ID: " + str(sessionid))
#         print("ChatGPT返回内容: ")
#         print(message)
#         return message
#     except Exception as error:
#         chatbot.reset_chat()
#         traceback.print_exc()
#         return str('异常: ' + str(error) + '\n如果报错持续出现，请对我发送 `重置会话`')

def get_cf_shit():
    global config

    try:
        print('开始获取Cloudflare Cookie')
        data = {"timeout": 60, "url": 'http://chat.openai.com'}
        res = requests.post(url="https://cf-shit.aurorax.cloud/challenge", json=data).json()
        print("cf-shit回复: " + str(res))
        if res['success']:
            print('获取成功')
            config['cf_clearance'] = res['cookies']['cf_clearance']
            config['user_agent'] = res['user_agent']
        else:
            print('获取失败')
        return res
    except Exception as error:
        print("cf-shit获取失败：", error)


# 对话session
class ChatSession:
    def __init__(self):
        self.parent_id = None
        self.conversation_id = None
        self.reset_conversation()

    # 重置对话方法
    def reset_conversation(self):
        self.conversation_id = None
        self.parent_id = generate_uuid()

    # 获取对话内容方法
    def get_chat_response(self, message):
        try:
            chatbot.conversation_id = self.conversation_id
            chatbot.parent_id = self.parent_id
            return chatbot.ask(message)['message']
        finally:
            self.conversation_id = chatbot.conversation_id
            self.parent_id = chatbot.parent_id


# 获取对话session
def get_chat_session(sessionid):
    if sessionid not in sessions:
        sessions[sessionid] = ChatSession()
    return sessions[sessionid]


# 以流的方式对话
def printMessage():
    text = ''
    for i in chatbot.ask("你好"):
        print(str(i['message']).replace(text, ''))
        text = i['message']


def generate_uuid() -> str:
    uid = str(uuid.uuid4())
    return uid


class Config(object):
    JOBS = [
        {
            'id': 'get_cf_shit',
            'func': '__main__:get_cf_shit',
            'trigger': 'interval',
            'minutes': 60
        }
    ]
