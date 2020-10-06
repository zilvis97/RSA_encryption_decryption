from random_prime import *
from generate_rsa_keypairs import *
from encryption_decryption import *


min_val = 32437
size = 32
keys = GenerateRSAKeyPair(GenerateRandomPrime(min_val, 5), GenerateRandomPrime(min_val, 5))
public_key = keys[0]
private_key = keys[1]

int_to_encrypt = 83483
encrypted_int = RSA_EncInt(int_to_encrypt, public_key)
print(int_to_encrypt, "encrypted as :", encrypted_int)

decrypted_int = RSA_DecInt(encrypted_int, private_key)
print("Decrypted int: ", decrypted_int)

#encrypt string
plain_str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
encrypted_str = RSA_EncStr(plain_str, size, public_key)

decrytped_str = RSA_DecStr(encrypted_str, private_key)

print(decrytped_str)