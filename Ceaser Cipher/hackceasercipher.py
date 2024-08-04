# let the user specify the message to hack:

print("Enter the encrypted Ceasar cipher message to hack")
message = input("> ")

symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for key in range(len(symbols)):
    