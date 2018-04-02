# -*- coding: ISO-8859-1 -*-

import time, re, os, logging
import datetime
import csv


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


    def read_csv_file(self, filename):
        '''This creates a keyword named "Read CSV File"

        This keyword takes one argument, which is a path to a .csv file. It
        returns a list of rows, with each row being a list of the data in
        each column.
        '''
        data = []
        with open(filename, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        return data