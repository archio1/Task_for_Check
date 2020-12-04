#3)	Реалізувати декоратор. Виміряти час роботи функцій з першого завдання. Спрбувати реалізувати анонімну функцію.
#Стоверення бібіліотек if _main_
#Нагерувати масив набагато більше. Відображення до тисячної.


import time
from main import bubble_sort
from main import quick_sort


def benchmark(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        moretime = time.time_ns()
        print('Time of work: {} seconds.', moretime)
        return return_value
    return wrapper

start_array = [[12, 45, 1, 0, 66], [47, 32, 11, 7, 17], [65, 90, 21, 3, 16], [2, -16, 22, 12, 33]]
#print(start_array)
#@benchmark
#def checking_all():
#    lambda bubble_sort, quick_sort: bubble_sort(start_array), quick_sort(start_array)
#checking_all = lambda bubble_sort, quick_sort: bubble_sort(start_array), quick_sort(start_array)
#@checking_all(lambda bubble_sort, quick_sort: bubble_sort(start_array), quick_sort(start_array))

@benchmark
def checking_bubble_sort():
    bubble_sort(start_array)
@benchmark
def checking_quick_sort(): # можно ли одной функцией? start array is must be global??
    quick_sort(start_array)

checking_bubble_sort()
checking_quick_sort()

#checking_all()

