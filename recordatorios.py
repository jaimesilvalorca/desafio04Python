recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

recordatorios.insert(1,['2021-02-02','06:00',"Empezar el Año"])

#Aquí indico dos posibles opciones una con metodos pop e insert y la otra es recorriendo la lista.

# recordatorios.pop(3)
# recordatorios.insert(3,['2021-07-15', "13:00", "No hacer nada es feriado"])

for i,recordatorio in enumerate(recordatorios):   
    if recordatorio == ['2021-07-15', "13:00", "No hacer nada es feriado"]:
        recordatorios[i] = ['2021-07-16', "13:00", "No hacer nada es feriado"]

#Aquí indico dos posibles opciones una con metodos pop y remove y la otra es recorriendo la lista.           
# recordatorios.pop(2)
# recodatorios.remove(['2021-05-01', "15:00", "No trabajar"])

for i,recordatorio in enumerate(recordatorios):   
    if recordatorio == ['2021-05-01', "15:00", "No trabajar"]:
        recordatorios.pop(i)

#Aquí indico dos posibles opciones una con metodos insert y append y la otra es recorriendo la lista.

# recordatorios.insert(4,['2021-12-24', '22:00', 'Cena de Navidad'])
# recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])

for i,recordatorio in enumerate(recordatorios):
    if recordatorio == ['2021-09-18', "16:00", "Ramadas"]:
        recordatorios.insert(i+1,['2021-12-24', '22:00', 'Cena de Navidad'])
    if recordatorio == ['2021-12-25', "00:00", "Navidad"]:
        recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])
    
# Output
print(recordatorios)
