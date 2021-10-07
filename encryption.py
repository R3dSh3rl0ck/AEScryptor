from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode


def encryption(file, key):
    with open(file, 'rb') as enc:
        data = enc.read()
        # CFB MODE (cipher Feedback)
        cipher = AES.new(key, AES.MODE_CFB)
        # add if key < 16
        ciphertext = cipher.encrypt(pad(data, AES.block_size))
        # base64 for encoding
        iv = b64encode(cipher.iv).decode('UTF-8')
        ciphertext = b64encode(ciphertext).decode('UTF-8')
        # add the final ciphertext to iv 
        write = iv + ciphertext
    enc.close()
    with open(file + '.enc', 'w') as data:
        data.write(write)
    data.close()
    print(f'[+] Encryption Successful.')


