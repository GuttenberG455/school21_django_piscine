
from datetime import datetime
from django.conf import settings


class Logs(object):

    @staticmethod
    def get_logs():
        try:
            with open(settings.LOGFILE, 'r') as fd:
                data_logs = fd.readlines()
            return data_logs
        except IOError:
            return []

    @staticmethod
    def write_log(content):
        date = datetime.now()
        with open(settings.LOGFILE, 'a+') as fd:
            fd.write("%s  :  %s\n" % (date.strftime("%b %d %Y %H:%M:%S"), content))