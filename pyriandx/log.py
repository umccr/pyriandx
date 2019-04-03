import coloredlogs, logging

coloredlogs.DEFAULT_LOG_FORMAT = '%(message)s'
coloredlogs.install(level='INFO')
log = logging.getLogger()

