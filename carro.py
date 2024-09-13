class Plantas:
    plantas = []  

    def __init__(self, nome, nome_cientifico, genero, grupo):
        self.nome = nome
        self.nome_cientifico = nome_cientifico
        self.genero = genero
        self.grupo = grupo
        self.extinta = False
        Plantas.plantas.append(self)  

    def __str__(self):
        return (f"Nome: {self.nome} | {self.nome_cientifico} "
                f"Gênero: {self.genero}, Grupo: {self.grupo}, Extinta: {self.extinta}")

    @classmethod
    def listar_plantas(cls):  
        for planta in cls.plantas:
            print(f'{planta.nome} | {planta.nome_cientifico} | '
                  f'{planta.genero} | {planta.grupo} | {planta.extinta}') 


planta_Goiaba = Plantas("Goiaba", "Psidium guajava", "Psidium", "Angiosperma")
planta_Acerola = Plantas("Acerola", "Malpighia emarginata", "Malpighia", "Angiosperma")
planta_Pitaia = Plantas("Pitaia", "Hylocereus spp.", "Hylocereus", "Cactácea")


print(planta_Acerola)
print(planta_Goiaba)


Plantas.listar_plantas()
