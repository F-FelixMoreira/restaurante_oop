from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome:str, categoria:str):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls) -> None:
        print(f"\n---| Restaurantes cadastrados:\n")
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')

    @property
    def ativo(self) -> None:
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self) -> None:
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente: str, nota: int) -> None:
        if 0 < nota <= 10: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self) -> int:
        if not self._avaliacoes:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_de_notas = len(self._avaliacoes)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    def adicionar_no_cardapio(self, item: ItemCardapio) -> None:
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
        else:
            raise ValueError('Item precisa ser do tipo ItemCardapio')

    def listar_cardapio(self) -> None:
        print(f'\n--- | Cardápio do restaurante {self._nome}:\n')
        for i, item in enumerate(self._cardapio, start=1):
            print(f'{i} | Item: {item._nome} | Preço: R${item._preco}')
        
