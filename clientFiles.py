import os
import string
import operator
import datetime
from shutil import copyfile
import re

"""
This program looks into a file system and tries to find a file with a certain
value.
"""

class findClientFile():
    #default_path = r'\\sb2210009332.ad.ing.net\FACTORLINK\Import\Clients\Handled'
    result_path = r'H:\My Documents\Programming\clientfiles\\'
    max_time = 0
    regex = ''
    file_format = True
    file_found = False

    def __init__(self, sequence = '40', total_days = 100,
                 file_format = True, source = 'DEV') -> None:
        self.max_time = total_days
        self.path = self.find_source_directory(self.find_start_path(source))
        #self.changeFilePath()
        self.result_path = self.create_result_directory(self.result_path)
        self.regex = sequence
        self.file_format = file_format
        self.main(self.path)

    def __repr__(self) -> str:
        return self.file

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
        return r'\\'+source+'.ad.ing.net\FACTORLINK\Import\Clients\Handled'
        
    @staticmethod
    def create_result_directory(path):
        result_path = path

        if not os.path.exists(result_path):
            os.makedirs(result_path)
        return result_path

    def main(self, path) -> None:
        num_days = 0
        file_found = False
        while not(file_found) and num_days <self.max_time:
            file_path = self.find_directory(path, num_days)
            if self.check_directory(file_path):
                file_found = self.run_directory(file_path)
            num_days+= 1
            print(file_path + ' number of days back: ' + str(num_days))

        if file_found:
            print('file is found!')
            print(self.regex)
        else:
            print('no file is found :( ')

    def find_directory(self, path, num_days) -> os.path:
        new_date = str(datetime.date.today() - datetime.timedelta(days=num_days))
        return(path + '\\' + new_date + '\\')

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
            
    
    def changeFilePath(self) -> None:
        new_path = input("Change file path? Default: " + self.path + " ")
        if new_path == "Y":
            self.path = input("Give new file path: ")
            

if __name__ == '__main__':
    print("Program started from main")
    f = findClientFile()
else:
    print("Program started from outside")
    pass
