

class list_exist():
    def __init__(self, tested_value):
        self.tested_value = tested_value

        

    def isInListOrNistedListed(self, value):
        if self.tested_value in value:
            return self
    
        for l in value:
            if isinstance(l,list):
                if self.tested_value in l:
                    return self
        print("{} is not a value in list {}".format(self.tested_value,value))
        return self
