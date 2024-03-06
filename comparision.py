

class comparision():
    def __init__(self, tested_value):
        self.tested_value = tested_value
    
    def bigger(self,value):
        if not self.tested_value > value:
            print("{} is not bigger than {} !".format(self.tested_value,value))
        return self

    def smaller(self, value):
        if not self.tested_value < value:
            print("The first value is not smaller than the second !".format(self.tested_value,value))
        return self

    def equal(self, value):
        if self.tested_value != value:
            print("{} is not equal to {} !".format(self.tested_value,value))
        return self
