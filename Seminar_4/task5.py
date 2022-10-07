# Даны два файла, в каждом из которых находится запись многочленов. 
#  Задача - сформировать файл, содержащий сумму многочленов.


def read_file(file_name):
    my_list = []
    with open(file_name, 'r') as f1:
        data = f1.read()
        f1.close

    while data != "":
        position = data.index('\n')
        my_list.append(data[:position])
        data = data[position+1:]
    return my_list

def concat_equations():
    list1 = read_file('equation.txt')
    list2 = read_file('equation1.txt')

    if len(list1) == len(list2):
        with open('concatenation.txt','a') as concat:
            for i in range(len(list1)):
                line = list1[i][:len(list1[i])-3] + "+ " +list2[i]
                concat.write(line + "\n")
            concat.close
    else:
        print('The contents of the files do not match!')
        
        
concat_equations()