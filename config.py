import yaml
import os
from dataclasses import dataclass


@dataclass
class Log:
    log_dir: str
    log_filename: str
    log_level: str
    use_debug_mode: bool


@dataclass
class OpenAI:
    email: str
    password: str
    session_token: str
    proxy: str


@dataclass
class App:
    host: str
    port: int


@dataclass
class Config:
    log: Log
    openai: OpenAI
    app: App


def load_config(config_path: str) -> Config:
    with open(config_path, "r") as f:
        config_dict = yaml.safe_load(f)
        log = Log(**config_dict["log"])
        openai = OpenAI(**config_dict["openai"])
        app = App(**config_dict["app"])
        return Config(log=log, openai=openai, app=app)


# 获取当前脚本所在文件夹路径
curPath = os.path.dirname(os.path.realpath(__file__))
env = os.getenv('ENVIRONMENT', "dev")
# 获取yaml文件路径
yamlPath = os.path.join(curPath, "env/" + str(env) + ".yaml")
try:
    config = load_config(yamlPath)
    log = Log(**config.log.__dict__)
    openai = OpenAI(**config.openai.__dict__)
    app = App(**config.app.__dict__)
except Exception as e:
    # logger.error(e)
    raise e
else:
    print("读取配置文件:" + yamlPath)
