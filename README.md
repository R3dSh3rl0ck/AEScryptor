# AEScryptor Tool Description
Encrypt and Decrypt files with AES-128 (16bytes key).

<b>AES mode</b> = CFB (cipher Feedback) 

<b>security</b> = super safe!


# Usage
[1] Choose [1] or [0] ( [Encryption] or [Decryption] )

[2] Type keyphrase!

[3] Select a file (or path of a file)

[4] Enjoy!


# Real life usage

Everyday Example..

Alice wants to send a file to her friend Bob, but she wants to keep the content unreadable from the "Others"..After a long search at the web she found a tool called AEScryptor which contains operations which can make her file unreadalbe. She encrypts the file with a secret key of her choice and sends the encrypted file via e-mail to Bob. Bob receives an e-mail from Alice which contains a file and a random word..Bob realizes that the file was encrypted, immediately  uses AEScryptor to decrypt the message ( key = random word).It was a txt file which name was catme.txt, Bob uses his terminal to see the content $cat catme.txt and the pharse was <b> Respect Online Anonymity and Privacy </b>

<h3>Recommended package : pycryptodome --> $pip install pycryptodome</h3>
