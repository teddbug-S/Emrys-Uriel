import random

numbers = "1234567890ζαΔδξ¤¥֏௹₡฿₢₣₩₱₳"
symbols = "&?.,!@#$%;:_+=-*()~^<>}{[]"

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
space = " "
other_symbols = list("₼ϟϙͲ")
selected = random.choice(other_symbols)


def cipher_text(text, key):
    """This function takes a plain text argument at first position
       and an integer as second argument and returns
        a scrambled or cipher version of the text"""
    ciphered_text = ""
    try:
        for letter in text:
            if letter in alphabets:
                letter_position = alphabets.index(letter)
                new_letter = alphabets[(letter_position + key) % len(alphabets)]
                ciphered_text += new_letter

            elif letter in numbers:
                number_position = numbers.index(letter)
                new_symbol = symbols[(number_position + key) % len(symbols)]
                ciphered_text += new_symbol

            elif letter in symbols:
                symbol_position = symbols.index(letter)
                new_number = numbers[(symbol_position + key) % len(numbers)]
                ciphered_text += new_number

            elif letter in space:
                new_space = random.choice(other_symbols)
                ciphered_text += new_space
            else:
                ciphered_text += letter
        return ciphered_text
    except:
        raise


def decipher_text(text, key):
    """This function takes a ciphered text as first positional
        argument and an integer key as last positional argument
        used to cipher the text and returns a plain text"""
    deciphered_text = ""
    try:
        for letter in text:
            if letter in alphabets:
                letter_position = alphabets.index(letter)
                new_letter = alphabets[(letter_position - key) % len(alphabets)]
                deciphered_text += new_letter

            elif letter in numbers:
                number_position = numbers.index(letter)
                new_symbol = symbols[(number_position - key) % len(symbols)]
                deciphered_text += new_symbol

            elif letter in symbols:
                symbol_position = symbols.index(letter)
                new_number = numbers[(symbol_position - key) % len(numbers)]
                deciphered_text += new_number

            elif letter in other_symbols:
                old_space = space[0]
                deciphered_text += old_space
            else:
                deciphered_text += letter
        return deciphered_text
    except:
        raise
