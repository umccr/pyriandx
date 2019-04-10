import coloredlogs, logging

coloredlogs.DEFAULT_LOG_FORMAT = '%(message)s'
coloredlogs.DEFAULT_LEVEL_STYLES = {
    'info': {},
    'notice': {'color': 'magenta'},
    'verbose': {'color': 'blue'},
    'success': {'color': 'green', 'bold': True},
    'spam': {'color': 'cyan'},
    'critical': {'color': 'red', 'bold': True},
    'error': {'color': 'red'},
    'debug': {'color': 'blue'},
    'warning': {'color': 'yellow'}}
coloredlogs.install(level='INFO')
log = logging.getLogger()
