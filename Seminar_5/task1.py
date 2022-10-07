# Напишите программу, удаляющую из текста все слова, содержащие "абв". 
#  В тексте используется разделитель пробел

import random

number = int(input('Number of words: '))
 
def list_generator(num : int, row: str):
    if num > 0:
        line = ""
        while num:
            result = random.sample(row, k=3)
            line += result[0] + result[1] + result[2] + " "
            num-=1
        return line
    else:
        return "The data is incorrect"

def replacement(line, target: str):
    result = line.replace(target, '')    
    return result

ln = list_generator(number, 'абв')
print(ln)
print(replacement(ln, 'абв '))


