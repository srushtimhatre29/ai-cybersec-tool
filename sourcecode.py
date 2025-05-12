import string
import time


common_passwords = ['123456', 'password', '12345678', 'qwerty', 'abc123', '111111']

def check_strength(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_lower, has_upper, has_digit, has_symbol])
    
    print("\nPassword Analysis:")
    print(f"- Length: {length}")
    print(f"- Includes lowercase: {has_lower}")
    print(f"- Includes uppercase: {has_upper}")
    print(f"- Includes digits: {has_digit}")
    print(f"- Includes symbols: {has_symbol}")
    
    if password in common_passwords:
        print("Warning: This is a common weak password!")

    if length < 8 or score < 3:
        print("Strength: Weak")
    elif length >= 8 and score == 3:
        print("Strength: Moderate")
    else:
        print("Strength: Strong")

def estimate_brute_force_time(password):
    charset_size = 0
    if any(c.islower() for c in password): charset_size += 26
    if any(c.isupper() for c in password): charset_size += 26
    if any(c.isdigit() for c in password): charset_size += 10
    if any(c in string.punctuation for c in password): charset_size += len(string.punctuation)
    
    total_combinations = charset_size ** len(password)
    guesses_per_second = 1e6  
    seconds = total_combinations / guesses_per_second

    print(f"\nEstimated time to brute-force (1M guesses/sec): {seconds:.2e} seconds")
    if seconds < 60:
        print("=> Can be cracked in under a minute.")
    elif seconds < 3600:
        print("=> Can be cracked in under an hour.")
    elif seconds < 86400:
        print("=> Can be cracked in a day.")
    else:
        print("=> Cracking this would take days or more — relatively secure.")


if _name_ == "_main_":
    pwd = input("Enter a password to check: ")
    check_strength(pwd)
    estimate_brute_force_time(pwd)
