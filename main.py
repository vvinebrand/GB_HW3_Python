def f_task():
    g, num, count = int(input('Введите количество элементов: ')), int(input('Введите искомое: ')), 0
    print('Введите целые числа через Enter: ')
    a = [int(input()) for _ in range(g)]
    for j in a:
        if j == num:
            count += 1
    print(f'Количество искомых в массиве: {count} ')


def s_task():
    g, num = int(input('Введите количество элементов: ')), int(input('Введите искомое: '))
    print('Введите целые числа через Enter: ')
    arr, arr_new = [int(input()) for _ in range(g)], []
    for i in arr:
        arr_new.append(abs(num - i))
    b = arr_new.index(min(arr_new))
    print(f'Ближайший элемент к {num} -- {arr[b]}')


def th_task():
    value = {
        1: 'AEIOULNSTRАВЕИНОРСТ', 2: 'DGДКЛМПУ', 3: 'BCMPБГЁЬЯ', 4: 'FHVWYЙЫ', 5: 'KЖЗХЦЧ', 8: 'JXШЭЮ', 10: 'QZФЩЪ'
    }
    w, sm = input('Введите слово: ').upper(), 0
    for i in w:
        for a, b in value.items():
            if i in b:
                sm += a
    print(f"Стоимость слова: {sm}")


stp = True
while stp:
    n = int(input('Введите номер задачи: '))
    if n == 1:
        f_task()
    elif n == 2:
        s_task()
    elif n == 3:
        th_task()
    else:
        print('Программа завершена')
        stp = False
