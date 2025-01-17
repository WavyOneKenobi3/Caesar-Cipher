from alphabet import alphabet


while True:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt: ").lower()
    text = input("Type your message:\n").lower().strip()
    shift = int(input("Type the shift number:\n"))

    def caesar(text, shift, direction):
        cipher_text = ""
        if direction == "decode":
            shift *= -1  # Reverse the shift for decoding
        for let in text:
            if let in alphabet:  # Check if the character is in the alphabet
                position = alphabet.index(let)
                new_pos = position + shift
                cipher_text += alphabet[new_pos]
            else:
                cipher_text += let
        print(f"The {direction}d text is: {cipher_text}")

    # Call the function before asking if the user wants to continue
    caesar(text=text, shift=shift, direction=direction)

    keep_going = input("Do you wish to continue? Yes - continue, No - quit: ").lower()
    if keep_going == "no":
        break
