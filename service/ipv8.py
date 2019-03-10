import os
import logging
import sqlite3


class IPV8Service(object):

    def __init__(self):
        '''
        Setup environment
        '''
        os.environ['PYTHON_EGG_CACHE'] = os.path.realpath(os.path.join(os.getenv('ANDROID_PRIVATE'), '../cache'))

        # Set logging format and level
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

    def run(self):
        from twisted.internet import reactor
        from twisted.plugins.android_plugin import Options, service_maker

        options = Options()
        Options.parseOptions(options, os.getenv('PYTHON_SERVICE_ARGUMENT', '').split())
        service_maker.makeService(options)
        print "WILL RUN SERVICE"
        reactor.run()


if __name__ == '__main__':
    IPV8Service().run()
