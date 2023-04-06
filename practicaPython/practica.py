from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
# ----- FUNCIONES-----
def conexion_bbdd():
    conexion=sqlite3.connect("MetaDat")
    cursor=conexion.cursor()
    try:
        cursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50),
            APELLIDO VARCHAR(50),
            USER_GITHUB VARCHAR(50),
            EMAIL VARCHAR(50),
            RUTA VARCHAR(50))
            ''')
        
        messagebox.showinfo("Base de Datos", "La base de datos ha sido creada con exito")
    except:
        messagebox.showwarning("¡Atención!", "LA base de datos ya existe")

def salir_app():
    valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
    if valor == "yes":
        root.destroy()

def limpiar_campos():
    id.set("")
    nombre.set("")
    apellido.set("")
    github.set("")
    email.set("")
    ruta.set("")

def crear():
    conexion=sqlite3.connect("MetaDat")
    cursor=conexion.cursor()

    cursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,'" + nombre.get() +
                   "','" + apellido.get() + 
                   "','" + github.get() +
                   "','" + email.get() +
                   "','" + ruta.get() + "')")
    
    conexion.commit()
    messagebox.showinfo("Base de Datos", "Se ha agregado registro")
    
def leer():
    conexion=sqlite3.connect("MetaDat")
    cursor=conexion.cursor()

    cursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + id.get())

    usuario=cursor.fetchall()

    for dato in usuario:

        id.set(usuario[0])
        nombre.set(usuario[1])
        apellido.set(usuario[2])
        github.set(usuario[3])
        email.set(usuario[4])
        ruta.set(usuario[5])

    print(usuario)
    conexion.commit()

def actualizar():
    conexion=sqlite3.connect("MetaDat")
    cursor=conexion.cursor()

    cursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE='" + nombre.get() +
                   "', APELLIDO='" + apellido.get() + 
                   "', USER_GIRHUB='" + github.get() +
                   "', EMAIL='" + email.get() +
                   "', RUTA='" + ruta.get() + 
                   "' WHERE ID=" + id.get())
    
    conexion.commit()
    messagebox.showinfo("Base de Datos", "Se ha agregado registro")

# ------ INTERFAZ -----
root = Tk()
# ------ > BARRA DE MENUS ------
barra_menu=Menu(root)
root.config(menu=barra_menu, width=300, height=300)

bbdd_menu=Menu(barra_menu, tearoff=0)
bbdd_menu.add_command(label="Conectar", command=conexion_bbdd)
bbdd_menu.add_command(label="Salir", command=salir_app)

crud_menu=Menu(barra_menu, tearoff=0)
crud_menu.add_command(label="Crear", command=crear)
crud_menu.add_command(label="Leer", command=leer)
crud_menu.add_command(label="Actualizar", command=actualizar)
crud_menu.add_command(label="Limpiar Campos", command=limpiar_campos)
crud_menu.add_command(label="Borrar registro")

ayuda_menu=Menu(barra_menu, tearoff=0)
ayuda_menu.add_command(label="Licencias")
ayuda_menu.add_command(label="Acerca de ...")

barra_menu.add_cascade(label="BBDD", menu=bbdd_menu)
barra_menu.add_cascade(label="CRUD", menu=crud_menu)
barra_menu.add_cascade(label="AYUDA", menu=ayuda_menu)

# -------> ENTRADA DE DATOS
## ---- PRIMER FRAME
frm00 = Frame(root)
frm00.grid()
ttk.Label(frm00, text="DATOS DE USUARIO").grid(column=0, row=0, padx=10, pady=10)
## ---- SEGUNDO FRAME
frm01 = Frame(root, padx=10, pady=10)
frm01.grid()

id=StringVar()
nombre=StringVar()
apellido=StringVar()
github=StringVar()
email=StringVar()
ruta=StringVar()

Label(frm01, text="ID").grid(column=0, row=0, sticky= "e", padx=10, pady=10)
entrada_id=Entry(frm01, textvariable=id).grid(column=1, row=0, padx=10, pady=10)

Label(frm01, text="Nombres:").grid(column=0, row=1, sticky= "e", padx=10, pady=10)
entrada_nombre=Entry(frm01, textvariable=nombre).grid(column=1, row=1, padx=10, pady=10)

Label(frm01, text="Apellidos").grid(column=0, row=2, sticky= "e", padx=10, pady=10)
entrada_apellidos=Entry(frm01, textvariable=apellido).grid(column=1, row=2, padx=10, pady=10)

Label(frm01, text="User GitHub").grid(column=0, row=3, sticky= "e", padx=10, pady=10)
entrada_github=Entry(frm01, textvariable=github).grid(column=1, row=3, padx=10, pady=10)

Label(frm01, text="Email").grid(column=0, row=4, sticky= "e", padx=10, pady=10)
entrada_email=Entry(frm01, textvariable=email).grid(column=1, row=4, padx=10, pady=10)

Label(frm01, text="Ruta").grid(column=0, row=5, sticky= "e", padx=10, pady=10)
entrada_ruta=Entry(frm01, textvariable=ruta).grid(column=1, row=5, padx=10, pady=10)

## ----- TERCER FRAME
frm02 = Frame(root)
frm02.grid()

Label(frm02, text="ESPERANDO INSTRUCCIÓN ...").grid(column=0, row=0, padx=10, pady=10)
Button(frm02, text="Registar", command=crear).grid(column=0, row=1, sticky= "e", padx=10, pady=10)
Button(frm02, text="Buscar", command=leer).grid(column=1, row=1, sticky= "e", padx=10, pady=10)
Button(frm02, text="Actualizar", command=actualizar).grid(column=2, row=1, sticky= "e", padx=10, pady=10)
Button(frm02, text="Eliminar", command=root.destroy).grid(column=3, row=1, sticky= "e", padx=10, pady=10)

root.mainloop()
