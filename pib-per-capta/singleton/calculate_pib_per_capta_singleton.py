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


class AbstractCalculatePib(ABC):
    @abstractclassmethod
    def get_instance():
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

    def load_file(self):
        print("Inicio do script de PIB x Percapta")
        self.raw_data = pd.ExcelFile(Config._base_file)
        return self.raw_data

    def load_uf_by_region(self):
        self.current_content = pd.read_excel(self.raw_data, Config._region )
        return self.current_content

    def print_all_content(self):
        print(self.current_content)