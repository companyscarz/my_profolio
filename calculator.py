while True:
	try:
		num1 = float(input("num 1: "))
		num2 = float(input("num2: "))
		op = input("operator eg + - * ÷ !: ")
		if op=="+":
			print(num1+num2)
		elif op=="-":
			print(num1-num2)
		elif  op=="÷":
			print(num1/num2)
		elif op=="*":
			print(num1*num2)
		elif op=="!":
			exit()
		elif num1==0 or num2==0:
			pass
		elif op not in ["+", "-", "÷","*"]:
			print('invlaid operator')
	except ValueError:
		print('only intergers allowed')