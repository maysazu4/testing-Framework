

class dict_value_key():
    def __init__(self, tested_value):
        self.tested_value = tested_value


    def isAKeyInDictionary(self, value):
        for k,v in value.items():
            if self.tested_value == k:
                return self
            if isinstance(v,dict):
                for key,va in v.items():
                    if self.tested_value == key:
                        return self
        print("{} is not a key in dictionary {}".format(self.tested_value,value))
        return self

    def isAValueInDictionary(self, value):
        for k,v in value.items():
            if self.tested_value == v:
                return self
            if isinstance(v,dict):
                for key,va in v.items():
                    if self.tested_value == va:
                        return self
        print("{} is not a value in dictionary {}".format(self.tested_value,value))
        return self

    