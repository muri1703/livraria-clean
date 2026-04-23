class Livro:
    def __init__(self, id, titulo, autor, preco, genero, imagem):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.genero = genero
        self.imagem = imagem

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "preco": self.preco,
            "genero": self.genero,
            "imagem": self.imagem
        }