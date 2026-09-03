# min and max of a list



def find_max_and_min(lst):
    max_val = lst[0]
    min_val = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
        elif lst[i] < min_val:
            min_val = lst[i]
    print(f"Max is : {max_val}")
    print(f"Min is : {min_val}")


notes = [12, 18, 7, 15, 9, 20, 3, 14,12,12]



# filter

def filter_selon_une_seuil(list,seuil):
    for i in range(len(list)):
        if list[i] >= int(seuil):
            print(list[i])




# concurence count without counter

def count_concurence_of_an_element(lis,element):
    count = 0
    for i in range(len(lis)):
        if lis[i] == element:
            count += 1

    print(f"{element} appeared {count} times in this list ")


# reverse a list without reverse method

def reverse_a_list(items):
    reversed_items = []
    for i in range(1, len(items) + 1):
        reversed_items.append(items[-i])
    print(reversed_items)

liste1 = [1, 4, 7]
liste2 = [2, 3, 8, 9]

def fuse_two_lists_then_sort(list1,list2):
    fused_list = list1 + list2
    print(sorted(fused_list))



# Python list Comprehention

def square_of_even_numbers(numbers):
    return [item**2 for item in numbers if item % 2 == 0]

numbers = [3, 12, 7, 25, 8, 19, 2]

print(square_of_even_numbers(numbers))

