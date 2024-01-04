import logging
LOG_FILE = '/tmp/pgadmin4.log'
FILE_LOG_LEVEL = logging.DEBUG
FILE_LOG_FORMAT = '%(asctime)s: %(levelname)s:\t%(message)s'
CONSOLE_LOG_LEVEL = logging.DEBUG
CONSOLE_LOG_FORMAT = '%(levelname)s:\t%(message)s'
SERVER_MODE = True
LANGUAGES = {
    'ru': 'Russian',
    'en': 'English',
}
DEFAULT_BINARY_PATHS = {
        'pg': '/usr/local/pgsql-16',
        'pg-16': '/usr/local/pgsql-16'
}
