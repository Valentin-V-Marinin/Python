def write_data(data: str):
    with open('phone_book.csv', 'a') as f:
        f.writelines(data + '\n')


def read_data(all_contacts: bool, data=""):
    phone_books = []
    with open('phone_book.csv', 'r') as f:
        if all_contacts:
            [phone_books.append(i) for i in f]
        else:
            [phone_books.append(i) for i in f if data in i]
    return phone_books


def delete_data(data: list):
    replacement = str(data).replace('status1\\n', 'status0')[2:-2]
    with open('phone_book.csv', 'r') as f:
        lines = f.readlines()
    with open('phone_book.csv', 'w') as f:
        f.truncate(0)
        for line in lines:
            line = line.strip()
            if line in str(data):
                f.write(replacement + '\n')
            else:
                f.write(line + '\n')  
