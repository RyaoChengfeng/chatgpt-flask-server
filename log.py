import logging
import os
from config import log, debug
from logging.handlers import RotatingFileHandler

DEFAULT_LOG_DIR = "./logs"
DEFAULT_LOG_FILENAME = "app.log"
DEFAULT_LOG_LEVEL = "INFO"
DEFAULT_USE_DEBUG_MODE = False


class Log:
    def __init__(self, log_dir=DEFAULT_LOG_DIR, log_filename=DEFAULT_LOG_FILENAME, log_level=DEFAULT_LOG_LEVEL,
                 use_debug_mode=DEFAULT_USE_DEBUG_MODE):
        os.makedirs(log_dir, exist_ok=True)
        log_file_path = os.path.join(log_dir, log_filename)

        # 设置日志格式
        log_format = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        # 开启 debug 模式
        if use_debug_mode:
            log_level = logging.DEBUG

        # 设置文件处理器
        file_handler = RotatingFileHandler(log_file_path, maxBytes=1024 * 1024 * 10, backupCount=5)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(log_format)

        # 设置控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(log_format)

        # 设置日志记录器
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)


logger = Log(log_dir=log.log_dir, log_filename=log.log_filename, log_level=log.log_level,
             use_debug_mode=debug)
