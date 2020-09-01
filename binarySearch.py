data =  [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 8

# Iterative Binary Search
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        print("the mid element is {}".format(data[mid]))
        if target == data[mid]:
            print("found the target")
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
             low = mid + 1
    print("didn't found the element")
    return False

print(binary_search_iterative(data, target))
