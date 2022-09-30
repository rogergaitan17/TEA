maximo = 0 
minimo = 0
primer_numero = True
while True: 
    try:
        lista = input("Ingrese un número: ")
        if (lista == 'fin'):
            break
        else:
            if (primer_numero):
                maximo = int(lista)
                minimo = int(lista)
                primer_numero = False 
            else:
                if (int(lista) > maximo): maximo = int(lista)
                if (int(lista) < minimo): minimo = int(lista)
    except: 
        print("Valor no es válido")
        continue
print("Máximo", maximo)
print("Mínimo", minimo)
