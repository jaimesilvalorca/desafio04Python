with open("lorem_ipsum.txt", "r") as file:
    texto=file.read()
  
  
caracteres:list = []

def contador_de_palabras(texto):
    texto_split:list = texto.split(" ")
    contar_palabras = set(texto_split)
    return set(contar_palabras)
    
def contador_de_caracteres(texto):
    #otra opcion es solo ingresando set(texto).__len__()
    for caracter in texto:
        caracteres.append(caracter)
    return set(caracteres)

    
contar_caracteres:str = contador_de_caracteres(texto)
contar_palabras:str = contador_de_palabras(texto)

print(f"El número de caracteres distintos es: {len(contar_caracteres)}")
print(f"El número de palabras distintas es: {len(contar_palabras)}")