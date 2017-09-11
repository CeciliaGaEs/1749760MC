contador=0 #se edefine antes de la funcion
def selection(arr):
	global contador #es una variable definida fuera de la funcion
	for i in range(0,len(arr)-1):
		val=i
		for j in range(i+1,len(arr)):
			contador+=1
			if arr[j]<arr[val]:
				val=j
		if val!=i:
			aux=arr[i]
			arr[i]=arr[val]
			arr[val]=aux
	return arr


A=[1,12,43,64,76,34,87]
selection(A)#se manda a llamar la funcion para que ordene el arreglo
contador#es para saber cuántas operaciones hace el algoritmo

