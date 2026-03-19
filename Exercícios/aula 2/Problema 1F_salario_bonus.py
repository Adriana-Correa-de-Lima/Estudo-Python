nome = input('Primeiro nome do vendedor: ')
salario = float(input('Qual é o salário? '))
vendas = float(input('Qual é o total de vendas efetuada no mês, em dinheiro? '))

total = salario + (vendas * 0.15)

print (nome)
print (f'SALARIO = {salario: .2f}')
print (f'VENDAS = {vendas: .2f}')
print (f'TOTAL = {total: .2f}')