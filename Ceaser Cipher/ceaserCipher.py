# Ceaser cipher

try: 
    import pyperclip # this is for copying text to the clipboard
except ImportError:
    pass 

# Every possible character to be encrypted or decrypted

symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Ceaser Ciper")
print(
    """
    The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. 
    It encrypts letters by shifting them over by a certain number of places in the alphabet

    This program lets the user encrypt and decrypt messages according to this algorithm.
    """
)

print()

# allow the user to enter if they are either encrypting or decrypting
while True:
    print("Do you want to encrypt or decrypt?")
    response = input('> ').lower()
    
    if response.startswith('e'):
        mode = 'encrypt'
        break
    
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    
    print('Please enter the letter e or d')

# let the user enter the key to use:
while True:
    maxKey = len(symbols)-1
    print("Please enter the key (0 to {}) to use.".format(maxKey))
    response = input("> ").upper()
    
    if not response.isdecimal():
        continue
    
    if 0 <= int(response) < len(symbols):
        key = int(response)
        break
    

# let the user enter the message to encrypt or decrypt
print("Enter the message to {}.".format(mode))
message = input("> ")

# ceaser cipher only works on upercase letters:
message = message.upper()

# stores the encrypted or decrypted form of the message
translated = ""

# Encrypt or decrypt each symbol in the message
for symbol in symbols:
    if symbol in symbols:
        # Get the encrypted or decrypted number for this symbol
        num = symbols.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        
        # Handle the wrap-around if num is larger than the length of symbols or less than o
        if num >= len(symbols):
            num = num - len(symbols)
            
        elif num < 0:
            num = num + len(symbols)
        
        # add encrypted/decrypted numbers symbol to translated:
        translated = translated + symbols[num]
    else:
        # Just add the symbol without ecrypting or decrypting
        translated = translated + symbols

# Display the encrypted or decrypted string to the screen:
print(translated)

try:
    pyperclip.copy(translated)
    print("Full {}ed text copied to clipboard.".format(mode))
except:
    pass                


