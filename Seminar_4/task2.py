# Задайте натуральное число N. Напишите программу, которая 
#  составит список простых множителей числа N.


number = int(input('Введите число: '))

def simple_numbers():
    result = []
    for i in range(2,100):
        count = 2
        while count <= i:
            if not(i%count):
                if (i == count): result.append(i)
                break
            else:
                count+=1 
    return result

def list_simple_numbers(num, mylist : list):
    list_numbers = []
    count = 0
    while num-1:
        if not num % mylist[count]:
            list_numbers.append(mylist[count])
            num//=mylist[count]
        else:
            count+=1
    return list_numbers

smpl_numbs = simple_numbers()
print(smpl_numbs)
print(list_simple_numbers(number, smpl_numbs))

