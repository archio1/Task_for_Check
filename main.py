start_array = [[12, 45, 1, 0, 66], [47, 32, 11, 7, 17], [65, 90, 21, 3, 16], [2, -16, 22, 12, 33]]

# a = [elem[0] for elem in a]

interim_array = []
final_array = list()
for i in start_array:
    interim_array = interim_array + i

for j in interim_array:
    if j not in final_array:
        final_array.append(j)
result_for_quick_sort = final_array

#  b = list(set(b)), append?

def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)


def binarySearch(nums, item):
    i = 0
    j = len(nums) - 1
    m = int(j / 2)
    while nums[m] != item and i < j:
        if item > nums[m]:
            i = m + 1
        else:
            j = m - 1
        m = int((i + j) / 2)
    if i > j:
        return 'Not found'
    else:
        return m


print('For bubble sort: ', final_array)
print('For quick sort: ', result_for_quick_sort)
bubble_sort(final_array)
print(final_array)

quick_sort(result_for_quick_sort)
print(result_for_quick_sort)


print(binarySearch(final_array, 33))




