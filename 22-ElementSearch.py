'''
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) 
and another number. 
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.


Extras: Binary Search
'''

lst = [3,1,9,6,5,4]
newlst = sorted(lst)
print(newlst)
print(len(lst))
num = 0

def search_element(list1, number):
    if number in lst:
        return True
    return False




def binarySearcher(lista,value):
    value=int(value)
    if len(lista)>1:
        a=int(len(lista)/2)
        if value < int(lista[a]):
            return binarySearcher(lista[0:a], value)
        else:
            return binarySearcher(lista[a:len(lista)], value)
    else:
        if value==int(lista[0]):
            return True
        else:
            return False

if __name__=="__main__":
    orderedList=list(input("Please enter ordered list of numbers: \r\n").split())
    print(orderedList)
    numberToCheck=input("Please enter number to check existance in list: \r\n")
    existance=binarySearcher(orderedList,numberToCheck)
    print(existance)

    
    

