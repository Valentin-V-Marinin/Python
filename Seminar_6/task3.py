# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, 
#  ключи — первые буквы имён, значения — списки, содержащие имена, 
#  начинающиеся с соответствующей буквы.

from collections import defaultdict

list_names = ['Агата', 'Агнесса', 'Агния', 'Ада', 'Алевтина', 'Архип', 'Аскольд', 'Афанасий', 'Азамат', 
              'Ахмед', 'Акакий', 'Белла', 'Бронислава', 'Богдан', 'Борис', 'Валерия', 'Ванда', 'Варвара', 
              'Василиса', 'Валентин', 'Валерий', 'Варлаам', 'Варлам', 'Галина', 'Жанна', 'Зинаида', 'Зоя', 
              'Захар', 'Зиновий', 'Зосим', 'Завулон', 'Майя', 'Маргарита', 'Марианна', 'Марина', 'Мария', 
              'Марк', 'Матвей', 'Мирон', 'Митрофан', 'Михаил', 'Таисия', 'Тамара', 'Тарас', 'Терентий', 
              'Тимофей', 'Тимур', 'Тихон', 'Яков', 'Ян', 'Ярослав']

def get_dict(l_n: list):
    d = defaultdict(set)
    for i in range(len(l_n)): d[l_n[i][0]].add(l_n[i])
    print(d)
    return d

def get_dict_alter(l_n: list):
    d = {}
    for i in range(len(l_n)): d.setdefault(l_n[i][0],[]).append(l_n[i])
    print(d)
    return d

get_dict(list_names); print()
get_dict_alter(list_names)