import logging

logger = logging.getLogger(__name__)

class TwoHelloWorld(object):
    def __init__(self):
        pass

    def run(self, new):
        return "hello2" + new
