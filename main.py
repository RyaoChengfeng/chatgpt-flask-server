import flask
import json
import chatgpt
from flask import request
from config import app, debug
from log import logger

server = flask.Flask(__name__)


@server.route('/chat', methods=['post'])
def chatapi():
    requestJson = request.get_data()
    if requestJson is None or requestJson == "" or requestJson == {}:
        resu = {'code': 1, 'message': 'empty request body!'}
        return json.dumps(resu, ensure_ascii=False)
    data = json.loads(requestJson)
    logger.debug("request data: " + str(data))
    try:
        msg = chatgpt.chat(data['message'])
    except Exception as error:
        logger.error('chatgpt request error: ' + str(error))
        resu = {'code': 1, 'message': 'chatgpt request error: ' + str(error)}
        return json.dumps(resu, ensure_ascii=False)
    else:
        resu = {'code': 0, 'data': msg}
        return json.dumps(resu, ensure_ascii=False)


if __name__ == '__main__':
    server.run(port=app.port, host=app.host, debug=debug)

    # res = get_cf_shit()
    # if res['success']:
    #     server.config.from_object(Config())
    #     scheduler = APScheduler()
    #     scheduler.init_app(server)
    #     scheduler.start()
    #     server.run(port=app.port, host=app.host)
    # else:
    #     print('获取Cf Cookie失败')
