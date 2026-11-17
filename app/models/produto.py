from dataclasses import asdict, dataclass
from typing import Optional


@dataclass
class Produto:
    nome: str
    categoria: str
    marca: str
    preco: float
    quantidade: int
    fornecedor: str
    id: Optional[int] = None

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            nome=data["nome"],
            categoria=data["categoria"],
            marca=data["marca"],
            preco=data["preco"],
            quantidade=data["quantidade"],
            fornecedor=data["fornecedor"],
        )