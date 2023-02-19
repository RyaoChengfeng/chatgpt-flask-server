import flask
import json
from flask import request
from revChatGPT.V1 import Chatbot

from config import app, openai

config = {
    "email": openai.email,
    "password": openai.password
}

server = flask.Flask(__name__)
chatbot = Chatbot(config, conversation_id=None)


def chat(msg):
    message = chatbot.get_chat_response(msg)['message']
    print(message)
    return message


@server.route('/chat', methods=['post'])
def chatapi():
    requestJson = request.get_data()
    if requestJson is None or requestJson == "" or requestJson == {}:
        resu = {'code': 1, 'msg': '请求内容不能为空'}
        return json.dumps(resu, ensure_ascii=False)
    data = json.loads(requestJson)
    print(data)
    try:
        msg = chat(data['msg'])
    except Exception as error:
        print("接口报错")
        resu = {'code': 1, 'msg': '请求异常: ' + str(error)}
        return json.dumps(resu, ensure_ascii=False)
    else:
        resu = {'code': 0, 'data': msg}
        return json.dumps(resu, ensure_ascii=False)


if __name__ == '__main__':
    server.run(port=app.port, host=app.host)
