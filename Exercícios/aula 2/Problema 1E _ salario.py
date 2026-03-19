A = int(input ("Digite o número de identificação do funcionário: "))
B = int(input("Digite a quantidade de horas trabalhadas: "))
C = round(float(input("Digite o valor que o funcionário recebe por hora trabalhada: ")), 2)

salario = B * C
print ('NÚMERO = ', A)
print ('Para ', B, "horas trabalhadas e considerando o valor ", C, "por hora trabalhada: ")
print (f'SALÁRIO = {salario: .2f}')

msg = "O salário é %6.2f" % (salario)
print (msg)


msg = "O salário é %9.2f" % (salario)
print (msg, end = "Trabalhe mais!")