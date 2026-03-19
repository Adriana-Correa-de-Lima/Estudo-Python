idade = int(input("Informe sua idade em dias: "))

anos = idade // 365
meses = (idade % 365) // 30
dias = (idade % 365) % 30

print('Sua idade é: ', idade, 'dias')
print('Isso equivale a: ')
print(anos, 'ano(s)')
print(meses, 'mes(es)')
print(dias, 'dia(s)')