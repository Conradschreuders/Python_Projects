import os
import string
import operator


class Histofile():
    default_path = 'H:\My Documents\Programming\joblog\\'
    histogram = {}

    def __init__(self) -> None:
        self.path = self.default_path
        #self.changeFilePath()
        self.result_path = self.create_result_directory(self.path)
        self.run_directory(self.path, self.result_path)

    def __repr__(self) -> str:
        return self.file

    @staticmethod
    def create_result_directory(path):
        result_path = path + 'result\\'

        if not os.path.exists(result_path):
            os.makedirs(result_path)
        return result_path

    def main(self, path):
        self.run_directory(path)

    def run_directory(self, path, result_path):
        for file in os.listdir(path):
            if file.endswith(".txt"):
                self.create_histogram(path, result_path, file)

    def create_histogram(self, path, result_path, file) -> None:
        read_file = open(path + file, 'r')
        for line in read_file:
            new_line = line.split()
            self.handle_line(new_line)

        self.write_ordered_file(result_path, file, self.order_histogram(self.histogram))
        read_file.close()
        print("file created: " + 'result_'+file)


    def handle_line(self, line) -> None:
        for word in line:
            new_word = word.strip(string.punctuation).lower()

            if new_word in self.histogram:
                self.histogram[new_word] += 1
            else:
                self.histogram[new_word] = 1
            
    @staticmethod
    def order_histogram(histogram) -> dict:
        sorted_list = sorted(histogram.items(), key=operator.itemgetter(1), reverse = True)
        return sorted_list

    @staticmethod
    def write_ordered_file(path, file, sorted_hist) -> None:
        write_file = open(path+'result_'+ file,'w')

        for item in sorted_hist:
            write_file.write(str(item)+"\n" )
        write_file.close()

    def changeFilePath(self) -> None:
        new_path = input("Change file path? Default: " + self.path + " ")
        if new_path == "Y":
            self.path = input("Give new file path: ")
            

if __name__ == '__main__':
    print("Program started from main")
else:
    h = Histofile()
