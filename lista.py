salida=False
while not salida:
    print("\n\nMENU")
    print("\n\n1)Crear lista")
    print("2)Anadir elemento")
    print("3)Eliminar elemento")
    print("4)Modificar elemento")
    print("5)Mostrar datos")
    print("6)Mostar datos de forma inversa")
    print("7)Limpiar lista")
    print("8)Borrar lista")
    print("9)salir")
    opcion=input("\n\nError, ingrese un numero de opcion valido ")
    print("\n\n")
    
    if(opcion=='1'):
        print("--->Crear lista<---")
        if 'lista' in locals():
            print("\nLa lista es existente")
        else:
            lista=[]
            print("\nBien, La Lista fue creada")

    elif(opcion=='2'):
        print("-->Agregar elemento<--")
        if 'lista' in locals():
            ll=input("\nIngrese un elemento: ")
            lista.append(ll)
            print("\nElemento ingresado correctamente")
        else:
            print("\nLa lista no existe")
            

    elif(opcion=='3'):
        print("-->Eliminar elemento<--")
        if 'lista' in locals():
            lista[0]=''
            print("\nElemento eliminado")
        else:
            print("\La lista no existe")

    elif(opcion=='4'):
        print("-->Modificar elemento<--")
        if 'lista' in locals():
            lista[0]=input('\nSustitucion:')
            print("Elemento modificado")
        else:
            print("\La lista no existe")

    elif(opcion=='5'):
        print("-->Mostrar datos<--")
        if 'lista' in locals():
            print(lista)
        else:
            print("\nLa lista no contiene ningun dato")

    elif(opcion=='6'):
        print("-->Mostar datos de forma inversa<--")
        if 'lista' in locals():
            for x in reversed(lista):
                print(x)
        else:
            print("\nLa lista no contiene ningun dato")

    elif(opcion=='7'):
        print("-->Limpiar lista<--")
        if 'lista' in locals():
            del(lista)
            lista=[]
            print("\Elementos de la lista eliminados")
        else:
            print("\nLa lista no existe")

    elif(opcion=='8'):
        print("-->Borrar lista<--")
        if 'lista' in locals():
            del(lista)
            print("\nLista eliminada con exitosamente")
        else:
            print("\nLa lista no existe")

    elif(opcion=='9'):
        print("\nHasta la proxima :) ")
        salida=True
        
    else:
        print("opcionion o valor invalido")
