# ----------------------------------------------- Ejercicio #1 -----------------------------------------------

Num1 = 7
Num2 = 10

print('\n','Num1 = ',Num1,'\n')
print(' Num2 = ',Num2,'\n')

# ----------------------------------------------- Ejercicio #2 -----------------------------------------------
Resultados = []
suma = Num1 + Num2
resta = Num1 - Num2
div = Num1/Num2
mult = Num1*Num2
pot = Num1**Num2

Resultados.append(suma)
Resultados.append(resta)
Resultados.append(div)
Resultados.append(mult)
Resultados.append(pot)

# ----------------------------------------------- Ejercicio #3 -----------------------------------------------

print('El resultado de suma entre ', Num1, 'y ', Num2, ' es: ',Resultados[0],'\n')
print('El resultado de resta entre ', Num1,'y ', Num2, ' es: ', Resultados[1], '\n')
print('El resultado de división entre ', Num1,'y ', Num2, ' es: ', Resultados[2], '\n')
print('El resultado de la multiplicación entre ',Num1, 'y ', Num2, ' es: ', Resultados[3], '\n')
print('El resultado de la potencia entre ', Num1,'y ', Num2, ' es: ', Resultados[4], '\n')


# ----------------------------------------------- Ejercicio #4 -----------------------------------------------
i=0
A = [[1, 4, 5, 12, 55, 77, 70], [5, 87, -5, 8, 9, 0, 1], [-6, 7, 71, 900,87, 11, 19], [-1, 9, 76, 960, 67, 61, 195], [9000, 734, 741, 9400, 847, 411, 419], [-446, 47, 371, 9200, 187, 111, 119], [906, 7000, 711111, 9200, 873, 115, 194]]
newA =[[]]
print('A=')
# imprimir matriz entera mediante ciclo for
for k in A:

    print (k)
'''
for i in range(0,7):
    B = []
    for j in range(0,7):
        x = j+1
        B.append(x)
    A.append(B)
'''

print('A=',str(A))

# ----------------------------------------------- Ejercicio #5 -----------------------------------------------

for i in range(0, 7):
    
    A[i][i] = i+1

print('\nNueva Matriz=')

for k in A:

    print (k)
