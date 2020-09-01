data =  [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 28
i = 0

def linear_search(data, target):
    print("Looking for {} in list {}".format(target,data))
    for i in range(len(data)):
        if data[i] == target:
            print("found on try number {}".format(i+1))
            print("{} is  the target ({})".format(data[i], target))
            return True
        print("try number {}".format(i+1))
        print("{} is not target ({})".format(data[i], target))
    return False
    print("not found")


linear_search(data, target)
