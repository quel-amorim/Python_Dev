import secrets
import string

def gerar_senha_simples(tamanho=12):
    # Combina todos os tipos de caracteres
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Gera a senha escolhendo caracteres aleatórios
    senha = ''.join(secrets.choice(caracteres) for i in range(tamanho))
    
    return senha

# Testa o gerador
senha_gerada = gerar_senha_simples()
print(f"Sua senha segura: {senha_gerada}")
