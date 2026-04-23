from flask import request, jsonify
from usecases.livro_usecase import LivroUseCase
from infrastructure.livro_repository_txt import LivroRepositoryTXT

repo = LivroRepositoryTXT()
usecase = LivroUseCase(repo)

def get_livros():
    query = request.args.get("q")
    preco_min = request.args.get("preco_min")

    livros = usecase.listar_livros(query, preco_min)
    return jsonify([l.to_dict() for l in livros])


def get_livro(id):
    livro = usecase.buscar_por_id(id)

    if livro:
        return jsonify(livro.to_dict())
    return jsonify({"erro": "Livro não encontrado"}), 404