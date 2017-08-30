import time
import random as rnd


# time O(N^2), memory O(1)
def bubble_sort(mass):
    for j in range(0,len(mass)):
        for i in range(0,len(mass)-j-1):
            if mass[i]>mass[i+1]:
                mass[i],mass[i+1] = mass[i+1],mass[i]


# time O(N^2), memory O(1)
def shake_sort(mass):
    left = 0
    right = len(mass)-1
    cur_index = left
    while left < right:
        while cur_index < right:
            if mass[cur_index] > mass[cur_index+1]:
                mass[cur_index], mass[cur_index+1] = mass[cur_index+1], mass[cur_index]
            cur_index += 1
        right -= 1
        while cur_index>left:
            if mass[cur_index] < mass[cur_index-1]:
                mass[cur_index], mass[cur_index-1] = mass[cur_index-1],mass[cur_index]
            cur_index -= 1
        left += 1


# time O(N^2), memory O(1)
def selective_sort(mass):
    for a in range(0, len(mass)):
        local_min_item = mass[a]
        local_min_item_id = a
        change = False
        for b in range(a+1, len(mass)):
            if mass[b] < local_min_item:
                local_min_item = mass[b]
                local_min_item_id = b
                change = True
        if change:
            mass[local_min_item_id], mass[a] = mass[a],mass[local_min_item_id]


# (exchange sort) time O(NlogN), memory O(n)
def quick_sort(mass, left = 0, right = None):
    if right is None:
        right = len(mass)-1

    comparand = mass[(left+right)/2]
    i = left
    j = right
    while i <= j:
        while mass[i] < comparand and i < right:
            i += 1
        while mass[j] > comparand and j > left:
            j -= 1
        if i <= j:
            mass[i],mass[j] = mass[j],mass[i]
            i += 1
            j -= 1
    if left < j:
        quick_sort(mass, left, j)
    if right > i:
        quick_sort(mass, i, right)


# time O(n^2), memory O(n)
def insert_sort(mass):
    for j in range(1, len(mass)):
        temp=mass[j]
        i = j-1
        while i>=0 and temp<mass[i]:
            mass[i], mass[i+1] = mass[i+1], mass[i]
            i -= 1
        mass[i+1] = temp


# (exchange sort) time O(nlogn), memory O
def shell_sort(mass):
    # numbers can be different
    steps = [9, 5, 3, 2, 1]
    for cur_step in steps:
        for j in range(cur_step, len(mass)):
            temp = mass[j]
            i = j-cur_step
            while i >= 0 and temp < mass[i]:
                mass[i+cur_step] = mass[i]
                i -= cur_step
            mass[i+cur_step] = temp
            j -= 1


# time O(nlogn), memory O(n)
def merge_sort(mass):
    middle = len(mass)/2
    left = mass[0:middle]
    right = mass[middle:]
    if len(left) > 1:
        merge_sort(left)
    if len(right) > 1:
        merge_sort(right)
    left = merge(left, right)
    for i in range(len(left)):
        mass[i] = left[i]


def merge(sorted_mass1, sorted_mass2):
    result = []
    while len(sorted_mass1) > 0 and len(sorted_mass2) > 0:
        min1 = min(sorted_mass1)
        min2 = min(sorted_mass2)
        if min1 < min2:
            result.append(min1)
            sorted_mass1.remove(min1)
        else:
            result.append(min2)
            sorted_mass2.remove(min2)

    # append sorted "tails" if they exist
    if len(sorted_mass1) > 0:
        result += sorted_mass1
    if len(sorted_mass2) > 0:
        result += sorted_mass2

    return result


def generate_random_int_mass(mass_len):
    target = []
    for i in range(mass_len):
        target.append(rnd.randint(0,100))
    return target


def get_mass_copy(input):
    target = []
    for i in input:
        target.append(i)
    return target


def apply_sort(sort,mass):
    mass_to_sort = get_mass_copy(mass)
    print("sort: "+ str(sort.__name__))
    start_time = time.time()
    sort(mass_to_sort)
    print ("time passed: " + str(time.time()-start_time))
    print("result: ")
    print (mass_to_sort)
