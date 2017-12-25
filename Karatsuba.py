'''Program to perform Karatsuba Multiplication'''

'''
Method Definition performing Karatsuba Multiplication
'''

def karatsuba_product(x,y):
  '''
  Converts the two numbers in to strings for
  the purpose of iterating on the digits
  '''
  x = str(x)
  y = str(y)

  '''
  Empty list to hold the digits for the first number
  '''
  l1 = []

  '''
  loop to populate list with digits of the first number
  '''
  for ch in x:
    l1.append(int(ch))

  ''' Calculates length of the list which represents
  the number of digits in the first number. For Karatsuba
  multiplication, the number is split into two'''

  length = int(len(l1)/2)

  '''
  Slicing the list into two equal halves which will
  represent 'a' and 'b'
  '''
  a_list = l1[:length]
  b_list = l1[length:]

  '''
  Joining the list of digits to form two numbers
  '''
  a_num = "".join(map(str, a_list))
  b_num = "".join(map(str, b_list))

  '''
  Converting two strings of number into integers
  '''
  a = int(a_num)
  b = int(b_num)
  
  '''
  Prints the two numbers 'a' and 'b'
  '''
  print("a =",a)
  print("b =",b)

  '''
  Empty list to hold the digits for the second number
  '''
  l2 = []

  '''
  loop to populate list with digits of the second number
  '''
  for ch2 in y:
    l2.append(int(ch2))

  ''' Calculates length of the list which represents
  the number of digits in the second number. For Karatsuba
  multiplication, the number is split into two'''
  length = int(len(l2)/2)

  '''
  Slicing the list into two equal halves which will
  represent 'a' and 'b'
  '''
  c_list = l2[:length]
  d_list = l2[length:]

  '''
  Joining the list of digits to form two numbers
  '''
  c_num = "".join(map(str, c_list))
  d_num = "".join(map(str, d_list))

  '''
  Converting two strings of number into integers
  '''
  c = int(c_num)
  d = int(d_num)
  
  print("c =",c)
  print("d =",d)


  '''
  Calculating and printing step one which is a*c
  '''
  step1 = a*c
  print("\nStep 1 - a.c = ",step1)

  '''
  Calculating and printing step two which is b*d
  '''
  step2 = b*d
  print("\nStep 2 - b.d = ",step2)

  '''
  Calculating and printing step three which is ((a+b)*(c+d))
  '''
  step3 = ((a+b)*(c+d))
  print("\nStep 3 - (a+b)*(c+d) =",step3)

  '''
  Calculating and printing step four which is Step 3 - Step 2 - Step 1
  '''
  step4 = step3 - step2 - step1
  print("\nStep 4 -> Step 3 - Step 2 - Step 1 =",step4)

  '''
  Calculating and printing step five, the result of Karatsuba Multiplication
   which is: (10^n * Step 1) + (10^n/2 * Step 4) + Step 2 
  '''
  step5 = ((pow(10,length*2))*step1) + ((pow(10,length))*step4) + step2
  print("\nStep 5 =",step5)

  '''
  Calculates and prints product using conventional multiplication
  '''
  conv_prod = int(n1)*int(n2)
  print("\nConventional product of the two numbers =",conv_prod)

  '''
  Calculates and prints the difference between the results of
  Karatsuba multiplication and conventional multiplication. If
  this error is zero, the Karatsuba product is calculated correctly
  '''
  print("Error = ",step5-conv_prod)


'''
Inputs the two numbers to be multiplied using Karatsuba Multiplication
'''
n1= (input("\nEnter first number(Number of digits should be a power of 2):"))
print("Entered number 1", n1)
n2= (input("\nEnter second number(Number of digits should be a power of 2):"))
print("Entered number 2", n2)

'''
Calling the function performing Karatsuba Multiplication with two numbers
as arguments
'''
karatsuba_product(n1,n2)




