import logging
from functools import wraps
import os
import sys

class LoggingConfigurator:
    def __init__(self):
        self.setup_logging()

    def setup_logging(self):
        # Ensure the logs directory exists
        if not os.path.exists('logs'):
            os.makedirs('logs')

        # Configure formatters
        default_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        access_formatter = logging.Formatter('%(asctime)s - %(message)s')

        # Configure handlers
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(default_formatter)
        console_handler.setLevel(logging.DEBUG)

        uvicorn_handler = logging.FileHandler('logs/uvicorn.log')
        uvicorn_handler.setFormatter(default_formatter)
        uvicorn_handler.setLevel(logging.DEBUG)

        uvicorn_error_handler = logging.FileHandler('logs/uvicorn.error.log')
        uvicorn_error_handler.setFormatter(default_formatter)
        uvicorn_error_handler.setLevel(logging.ERROR)

        uvicorn_access_handler = logging.FileHandler('logs/uvicorn.access.log')
        uvicorn_access_handler.setFormatter(access_formatter)
        uvicorn_access_handler.setLevel(logging.INFO)

        ddtrace_handler = logging.FileHandler('logs/ddtrace.log', mode='a', encoding='utf-8')
        ddtrace_handler.setFormatter(default_formatter)
        ddtrace_handler.setLevel(logging.DEBUG)

        sqlalchemy_handler = logging.FileHandler('logs/sqlalchemy.log')
        sqlalchemy_handler.setFormatter(default_formatter)
        sqlalchemy_handler.setLevel(logging.DEBUG)

        botocore_handler = logging.FileHandler('logs/botocore.log')
        botocore_handler.setFormatter(default_formatter)
        botocore_handler.setLevel(logging.DEBUG)

        agent_handler = logging.FileHandler('logs/agent.log')
        agent_handler.setFormatter(default_formatter)
        agent_handler.setLevel(logging.DEBUG)

        # Clear existing handlers to avoid duplicate logs
        for logger_name in logging.root.manager.loggerDict:
            logger = logging.getLogger(logger_name)
            logger.handlers = []

        # Configure root logger
        logging.basicConfig(level=logging.DEBUG, handlers=[console_handler, uvicorn_handler])

        # Configure loggers
        logger_names = [
            'uvicorn', 'uvicorn.access', 'uvicorn.error', 'ddtrace',
            'datadog', 'sqlalchemy', 'botocore', 'agent'
        ]

        for name in logger_names:
            logger = logging.getLogger(name)
            logger.setLevel(logging.DEBUG)
            logger.addHandler(console_handler)
            if name == 'uvicorn.access':
                logger.addHandler(uvicorn_access_handler)
                logger.setLevel(logging.INFO)
            elif name == 'uvicorn.error':
                logger.addHandler(uvicorn_error_handler)
                logger.setLevel(logging.ERROR)
            elif name == 'uvicorn':
                logger.addHandler(uvicorn_handler)
            elif name == 'ddtrace' or name == 'datadog':
                logger.addHandler(ddtrace_handler)
            elif name == 'sqlalchemy':
                logger.addHandler(sqlalchemy_handler)
            elif name == 'botocore':
                logger.addHandler(botocore_handler)
            elif name == 'agent':
                logger.addHandler(agent_handler)

        for logger_name in logging.root.manager.loggerDict:
            if logger_name not in logger_names:
                logger = logging.getLogger(logger_name)
                logger.addHandler(uvicorn_handler)

        # Test log messages to confirm configuration
        root_logger = logging.getLogger()
        root_logger.debug("Root logger is configured.")
        logger = logging.getLogger('agent')
        logger.debug("Agent logger is configured.")

    @staticmethod
    def log_method(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            logger = logging.getLogger('agent')
            logger.info(f"Method {func.__name__} called with args: {args}, kwargs: {kwargs}")
            try:
                result = func(self, *args, **kwargs)
                logger.info(f"Method {func.__name__} returned: {result}")
                return result
            except Exception as e:
                logger.error(f"Method {func.__name__} raised an exception: {e}")
                raise
        return wrapper

    @staticmethod
    def log_debug(message):
        logger = logging.getLogger('agent')
        logger.debug(message)

    @staticmethod
    def log_info(message):
        logger = logging.getLogger('agent')
        logger.info(message)

    @staticmethod
    def log_error(message):
        logger = logging.getLogger('agent')
        logger.error(message)