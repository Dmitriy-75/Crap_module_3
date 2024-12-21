#1.Функция с параметрами по умолчанию:

def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# print_params(b=25)
# print_params(c=[1, 2, 3]

# Результат

# Traceback (most recent call last):
#   File "C:\Users\kolya\PycharmProjects\Module3\module_3_3.py", line 7, in <module>
#     print_params(b=25)
# TypeError: print_params() missing 2 required positional arguments: 'a' and 'c'
#
# Process finished with exit code 1

#2.Распаковка параметров:

values_list = [16, False, "fortune"]
values_dict = {"a": 56, "b": "gambler", "c": False}
print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры:

values_list_2 = [100,"Forever young"]
print_params(*values_list_2,"i wont to be forever young")

