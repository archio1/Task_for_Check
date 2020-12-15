#3)	Реалізувати декоратор. Виміряти час роботи функцій з першого завдання. Спрбувати реалізувати анонімну функцію.
#Стоверення бібіліотек if _main_
#Нагерувати масив набагато більше. Відображення до тисячної.
import time
import random
from Functions_for_fifth_task import bubble_sort
from Functions_for_fifth_task import partition
from Functions_for_fifth_task import quick_sort


def benchmark(func):

    def wrapper(*args, **kwargs):
        start = time.time_ns()
        return_value = func(*args, **kwargs)
        end = time.time_ns()
        #moretime = time.time_ns()
        print('Time of work: {} seconds.', format(end-start))
        return return_value
    return wrapper

def random_array(number, first_value = 0, last_value = 100):
    temp_array = []
    for i in range(number):
        temp_array.append(random.randint(first_value, last_value))
    return temp_array

another_array = random_array(100)

#start_array = random.randint()
#print(start_array)
#@benchmark
#def checking_all():
#    lambda bubble_sort, quick_sort: bubble_sort(start_array), quick_sort(start_array)
#checking_all = lambda bubble_sort, quick_sort: bubble_sort(start_array), quick_sort(start_array)
#@checking_all(lambda bubble_sort, quick_sort: bubble_sort(start_array), quick_sort(start_array))
print(another_array)
@benchmark
def checking_bubble_sort():
    bubble_sort(another_array)
@benchmark
def checking_quick_sort():
    partition(another_array, 20, 80)
    quick_sort(another_array)

checking_bubble_sort()
checking_quick_sort()


#checking_all()

