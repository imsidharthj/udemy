from caesar_logo import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def main():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    print(f"Here's the {direction}d result:{ caesar(text, shift, direction)}")
def caesar(incial_text, shift_amount, code_direction):
    result = ''
    for i in incial_text:
        if i.isalpha():
            index = alphabet.index(i)
            if code_direction == "encode":
                new_index = (index + shift_amount) % 26
            elif code_direction == "decode":
                new_index = (index - shift_amount) % 26
            result = result + alphabet[new_index]
        else:
            result = result + i
    return result
if __name__ == "__main__":
    print(logo)
    while True:
        main()
        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
        if restart == "yes":
            continue
        else:
            break