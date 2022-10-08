# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления 
# данных.Входные и выходные данные хранятся в отдельных текстовых файлах.

from random import randint, randrange
from secrets import choice


def text_file_ctreation():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    with open(input('File name: '),'a') as f:
        for i in range(randint(2,10)):
            line_length_counter = 0
            new_line = ""
            while line_length_counter < 70:
                new_line+= choice(alphabet)*randrange(1,11)
                line_length_counter+= len(new_line)
            f.write(new_line + "\n")
         

def file_encoding():
    try:
        read_file = open(input('File name: '),'r')
        write_file = open("enc_" + read_file.name,'a')

        for data in read_file:    
            encoding_row = ""; counter = 0
            for i in range(1,len(data)):
                if data[i-1] != data[i]:
                    encoding_row+= str(i-counter) + data[i-1]
                    counter+=  i - counter
            write_file.write(encoding_row + "\n") 
    finally:    
        read_file.close
        write_file.close
    
    
def file_decoding():
    try:
        read_file = open(input('File name: '),'r')
        write_file = open("dec_" + read_file.name,'a')

        for data in read_file:    
            data = data[:-1]
            decoding_row = ""; counter = 0
            for i in range(len(data)):
                if not data[i].isdigit():
                    decoding_row+= int(data[counter:i]) * data[i]
                    counter = i+1
            write_file.write(decoding_row + "\n") 
    finally:    
        read_file.close
        write_file.close
    

text_file_ctreation() # v.txt
file_encoding()       # v.txt
file_decoding()       # enc_v.txt