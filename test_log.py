import logging
import time


class Logger(object):
    def __init__(self, logger_name=None, level='info'):
        global log_path
        log_path = '.'
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOSET)
        self.logFileName = time.strftime("%Y_%m_%d_") + f'_{logger_name}.log'
        self.backupCount = 5

        level = level.upper()
        try:
            self.consoleOutputLevel = level  # debug,error,info,warning,critical
        except Exception as e:
            self.consoleOutputLevel = 'INFO'
            print("日志等级有误", e)

        try:
            self.fileOutputLevel = level
        except Exception as e:
            self.fileOutputLevel = 'INFO'
            print("文件等级有误", e)
