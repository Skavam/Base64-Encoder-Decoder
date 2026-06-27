# Base64 Encoder/Decoder program by @Skavam on GitHub

import base64
from colorama import Fore

def main():
    print("Welcome to Base64 Encoder/Decoder")
    print("1 - Encode a string to Base64")
    print("2 - Decode a Base64 string", "\n")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        user_string = input("Enter the string to encode: ")
        encoded = string_to_base64(user_string)
        print(f"\n Encoded Base64: {Fore.GREEN}{encoded}{Fore.RESET}")

    elif choice == '2':
        user_b64 = input("Enter the Base64 string to decode: ")

        if user_b64.strip() == "":
            print(f"{Fore.RED}Error: Input can't be empty.{Fore.RESET}")
            return
        
        try:
            base64.b64decode(user_b64, validate=True)

        except Exception as error:
            print(f"{Fore.RED}Error: Invalid Base64 string.{Fore.RESET}")
            return

        decoded = base64_to_string(user_b64)
        print(f"\n Decoded string: {Fore.GREEN}{decoded}{Fore.RESET}")

    else:
        print(f"{Fore.RED}Invalid choice. Please enter 1 or 2.{Fore.RESET}")

def string_to_base64(s):
    return base64.b64encode(s.encode()).decode()

def base64_to_string(b64):
    return base64.b64decode(b64.encode()).decode()
    
if __name__ == "__main__":
    main()
