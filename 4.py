pn = int(input())
i = d =  m = 1  # Присваиваем счетчики и максимум
while pn != 0:
    n = int(input())
    if n == 0:  # Если введенное число равно нулю, то останавливаем цикл
        break
    if n > pn:  # Если введенное число больше предыдущего, то прибавляем счетчик увеличения и сбрасываем счетчик убывания
        i += 1
        if i > m:  # И если счетчик больше максимума, то присваиваем
            m = i
        d = 1
    elif n < pn:  # Так же, как с первым, только наоборот
        d += 1
        if d > m:
            m = d
        i = 1
    else:  # В остальных же случаях сбрасываем счетчики
        d = i = 1
    pn = n  # Ставим текущее число на предыдущее место
print(m)
