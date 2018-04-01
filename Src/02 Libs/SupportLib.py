# -*- coding: ISO-8859-1 -*-

import time, re, os, logging
import datetime


class SupportLib:

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)-35s %(levelname)-12s %(message)s',
                            datefmt='%d.%m.%Y %H:%M:%S',
                            filename='%s/RobotFramework_Execution.log' % (os.getcwd()),
                            filemode='a')

        self.logger = logging.getLogger('SupportLib')

    def GetTime(self):
        """
        @Returns current time
        """
        return (time.strftime("%d.%m.%Y %H:%M:%S"), time.strftime("%Y-%m-%d 00:00:00.0"), time.strftime("%Y-%m-%d"))