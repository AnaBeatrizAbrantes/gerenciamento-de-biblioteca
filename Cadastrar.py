livros = []

def cadastrar_livro(titulo, autor, ano):
    """Cadastra um novo livro."""
    livro = {"titulo": titulo, "autor": autor, "ano": ano}
    livros.append(livro)
    return livro

def listar_livros():
    """Retorna todos os livros cadastrados."""
    return livros

def buscar_livro(titulo):
    """Busca livros pelo título (parcial)."""
    resultado = [l for l in livros if titulo.lower() in l["titulo"].lower()]
    return resultado


def testar_biblioteca():
    print(" Testando Sistema de Biblioteca...")

    cadastrar_livro("Dom Casmurro", "Machado de Assis", 1899)
    cadastrar_livro("O Hobbit", "J.R.R. Tolkien", 1937)
    cadastrar_livro("1984", "George Orwell", 1949)

    print("\n Lista de livros cadastrados:")
    for l in listar_livros():
        print(f"- {l['titulo']} ({l['autor']}, {l['ano']})")

    termo_busca = "hobbit"
    print(f"\n Buscando por '{termo_busca}':")
    resultados = buscar_livro(termo_busca)
    if resultados:
        for r in resultados:
            print(f"→ {r['titulo']} - {r['autor']}")
    else:
        print("Nenhum livro encontrado.")

if __name__ == "__main__":
    testar_biblioteca()
