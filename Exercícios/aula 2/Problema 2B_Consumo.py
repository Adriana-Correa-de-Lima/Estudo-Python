X = int(input("Digite a distância total percorrida(em Km): "))
Y = round(float(input("Digite o total de combustível gasto: ")), 1)

consumoMedio = X / Y

print(X)
print(Y)
print(f'{consumoMedio:4.3f} Km/L')