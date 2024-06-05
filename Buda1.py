import hashlib

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# Reemplaza 'TU_TEXTO_AQUI' con el string que quieres verificar
text_to_check = 'cZZetplyyV'
hash_result = sha256_hash(text_to_check)

print(f"Texto: {text_to_check}")
print(f"Hash SHA256: {hash_result}")

# Verificar si el hash contiene 'b00da'
contains_b00da = 'b00da' in hash_result

print(f"¿Contiene 'b00da'? {contains_b00da}")
