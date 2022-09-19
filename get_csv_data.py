class CsvReader:
    def get_csv_data(self, path):
        print("读取csv文件: ")
        file = open(path)
        # next(file)
        line = file.readline()
        data = []
        print(line, end="")
        line = file.readline()
        while line:
            print(line,end="")
            data.append(line.split(","))
            line = file.readline()
        return data

    def get_yml_data(self, path):
        pass
