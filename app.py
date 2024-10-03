from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_felix = Restaurante('Felix', '5 estrelas')
vitamina_de_goiaba = Bebida("Vitamina de goiaba", 15, "medio")
prato_feito = Prato("feijoada", 25, "Feijoada completa")

restaurante_felix.adicionar_no_cardapio(vitamina_de_goiaba)
restaurante_felix.adicionar_no_cardapio(prato_feito)

restaurante_felix.receber_avaliacao("Rodrigo", 7)
restaurante_felix.receber_avaliacao("Fernando", 10)
restaurante_felix.receber_avaliacao("Ana", 6)

def main():
    restaurante_felix.alternar_estado()
    Restaurante.listar_restaurantes()
    restaurante_felix.listar_cardapio()
    
if __name__ == '__main__':
    main()
    
    
