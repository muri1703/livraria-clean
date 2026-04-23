class LivroUseCase:

    def __init__(self, repository):
        self.repository = repository

    def listar_livros(self, query=None, preco_min=None):
        livros = self.repository.get_all()

        if query:
            query = query.lower()
            livros = [
                l for l in livros
                if query in l.titulo.lower()
                or query in l.autor.lower()
                or query in l.genero.lower()
            ]

        if preco_min:
            livros = [l for l in livros if l.preco >= float(preco_min)]

        return livros

    def buscar_por_id(self, id):
        return self.repository.get_by_id(id)