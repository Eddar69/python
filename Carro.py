class Carro:
    """Clase para crear un carro"""

    brand = None
    serie = None
    model = None
    color = None
    engine_status = False

    def __init__(self, brand=None, serie=None, model=None, color=None):
        self.brand = brand
        self.serie = serie
        self.model = model
        self.color = color

    def get_details(self):
        print("""
Marca: \"{}\", 
Serie: {}, 
Modelo: {}, 
Color: {}
        """.format(str(self.brand), str(self.serie), str(self.model), str(self.color)))

    def toggle_engine(self):

        self.engine_status = not self.engine_status
        self.view_status_engine()

    def view_status_engine(self):

        if self.engine_status:
            print("Motor: encendido")
        else:
            print("Motor: Apagado")
