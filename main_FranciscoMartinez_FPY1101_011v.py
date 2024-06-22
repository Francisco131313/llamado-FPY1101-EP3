import csv
Menu = ["Registrar libro","Prestar libro","Listar todos los libros","Imprimir reporte de préstamos", "Salir del Programa"]
def RegistarLibro(libros):
    libros = input("Ingrese titulo del libro")
    
    while libros.lower() not in libros:
        print("no pudimos encontar el autor, verifique e intente nuevamente.")
        Autor = input("ingrese el autor del libro:")

def Listalibros  (libros):
    for libro in libros:
        for dato in libro:
            print(dato, end="\t")
        print()

def imprimirPlantilla(libros):
    libroSeleccionado = input("escriba el libroque desea seleccionar".lower())
    if libroSeleccionado == "todos":
        with open (f"listadelibros"):
print ("Libro no valio. Intentenuevmente.")


