from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 2)

restaurante_felix = Restaurante('Felix', '5 estrelas')
restaurante_felix.receber_avaliacao('Felipe', 10)
restaurante_felix.receber_avaliacao('Pedro', 8)
restaurante_felix.receber_avaliacao('Moreira', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
    print(restaurante_felix)
    
