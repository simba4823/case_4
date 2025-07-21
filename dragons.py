def max_power(n):
    max_value = 0
    for a in (range(1, n + 1)):  # количество драконов с одной головой
        for b in (range(a, n - a + 1)): # количество драконов с двумя головами
            for c in (range(b, n - b + 1)): # количество драконов с тремя головами
                for d in (range(c, n - c + 1)): # количество драконов с четырьмя головами
                    for e in (range(d, n - d + 1)):   # количество драконов с пятью головами
                        for f in (range(e, n - e + 1)):   # количество драконов с шестью головами
                            if (n - a - b - c - d - e - f) % 7 == 0:  # проверка на возможность дополнить до N
                                max_value = max(max_value, a * b * c * d * e * f * (n - a - b - c - d - e - f))
    return max_value

N = int(input("Введите количество голов в стае: "))
print("Максимально возможное значение силы стаи драконов:", max_power(N))
