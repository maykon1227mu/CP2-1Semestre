codigoEstado = int(input("Digite um número entre 1 e 5: "))
pesoCam = float(input("Digite o peso do caminhão em toneladas: "))
codigoCarga = int(input("Digite o número da carga (Entre 10 e 40): "))

pesoCarga = pesoCam * 1000  # converte para kg

if codigoCarga >= 10 and codigoCarga <= 20:
    precoFinal = pesoCarga * 100
    print("Preço por quilo é 100 reais")
elif codigoCarga >= 21 and codigoCarga <= 30:
    precoFinal = pesoCarga * 250
    print("Preço por quilo é 250 reais")
elif codigoCarga >= 31 and codigoCarga <= 40:
    precoFinal = pesoCarga * 340
    print("Preço por quilo é 340 reais")
else:
    print("Código de carga inválido")
    precoFinal = 0

if codigoEstado == 1:
    imposto = precoFinal * (35 / 100)
elif codigoEstado == 2:
    imposto = precoFinal * (25 / 100)
elif codigoEstado == 3:
    imposto = precoFinal * (15 / 100)
elif codigoEstado == 4:
    imposto = precoFinal * (5 / 100)
else:
    imposto = 0


print(precoFinal + imposto)   