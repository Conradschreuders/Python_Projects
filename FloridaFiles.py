import os
import string
import operator
from datetime import date
import datetime
from shutil import copyfile
from dateutil.relativedelta import * 
import re
import calendar

"""
This program looks into a file system and tries to find a file with a certain
value.
"""

class findFloridaFile():
    #default_path = r'\\sb2210009332.ad.ing.net\FACTORLINK\Import\Clients\Handled'
    start_path = ''
    result_path = r'H:\My Documents\Programming\floridafiles\\'
    max_time = 0
    file_type = ''
    file_found = False

    def __init__(self, file = 'SD3', total_days = 100, source = 'DEV') -> None:
        self.max_time = total_days
        self.start_path = self.find_source_directory(self.find_start_path(source))
        self.result_path = self.create_result_directory(self.result_path)
        self.file_type = file

        self.main(self.start_path)

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
        num_months = 0
        self.file_found = False
        while not(self.file_found) and num_months <self.max_time:
            path_days_date = self.find_date_stamp(num_months)

            self.find_inner_directory(path_days_date[0],path_days_date[1],
                                      path_days_date[2])
            
            num_months+= 1

        if self.file_found:
            print('file is found!')
        else:
            print('no file is found :( ')

    def find_directory(self, path, sub_path) -> os.path:
        return path + str(sub_path) + r'\\' 


    def find_date_stamp(self, num_months) -> tuple:
        new_date =  date.today() + relativedelta(months=-num_months)
        total_days = calendar.monthrange(new_date.year,new_date.month)[1]
        start_path = self.start_path + new_date.strftime("%Y-%m")        
        
        return(start_path,total_days, new_date.strftime("%Y-%m"))

    def find_inner_directory(self, path, num_days, year_month):
        for days in range (num_days):
            if days < 10:
                days = '0'+str(days)
            new_path = path + '\\' + year_month + '-' + str(days) + '\\'
            print(new_path)
            if self.check_directory(new_path):
                if self.run_directory(new_path):
                    break;
            
    def check_directory(self, path) -> bool:
        return os.path.exists(path)
    
    def run_directory(self, path) -> bool:        
        for file in os.listdir(path):
            if self.read_file_name(file):
                print(path+file)
                print(self.result_path+file)
                copyfile(path+file, self.result_path+'\\'+file)
                self.file_found = True
                return True
        return False
    

    def read_file_name(self, file):
        matches = re.findall(self.file_type, file)
        return len(matches) > 0

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
