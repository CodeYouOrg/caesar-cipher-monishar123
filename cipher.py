
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Calculate the position of the shifted character
            new_char = chr(start + (ord(char) - start + shift) % 26)
            encrypted_text += new_char
        else:
            # If the character is not a letter, keep it as it is
            encrypted_text += char
    return encrypted_text

def main():
    # Ask the user for a plain text sentence
    plain_text = input("Please enter a plain text sentence: ")
    shift = 5  # Right shift of 5
    encrypted_text = caesar_cipher(plain_text, shift)
    # Print the encrypted text
    print("Encrypted text:", encrypted_text)

# Call the main function to run the program
if __name__ == "__main__":
    main()
 add your code here
