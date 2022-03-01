import logging

FORMAT = '%(asctime)s %(levelname)s: %(message)s'  # 顯示出的格式，可以自己修改、asctime日期時間, 格式為 YYYY-MM-DD HH:mm:SS,ms
DATE_FORMAT = '%Y%m%d %H:%M:%S'  # 更改日期格式
# logging.basicConfig(level=logging.DEBUG, filemode='w', format=FORMAT)
logging.basicConfig(level=logging.DEBUG, filename='myLog.log', filemode='w', format=FORMAT)
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
