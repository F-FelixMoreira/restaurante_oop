from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida


restaurante_felix = Restaurante('Felix', '5 estrelas')
vitamina_de_goiaba = Bebida("Vitamina de goiaba", 15, "medio")
prato_feito = Prato("feijoada", 25, "Feijoada completa")

def main():
    Restaurante.listar_restaurantes()
    print(vitamina_de_goiaba)
    print(prato_feito)

if __name__ == '__main__':
    main()
    print(restaurante_felix)
    
