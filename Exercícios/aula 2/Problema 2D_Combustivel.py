tempo = int(input('Tempo gasto na viagem (em horas): '))
Vm = int(input('Velocidade Média durante a viagem (em km/h): '))
distancia = Vm * tempo

litros = distancia / 12

print (tempo, 'h')
print (Vm, 'km/h')

print(f' {distancia: .3f} km')
print (f'{litros: .3f} L')

