def encrypt(message):
    key = "5pR1nG21"  # Fixed 8-character alphanumeric key
    num_columns = len(key)
    
    # Pad the message with spaces to make its length a multiple of the number of columns
    message += ' ' * (num_columns - (len(message) % num_columns))
    
    # Create a list of strings, each representing a column in the transposition grid
    columns = [''] * num_columns
    for i, char in enumerate(message):
        column_index = i % num_columns
        columns[column_index] += char
    
    # Rearrange the columns according to the sorted key
    sorted_key = ''.join(sorted(key))
    encrypted_message = ''
    for char in sorted_key:
        index = key.index(char)
        encrypted_message += columns[index]
    
    return encrypted_message

def decrypt(encrypted_message):
    key = "5pR1nG21"  # Fixed 8-character alphanumeric key
    num_columns = len(key)
    encrypted_length = len(encrypted_message)
    
    # Calculate the number of rows in the transposition grid
    num_rows = encrypted_length // num_columns
    
    # Determine the number of characters in the last column (if the message is padded)
    remainder = encrypted_length % num_columns
    
    # Create a list of empty strings to represent the transposition grid
    grid = [''] * num_columns
    
    # Populate the grid by rearranging the encrypted message according to the key
    sorted_key = ''.join(sorted(key))
    char_index = 0
    for char in sorted_key:
        index = key.index(char)
        if index < remainder:
            grid[index] = encrypted_message[char_index:(char_index + num_rows + 1)]
            char_index += num_rows + 1
        else:
            grid[index] = encrypted_message[char_index:(char_index + num_rows)]
            char_index += num_rows
    
    # Read the grid column by column to retrieve the decrypted message
    decrypted_message = ''
    for i in range(num_rows):
        for j in range(num_columns):
            if i < len(grid[j]):  # Check if the row index is within the string length
                decrypted_message += grid[j][i]
    
    return decrypted_message.strip()

# Main program for encryption and decryption
def main():
    while True:
        choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").strip().lower()
        if choice == 'q':
            print("Exiting the program.")
            break
        
        if choice == 'e':
            message = input("Enter the message to encrypt: ").strip()
            encrypted_message = encrypt(message)
            print("Encrypted message:", encrypted_message)
        
        elif choice == 'd':
            encrypted_message = input("Enter the message to decrypt: ").strip()
            decrypted_message = decrypt(encrypted_message)
            print("Decrypted message:", decrypted_message)
        
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")


if __name__ == "__main__":
    main()
