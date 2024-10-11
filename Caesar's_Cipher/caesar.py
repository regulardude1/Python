def caesar_cipher(text, shift, encrypt_or_decrypt):
    result = ""
    if encrypt_or_decrypt == "decrypt":
        shift = -shift

    for char in text:
        # Checking if character is an uppercase letter
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Checking if character is a lowercase letter
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabet characters will stay the same

    return result

message = input("Enter the message: ")
shift_amount = int(input("Enter the shift number: "))
choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

output = caesar_cipher(message, shift_amount, choice)
print(f"The resulting message is: {output}")
