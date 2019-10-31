import logging

logger = logging.getLogger(__name__)


class OneHelloWorld(object):

    def __init__(self):
        self.message = list(['z', 'z2'])

    def get(self, new):
        for x in range(len(self.message)):
            if(self.message[x] == new):
                return "find: " + new
        return "we do not find" + new

    def put(self, new):
        self.message.append(new)

if __name__ == "__main__":
    pass
