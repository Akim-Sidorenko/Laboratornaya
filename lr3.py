# Лабоораторная работа №3
import random
def get_random_values (d):
    return[d[key] for key in random.sample(d.keys(), len(d))]
my_dict = {'a':1,'b':2,'c':3}
random_values_list = get_random_values(my_dict)
print(random_values_list)