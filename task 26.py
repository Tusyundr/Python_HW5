#Задача 26: Напишите программу, которая на вход принимает два числа A и B,
#и возводит число А в целую степень B с помощью рекурсии.
#Пример:
#A = 3; B = 5 -> 243 
#A = 2; B = 3 -> 8

def f(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * f(a, b - 1))
a = int(input("Введите число A: "))
b = int(input("Введите его степень B: "))
print("Результат:", f(a, b))

#еще один вариант:

# def f(a, b):
#      def k(b):
#           if b % 2 == 0:
#                return True
#           return False
#      if b == 0:
#           return 1
#      if k(b):
#           x = f(a, b / 2)
#           return x * x
#      return a * f(a, b - 1)
# a = int(input('Введите A:'))
# b = int(input('Введите B:'))
# print(f'Результат: {f(a, b)}')
