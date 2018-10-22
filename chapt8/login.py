first = input('Enter first name > ')
last = input('Enter last name  > ')
id_num = input('Enter ID number  > ')


def generate_login(name1, name2, id_cred):
    set1 = name1[:3]
    set2 = name2[:3]
    set3 = id_cred[-3:]

    return set1 + set2 + set3


print(generate_login(first, last, id_num))
