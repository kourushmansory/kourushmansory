from random import  *
def login(x):
    """
    Функция для создания догина пользователя
    x - все данные о пользователе
    return - логин вида Фамилия_ИО
    """
    f,i,o = x[1].split()
    ln = f'{f}_{i[0]}{o[0]}'
    return ln

def password():

    A='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a= A.lower()
    c='0123456789'
    p = [choice(A),choice(A),choice(A),choice(a),choice(a),choice(a),choice(c),choice(c)]
    shuffle(p)
    p = ''.join(p)
    return p



a=open('students.csv', encoding='utf8').readlines()
shapka = a.pop(0)
for i in range(len(a)):
    a[i] =a[i].strip().split(',')
    a[i] += [login(a[i]), password()]

f = open('students_password.csv', 'w', encoding='utf8')
f.write(shapka.strip() + ',login,password\n')
for x in a:
    f.write(','.join(x)+'\n')