import random
from string import ascii_lowercase
my_universal_list = ['qwearty','asadfg','zxcvab','uiop','hjkl','nmqwae','a12345','aaaaa','bcdfg']
# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
def reverse_strings_on_even_indexes(my_list):
    my_new_list = []
    for index, element in enumerate(my_list):
        my_new_list.append(element[::-1]) if (index % 2) == 1 else my_new_list.append(element)
    return my_new_list
print("1:", reverse_strings_on_even_indexes(my_universal_list))
# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".
def finding_elements_with_first_letter_a(my_list):
    my_new_list = [element for element in my_list if element[0] == "a"]
    return my_new_list
print("2:", finding_elements_with_first_letter_a(my_universal_list))
# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.
def return_strings_with_letter_a_anywhere(my_list):
    my_new_list = [element for element in my_list if "a" in element]
    return my_new_list
print("3:", return_strings_with_letter_a_anywhere(my_universal_list))
# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.
def return_only_str(my_list):
    my_new_list = [element for element in my_list if type(element) == str]
    return my_new_list
my_list_for_task_4 = ['safdasf', '2134324', 'sadfdsa', 213, 'asdfsad', 1, 2, 3, "qwerty"]
print("4:", return_only_str(my_list_for_task_4))
# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.
def return_unique_symbols_from_string(my_str):
    my_new_list = [element for element in my_str if my_str.count(element) == 1]
    return my_new_list
my_string = "qqqqweeeeeertttttyuiiiiii1112"
print("5:", return_unique_symbols_from_string(my_string))
# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
def return_list_with_elements_in_both_lists(my_string_1, my_string_2):
    my_new_list = [element for element in set(my_string_1).intersection(set(my_string_2))]
    return my_new_list
print("6:", return_list_with_elements_in_both_lists("qwewretwetewtwecbnrt", "dsfafasdfasdfqwewwrtqery"))
# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
def return_intersection_of_unique_elements(my_string_1, my_string_2):
    my_new_list = [element for element in set(my_string_1).intersection(set(my_string_2)) if my_string_1.count(element) == 1 and my_string_2.count(element) == 1]
    return my_new_list
print("7:", return_intersection_of_unique_elements("12234566789", "111123333334555567889"))
# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.

# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com
names = ["abrams","atkins","king","smith","wood","walker"]
domains = ["net", "com", "ua"]
def create_email(domains, names):
    first_part_of_e_mail = random.choice(names) + "." + str(random.randint(100, 999))
    second_part_of_e_mail = "@" + ''.join(random.choice(ascii_lowercase) for element in range(random.choice([5,6,7]))) + "." + random.choice(domains)
    e_mail = first_part_of_e_mail + second_part_of_e_mail
    return e_mail
e_mail = create_email(domains,names)
print("7:", e_mail)