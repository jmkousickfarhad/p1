# ###################### INPUT/PRINT/CONCATANATION OF STRING/FORMATTING/VARIABLE TYPE
# name = input('what is your name? ')
# color = input('What is your Favourite color? ')
# print(name + ' likes ' +color)
# print (f'{name} likes {color}')# here f is prifix formatted string
# #cw 2
#
# weight = input('enter weight in Pound: ')
# convertion = float(weight) * 0.453592
# print(weight +'lbs = '+str(convertion)+'kg')
# #cw 3 (input is always assigned as Sting in python)
#
# ################### MULTIPLE LINEs UNDER ONE VARIABLE
# message='''
# hi kousick
#
# how are you
#
# it's not good :(
# '''
# print(message)
#
# ########### DELING WITH INDEX
# name= 'Kousick Farhad'
# print(name[0])#from left-K
# print(name[-14])#from right-K
# print(name[0:7])#[start from:length]-Kousick
# print(name[-6:])#Farhad
# print(name[1:-1])#ousick Farha
# print(name[:])#to copy and print whole name
#
# ################# METHODS AND FUNCTION COMPAIRSM/ in OPERATOR
# name='my name is Kousick Farhad'
# print(len(name))
# #here len or print are general purpose function means not only belong or useed in a specefic variable type or object..
# print(name.upper())
# print(name.lower())
# #here .upper() is used in a specefic variable type(string) which is called as method is also a type of function.
# #method will not change our orginal variable.it makes a colon of given string and modify it.. let's see
# print(name)
#
# # other methodes
# print(name.find('K'))
# #find method gives us the index or position number of a particuler character.
# print(name.find('Farhad'))#can not find farhad because python is case sensetive.
# #here find method gives us the starting index number of Farhad in our name string.
#
# print(name.replace('Kousick','JM'))#varName.replace('which part to replace','with what to replace') is called find-replace method.
#
# #in operator (boolian)
# print('Farhad' in name)# is Farhad exists in name variable?
# print('JM' in name)
#
# ######################### ARITHMATIC OPERATORS
# arithmatic operatprs are
# + addition
# - subtraction
# / division with decimal point if exists
# // only for quotient
# % only for remainder
# * for multiplication
# ** for exponent
#
# ######################### ARITHMATIC OPERATIOONS EXAMPLE
# some arithmatic operations
# x=3
# x+=2 # same as x=x+2
# print(x)
#
# a=2
# a **=3 #same as 2**3
# print(a)
#
# b=-2.76
# print(round(b))#to round up
# print(abs(b))#to get absulate value
#
# ############### MATH MODULE
# #we can import math module to make our mathmatical task easily.such as
# import math
# p=math.atan(math.isqrt(3))#other wise we have to write down code for trigonomatric function and so one.
# print(p)
# print(f'converted value is {math.degrees(float(p))} Degree')
#
# ######################## IF/ELIF/ELSE WITH IN OPERATOR
# #if elif else with in operator
# print('''how is the weather codition?\nPress:\nH if it's "hot"\nC if it's "cold"\nR if it's "rainy"\nS if it's "shiny"''')
# x=input('Enter the weather condition: ')
# y=x.lower()
# if 'c' in y:
#     print('Wear worm cloth')
# if 'h' in y:
#     print('Drink water properly ')
# if 'r' in y:
#     print('Stay home or take rain coat while going outside')
# if 's' in y:
#     print('You can go to sea beach for enjoying the day')
# else:
#     print("You have enter wrong key" )
#
# print('Thank you')
#
# ########### CW3
# rate = 1000000
# type=input('Please enter cradit type(good/bad): ').lower()
#
# if 'good' in type:
#     print(f'downpaiment is ${int(rate)*(10/100)}')
# else:
#     print(f'downpaiment is ${int(rate) * (20 / 100)}')
#
# ###################### LOGICAL OPERATOR-AND/OR/NOT
# highIncome=input('Is clints income high(yes/no): ').lower()
# goodCradit=input('Does clint has good Cradit(yes/no): ').lower()
#
# #AND-BOTH CONDITIONS HAVE TO BE TRUE.
#
# if 'yes' in highIncome and 'yes' in goodCradit:
#     print('You are eligible for loan.')
# else:
#     print('Sorry,You are not eligible for loan.')
#
# #OR-IF ONE IS TRUE THEN WHOLE CONDITION WILL BE TRUE.
#
# if 'yes' in highIncome or 'yes' in goodCradit:
#     print('You are eligible for loan.')
# else:
#     print('Sorry,You are not eligible for loan.')
#
#
# goodCradit=input('Does clint has good Cradit(yes/no): ').lower()
# criminalRecord= input('does the applicant has criminal record(yes/no): ').lower()
# if 'yes' in goodCradit and not 'yes' in criminalRecord: # not operator will change the condition opposit
#     print('applicant is eligible for lone.')
# else:
#     print('applicant is not elegible for the lone.')
#
# ######################### COMPARISON OPERATOR >/</>=/<=/==/!=
#temp = input("enter the temperature: ")

# if int(temp)>30:
#     print("It's a Hot day." )
# elif int(temp)<10:
#     print("It's a Cold day.")
# else:
#     print("It's nither Hot or Cold day.")

######OR

# temp = int(input("enter the temperature: "))
# if (temp)>30:
#     print("It's a Hot day." )
# elif (temp)<10:
#     print("It's a Cold day.")
# else:
#     print("It's nither Hot or Cold day.")

# ##############CW4
# name = input('please input your name here: ')
# if len(name)<3:
#     print('invalid name.\nyour name should contain at least 3 characters.')
# elif len(name)>50:
#     print('invalid name.\nyour name should contain at most 50 characters.')
# else:
#     print('name looks good.')

# #OR
# name = len(input('please input your name here: '))
# if 3 < name < 50:
#      print ('name looks good')
# else:
#      print ('name must be in between 3 to 50 characters.')

##########################CW5-1:17
# weight = int(input('please enter your weight: '))
# unit = input('enter you unit of weight that you have entered  if Lsb(pound) press (L) or if Kg press (K): ').lower()
#
# if 'l' in unit:
# #OR we can use
# # if unit==l
#     print(f'your converted unit is {weight*0.45}kg')
# elif 'k' in unit:
# # OR we can use
# # if unit==k
#     print(f'your converted unit is {weight/0.45}pound')
#
# else:
#     print('please enter a valid unit and try again.')


