import pandas as pd

# Passos para refatorar
# 1. Verificar métodos com nomes significativos
# 2. Padronizar nomes de métodos com o snake_pattern
# 3. Remover código hard-coded
# 4. Padronizar nomes de atributos e constantes
# 5. Padronizar a estrutura do código em formatação de tabelas (com espaços)
# 6. Padronizar e organizar blocos de código com responsabilidade semelhante

class Config:
    _base_file = "data/base.xlsx"
    _region    = "UF_Regiao"

class CalculatePibPerCaptaSingleton:
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

def main():
    calculate1 = CalculatePibPerCaptaSingleton.get_instance()
    calculate2 = CalculatePibPerCaptaSingleton.get_instance()
    
    print(calculate1)
    print(calculate2)
    
    calculate2.load_file()
    calculate2.load_uf_by_region()
    calculate2.print_all_content()
    

main()