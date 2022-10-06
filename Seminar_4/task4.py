# Задана натуральная степень k. Сформировать случайным 
#  образом список коэффициентов (от 0 до 10) многочлена, 
#  записать в файл полученный многочлен не менее 3-х раз.

from random import randrange

def sign():
    s = ['-','+']
    return s[randrange(0,2)]    

def line_shaping():
    new_degrees = randrange(0,10)
    coeffs = [randrange(0,9) for i in range(11)]
    line = ""
    if new_degrees:
        for i in range(len(coeffs)):
            if not new_degrees:
                if coeffs[i]: 
                    line+= str(coeffs[i]) +  " = 0"
                elif ('x' in line):  
                    line= line[:len(line)-3] + " = 0"
                else:
                    line = ""
                break
            if coeffs[i]:
                line+= f"{coeffs[i]}*x^{new_degrees} {sign()} "
            new_degrees-=1
    return line    
    

def file_equations():
    try:
        with open('equation.txt','a') as f:
            line = line_shaping()
            if len(line): 
                f.write(line +"\n")
            f.close
    except:
        f.close
 
def number_repitition():
    number = int(input('Сколько уравнений нужно записать в файл: '))
    for i in range(number):
        file_equations()

number_repitition()