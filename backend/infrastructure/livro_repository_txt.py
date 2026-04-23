import json
from interfaces.livro_repository_interface import LivroRepositoryInterface
from domain.livro import Livro

class LivroRepositoryTXT(LivroRepositoryInterface):

    def __init__(self, file_path="data/livros.txt"):
        self.file_path = file_path

    def _load_data(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []

    def get_all(self):
        data = self._load_data()
        return [Livro(**l) for l in data]

    def get_by_id(self, id):
        data = self._load_data()
        for l in data:
            if l["id"] == id:
                return Livro(**l)
        return None