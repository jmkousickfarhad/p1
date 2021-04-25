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

####################
# message='''
# hi kousick
#
# how are you
#
# it's not good :(
# '''
# print(message)

############
# name= 'Kousick Farhad'
# print(name[0])#from left-K
# print(name[-14])#from right-K
# print(name[0:7])#[start from:length]-Kousick
# print(name[-6:])#Farhad
# print(name[1:-1])#ousick Farha
# print(name[:])#to copy and print whole name

##################
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
##########################