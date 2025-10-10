#Ejercicio 1
nome = input("Introduce o nome do artigo: ")
vendas = int(input("Introduce as vendas anuais: "))


if vendas <= 100:
   tipo = "baixo"
elif vendas <= 500:
   tipo = "medio"
elif vendas <= 1000:
   tipo = "alto"
else:
   tipo = "primeira necesidade"


print(f"Artigo: {nome} — Vendas: {vendas} → Tipo: {tipo}")

#Ejercicio 2
def crearMenu():
   print("De que figura quere calcular a area:")
   print("1. Triangulo")
   print("2. Cuadrado")
   print("3. Circulo")
   print("Elixa opcion:")


   crearMenu()


def calcularAreaTriangulo(base, altura):
   area = base * altura/2
   return area


def calcularAreaRectangulo(base, altura):
    area = calcularAreaTriangulo(base, altura) / 2
    return area


def calcularAreaCirculo(radio):
    return radio * radio * math.pi


def recollerPArametros(opcion):
    if opcion == 1 or opcion == 2:
        base = float(input("Ingresa la base: "))
        altura = float(input("Ingresa la altura: "))
        return base, altura
    elif opcion == 3:
        radio = float(input("Ingresa la radio: "))


def exercicioBoletin_4_2():
    while opcion != 4:
        crearMenu()
        opcion = int(input("Ingresa una opcion: "))
        if opcion > 0 and opcion < 5:
            if opcion == 1 or opcion == 2:
                base, altura = recollerPArametros(opcion)
                if opcion == 1:
                    area = calcularAreaRectangulo(base, altura)
                    print("O area do rectangulo eh: ", area)
                    if opcion == 2:
                        area = calcularAreaTriangulo(base, altura)
                        print("O area do triangulo eh: ", area)
                        elif opcion == 3:
                        radio = calcularAreaCirculo(base)
                    area = calcularAreaRectangulo(base, altura)
                    print("O radio do circulo eh: ", radio)


    else:
        print("opcion non valida")
#Ejercicio 3
numero = float(input("Introduce un número: "))
valor_absoluto = numero if numero >= 0 else -numero
print(f"O valor absoluto de {numero} é {valor_absoluto}")

#Ejercicio 4
num = int(input("Pon un número entre 1 e 99: "))

iniciais = {
    0: "",
    1: "un",
    2: "dous",
    3: "tres",
    4: "catro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "oito",
    9: "nove",
    10: "dez",
    11: "once",
    12: "doce",
    13: "trece",
    14: "catorce",
    15: "quince",
    16: "dezaseis",
    17: "dezasete",
    18: "dezaoito",
    19: "dezanove"
  }

decenas = {
    2: "vinte",
    3: "trinta",
    4: "cuarenta",
    5: "cinconta",
    6: "sesenta",
    7: "setenta",
    8: "oitenta",
    9: "noventa"
  }

if num < 1 or num > 99:
    print("Número incorrecto.")
else:
      if num < 20:
        print(iniciais[num])
      else:
        num = str(num)
        a = int(num[0])
        b = int(num[1])
        if b == 0:
          print(decenas[a],iniciais[b])
        else:
          print(decenas[a],"e",iniciais[b])
#ejercicio 5
dni = int(input("Introduce DNI sen letra: "))

tabla = [
    "T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"
    ]

numletra = dni % 23

letra = tabla[numletra]

print(f"O DNI completo é: {dni}{letra}")

