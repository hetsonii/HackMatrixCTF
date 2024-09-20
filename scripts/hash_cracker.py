import hashlib

def crack_sha256_hash(hash_to_crack, wordlist_file):
    try:
        # Open the wordlist file
        with open(wordlist_file, 'r') as wordlist:
            for word in wordlist:
                word = word.strip()  # Remove newline characters
                
                # Hash the word using SHA-256
                hashed_word = hashlib.sha256(word.encode('utf-8')).hexdigest()
                
                # Compare the hashed word with the target hash
                if hashed_word == hash_to_crack:
                    print(f"Hash cracked! The password is: {word}")
                    return
                
        print("Password not found in wordlist.")
    
    except FileNotFoundError:
        print(f"Wordlist file '{wordlist_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace with your SHA-256 hash and wordlist path
hash_to_crack = '72b2101e358950e04554187d244be259d55054e7cb11354b0b7d9e6c932a7031'
wordlist_file = 'wordlist1.txt'

crack_sha256_hash(hash_to_crack, wordlist_file)

