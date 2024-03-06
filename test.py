from assertion_class import *
from comparision import *
from dict_value_key_exist import * 
from list_element_exist import *

''' If the assertion is okay, nothing will be printed '''
def comparision_test():
    assert_that(7).bigger(5).smaller(10)
    assert_that(2).smaller(5).equal(2).bigger(1).smaller(5)
    assert_that(3).equal(3).bigger(2).smaller(10)

def list_test():
    assert_that(5).isInListOrNistedListed([3,2]).isInListOrNistedListed([4,5,3]).isInListOrNistedListed([1,[5]])
    assert_that(5).isInListOrNistedListed([3,[5,2]]).equal(5).bigger(3).smaller(10)
    assert_that('banana').isInListOrNistedListed(['strawberry', 'orange', 'kiwi']).isInListOrNistedListed(['strawberry', 'orange', 'kiwi','banana'])
    assert_that(5).isInListOrNistedListed([3,2]).isAKeyInDictionary({1:3 , 2:4 , 3:5})

def dict_test():
    assert_that(5).isAKeyInDictionary({1:3 , 2:4 , 3:5})
    assert_that(5).isAKeyInDictionary({1:3 , 2:4 ,7:{3:5}})
    assert_that(5).isAValueInDictionary({1:3 , 2:4 ,5:2})
    assert_that(5).isAValueInDictionary({1:3 , 2:4 ,3:{5:2}})
    fruits_dict1  = {'strawberry':'yummy', 'orange':'good', 'kiwi':'good' ,'banana':'yummy'}
    fruits_dict2 = {'first':'strawberry', 'second':'orange', 'third':'kiwi' ,'fourth':'banana'}
    assert_that('banana').isAKeyInDictionary(fruits_dict1).isAValueInDictionary(fruits_dict1)
    assert_that('orange').isAValueInDictionary(fruits_dict2).isAKeyInDictionary(fruits_dict1).isAKeyInDictionary(fruits_dict2)
    assert_that('orange').isAValueInDictionary(fruits_dict2).isInListOrNistedListed(['banana' ,['kiwi','orange']])


if __name__ == '__main__':

    comparision_test()
    list_test()
    dict_test()


