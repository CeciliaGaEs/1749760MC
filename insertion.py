cnt=0
def insertion(arr):
	global cnt
	for indice in range(1,len(arr)):
		valor=arr[indice] #valor del elemento a comparar
		i=indice-1	  #i es el valor anterior al elemento que se esta comparando
		while i>=0:
			cnt+=1
			if valor<arr[i]:
				arr[i+1]=arr[i]
				arr[i]=valor
				i-=1
			else:
				break
	return arr
