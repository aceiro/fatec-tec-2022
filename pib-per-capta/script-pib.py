import pandas as pd

class CalculatePibPerCapta:
    _instance = None
    _BASE_FILE = "data/base.xlsx"
    raw_data = None
    current_content = None

    def instance(self):
        # 1 - Criar uma instancia unica
        # use o Design Pattern Singleton
        # sugestao de implementacao
        # https://python-patterns.guide/gang-of-four/singleton/
        # https://github.com/Sean-Bradley/Design-Patterns-In-Python/tree/master/singleton
        print(None)

    def load_file(self):
        print("Inicio do script de PIB x Percapta")
        self.raw_data = pd.ExcelFile(self._BASE_FILE)
        return self.raw_data

    def load_uf_by_region(self):
        self.current_content = pd.read_excel(self.raw_data, "UF_Regiao")
        return self.current_content

    def print_all_content(self):
        print(self.current_content)

def main():
    calculate1 = CalculatePibPerCapta()
    print(calculate1)
    calculate2 = CalculatePibPerCapta()
    print(calculate2)
    calculate2.load_file()
    calculate2.load_uf_by_region()
    calculate2.print_all_content()
    

main()