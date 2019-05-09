import os
import string
import operator
from datetime import date
from shutil import copyfile
from dateutil.relativedelta import * 
import re

"""
This program looks into a file system and tries to find a file with a certain
value.
"""

class findFloridaFile():
    #default_path = r'\\sb2210009332.ad.ing.net\FACTORLINK\Import\Clients\Handled'
    start_path = ''
    result_path = r'H:\My Documents\Programming\clientfiles\\'
    max_time = 0
    file_type = ''
    file_found = False

    def __init__(self, file = 'SD5', total_days = 100, source = 'DEV') -> None:
        self.max_time = total_days
        self.start_path = self.find_source_directory(self.find_start_path(source))
        self.result_path = self.create_result_directory(self.result_path)
        self.file_type = file

    def __repr__(self) -> str:
        return self.file_type

    @staticmethod
    def find_start_path(source) -> str:
        if source == 'DEV':
            return 'sb2210009332'
        elif source == 'TST':
            return 'sb2210009743'
        elif source == 'ACC':
            return 'sb2110009096'
        return 'sb2210009332'

    @staticmethod
    def find_source_directory(source) -> os.path:
        return r'\\'+source+r'.ad.ing.net\FACTORLINK\Florida\Backup' + '\\'

    @staticmethod
    def changeFilePath(self) -> None:
        new_path = input("Change file path? Current: " + self.start_path + " ")
        if new_path.upper() == "Y":
            self.start_path = input("Give new file path: ")

    @staticmethod
    def changeResultPath(self) -> None:
        new_path = input("Change result path? Current: " + self.result_path + " ")
        if new_path.upper() == "Y":
            self.result_path = input("Give new result path: ")
    
    @staticmethod
    def create_result_directory(path):
        result_path = path

        if not os.path.exists(result_path):
            os.makedirs(result_path)
        return result_path

    def main(self, path) -> None:
        print("to here")
        
        num_months = 0
        file_found = False
        while not(file_found) and num_months <self.max_time:
            date_now = self.find_date_stamp(num_months)
            start_path = self.find_directory(path, date_now)
            
            print(start_path)
            file_path = self.find_directory(path, num_months)
            if self.check_directory(file_path):
                file_found = self.run_directory(file_path)
            num_months+= 1
           # print(file_path + ' number of days back: ' + str(num_days))

        if file_found:
            print('file is found!')
            print(self.regex)
        else:
            print('no file is found :( ')

    def find_directory(self, path, sub_path) -> os.path:
        return path + str(sub_path) + r'\\' 


    def find_date_stamp(self, num_months) -> date:
        new_date = date.today() + relativedelta(months=-num_months)
        return new_date.strftime("%Y-%m")
        

    def find_inner_directory(self, path, num_days) -> os.path:
        new_date = str(datetime.date.today() - datetime.timedelta(days=num_days))
        return(path + new_date)

    def check_directory(self, path) -> bool:
        return os.path.exists(path)
    
    def run_directory(self, path) -> bool:
        for file in os.listdir(path):
            if self.read_file(path, file):
                copyfile(path+file, self.result_path+file)
                return(True)
        return(False)            

    def read_file(self, path, file) -> bool:            
        with open(path + file, 'r') as read_file:
            new_line = read_file.readline()
            update_line = new_line.replace(';',' ')

            if self.file_format:
                return self.find_text(update_line.split()[0])
            else:
                return self.find_text(update_line)

    def find_text(self, line) -> bool:
        regex = re.compile(self.regex)
        regex_search = regex.search(line)

        return regex_search != None             
    

            

if __name__ == '__main__':
    print("Program started from main")
    f = findFloridaFile()
else:
    print("Program started from outside")
    pass
