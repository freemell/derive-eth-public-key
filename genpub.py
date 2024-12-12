from eth_account import Account
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from Crypto.Hash import keccak
import binascii

# Ethereum address to match
target_address = "0x4C03D23cC646aB7844eF91995608600591ffB58D"

# Function to generate Ethereum address from public key
def public_key_to_address(public_key):
    # Keccak-256 hash of the public key (uncompressed format)
    keccak_hash = keccak.new(digest_bits=256)
    keccak_hash.update(public_key[1:])  # Skip the first byte (0x04) to get the raw public key
    address = keccak_hash.hexdigest()[-40:]  # Take last 20 bytes (40 hex characters)
    return "0x" + address.lower()

# Function to check if a private key matches the target address
def check_private_key(private_key_hex):
    try:
        # Convert private key from hex to integer
        private_key_int = int(private_key_hex, 16)
        
        # Generate the public key from the private key
        private_key = ec.derive_private_key(private_key_int, ec.SECP256K1(), default_backend())
        public_key = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.X962,
            format=serialization.PublicFormat.UncompressedPoint
        )
        
        # Debugging step: print the public key
        print(f"Public Key (uncompressed): {binascii.hexlify(public_key)}")
        
        # Generate Ethereum address from the public key
        generated_address = public_key_to_address(public_key)
        
        # Debugging step: print the generated address
        print(f"Generated Ethereum Address: {generated_address}")
        
        # Compare the generated address with the target address
        if generated_address.lower() == target_address.lower():
            print(f"Match found! Private key: {private_key_hex}")
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking private key {private_key_hex}: {e}")
        return False

# Function to load private keys from the file and check each one
def check_keys_from_file(file_name="generakeys.txt"):
    with open(file_name, "r") as file:
        for line_num, line in enumerate(file, 1):
            private_key = line.strip()
            if check_private_key(private_key):
                print(f"Private key that matches: {private_key}")
                return private_key  # Stop once a match is found
    print("No matching private key found.")
    return None

if __name__ == "__main__":
    # Check keys from the list
    check_keys_from_file()
