#se declaran diccionarios = objetos
clienteUno={
    "id":5,
    "nombre":"edif1",
    "consumo":200
}

clienteDos={
    "id":58,
    "nombre":"edif2",
    "consumo":500
}

#se declara una lista = arreglo
clientesAsociados=[
    clienteUno,
    clienteDos

]
#RECORRER UNA LISTA O ARREGLO
#print(clientesAsociados)

'''for i in range(2):
    print(clientesAsociados[i]["consumo"])'''

#programemos un foreach que es eun for
#especializado en recorrer arreglos (listas)
for cliente in clientesAsociados:
    print(cliente["id"],'=>',cliente['consumo'],'KWH')
    print(f"{cliente["id"]},'=>',cliente['consumo'],'KWH')

