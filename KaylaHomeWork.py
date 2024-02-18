import  random

def my_count(x, lst):
    #
    return 

def occurs_more(x, y, lst=[]):
    """
    This function determines whether the element x occurs more times in a list than the element y.
    Parameters:
        x (any): the first input object
        y (any): the second input object
        lst (list): the list to search in
    Returns:
        bool: True if x occurs more times in the list than y, False otherwise
    """
    if not lst:
        return True
    else:
        num_x = lst.count(x)
        num_y = lst.count(y)
        if num_x > num_y:
            return True
        else:
            return False

    

def equal_remove(x, y, lst):
    """
    This function removes x or y element from a list until x and y are equal.
    Input Parameters:
        x (any): the first input object
        y (any): the second input object
        lst (list): the list to search in
    Returns:
        list: a new list with equal amount of x or y element
    """
    
    """ If the number of occurrences of x is not equal to the number of occurrences of y, 
        the code determines how many elements of x and y need to be removed from the list to make them equal. 
        It append the element that doesn't need to be removed to the new list
    """
    num_x = lst.count(x)
    num_y = lst.count(y)
    if num_x == num_y:
        return lst

    elif num_x > num_y:
        num_remove_x = num_x - num_y
        num_remove_y = 0
    else:
        num_remove_x = 0
        num_remove_y = num_y - num_x

    new_list = []
    pos = 0
    for i in lst:
        if i == x:
            if num_remove_x==0:
                #new_list.append(i)
                new_list[pos] = i
                pos = pos + 1
            else:
                num_remove_x = num_remove_x - 1
        elif i == y:
            if num_remove_y==0:
                #new_list.append(i)
                new_list[pos] = i
                pos = pos + 1
            else:
                num_remove_y = num_remove_y - 1
        else:
            #new_list.append(i)
            new_list[pos] = i
            pos = pos + 1
        
    print("number of element in my new list:", pos)    
    return new_list    

print(occurs_more(4,3,[]))


test_list = []
for i in range(20):
    test_list.append(random.randint(1,4))

print(test_list, test_list.count(2), test_list.count(3))
print(occurs_more(2,3,test_list))
eq_list23 = equal_remove(2,3,test_list)
print(test_list, eq_list23, eq_list23.count(2), eq_list23.count(3))

print(test_list, test_list.count(4), test_list.count(3))
print(occurs_more(4,3,test_list))
eq_list43 = equal_remove(4,3,test_list)
print(test_list, eq_list43, eq_list43.count(4), eq_list43.count(3))

print(test_list, test_list.count(1), test_list.count(3))
print(occurs_more(1,3,test_list))
eq_list13 = equal_remove(1,3,test_list)
print(test_list, eq_list13, eq_list13.count(1), eq_list13.count(3))

print(test_list, occurs_more(2,3,equal_remove(2,3,test_list)))



