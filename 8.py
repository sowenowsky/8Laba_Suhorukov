from random import randint
import logging

logger_obj = logging.getLogger(__name__)

w_handler = logging.StreamHandler()
e_handler = logging.FileHandler('8LabaLog.log')
w_handler.setLevel(logging.WARNING)
e_handler.setLevel(logging.ERROR)

c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
w_handler.setFormatter(c_format)
e_handler.setFormatter(f_format)

logger_obj.addHandler(w_handler)
logger_obj.addHandler(e_handler)


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
k = 0
for k in range (1, Barrel+1): #основной цикл
    print("1 - Достать случайное число\n2 - Закончить ")
    i = i_Check() #пользователь решает что сделать
    if i == 1:
        num = randint(1, Barrel) #узнаем число
        if num in All_Num: #проверка выпадение этого числа ранее
            while num in All_Num: #цикл, чтобы выбрать другое число
                num = randint(1, Barrel)
        print ("В этот раз выпало число: ", num, "\n")
        All_Num.append(num) #записываем число в массив
    if k == Barrel:
        print("Вы достали эти числа: ", All_Num)
    if i == 2: #если пользователь заканчивает программу раньше
        if sum(All_Num) == 0:
            print ("Вы не достали ни одного числа")
        else:
            print ("Вы достали эти числа: ", All_Num)
        break