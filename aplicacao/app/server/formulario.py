from server.database import getconection

class Formulario():

    def findFormularios():

        formularios_collectio = getconection().find()
        formularios = []
        for formulario in formularios_collectio:
            formularios.append(formulario)
        return formularios