from alphabet import alphabet


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrpyt:\n").lower()
    text = input("type your message:\n").lower().strip()
    shift = int(input("Type the shift number:\n"))

    def encrypt(plain_text, amount_shift):
        cipher_text = ""
        for let in plain_text:
            if let in alphabet:                             #checks if nay space or punctuatuion
                position = alphabet.index(let)
                new_pos = position + amount_shift
                new_let = alphabet[new_pos]
                cipher_text += new_let
            else:
                cipher_text += let              
        print(f"The encoded text is {cipher_text}")   
            

    def decrypt(crypted_text, shifted_amount):
        cipher_text = ""
        for let in crypted_text:
            if let in alphabet:                             #checks if nay space or punctuatuion
                position = alphabet.index(let)
                new_pos = position - shifted_amount
                new_let = alphabet[new_pos]
                cipher_text += new_let
            else:
                cipher_text += let              
        print(f"The decode text is {cipher_text}")
     
    if direction == "encode":
        encrypt(plain_text=text, amount_shift=shift)
    elif direction == "decode"
        decrypt(crypted_text=text, shifted_amount=shift)
    
    #break while loop