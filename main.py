from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

import encryption
import decryption
print(r"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~          
*             _____   ____     ____     ____                  #
*            /       |    \     /|     /    \                 #
*           |        |     |   / |     \    /                 #
*             \      |    /      |      \__/                  #
*               |    |  /        |     /    \                 #   
*                /   |  \        |     \    /                 #
*          _____/    |    \    __|__    \__/                  #
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
print('\n***************************************************************')
print('* ShadowRoot18                                                *')
print('* Tool name : AES Cryptor                                     *')
print('* Operation : Encrypt/Decrypt any files!                      *')
print('***************************************************************\n')

# Menu
while True:
    print(26*'*'+ 'AES_Cryptor' + 26*'*'+ '\n')
    choice = input(f'[+] [1] Encryption Area\n[+] [0] Decryption Area\n>')
    # 1 = Encryption!
    if choice == '1':
        key = input(f'[+] Usage : Insert a phrase which will be used as a key.\n>')
        # bit form
        key = key.encode('UTF-8')
        # fill.. block size = 16 bits
        key = pad(key, AES.block_size)
        # enter file name or the path for encryption
        filename = input(f'[+] Enter the Filename or Path.\n>')
        # Encrypt the file..
        encryption.encryption(filename, key)
        break
    # 0 = Decryption!
    elif choice == '0':
        keyd = input(f'[+] Usage : Insert a phrase which will be used as a key.\n>')
        # bit form
        keyd = keyd.encode('UTF-8')
        # fill.. block size = 16 bits
        keyd = pad(keyd, AES.block_size)
        # enter file name or the path for decryption
        filenamed = input(f'[+] Enter the Filename or Path.\n>')
        # Reveal the hidden file.
        decryption.decryption(filenamed ,keyd)
        break
    else:
        print(f'Unexpected operation .. Please Try again! ( Usage : [1] Encryption [0] Decryption.\n')
