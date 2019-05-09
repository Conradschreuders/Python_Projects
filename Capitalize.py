import os
import time

class MakeCapital():
    default_path = 'H:\My Documents\Programming\scripts\\'

    def __init__(self) -> None:
        path = self.default_path
        result_path = self.create_result_directory(path)
        self.run_directory(path, result_path)

    def __repr__(self) -> str:
        return "make capital"

    @staticmethod
    def create_result_directory(path):
        result_path = path + 'result\\'

        if not os.path.exists(result_path):
            os.makedirs(result_path)
        return result_path

    def run_directory(self, path, result_path):
        for file in os.listdir(path):
            if file.endswith(".txt"):
                self.capitalize_file(path, result_path, file)

    @staticmethod
    def capitalize_file(path, result_path, file) -> None:
        read_file = open(path+file, 'r')
        write_file = open(result_path + 'result_' + file,'w')

        for line in read_file:
            write_file.write(line.upper())

        print("File created: 'result_" + file + "'")
        read_file.close()
        write_file.close()

    def change_file_path(self) -> None:
        new_path = input("Change file path? Default: " + self.path + " ")
        if new_path == "Y":
            self.path = input("Give new file path: ")


if __name__ == '__main__':
    print("running in main")
else:
    MakeCapital()
