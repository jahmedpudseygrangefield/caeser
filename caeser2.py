def main():
	print("Welcome to the caeser cypher shifting programme.")
	print("==================================================")
	print("  1. Encrypt\n     2. decrypt\n  3. decrypt a file\n")
	print("==================================================")


	option = int(input("option: "))

	
	message = input("input your appelative here:    ")
	shift = int(input("Input the shift value:    "))


	if option == 1:
		encrypt(message, shift)
	elif option ==2:
		decrypt(message, shift)
	elif option == 3:
		FileRead()
	else:
		print("Incorrect input")
		main()


def encrypt(message, shift):
	encrypted = ''
	for i in range(len(message)):
		if message[i].isalpha():
			if message[i].islower():
				num = ord(message[i]) + shift
				if num > ord('z'):
					num -= 26
					encrypted += chr(num)
				else:
					encrypted += chr(num)
			elif message[i].isupper():
				num = ord(message[i]) + shift
				if num > ord('Z'):
					num -= 26
					encrypted += chr(num)
				else:
					encrypted += chr(num)
		elif ord(message[i]) ==32:
			encrypted += ' '
		else:
			encrypted += message[i]
	print(encrypted,)
	
	FileWrite(encrypted)



def decrypt(message, shift):
	decrypted = ''
	for i in range(len(message)):
		if message[i].isalpha():
			if message[i].islower():
				num = ord(message[i]) - shift
				if num > ord('z'):
					num -= 26
					decrypted += chr(num)
				else:
					decrypted += chr(num)
			elif message[i].isupper():
				num = ord(message[i]) - shift
				if num > ord('Z'):
					num -= 26
					decrypted += chr(num)
				else:
					decrypted += chr(num)
		elif ord(message[i]) ==32:
			decrypted += ' '
		else:
			decrypted += message[i]
	print (decrypted)
	



def FileWrite(encrypted):
	file = open("encrypted.txt", "w")
	file.write(encrypted)
	file.close()
	print(f'the message: {encrypted}, has been written to a text file.')


def FileRead(decrypted):
	message = ''
	file = open("encrypted.txt","r")
	message += file.readline()
	shift = int(input("Enter shift: "))
	file.close()
	decrypt(message, shift)


if __name__ == "__main__":
	main()