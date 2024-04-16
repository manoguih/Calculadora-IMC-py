def calcular_altura_m(altura_cm):
    altura_m = altura_cm / 100
    return altura_m

def calcular_imc(altura_m, peso):
    imc = peso / (altura_m ** 2)
    return imc

def pesoideal_imc(idade, imc):
    if 60 <= idade:
        if 22 > imc:
            return "Você esta abaixo do peso ideal"
        elif 22 <= imc < 27:
            return "Você esta com o peso ideal"
        else:
            return "Você está com sobrepeso"
    else :
        if 17 > imc:
            return "Você esta muito abaixo do peso ideal"
        elif 17 <= imc < 18.5:
            return "Você esta abaixo do peso ideal"
        elif 18.5 <= imc < 25:
            return "Você esta com o peso ideal"
        elif 25 <= imc < 30:
            return "Você está com sobrepeso"
        elif 30 <= imc < 35:
            return "Você está com obesidade grau 1"
        elif 35 <= imc < 40:
            return "Você está com obesidade grau 2"
        else :
            return "Você esta com obesidade mórbida"
        
def peso_minimo_adulto(altura_m):
    return 18.5 * (altura_m ** 2)

def peso_maximo_adulto(altura_m):
    return 25 * (altura_m ** 2)

def peso_minimo_idoso(altura_m):
    return 22 * (altura_m ** 2)

def peso_maximo_idoso(altura_m):
    return 27 * (altura_m ** 2) 

altura_cm = float(input("Digite sua altura em centimetros: "))
peso = float(input("Digite seu peso: "))
idade = int(input("Digite sua idade: "))

altura_m = calcular_altura_m(altura_cm)

imc = calcular_imc(altura_m, peso)
imc_formatado = "%.2f" % imc

if 18 > idade :
    print("Essa calculadora de IMC não é indicada para crianças e adolescentes, procure um especialista")
elif 60 <= idade :
    print("Seu IMC é:", imc_formatado)
    print(pesoideal_imc(idade, imc))
    print(f"seu peso ideal está entre{peso_minimo_idoso(altura_m): .2f}kg e{peso_maximo_idoso(altura_m): .2f}kg")
else:
    print("Seu IMC é:", imc_formatado)
    print(pesoideal_imc(idade, imc))
    print(f"seu peso ideal está entre{peso_minimo_adulto(altura_m): .2f}kg e{peso_maximo_adulto(altura_m): .2f}kg")