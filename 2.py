n = int(input())
tf = False
for i in range(n):  #  Цикл будет повторяться то число раз, какое ввел пользователь
    num = int(input())  # Ввод числа для проверки
    if num == 0:  #  Если число оказалось нулём, присваиваем переменной true и выходим
        tf = True
        break
if tf:  # Если в введенных числах есть 0, то выводим да, если нет, то выводим нет
    print('YES')
else:
    print('NO')

