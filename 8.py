from random import randint
import logging
logging.basicConfig(filename="Логирование_8_задание.log", level=logging.INFO)


def Barrel_Check():  # обработчик ошибки ввода кол-ва бочонков
    while True:
        try:
            Barrel = int(input("Введите кол-во бочонков цифрой: "))
            return Barrel
        except ValueError:
            print("Нужно ввести цифру!")

def i_Check():  # обработчик ошибки ввода числа i
    while True:
        try:
            i = int(input("Введите: "))
            return i
        except ValueError:
            print("Нужно ввести цифру!")



All_Num = [] #массив со всеми "выпавшими" числами
Barrel = Barrel_Check()
logging.info('Пользователь выбрал данное кол-во бочек: ' + str(Barrel))
k = 0
for k in range (1, Barrel+1): #основной цикл
    print("1 - Достать случайное число\n2 - Закончить ")
    i = i_Check() #пользователь решает что сделать
    logging.info('Между 1 (достать случайное число) и 2 (закончить) пользователь выбрал ' + str(i))
    if i == 1:
        num = randint(1, Barrel) #узнаем число
        if num in All_Num: #проверка выпадение этого числа ранее
            while num in All_Num: #цикл, чтобы выбрать другое число
                num = randint(1, Barrel)
        print ("В этот раз выпало число: ", num, "\n")
        logging.info('Пользователю выпало число ' + str(num))
        All_Num.append(num) #записываем число в массив
    if k == Barrel:
        print("Вы достали эти числа: ", All_Num)
    if i == 2: #если пользователь заканчивает программу раньше
        if sum(All_Num) == 0:
            print ("Вы не достали ни одного числа")
        else:
            print ("Вы достали эти числа: ", All_Num)
        break
