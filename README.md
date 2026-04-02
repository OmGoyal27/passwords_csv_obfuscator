# Passwords CSV Obfuscator

This is a project if you are a super paranoid person, but want to store your passwords locally on a file, this is for you!

# What does it do

It can encrypt and decrypt the exported passwords file list. (Only CSV will be supported.)

## How to use

To encrypt a file, run it through the encrypter program.

To decrypt a file, run it through the decryptor program.

The encryption and decryption of the file would be done via a master password.
This master password will not be stored anywhere and would be asked every time.

# Security limitation

If an attacker has access to your file, they can run brute-force attacks, but if you have a strong enough passwords, it would take them years to decrypt it.
This program just adds a layer of security, please note that no software is fool-proof.