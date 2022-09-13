def bubble_sort(list):
    swapped = False
    n = len(list)
    for i in range(n):
        for j in range(0, n-1):
            if test_num(list[j],list[j+1]):
                list = swap_item(list, j,j+1)
                #print(list)
                swapped = True
        if not swapped:
            return

def test_num(a,b):
    if a > b:
        return True
    else:
        return False

def swap_item(list,pos1,pos2):
    #print(f"Swapped {list[pos1]} at {pos1}, {list[pos2]} at {pos2}")
    list[pos1], list[pos2] = list[pos2],list[pos1]
    return list

new_list = [3,7,2,8,0,4,1,6,9,5]

bubble_sort(new_list)
print(new_list)
