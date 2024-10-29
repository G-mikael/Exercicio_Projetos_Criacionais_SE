from classes import HumanoFactory, ElfoFactory, OrcFactory, AnaoFactory, Guerreiro, Mago, Ladino, Anao
def main():
    """
    Função principal para criação de heróis de acordo com as escolhas do usuário.

    Solicita ao usuário a escolha de nome, raça e classe, e exibe os atributos
    e habilidades do herói criado.
    """
    # Definindo Raças e Classes Disponíveis
    racas = {"humano": HumanoFactory(), "elfo": ElfoFactory(), "orc": OrcFactory(), "anao": AnaoFactory()}
    classes = {"guerreiro": Guerreiro, "mago": Mago, "ladino": Ladino}
    # Entrada do Usuário
    nome = input("Nome do herói: ")
    raca_input = input("Escolha a raça (humano, elfo, orc, anao): ").lower()
    classe_input = input("Escolha a classe (guerreiro, mago, ladino): ").lower()

    # Criação do Herói
    try:
        fabrica_raca = racas[raca_input]
        classe_escolhida = classes[classe_input]()
        heroi = fabrica_raca.criar_heroi(nome, classe_escolhida)

        # Exibindo Atributos e Habilidades
        print(f"Herói criado: {nome}")
        print(f"Atributos: Força = {heroi.forca}, Inteligência = {heroi.inteligencia}, Destreza = {heroi.destreza}")
        print(f"Habilidades: {heroi.apresentar_habilidades()}")

    except KeyError:
        print("Raça ou Classe inválida. Tente novamente.")

if __name__ == "__main__":
    main()
