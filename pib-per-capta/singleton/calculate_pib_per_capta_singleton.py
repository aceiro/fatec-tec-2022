import pandas as pd
from abc import ABC, abstractclassmethod

# QUIZ - 
# Qual classe é a Abstração e qual é a implementação ?
# R: Abstração --> AbstractCalculatePib Implementação --> CalculatePibPerCaptaSingleton

# Para casa:
# 1) Implementar a abstração completa CalculatePibPerCaptaSingleton
# 2) Fazer o diagrama UML do PIB Per Capta
class Config:
    _base_file = "data/base.xlsx"
    _region    = "UF_Regiao"


# Uma Classe Abstrata representa um contrato com regras
# cada regra em um código é uma função ou método que 
# contém as assinaturas.
# 
# Uma assinatura é a definição de um método, com parâmetros,
# tipos e retorno.
# 
# No exemplo abaixo AbstractCalculatePib, responda:
# 1) Quantos contratos temos ? 
# R: 1

# 2) Quantas regras temos ? 
# R: 4

# 3) Quantas assinaturas temos ? 
# R: 4

# 4) Como podemos violar o contrato da AbstractCalculatePib ?
# R: Não implementando a classe AbstractCalculatePib ou não implementando
#    ao menos um método (regra) da classe

class AbstractCalculatePib(ABC):
    @abstractclassmethod
    def get_instance():
        raise RuntimeError('TODO: Método ainda não implementado')

    @abstractclassmethod
    def load_file(self):
        raise RuntimeError('TODO: Método ainda não implementado')
    
    @abstractclassmethod
    def load_uf_by_region(self):
        raise RuntimeError('TODO: Método ainda não implementado')

    @abstractclassmethod
    def print_all_content(self):
        raise RuntimeError('TODO: Método ainda não implementado')
    
class CalculatePibPerCaptaSingleton(AbstractCalculatePib):
    # atributos da classe 
    _instance = None
    raw_data  = None
    current_content = None


    # Métodos

    # Construtor da classe
    def __init__(self):
        # Estamos lançando uma exception em 
        # tempo de execução
        raise RuntimeError('Singleton!!')

    @classmethod
    def get_instance(cls):
        # 1 - Criar um Singleton para o projeto pib-per-capta
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            return cls._instance
        else:
            return cls._instance

    @classmethod
    def load_file(self):
        print("Inicio do script de PIB x Percapta")
        self.raw_data = pd.ExcelFile(Config._base_file)
        return self.raw_data

    @classmethod
    def load_uf_by_region(self):
        self.current_content = pd.read_excel(self.raw_data, Config._region )
        return self.current_content

    @classmethod
    def print_all_content(self):
        print(self.current_content)