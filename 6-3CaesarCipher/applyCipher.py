# applyCipher.py
# A program to encrypt/decrypt user text
# using Caesar Cipher
#
# Author: rc.ruiz.rosaura [at] leadps.org

# makes a mapping of encode alphabet to decoded alphabet
# arguments: key
# returns: dictionary of mapped letters
def createDictionary():

	#placeholder
	return {}

# receive: user's encrypted message
# arguments: none
# return: encoded message
def getMessage():
	pass

# for each letter in the message, decodes and record
# arguments:encoded message, dictionary
# returns decoded message
def decodedMessage(message, dictionary):
	pass

# outputs the message to the terminal 
# arguments: decoded message
# returns: none
def printMessage(message):
	pass

# execution starts here

# ask user for key
print("What key would you like to use decode?")

key = int(raw_input())

dictionary = createDictionart(key)
encodedMessage = getMessage()
decodedMessage = decodedMessage(encodedMessage, dictionary)
printMessage(decodedMessage)
