from Camioneta import Camioneta


class Tractomula(Camioneta):
    cabezote = None
    trailer = True

    def __init__(self, cabezote=None, brand=None, serie=None, model=None, color=None):
        super(Tractomula, self).__init__(brand, serie, model, color)
        self.cabezote = cabezote

    def toggle_trailer(self):
        self.trailer = not self.trailer
        self.view_trailer()

    def view_trailer(self):

        if self.trailer:
            print("trailer: conectado")
        else:
            print("trailer: desconectado")

    def toggle_all(self):
        self.toggle_engine()
        self.toggle_valvula_platon()
        self.toggle_trailer()


