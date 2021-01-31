x=1000
n=int(input("ENTER YOUR PASSWORD:"))
m=int(input("CONFIRM YOUR PASSWORD:"))
if n==m:
	print("YOUR PASSWORD IS UPDATED.")
	print("To hack the password press 'y'  ")
	i=input(":")
	if i =='y':
		while (1000<=x<=9999):
			print(x)
			x=x+1
			if x==n:
				print("Password is",x)
				break
	else:
		print("sorry")
else:
	print("TRY AGAIN LATER.")
