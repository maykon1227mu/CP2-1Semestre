nomeDev = input("Digite o seu nome: ")
idadeDev = int(input("Digite a sua idade: "))
rendaDev = float(input("Digite a sua Renda: "))
empresDev = float(input("Digite o valor de empréstimo: "))
parceDev = int(input("Digite o número de parcelas(3 até 24): "))

juros = 0
valParcela = 0
valtotal = 0

def definir_taxas():
    global juros
    if(parceDev < 6):
        juros = 0.05
    elif(parceDev >= 7 and parceDev <= 12):
        juros = 0.08
    elif(parceDev > 12 and parceDev < 24):
        juros = 0.10
    else:
        ("O valor digitado de parcelas não está dentro do parâmetro")

def calcular_taxa():
    global valParcela
    valParcela = empresDev * ((juros * (1 + juros)**parceDev) / ((1 + juros)**parceDev - 1))
    print("A taxa aplicada é: ", juros)
    print("O valor da parcela é: ", valParcela)

def calcular_total():
    global valtotal
    valtotal = valParcela * parceDev
    print("O valor total pago é: ", valtotal)

def calcular_juros():
    valJuros = valtotal - empresDev
    print("O valor a pagar somente de juros é: ", valJuros)

def pode_aprovar(idade, renda, emprestimo):
    if(idade >= 18 and emprestimo <= 20 * renda):
        print("O empréstimo foi liberado")
        definir_taxas()
        calcular_taxa()
        calcular_total()
        calcular_juros()
    else:
        print("Você não pode realizar um empréstimo")

pode_aprovar(idadeDev, rendaDev, empresDev)