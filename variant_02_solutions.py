"""
Лабораторна робота: Варіант 2
Студент: [Осін Ростислав]
Група: [EIP-30]
"""
from math import log, exp

def fun(x):
    return log(x) - 1/(1+x**2)

def solve_iteration(fun, a, b, e):
    #fun Функція яку перевіряємо
    # a and b межі
    #e проміжок похибки
    x_current = (a + b) / 2
    while True:
        x_next = (a + b) / 2
        if abs(x_next - x_current) < e:
            return x_next
        if fun(x_next) * fun(a) < 0:
            b = x_next
        else:
            a = x_next
        x_current = x_next

def main():
    a = float(input("Введіть нижню межу(1)"))
    b = float(input("Введіть верхню межу(2)"))#пишемо межі
    e = float(input("Введіть епсілу(0,00005)"))#Записуємо епсілу
    print("Розв'язок рівняння log(x) - 1/(1+x^2) = 0 на проміжку [{}, {}] з точністю {}: {:.5f}".format(a, b, e, solve_iteration(fun, a, b, e)))


if __name__ == "__main__":
    main()
