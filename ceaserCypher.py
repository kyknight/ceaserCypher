#encrypt function project
key = 3
orgMess = 'I love tacos'

def encrypt(orgMess, key)
	alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	#key = 3
	#orgMess = 'I love tacos'
	encryptMess = ''

	orgMess = orgMess.upper()

	for character in orgMess:
		newCharacter = ''
		if character in alpha:
			orgMess = alpha.find(character)
			newPos = orgMess + key

			if newPos > len(alpha)-1:
				newPos = orgMess + key - len(alpha)
			newCharacter = alpha[newPos]
		else:
			newCharacter = character

		encryptMess += newCharacter

	return encryptMess

#################################################
encryptMess = encrypt(orgMess, key)
print(encryptMess)


#hackcc function

def decrypt(encryptMess, key):
	alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	orgMess = ''
	#encryptMess = 'L ORYH WDFRV'
	encryptMess = encryptMess.upper()

	for encryptCharacter in encryptMess:
		origCharacter = ''
		if encryptCharacter in alpha:
			encryptCharacterPos = alpha.find(encryptCharacter)
			orgMessPos = encryptCharacterPos - key

			if orgMessPos < 0:
				orgCharacterPos = orgMessPos + len(alpha)
			orgCharacter = alpha[orgCharacterPos]
		else:
			orgCharacter = encryptCharacter

		orgMess += orgCharacter

	return orgMess

def hack(encryptMess):
	for key in range(1,26):
		print(decrypt(encryptMess, key))

##################################################
