from comparision import comparision
from list_element_exist import list_exist
from dict_value_key_exist import dict_value_key


def assert_that(val):
    return assertionCheck(val)

class assertionCheck(comparision,list_exist,dict_value_key):
    def __init__(self, tested_value):
        super().__init__(tested_value)
   