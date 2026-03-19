tempo = int(input("Tempo de duração em segundos: "))
horas = tempo //3600
minutos = (tempo % 3600) // 60
segundos = ((tempo % 3600) % 60)


print (tempo, 's')
print ('Esse tempo equivale a ', horas, ':', minutos, ':' , segundos)
