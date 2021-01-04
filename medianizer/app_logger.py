import logging

file_log_fmt = ("%(asctime)s - [%(levelname)s] - "
                "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
stream_log_fmt = ("%(asctime)s [%(levelname)s] - %(message)s")


def get_file_handler():
    file_handler = logging.FileHandler('medianizer.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(file_log_fmt))
    return file_handler


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(stream_log_fmt))
    return stream_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger
