import flask
import json
import chatgpt
from flask import request
from config import app

server = flask.Flask(__name__)


@server.route('/chat', methods=['post'])
def chatapi():
    requestJson = request.get_data()
    if requestJson is None or requestJson == "" or requestJson == {}:
        resu = {'code': 1, 'msg': '请求内容不能为空'}
        return json.dumps(resu, ensure_ascii=False)
    data = json.loads(requestJson)
    print(data)
    try:
        msg = chatgpt.chat(data['msg'])
    except Exception as error:
        print("接口报错")
        resu = {'code': 1, 'msg': '请求异常: ' + str(error)}
        return json.dumps(resu, ensure_ascii=False)
    else:
        resu = {'code': 0, 'data': msg}
        return json.dumps(resu, ensure_ascii=False)


if __name__ == '__main__':
    server.run(port=app.port, host=app.host)

    # res = get_cf_shit()
    # if res['success']:
    #     server.config.from_object(Config())
    #     scheduler = APScheduler()
    #     scheduler.init_app(server)
    #     scheduler.start()
    #     server.run(port=app.port, host=app.host)
    # else:
    #     print('获取Cf Cookie失败')
