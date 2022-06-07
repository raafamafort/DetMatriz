# V
matriz = []
# IN
for c in range(1, 4):
    matriz.append(int(input(f'Digite a matriz [1][{c}]: ')))
for c in range(1, 4):
    matriz.append(int(input(f'Digite a matriz [2][{c}]: ')))
for c in range(1, 4):
    matriz.append(int(input(f'Digite a matriz [3][{c}]: ')))
# OUTPUT
print(11 * '=')
print(f'[{matriz[0]}][{matriz[1]}][{matriz[2]}]\n'
      f'[{matriz[3]}][{matriz[4]}][{matriz[5]}]\n'
      f'[{matriz[6]}][{matriz[7]}][{matriz[8]}]')
print(11 * '=')
# DETERMINANTE CALCULO
det1 = matriz[0] * matriz[4] * matriz[8] + matriz[1] * matriz[5] * matriz[6] + matriz[2] * matriz[3] * matriz[7]
det2 = matriz[2] * matriz[4] * matriz[6] + matriz[0] * matriz[5] * matriz[7] + matriz[1] * matriz[3] * matriz[8]
det = det1 - det2
# OUTPUT RESULADO
print(f'A Determinante da sua Matriz é: {det}')
