import hashlib

def criptografar(senha):
    # Cria um objeto de hash usando o algoritmo SHA-256
    hash_object = hashlib.sha256()
    # Codifica a senha em bytes antes de passá-la para a função hash
    senha_codificada = senha.encode('utf-8')
    # Atualiza o objeto de hash com a senha codificada
    hash_object.update(senha_codificada)
    # Obtém a representação hexadecimal do valor de hash
    senha_criptografada = hash_object.hexdigest()
    # Retorna a senha criptografada
    return senha_criptografada
