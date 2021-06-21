import importlib
import sys
import pytz

from datetime import datetime
from functools import wraps
from time import time
from typing import Any 

from fastapi import FastAPI

from app.conf import settings 

def resolve_dotted_path(path: str) -> Any: 
    '''
    retrieves attribute (var, function, class, etc) from module by dotted path
    .. code-block:: python
        
        from datetime.datetime import utcnow as default_utcnow
        utcnow = resolve_dotted_path('datetime.datetime.utcnow')
        assert utcnow == default_utcnow

    :param path: dotted path to the attribute in module
    :return: desired attribute or None 
    '''
    splitted = path.split(".")
    if len(splitted) <= 1:
        return importlib.import_module(path)
    module, attr = ".".join(splitted[:-1]), splitted[-1]
    module = importlib.import_module(module)
    return getattr(module, attr)

def get_logger() -> Any: 
    '''
    gets logger that will be used thoughout this whole library.
    first it finds and imports the logger, then if it can be configured
    using loguru-compatible config, it does so.

    :return: desired logger (pre-configured if loguru)
    '''
    lib_logger = resolve_dotted_path(settings.logger)
    if hasattr(lib_logger, "configure"):
        logger_config = {
            "handlers": [
                {
                    "sink": sys.stdout,
                    "level": settings.log_level,
                    "format": "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>"
                    " | <level>{level: <8}</level> | "
                    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:"
                    "<cyan>{line}</cyan> -"
                    " <level>{message}</level>",
                }
            ]
        }
        lib_logger.configure(**logger_config)

    return lib_logger

logger = get_logger()

def get_current_app() -> FastAPI:
    '''
    retrieves FastAPI app instance from the path, specified in project's conf.
    :return: FastAPI app
    '''
    # to do = cache this
    app = resolve_dotted_path(settings.fastapi_app)
    return app

def async_timing(func):
    '''
    decorator for logging timing of async functions.
    used in this library internally for taking DB functions performance.

    :param func: fuction to be decorated
    :return: wrapped function
    '''
    @wraps(func)
    async def wrap(*args, **kwargs):
        time1 = time()

        raised_exception = True 
        try: 
            ret = await func(*args, **kwargs)
            raised_exception = False 
            if not settings.debug_timing:
                return ret 
        finally: 
            time2 = time()
            duration = (time2 - time1) * 1000.0

            logger.debug(
                "\t [TIMING] {:s} {:s} {:.3f} ms".format(
                    func.__module__.ljust(20),
                    func.__name__.ljust(20),
                    duration,
                )
            )
            if not raised_exception:
                return ret 
    
    return wrap 

def get_now() -> datetime:
    '''
    retrieves `now` function from path, specificied in project's conf.
    :return: datetime of "now"
    '''
    # to do = cache this
    if settings.now_function:
        return resolve_dotted_path(settings.now_function)()
    return datetime.now(tz=get_timezone())

def get_timezone():
    '''
    retrieves timezone name from settings and tries to create tzinfo from it.
    :return: tzinfo object
    '''
    return pytz.timezone(settings.TZ)