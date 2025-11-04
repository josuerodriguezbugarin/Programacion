temperatura = []
dias = ["Lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
for i in dias:
    decir = int(input("Que temaperaturas hay esta semana"))
    temperatura.append(decir)
#Aqui hago la primera funcion
for a in range(len(dias)):
    print(f"El {dias[a]} hace {temperatura[a]}")
#Aqui hago una modificacion de la primera fucnion
def calculo_temp(dias):
    for i in range(len(dias)):
        if dias[i] > dias[i + 1]:
            return False
    return True
#Aqui le digo que me printee el calculo
print(calculo_temp(dias))
#aqui le digo otra funcion
def calculo_media(dias):
    if dias = 0
    

def calculo_valor(dias):
#Aqui cambio los metodos

def calculoelvalordelavariabe(dias):
    for i in range(len(dias)):
        if dias[i] > dias[i + 1]:
