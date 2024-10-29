from abc import ABC, abstractmethod

# Classe Abstrata Heroi
class Heroi(ABC):
    """
    Classe abstrata que define a estrutura básica para heróis.

    Atributos:
        nome (str): Nome do herói.
        forca (int): Atributo de força do herói.
        inteligencia (int): Atributo de inteligência do herói.
        destreza (int): Atributo de destreza do herói.
    """

    def __init__(self, nome, forca, inteligencia, destreza):
        self.nome = nome
        self.forca = forca
        self.inteligencia = inteligencia
        self.destreza = destreza

    @abstractmethod
    def apresentar_habilidades(self):
        """
        Método abstrato para apresentar as habilidades do herói.
        
        Deve ser implementado nas subclasses concretas.
        """
        pass

# Classes de Classe Concretas
class Guerreiro:
    """
    Classe que representa a classe Guerreiro de um herói.

    Modificadores de atributos:
        forca (int): Modificador de força para a classe.
        inteligencia (int): Modificador de inteligência para a classe.
        destreza (int): Modificador de destreza para a classe.
    """

    def __init__(self):
        # Definindo modificadores específicos para a classe Guerreiro
        self.forca = 5
        self.inteligencia = -2
        self.destreza = 3

    def apresentar_habilidades(self, nome):
        """
        Retorna uma descrição das habilidades específicas do Guerreiro.

        Args:
            nome (str): Nome do herói.

        Returns:
            str: Descrição das habilidades do Guerreiro.
        """
        return f"{nome} usa habilidades de combate corpo a corpo e alta resistência."

class Mago:
    """
    Classe que representa a classe Mago de um herói.

    Modificadores de atributos:
        forca (int): Modificador de força para a classe.
        inteligencia (int): Modificador de inteligência para a classe.
        destreza (int): Modificador de destreza para a classe.
    """

    def __init__(self):
        self.forca = -2
        self.inteligencia = 5
        self.destreza = 1

    def apresentar_habilidades(self, nome):
        """
        Retorna uma descrição das habilidades específicas do Mago.

        Args:
            nome (str): Nome do herói.

        Returns:
            str: Descrição das habilidades do Mago.
        """
        return f"{nome} usa feitiços poderosos e alta inteligência."

class Ladino:
    """
    Classe que representa a classe Ladino de um herói.

    Modificadores de atributos:
        forca (int): Modificador de força para a classe.
        inteligencia (int): Modificador de inteligência para a classe.
        destreza (int): Modificador de destreza para a classe.
    """

    def __init__(self):
        self.forca = 1
        self.inteligencia = 2
        self.destreza = 5

    def apresentar_habilidades(self, nome):
        """
        Retorna uma descrição das habilidades específicas do Ladino.

        Args:
            nome (str): Nome do herói.

        Returns:
            str: Descrição das habilidades do Ladino.
        """
        return f"{nome} usa furtividade e habilidades de roubo."

# Classes Concretas para cada Raça
class Humano(Heroi):
    """
    Classe que representa a raça Humano de um herói, herda de Heroi.

    Modificadores de atributos base:
        forca (int): Atributo de força base do Humano.
        inteligencia (int): Atributo de inteligência base do Humano.
        destreza (int): Atributo de destreza base do Humano.
    """

    def __init__(self, nome, classe):
        """
        Inicializa um herói humano e aplica os modificadores de atributos da classe escolhida.

        Args:
            nome (str): Nome do herói.
            classe (Classe de Classe): Classe específica do herói (Guerreiro, Mago, ou Ladino).
        """
        # Atributos base da raça Humano
        forca_base = 10
        inteligencia_base = 10
        destreza_base = 10

        # Adiciona modificadores da classe
        self.classe = classe
        super().__init__(nome,
                         forca=forca_base + self.classe.forca,
                         inteligencia=inteligencia_base + self.classe.inteligencia,
                         destreza=destreza_base + self.classe.destreza)

    def apresentar_habilidades(self):
        """
        Retorna uma descrição das habilidades do herói humano, de acordo com sua classe.

        Returns:
            str: Descrição das habilidades do herói.
        """
        return f"Humano {self.classe.apresentar_habilidades(self.nome)}"

