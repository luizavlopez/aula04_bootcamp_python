# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. 
# Imprima cada informação.

livros: dict = {
    "livro_01": {
        "título": "Cem Anos de Solidão",
        "autor": "Gabriel García Márquez",
        "ano": "1967"},
    
    "livro_02": {
        "título": "1984",
        "autor": "George Orwell",
        "ano": "1949"},
    
    "livro_03": {
        "título": "Dom Casmurro",
        "autor": "Machado de Assis",
        "ano": "1899"}
    }

for chave, dados in livros.items():
    print(f"Título: {dados['título']}")
    print(f"Autor: {dados['autor']}")
    print(f"Ano: {dados['ano']}")
    print()

# livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
# for chave, valor in livro.items():
#     print(f"{chave}: {valor}")