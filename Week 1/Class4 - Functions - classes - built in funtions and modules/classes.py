

class Car():
    pass

class Preprocessing():
    pass



class ProcessData():
    def __init__(self, directory):
        self.path = directory

    def count(self):
        return len(self.path)

processData = ProcessData("E:/new folder")
print(processData.path)
print(processData.count())

