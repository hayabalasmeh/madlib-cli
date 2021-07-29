
def binarysearch(sortedarray, value):
    startpoint = 0
    endpoint = len(sortedarray)

    def analysis(startpoint=0, endpoint=len(sortedarray)):

        middle_index = (startpoint + endpoint)//2
        if sortedarray[middle_index] == value:
            return middle_index
        elif sortedarray[middle_index] < value:
            return analysis(sortedarray, value, middle_index+1, endpoint)
        elif sortedarray[middle_index] > value:
            return analysis(sortedarray, value, middle_index-1, startpoint)
        else:
            return -1
    return analysis()


print(binarysearch([-131, -82, 0, 27, 42, 68, 179], 42))


test = 5//2
print(5//2)
