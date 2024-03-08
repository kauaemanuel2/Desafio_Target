sequencia_a = [1, 3, 5, 7]
prox_elemento_a = sequencia_a[-1] + 2
print(f"a) Próximo elemento: {prox_elemento_a}")

sequencia_b = [2, 4, 8, 16, 32, 64]
prox_elemento_b = sequencia_b[-1] * 2
print(f"b) Próximo elemento: {prox_elemento_b}")

sequencia_c = [0, 1, 4, 9, 16, 25, 36]
prox_elemento_c = (len(sequencia_c)) ** 2
print(f"c) Próximo elemento: {prox_elemento_c}")

sequencia_d = [4, 16, 36, 64]
prox_elemento_d = (len(sequencia_d) + 1) ** 2
print(f"d) Próximo elemento: {prox_elemento_d}")

sequencia_e = [1, 1, 2, 3, 5, 8]
prox_elemento_e = sequencia_e[-1] + sequencia_e[-2]
print(f"e) Próximo elemento: {prox_elemento_e}")

sequencia_f = [2, 10, 12, 16, 17, 18, 19]
prox_elemento_f = sequencia_f[-1] + 2
print(f"f) Próximo elemento: {prox_elemento_f}")
