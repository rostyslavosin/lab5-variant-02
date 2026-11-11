"""
Лабораторна робота: Варіант 2
Студент: [Осін Ростислав]
Група: [EIP-30]
"""
from math import log, exp

def fun(x):
    return log(x) - 1/(1+x**2)

def fun_derivative(x):
    return 1/x + 2*x/(1+x**2)**2
    
def phi(x):
    return exp(1/(1+x**2))

def solve_iteration(fun, a, b, e):
    #fun Функція яку перевіряємо
    # a and b межі
    #e проміжок похибки

    x_current = (a + b) / 2   #Точка відліку
    x_next = phi(x_current)   #Наступна точка
    if fun(a) * fun(b) <= 0:
        while abs(x_next - x_current) >= e:
            x_current = x_next
            x_next = phi(x_current)
        return x_next



def main():
    a = float(input("Введіть нижню межу(1)"))
    b = float(input("Введіть верхню межу(2)"))#пишемо межі
    e = float(input("Введіть епсілу(0,00005)"))#Записуємо епсілу
    print("Розв'язок рівняння log(x) - 1/(1+x^2) = 0 методом ітерацій: ", solve_iteration(fun, a, b, e))#Виводимо розв'язок


if __name__ == "__main__":
    main()
