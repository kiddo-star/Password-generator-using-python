import string
import random

def generatePassword(num):
	password = ''
	
	for n in range(num):
		x = random.randint(0,94)
		password += string.printable[x]
	
	return password

	# generate and print a 16 character random password

print (generatePassword(16))