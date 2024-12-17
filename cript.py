#!/usr/bin/env python3
import os
import argparse
from hashlib import sha256
from Crypto.Cipher import AES, DES3, Blowfish
from Crypto.Util.Padding import pad, unpad

# Constantes para tamanho do bloco (em bytes)
BLOCK_SIZE = 16  # Tamanho do bloco para AES
DES3_BLOCK_SIZE = 8  # Tamanho do bloco para DES3

def encrypt_file(file_path, algorithm, password):
    with open(file_path, 'rb') as f:
        file_data = f.read()

    key = sha256(password.encode()).digest()

    # Ajusta o tamanho do IV dependendo do algoritmo
    if algorithm == 'AES':
        iv = os.urandom(BLOCK_SIZE)
        cipher = AES.new(key, AES.MODE_CBC, iv)
    elif algorithm == 'DES3':
        iv = os.urandom(DES3_BLOCK_SIZE)
        cipher = DES3.new(key[:24], DES3.MODE_CBC, iv)
    elif algorithm == 'Blowfish':
        iv = os.urandom(Blowfish.block_size)
        cipher = Blowfish.new(key[:16], Blowfish.MODE_CBC, iv)
    else:
        print("Algoritmo inválido.")
        return

    # Criptografa o arquivo com padding
    encrypted_data = iv + cipher.encrypt(pad(file_data, cipher.block_size))

    # Sobrescreve o arquivo original com o conteúdo criptografado
    with open(file_path, 'wb') as f:
        f.write(encrypted_data)

    print(f"Criptografia concluída no arquivo original: {file_path}")

def decrypt_file(file_path, algorithm, password):
    with open(file_path, 'rb') as f:
        ciphertext = f.read()

    key = sha256(password.encode()).digest()

    # Ajuste do tamanho do IV dependendo do algoritmo
    if algorithm == 'AES':
        iv_size = BLOCK_SIZE  # 16 bytes para AES
    elif algorithm == 'DES3':
        iv_size = DES3_BLOCK_SIZE  # 8 bytes para DES3
    elif algorithm == 'Blowfish':
        iv_size = Blowfish.block_size  # 8 bytes para Blowfish
    else:
        print("Algoritmo inválido.")
        return

    iv = ciphertext[:iv_size]
    data = ciphertext[iv_size:]

    # Cria o cipher com o IV correto
    if algorithm == 'AES':
        cipher = AES.new(key, AES.MODE_CBC, iv)
    elif algorithm == 'DES3':
        cipher = DES3.new(key[:24], DES3.MODE_CBC, iv)
    elif algorithm == 'Blowfish':
        cipher = Blowfish.new(key[:16], Blowfish.MODE_CBC, iv)

    # Descriptografa os dados e remove o padding
    plaintext = unpad(cipher.decrypt(data), cipher.block_size)

    # Sobrescreve o arquivo original com o conteúdo descriptografado
    with open(file_path, 'wb') as f:
        f.write(plaintext)

    print(f"Descriptografia concluída no arquivo original: {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Criptografia e Descriptografia de Arquivos")
    parser.add_argument('-f', '--file', required=True, help="Caminho do arquivo para criptografar ou descriptografar")
    parser.add_argument('-m', '--mode', required=True, choices=['encrypt', 'decrypt'], help="Modo: criptografar ou descriptografar")
    parser.add_argument('-a', '--algorithm', required=True, choices=['AES', 'DES3', 'Blowfish'], help="Algoritmo de criptografia")
    parser.add_argument('-p', '--password', required=True, help="Senha para criptografia/descriptografia")

    args = parser.parse_args()

    # Escolhe o modo de operação
    if args.mode == 'encrypt':
        encrypt_file(args.file, args.algorithm, args.password)
    elif args.mode == 'decrypt':
        decrypt_file(args.file, args.algorithm, args.password)

if __name__ == "__main__":
    main()
