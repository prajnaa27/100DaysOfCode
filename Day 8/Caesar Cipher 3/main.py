from art import logo

print(logo)
go_again='yes'
alphabets = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}

def get_key_by_value(dictionary,value):
    for key,val in dictionary.items():
        if val==value:
            return key
    return None

def caesar_cipher(type,message,shift_no):
    if type=='encode':
        encoded_message=""
        for letter in message:
            alphabet_index=alphabets[letter]
            encoded_index=alphabet_index+shift_no
            if encoded_index>26:
                encoded_index=encoded_index%26
            encoded_letter=get_key_by_value(alphabets,encoded_index)
            encoded_message+=encoded_letter.lower()
        return encoded_message

    elif type=='decode':
        decoded_message = ""
        for letter in message:
            alphabet_index = alphabets[letter]
            decoded_index = alphabet_index - shift_no
            if decoded_index <=0:
                decoded_index = 26+decoded_index
            decoded_letter = get_key_by_value(alphabets, decoded_index)
            decoded_message += decoded_letter.lower()
        return decoded_message
    else:
        print("Invalid type")
    return None

while 'no' not in go_again:
    action_type=input("Type 'encode' to encrypt and type 'decode' to decrypt\n")
    if action_type== 'encode' or action_type== 'decode':
        message=input("Type your message\n").upper()
        shift_no=int(input("Type the shift number\n"))
        if action_type== 'encode':
            encoded_message=caesar_cipher(action_type, message, shift_no)
            print(f"Here's the encoded message : {encoded_message}")
        else:
            decoded_message=caesar_cipher(action_type, message, shift_no)
            print(f"Here's the decoded message : {decoded_message}")
        go_again = input("Type 'yes' if you want to go again . Otherwise type 'no'\n").lower()
    else:
        print(f"Invalid choice, please choose 'encode' or 'decode'")