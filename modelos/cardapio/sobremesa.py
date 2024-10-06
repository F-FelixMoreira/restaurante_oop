from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):

    def __init__(self, nome: str, preco: str, tipo: str, tamanho: float, descricao: str):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho
        self._descricao = descricao

    def __str__(self) -> str:
        return self._nome

    def aplicar_desconto(self) -> None:
        pass