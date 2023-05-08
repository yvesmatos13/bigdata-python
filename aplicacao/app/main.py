from server.formulario import Formulario

def main():
    formularios = Formulario.findFormularios()
    print(formularios)

main()