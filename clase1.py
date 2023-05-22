lista = [15,"nombre", 3.1415,True]
print (lista [1])
usuario = ["usernameTest1","pass123","correo@correo.cl"]
numero = [10,50,100,155,500]
 #Appen= agregar um objeto a la ultima posicion 
numero.append (1000)
print(numero)
#extends = agrega un arreglo al final de nuestra lista
extra =[75,350,999]
numero.extend(extra)
print(numero)
#insert = agrega valor a una psicion especifica 
numero.insert(6,5000)
print(numero)
#remove= entrega valor, se busca y se elimina
numero.remove(50)
print(numero)
#PoP = elimina el ultimo registro 
#(i) = elimina la posicion del numero
numero.pop()
print(numero)
numero.pop(3)
print(numero)
#reverse = invierte orden de la lista
numero.reverse()
print(numero)
#sort = ordena los valores de menor a mayor
#sort(reverse=true) = ordena los valores de mayor a menor
numero.sort()
print(numero)
numero.sort(reverse=True)
print(numero)