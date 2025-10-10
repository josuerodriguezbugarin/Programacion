#boletin 5, 1

for i in range(10, 21):
    print(i)

#boletin 5, 2

F = float(input("Dime una medida para pasarla a grados celsius"))

C = (F - 32) * 5/9

print(C)

#boletin 5, 3

F = float(input("Dime una medida para pasarla a grados celsius"))

for F in range(0, 121, 10):

    C = (F - 32) * 5 / 9

print(F, "ºF=", round(C, 2), "ºC")

#boletin 5, 4

try:
    inicio = int(input("Introduce el primer número: "))
    fin = int(input("Introduce el segundo número: "))
except ValueError:
    print("Por favor, introduce números enteros.")
    raise SystemExit

if inicio > fin:
    inicio, fin = fin, inicio

start = inicio if inicio % 2 == 0 else inicio + 1

for n in range(start, fin + 1, 2):
    print(n)

#boletin 5, 5

b = int(input("Dime un numero para escribir los primeros numeros triangulares"))

for m in range(1, b + 1):
    triangular = m * (m + 1) // 2
    print(m, "-", triangular)
#boletin 5, 6

m = int(input("¿Cuántos valores quieres ingresar? "))

for i in range(1, m + 1):
    num = int(input(f"Introduce el valor #{i}: "))


    factorial = 1
    for j in range(1, num + 1):
        factorial *= j

    print(f"{i} - {num}! = {factorial}")

#boletin 5, 7
input("Fichas de dominó")
for a in range(7):
    for b in range(a, 7):
        print(a, "-", b)

#boletin 5, 8
n = int(input("di un numero para generar fichas"))
for a in range(n):
    for b in range(0 , n):
        print(a, "-", b)

#boletin 5, 9

positivos = 0
negativos = 0
ceros = 0

for i in range(10):
    n = int(input("Introduce un número entero: "))
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
    else:
        ceros += 1

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Ceros:", ceros)

#boletin 5, 10
n = int(input("Introduce la base del rectangulo: "))
m = int(input("Introduce la altura del rectangulo: "))

area = n * m

print("el area del rectangulo es:", area)

#boletin 5, 11

while True:
    numero = int(input("Introduce un número (0 para saír): "))
    if numero == 0:
        break
    print(f"Táboa de multiplicar do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


#boletin 5, 13

while True:
   entrada = input("Introduce 10 números separados por espacios: ").split()
   if len(entrada) == 10:
       try:
           numeros = list(map(int, entrada))
           if 999 in numeros:
               print("No puedes añadir el número 999. Intenta de nuevo.")
               continue
           total = sum(numeros)
           print(f"El valor total es: {total}")
           break
       except ValueError:
           print("Todos los valores deben ser números.")
   else:
       print("Introduce exactamente 10 números.")