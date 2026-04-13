
nome = input('nome do funcionario: ')
print("Cargo:")
print("1 - Gerente")
print("2 - Analista")
print("3 - Assistente")
print("4 - Estagiário")
cargo = int(input("Escolha o cargo: "))
salario = float(input('salario base: '))
hr_extra = int(input('total de horas extras trabalhadas: '))
faltas = int(input('total de faltas no mes: '))
bonus = input('voce Recebeu bonus no mes? ')

def calcular_horas_extras(salario_base, horas):
    return salario_base * 0.015 * horas


def calcular_descontos_faltas(salario_base, faltas):
    return salario_base * 0.02 * faltas


def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus == 's':
        if cargo == 1:
            return 1000
        elif cargo == 2:
            return 500
        elif cargo == 3:
            return 300
        elif cargo == 4:
            return 100
    return 0


total_hr_extra = calcular_horas_extras(salario, hr_extra)
desconto_falta = calcular_descontos_faltas(salario, faltas)
valor_bonus = calcular_bonus(cargo, bonus)

salario_bruto = salario
total_acrescimos = total_hr_extra + valor_bonus
salario_final = salario_bruto + total_acrescimos - desconto_falta


print("Nome do funcionario:", nome)
print("Salario bruto: R$", round(salario_bruto, 2))
print("Total de acrescimos: R$", round(total_acrescimos, 2))
print("Total de descontos: R$", round(desconto_falta, 2))
print("Salario final: R$", round(salario_final, 2))



