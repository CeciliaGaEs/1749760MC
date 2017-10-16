def primo(n):
	cnt=0
	for i in range(2, round(n**0.5)):
		cnt= cnt+1
		if((n%1)==0):
			return("no es primo")
	return ("es primo")
