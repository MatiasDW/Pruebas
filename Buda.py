import hashlib

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# Reemplaza 'TU_TEXTO_AQUI' con el string que quieres verificar
text_to_check = 'cZZetplyyV'
hash_result = sha256_hash(text_to_check)

print(f"Texto: {text_to_check}")
print(f"Hash SHA256: {hash_result}")
