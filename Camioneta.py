from Carro import Carro


class Camioneta(Carro):
    platon = None
    valvula_platon = False

    def __init__(self, brand=None, serie=None, model=None, color=None, platon=None):
        super(Camioneta, self).__init__(brand, serie, model, color)
        self.platon = platon

    def toggle_valvula_platon(self):
        self.valvula_platon = not self.valvula_platon  # carga el vavor n lavariable y lo niega y se llam y vuelve y change
        self.view_valvula_platon()

    def view_valvula_platon(self):

        if self.valvula_platon:
            print("Platon: arriba")
        else:
            print("Platon: apagado")
