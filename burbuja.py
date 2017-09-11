cnt=0

#funcion burbuja
def burbuja(arr):
	global cnt
	for i in range(1, len(arr)):
		for j in range(0, len(arr)-1):
			cnt+=1
			if arr[j+1]<arr[j]:
				aux=arr[j]
				arr[j]=arr[j+1]
				arr[j+1]=aux
	return arr