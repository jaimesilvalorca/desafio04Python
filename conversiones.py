from sys import argv

print(argv)

if len(argv) != 5:
    print("Cantidad ingresada es menor.")
else:
    sol:float = float(argv[1])
    argentino:float = float(argv[2])
    dolar:float = float(argv[3])
    chileno:float = float(argv[4])
    tasas = {
    "sol peruano":sol,
    "peso argentino":argentino,
    "dolar":dolar,
    }  
        
conversion = {k:v*chileno for k,v in tasas.items()} 

print(f"""
Los {chileno} pesos equivalen a:
{conversion.get('sol peruano')} Soles
{conversion.get('peso argentino')} Pesos Argentinos
{conversion.get('dolar')} Dólares           
      """)

    

    

    




