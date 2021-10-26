from config import *

# Declaração do objeto carro e seus atributos
class Carro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(254))
    modelo = db.Column(db.String(254))
    ano = db.Column(db.String(254))

    def __str__(self):
        return str(self.id) + ", " + self.marca + ", " +\
            self.modelo + ", " + self.ano

    # Retornar dados da classe em formato json
    def json(self):
        return {
            "id": self.id,
            "marca": self.marca,
            "modelo": self.modelo,
            "ano": self.ano
        }

# Testando
if __name__ == "__main__":
    # Remover o arquivo
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar BD
    db.create_all()

    # Instanciar objeto Carro
    carro = Carro(marca = "Renault", modelo = "Sandero", ano = "2015")
    carro2 = Carro(marca = "Peugeot", modelo = "208", ano = "2006")
    carro3 = Carro(marca = "Renault", modelo = "Captur", ano = "2019")
    carro4 = Carro(marca = "Volkswagen", modelo = "UP", ano = "2020")

    # Adicionar e persistir no banco
    db.session.add(carro)
    db.session.add(carro2)
    db.session.add(carro3)
    db.session.add(carro4)
    db.session.commit()

    print('--- Teste STR --- ')
    print(carro)
    print(carro2)
    print('--- Teste JSON --- ')
    print(carro.json())
    print(carro2.json())