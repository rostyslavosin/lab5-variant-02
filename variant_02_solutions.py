"""
Лабораторна робота: Варіант 2
Студент: Осін Ростислав
Група: EIP-30
"""
from math import log, exp
from typing import Callable


def fun(x):                   # Функція яку перевіряємо
    return log(x) - 1/(1+x**2)
    
def phi(x):                  # Функція для ітераційного методу
    return exp(1/(1+x**2))

def phi_derivative(x):      # Похідна функції для ітераційного методу
    return phi(x) * (-2 * x / (1 + x**2) ** 2)

def q_val(d_phi: Callable[[float], float], a: float, b: float) -> float:
    return max(abs(d_phi(a)), abs(d_phi(b)))                # Функція для обчислення q(a, b)

def save_to_file(filename, root, iteration_count, protocol):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Результати обчислень:\n")
        file.write(f"Знайдений корінь: {root}\n")
        file.write(f"Кількість ітерацій: {iteration_count}\n")

        file.write(f"{'Iter':<10} | {'x_n':>10} | {'x_n+1':>10} | {'|x_n+1 - x_n|':>15} | {'f(x_n+1)':>14}\n")
        file.write("-" * 80 + "\n")

        for step, x_n, x_next, diff, f_val in protocol:
            file.write(f"{step:<10} | {x_n:>10.6f} | {x_next:>10.6f} | {diff:>15.4e} | {f_val:>14.4e}\n")


def solve_iteration(
    fun: Callable[[float], float],         
    phi: Callable[[float], float],            
    phi_derivative: Callable[[float], float],  
    a: float,
    b: float,
    e: float,
):
    x_current = (a + b) / 2
    x_next = phi(x_current)
    q = q_val(phi_derivative, a, b)            #Обчислюємо q(a, b)

    iteration_count = 1    #лічильник ітерацій
    protocol = [(iteration_count, x_current, x_next, abs(x_next - x_current), fun(x_next))]
    
    
    if fun(a) * fun(b) <= 0 and q < 1:
        if phi_derivative(x_current) < 0:
            while abs(x_next - x_current) >= e:
                x_current = x_next
                x_next = phi(x_current)
                iteration_count += 1
                protocol.append((iteration_count, x_current, x_next, abs(x_next - x_current), fun(x_next)))
            return x_next, iteration_count, protocol
        elif phi_derivative(x_current) > 0 and phi_derivative(x_current) <= q:
            while abs(x_next - x_current) >= (e*((1-q)/q)):
                x_current = x_next
                x_next = phi(x_current)
                iteration_count += 1
                protocol.append((iteration_count, x_current, x_next, abs(x_next - x_current), fun(x_next)))
            return x_next, iteration_count, protocol
        return None, 0, []


def main():
    a = float(input("Введіть нижню межу(1)"))
    b = float(input("Введіть верхню межу(2)"))#пишемо межі
    e = float(input("Введіть епсілу(0.00005)").replace(",","."))#Записуємо епсілу

    root, iterations, protocol = solve_iteration(fun, phi, phi_derivative, a, b, e)

    if root is not None:
        print(f"Розв'язок рівняння ln(x) - 1/(1+x^2) = 0 методом ітерацій: {root:.6f}")
        print(f"Кількість ітерацій: {iterations}")
        save_to_file("results_variant_02.txt", root, iterations, protocol)
        print("Результати збережено у файл results_variant_02.txt")
    else:
        print("Метод ітерацій не збігається на заданому відрізку.")


if __name__ == "__main__":
    main()
