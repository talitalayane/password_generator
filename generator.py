import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    """Gera uma senha aleatória com base nos parâmetros fornecidos.

    Args:
        length (int): Comprimento da senha gerada.
        use_uppercase (bool): Incluir letras maiúsculas.
        use_digits (bool): Incluir dígitos.
        use_special_chars (bool): Incluir caracteres especiais.

    Returns:
        str: Senha gerada.
    """
    # Conjunto básico de caracteres
    characters = string.ascii_lowercase  # Letras minúsculas

    # Adiciona maiúsculas, dígitos e caracteres especiais conforme a configuração
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    # Gera a senha
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    length = int(input("Comprimento da senha: "))
    use_uppercase = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == 's'
    use_digits = input("Incluir dígitos? (s/n): ").strip().lower() == 's'
    use_special_chars = input("Incluir caracteres especiais? (s/n): ").strip().lower() == 's'

    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    print(f"Senha gerada: {password}")

# def main():
#     # Configurações padrão
#     length = 12
#     use_uppercase = True
#     use_digits = True
#     use_special_chars = True

#     # Exemplo de geração de senha
#     password = generate_password(length, use_uppercase, use_digits, use_special_chars)
#     print(f"Senha gerada: {password}")

if __name__ == "__main__":
    main()
