import datetime as date
import math as mt
today=date.datetime.now()
print('Welcome to TecH CracK !!!')
print('The date and time is : ',today)
def matrix_addition(mat, mat1):
	a = len(mat)
	number = []
	for z in range(a):
		num = []
		b = len(mat[z])
		for y in range(b):
			c = mat[z][y]+mat1[z][y]
			num.append(c)
		number.append(num)
	return number
def matrix_subtraction(mat, mat1):
	a = len(mat)
	number = []
	for z in range(a):
		num = []
		b = len(mat[z])
		for y in range(b):
			c = mat[z][y]-mat1[z][y]
			num.append(c)
		number.append(num)
	return number
def matrix_transpose(mat):
	a = len(mat)
	number = []
	for z in range(a):
		b = len(mat[z])
		num = []
		for y in range(b):
			num.append(mat[y][z])
		number.append(num)
	return number
def matrix_multiplication(mat, mat1):
	a = len(mat)
	b = len(mat[0])
	c = len(mat1)
	number = []
	if b == c:
		for z in range(a):
			sum = 0
			num = []
			for y in range(c):
				for x in range(b):
					sum = sum + (mat[z][x] * mat1[x][y])
				num.append(sum)
			number.append(num)
		return number
	else:
		print('For multiplication of matrix must be like thiss 4 * 3 3 * 2...\nYou are not entered like this!!!')
def input1():
	number=[]
	while True:
		try:
			a : int =int(input('Enter the row size :'))
			b=int(input('Enter the column size :'))
			for z in range(a):
				num=[]
				for y in range(b):
					c=int(input())
					num.append(c)
				number.append(num)
			return number

		except ValueError as e:
			print('Not Entered correct value!!! RE ENTER',e)
def user_sum(a):
	sum=0
	for i in range(1,a+1):
		sum=sum+i
	return sum
def lcm(a,b) -> int:
	i = 2
	while True:
		if i % a == 0 and i % b==0:
			return i
		i += 1
print('Hey buddy!!!\nHere we can perform following operations..\nArithmetic operation -1\nMatrix operation\n1) Addition-21\n2) Subtraction-22\n3) Multiplication-23\n4) Transpose-24')
print('GCD-3\nLCM-4\nConversion-5\nFactorial-6\nSum of n numbers-7\nSquare root-8')
while True:
	print()
	inter = input('May I help you to solve Your  doubts(Yes/No) :   ')
	print()
	if inter.lower() == 'yes':
		el = int(input('Select the operation as per given abovee : '))
		if el == 1:
			print('You selected arithmetic operation !!!')
			while True:
				try:
					a = eval(input('Enter the Expression : '))
					print('Required Answer is : ',a)
					break
				except ZeroDivisionError as e:
					print('One by zero is not possible !!! RE ENTER ',e)
				except ValueError as g:
					print(f'Not Entered correct value !!!{g}\nRE ENTER')
				except Exception as f:
					print('Wrong inputs..RE ENTER', f)
		elif el == 21:
			print('You selected matrix addittion !!!')
			a = input1()
			b = input1()
			c = matrix_addition(a, b)
			print('Executed Answer : ',c)
		elif el == 22:
			print('You selected matrix Subtraction !!!')
			a = input1()
			b = input1()
			c = matrix_subtraction(a, b)
			print('Executed Answer is : ',c)
		elif el == 23:
			print('You selected matrix multiplication !!!')
			a=input1()
			b=input1()
			c=matrix_multiplication(a, b)
			print('Executed Answer is : ',c)
		elif el==24:
			print('You selected matrix transpose !!!')
			a = input1()
			b = matrix_transpose(a)
			print('Executed Answer is : ',b)
		elif el == 5:
			ell = input('Enter the Conversion type : ')
			if ell.lower() == 'binary':
				while True:
					try:
						a = int(input())
						print('Executed Answer is :',bin(a))
						break
					except ValueError as e:
						print('Not Entered correct value!!! RE ENTER',e)
			elif ell == 'octal':
				while True:
					try:
						a = int(input())
						print('Executed Answer is :',oct(a))
						break
					except ValueError as e:
						print('Not Entered correct value!!! RE ENTER',e)
			elif ell == 'hexa':
				while True:
					try:
						a  = int(input())
						print('Executed Answer is :',hex(a))
						break
					except ValueError as e:
						print('Not Entered correct value!!! RE ENTER',e)
			else:
				a = input('Enter the value for binary conversion if no enter(No)')
				b =  ['b','o','x']
				if a[1] == 'b':
					print('Executed Answer is : ',int(a,2))
				elif a[1] =='o':
					print('Executed Answer is : ',int(a,8))
				elif a[1] == 'x':
					print('Executes Answer is : ',int(a,16))
				else:
					print('You entered wrong onee !!!')
		elif el == 3:
			print('You are selected GCD !!!')
			while True:
				try:
					a = int(input())
					b = int(input())
					print('Executed Answer is : ',mt.gcd(a,b))
					break
				except ValueError as e:
					print('Not Entered correct value!!! RE ENTER',e)
		elif el == 6:
			print('You are selected factorial !!!')
			while True:
				try:
					a=int(input())
					print('Executed Answer is : ',mt.factorial(a))
					break
				except ValueError as e:
					print('Not Entered correct value!!! RE ENTER',e)
		elif el == 7:
			print('You are selected sum of numbers !!!')
			while True:
				try:
					a = int(input())
					b = user_sum(a)
					print('Executed Answer is : ',b)
					break
				except ValueError as e:
					print('Not Entered correct value!!! RE ENTER',e)
		elif el == 8:
			print('You are selected square root !!!')
			while True:
				try:	
					a = int(input())
					print('Executed Answer is : ',mt.sqrt(a))
					break
				except ValueError as e:
						print('Not Entered correct value!!! RE ENTER',e)
		elif el == 4:
			print('You are selected LCM !!!')
			while True:
				try:
					a = int(input())
					b =  int(input())
					c = lcm(a,b)
					print('Executed Answer is : ',c)
					break
				except ValueError as e:
					print('Not Entered correct value!!! RE ENTER',e)
		else:
			print('You entered is wrong or it doesn\'t exist !!!')
		print()
		print('_____________________')
	else:
		break