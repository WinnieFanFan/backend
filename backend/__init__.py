import logging
def get_logger(name, level):
    logging.basicConfig(format='%(levelname)s: %(message)s - %(asctime)s - %(pathname)s[line:%(lineno)d] ',
                        level=level)
    return logging.getLogger(name)