# 🔒 Criptografia e Descriptografia de Arquivos

Este projeto permite criptografar e descriptografar arquivos usando os algoritmos **AES**, **DES3** e **Blowfish**.

⚠️ **Atenção**: Use este programa com responsabilidade. Faça backup de seus arquivos antes de criptografá-los, e guarde as senhas com segurança.

---

## 📦 **Requisitos**

Instale as dependências com o comando:
```bash

🚀 Como Usar
Clone o repositório:
git clone https://github.com/12rkk/cript.git
cd cript

pip install -r requirements.txt

1. Criptografar um Arquivo
Execute o seguinte comando:
python cript.py -f <caminho/do/arquivo> -m encrypt -a <algoritmo> -p <senha>

2. Descriptografar um Arquivo
Execute o seguinte comandoo:
python cript.py -f <caminho/do/arquivo> -m decrypt -a <algoritmo> -p <senha>

Exemplo:
python cript.py -f arquivo.txt -m decrypt -a AES -p minhaSenha123

🔹 Exemplos
Criptografando com AES:
python cript.py -f exemplo.txt -m encrypt -a AES -p senhaSegura

Descriptografando com AES:
python cript.py -f exemplo.txt -m decrypt -a AES -p senhaSegura