class Elfo(Heroi):
    """
    Classe que representa a raça Elfo de um herói, herda de Heroi.

    Modificadores de atributos base:
        forca (int): Atributo de força base do Elfo.
        inteligencia (int): Atributo de inteligência base do Elfo.
        destreza (int): Atributo de destreza base do Elfo.
    """

    def __init__(self, nome, classe):
        """
        Inicializa um herói elfo e aplica os modificadores de atributos da classe escolhida.

        Args:
            nome (str): Nome do herói.
            classe (Classe de Classe): Classe específica do herói (Guerreiro, Mago, ou Ladino).
        """
        forca_base = 7
        inteligencia_base = 12
        destreza_base = 11

        # Adiciona modificadores da classe
        self.classe = classe
        super().__init__(nome,
                         forca=forca_base + self.classe.forca,
                         inteligencia=inteligencia_base + self.classe.inteligencia,
                         destreza=destreza_base + self.classe.destreza)

    def apresentar_habilidades(self):
        """
        Retorna uma descrição das habilidades do herói elfo, de acordo com sua classe.

        Returns:
            str: Descrição das habilidades do herói.
        """
        return f"Elfo {self.classe.apresentar_habilidades(self.nome)}"

class Orc(Heroi):
    """
    Classe que representa a raça Orc de um herói, herda de Heroi.

    Modificadores de atributos base:
        forca (int): Atributo de força base do Orc.
        inteligencia (int): Atributo de inteligência base do Orc.
        destreza (int): Atributo de destreza base do Orc.
    """

    def __init__(self, nome, classe):
        """
        Inicializa um herói orc e aplica os modificadores de atributos da classe escolhida.

        Args:
            nome (str): Nome do herói.
            classe (Classe de Classe): Classe específica do herói (Guerreiro, Mago, ou Ladino).
        """
        forca_base = 12
        inteligencia_base = 6
        destreza_base = 9

        # Adiciona modificadores da classe
        self.classe = classe
        super().__init__(nome,
                         forca=forca_base + self.classe.forca,
                         inteligencia=inteligencia_base + self.classe.inteligencia,
                         destreza=destreza_base + self.classe.destreza)

    def apresentar_habilidades(self):
        """
        Retorna uma descrição das habilidades do herói orc, de acordo com sua classe.

        Returns:
            str: Descrição das habilidades do herói.
        """
        return f"Orc {self.classe.apresentar_habilidades(self.nome)}"

#A raça "Anão é a raça extra da atividade"    
class Anao(Heroi):
    """
    Classe que representa a raça Anão de um herói, herda de Heroi.

    Modificadores de atributos base:
        forca (int): Atributo de força base do Anão.
        inteligencia (int): Atributo de inteligência base do Anão.
        destreza (int): Atributo de destreza base do Anão.
    """

    def __init__(self, nome, classe):
        """
        Inicializa um herói anão e aplica os modificadores de atributos da classe escolhida.

        Args:
            nome (str): Nome do herói.
            classe (Classe de Classe): Classe específica do herói (Guerreiro, Mago, ou Ladino).
        """
        forca_base = 10
        inteligencia_base = 15
        destreza_base = -2

        # Adiciona modificadores da classe
        self.classe = classe
        super().__init__(nome,
                         forca=forca_base + self.classe.forca,
                         inteligencia=inteligencia_base + self.classe.inteligencia,
                         destreza=destreza_base + self.classe.destreza)

    def apresentar_habilidades(self):
        """
        Retorna uma descrição das habilidades do herói Anão, de acordo com sua classe.

        Returns:
            str: Descrição das habilidades do herói.
        """
        return f"Anão {self.classe.apresentar_habilidades(self.nome)}"

# Abstract Factory para criar Heroi
class HeroiFactory(ABC):
    """
    Classe abstrata de fábrica para criação de heróis.
    """

    @abstractmethod
    def criar_heroi(self, nome, classe):
        """
        Método abstrato para criar um herói com base na raça e classe escolhida.

        Args:
            nome (str): Nome do herói.
            classe (Classe de Classe): Classe específica do herói (Guerreiro, Mago, ou Ladino).

        Returns:
            Heroi: Instância de um herói com raça e classe específicos.
        """
        pass

class HumanoFactory(HeroiFactory):
    """Fábrica para criar heróis da raça Humano."""

    def criar_heroi(self, nome, classe):
        return Humano(nome, classe)

class ElfoFactory(HeroiFactory):
    """Fábrica para criar heróis da raça Elfo."""

    def criar_heroi(self, nome, classe):
        return Elfo(nome, classe)

class OrcFactory(HeroiFactory):
    """Fábrica para criar heróis da raça Orc."""

    def criar_heroi(self, nome, classe):
        return Orc(nome, classe)
    
class AnaoFactory(HeroiFactory):
    """Fábrica para criar heróis da raça Anão."""

    def criar_heroi(self, nome, classe):
        return Anao(nome, classe)

