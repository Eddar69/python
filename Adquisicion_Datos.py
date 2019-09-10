from Camioneta import Camioneta
from Carro import Carro
from Tractomula import Tractomula

if __name__ == '__main__':

    miCarro = Carro(brand="Audi", serie="A4", model=2019, color="Rojo")  # miCarro es una variable tipo objeto que pertenece a la classe carro  eso es instanciar

    miCamioneta = Camioneta(platon="Largo", brand="Volvo", serie="X", model="2019", color="Amarillo")

    miTractomula = Tractomula(cabezote="Largo", brand="Volvo", serie="X", model="2010", color="Morado")

    print(miTractomula.get_details())
    miTractomula.toggle_all()