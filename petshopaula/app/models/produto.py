from app.models.produto import produto

class Produto:
    def _init_(self, nome, categoria, marca, preco, quantidade, fornecedor):
        self.nome = nome
        self.categoria = categoria
        self.marca = marca
        self.preco = preco
        self.quantidade = quantidade       
        self.fornecedor = fornecedor

produto = Produto("Ração Premium", "Ração", "PetNutri" , 89.90, 20, "Distribuidora Pet")

print(f"Produto: ")