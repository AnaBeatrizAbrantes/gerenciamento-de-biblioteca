biblioteca = {
    "livros": [],   
    "usuarios": [],
    "emprestimos": []
}


def cadastrar_livro(titulo, autor, ano, genero):
    """Cadastra um novo livro na biblioteca."""
    livro = {
        "id": len(biblioteca["livros"]) + 1,
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "genero": genero,
        "disponivel": True
    }
    biblioteca["livros"].append(livro)
    return livro


def listar_livros():
    """Retorna todos os livros cadastrados."""
    return biblioteca["livros"]


def buscar_livro_por_titulo(titulo):
    """Busca livros que contenham o termo no título."""
    resultado = [l for l in biblioteca["livros"] if titulo.lower() in l["titulo"].lower()]
    return resultado


def atualizar_livro(id_livro, novo_titulo=None, novo_autor=None, novo_ano=None, novo_genero=None):
    """Atualiza os dados de um livro existente."""
    for livro in biblioteca["livros"]:
        if livro["id"] == id_livro:
            if novo_titulo:
                livro["titulo"] = novo_titulo
            if novo_autor:
                livro["autor"] = novo_autor
            if novo_ano:
                livro["ano"] = novo_ano
            if novo_genero:
                livro["genero"] = novo_genero
            return livro
    return None


def remover_livro(id_livro):
    """Remove um livro da lista."""
    for livro in biblioteca["livros"]:
        if livro["id"] == id_livro:
            biblioteca["livros"].remove(livro)
            return True
    return False


def cadastrar_usuario(nome, email):
    """Cadastra um novo usuário."""
    usuario = {
        "id": len(biblioteca["usuarios"]) + 1,
        "nome": nome,
        "email": email
    }
    biblioteca["usuarios"].append(usuario)
    return usuario


def listar_usuarios():
    """Lista todos os usuários cadastrados."""
    return biblioteca["usuarios"]


def emprestar_livro(id_livro, nome_usuario, dias):
    """Empresta um livro, registrando o nome e o prazo de devolução."""
    for livro in biblioteca["livros"]:
        if livro["id"] == id_livro:
            if not livro["disponivel"]:
                return "Livro já emprestado!"
            
            livro["disponivel"] = False
            emprestimo = {
                "livro_id": id_livro,
                "titulo": livro["titulo"],
                "usuario": nome_usuario,
                "dias": dias
            }
            biblioteca["emprestimos"].append(emprestimo)
            return f"Livro '{livro['titulo']}' emprestado para {nome_usuario} por {dias} dias."
    return "Livro não encontrado."


def listar_emprestimos():
    """Lista todos os livros atualmente emprestados."""
    if not biblioteca["emprestimos"]:
        return "Nenhum livro emprestado no momento."
    
    resultado = []
    for e in biblioteca["emprestimos"]:
        resultado.append(f"{e['titulo']} → {e['usuario']} ({e['dias']} dias)")
    return resultado


def devolver_livro(id_livro):
    """Devolve um livro emprestado e remove o registro do empréstimo."""
    for livro in biblioteca["livros"]:
        if livro["id"] == id_livro:
            if livro["disponivel"]:
                return "Este livro já está disponível."
            
            livro["disponivel"] = True
            biblioteca["emprestimos"] = [e for e in biblioteca["emprestimos"] if e["livro_id"] != id_livro]
            return f"Livro '{livro['titulo']}' devolvido com sucesso!"
    return "Livro não encontrado."


def testes():
    print(" SISTEMA DE BIBLIOTECA (com empréstimos) ")

    cadastrar_livro("Dom Casmurro", "Machado de Assis", 1899, "Romance")
    cadastrar_livro("O Hobbit", "J.R.R. Tolkien", 1937, "Fantasia")

    print("\n Livros cadastrados:")
    for l in listar_livros():
        print(f"→ {l['id']} - {l['titulo']} ({l['autor']})")

    print("\n Emprestando livro ID 1 para Maria por 7 dias...")
    print(emprestar_livro(1, "Maria", 7))

    print("\n Lista de empréstimos:")
    for e in listar_emprestimos():
        print(f"→ {e}")

    print("\n Devolvendo livro ID 1...")
    print(devolver_livro(1))

    print("\n Lista de empréstimos após devolução:")
    print(listar_emprestimos())

    print("\n Testes finalizados!")

if __name__ == "__main__":
    testes()
