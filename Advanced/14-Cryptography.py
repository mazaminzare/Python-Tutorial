from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher_suite = Fernet(key)
print(key)
# Encrypt a message
message = b"Secret message"
cipher_text = cipher_suite.encrypt(message)
print(cipher_text)

# Decrypt the message
plain_text = cipher_suite.decrypt(cipher_text)
print(plain_text)
