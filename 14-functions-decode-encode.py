import math

# # function
# def greet():
#     print('Hello')
#     print('Heiii')
#
# greet()

# # params
# def greet_with_name(name):
#     print(f"Hello {name}")
#
# greet_with_name('Python')

# # conditional params
# def greet_with(name, location):
#     print(f"Hi {name}. Your location {location} is near only")
#
# greet_with(name="Guna", location="test")

# # cans count with params
# def paint_can_calc(height, width, coverage_area):
#     return math.ceil((height * width) / coverage_area)
#
# can_count = paint_can_calc(height=int(input(f"Height of the wall ")), width=int(input(f"width of the wall ")), coverage_area=5)
#
# print(f"You need {can_count} cans of paint")

# # prime number calc with function params
# def prime_checker(number):
#     if(number < 1):
#         print(f"Enter value greater than 0")
#     elif(number==1 or number==2 or number==3):
#         print(f"{number} is prime")
#     elif((number % 2) == 0 or (number % 3) == 0):
#         print(f"{number} is not a prime")
#     else:
#         print(f"{number} is prime")
#
# prime_checker(number=int(input(f"Enter a numb to check ")))

# # caesar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

direction = input("Type 'encode' to encrypt, 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift_num = int(input("Type the shift number: \n"))


def cipher_text(msg, shift, mode):
    if shift > len(alphabet):
        shift = shift % len(alphabet)

    final = ''
    for char in msg:
        if char in alphabet:
            pos = alphabet.index(char)
            if mode == 'encode':
                if (pos + shift) >= len(alphabet):
                    final += alphabet[(pos + shift) - len(alphabet)]
                else:
                    final += alphabet[pos + shift]
            elif mode == 'decode':
                if (pos - shift) < 0:
                    final += alphabet[len(alphabet) + (pos - shift)]
                else:
                    final += alphabet[pos - shift]
        elif char == ' ':
            final += ' '
        else:
            final += '*'

    print(f"The Decoded text is {final}")


cipher_text(msg=text, shift=shift_num, mode=direction)