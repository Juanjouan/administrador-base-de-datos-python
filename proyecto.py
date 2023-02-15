import sqlite3
from tkinter import *
from tkinter import messagebox



#####       Funciones        #####
def conectar():
    try:
        miConexion=sqlite3.connect("Base_gestion")
        
        miCursor=miConexion.cursor()
        miCursor.execute('''
            CREATE TABLE DATOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(15),
            PASSWORD VARCHAR(20),
            APELLIDO VARCHAR(20),
            DIRECCION VARCHAR(20),
            COMENTARIOS VARCHAR(100)
            )
            ''')
        messagebox.showinfo("BBDD","se ha conectado con exito a la base de datos")
    except:
        messagebox.showwarning("ATENCION","la BBDD ya existe")

def salir():
    valor=messagebox.askquestion("salir","deseas salir de la aplicacion?")
    if valor=="yes":
        root.destroy()
        

def borrarCampos():
    miId.set("")
    miNombre.set("")
    miPassword.set("")
    miApellido.set("")
    miDireccion.set("")
    cuadroComentarios.delete(1.0, END)



def acerc():
    messagebox.showinfo("github: Juanjouan")


def crearCampo():

    miConexion=sqlite3.connect("Base_gestion")
    miCursor=miConexion.cursor()
    datos=miNombre.get(),miPassword.get(),miApellido.get(),miDireccion.get(),cuadroComentarios.get("1.0", END)
    """
    miCursor.execute("INSERT INTO DATOS VALUES(NULL,'" + miNombre.get()+
    "','" + miPassword.get() +
    "','" + miApellido.get() +
    "','" + miDireccion.get() +
    "','" + cuadroComentarios.get("1.0", END) + "')") """

    miCursor.execute("INSERT INTO DATOS VALUES(NULL,?,?,?,?,?", (datos) )

    miConexion.commit()

    messagebox.showinfo("BBDD","los datos fueron insertados con exito")
        


def leerCampo():
    miConexion=sqlite3.connect("Base_gestion")
    miCursor=miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOS WHERE ID=" + miId.get())
    elUsuario=miCursor.fetchall()
    for usuario in elUsuario:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miPassword.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        cuadroComentarios.insert(1.0, usuario[5])
        
    miConexion.commit()
    
def updateCampo():
    miConexion=sqlite3.connect("Base_gestion")
    miCursor=miConexion.cursor()

    datos=miNombre.get(),miPassword.get(),miApellido.get(),miDireccion.get(),cuadroComentarios.get("1.0", END)
    """ esta es la forma mas extensa y la siguiente es la mas simple pero hacen lo mismo
    miCursor.execute("UPDATE DATOS SET NOMBRE='" + miNombre.get() + 
    "', PASSWORD='" + miPassword.get() + 
    "', APELLIDO='" + miApellido.get() +
    "', DIRECCION='" + miDireccion.get() +
     "', COMENTARIOS='"+ cuadroComentarios.get("1.0", END) +
     "'WHERE ID=" + miId.get()) """

    miCursor.execute("UPDATE DATOS SET NOMBRE=?,PASSWORD=?,APELLIDO=?,DIRECCION=?,COMENTARIOS=?" +
    "WHERE ID=" + miId.get(), (datos) )

    miConexion.commit()
    messagebox.showinfo("BBDD","los datos fueron actualizados con exito")

def borrarCampo():
    miConexion=sqlite3.connect("Base_gestion")
    miCursor=miConexion.cursor()

    miCursor.execute("DELETE FROM DATOS WHERE ID=" + miId.get())

    miConexion.commit()
    
    messagebox.showinfo("BBDD","los datos fueron borrados con exito con exito")


#####       interfaz        #####
root=Tk()
root.title("sistema de gestion")
miFrame=Frame(root)
barraMenu=Menu(root)

root.config(menu=barraMenu,width=300,height=300)


bbddMenu=Menu(barraMenu,tearoff=0)
bbddMenu.add_command(label="conectar",command=lambda:conectar())
bbddMenu.add_command(label="salir",command=lambda:salir())

borrarMenu=Menu(barraMenu,tearoff=0)
borrarMenu.add_command(label="borrar",command=lambda:borrarCampos())


ayudaMenu=Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="acerca de ")

barraMenu.add_cascade(label="BBDD",menu=bbddMenu)

barraMenu.add_cascade(label="borrar",menu=borrarMenu)

barraMenu.add_cascade(label="ayuda",menu=ayudaMenu)

miId=StringVar()
miNombre=StringVar()
miPassword=StringVar()
miApellido=StringVar()
miDireccion=StringVar()

idcuadro=Entry(miFrame,textvariable=miId)
idcuadro.grid(row=1,column=1)

idLabel=Label(miFrame,text="id")
idLabel.grid(row=1,column=0)

cuadroNombre=Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=2,column=1)

nombreLabel=Label(miFrame,text="nombre")
nombreLabel.grid(row=2,column=0)


cuadroPassword=Entry(miFrame,textvariable=miPassword)
cuadroPassword.grid(row=3,column=1)
cuadroPassword.config(show="*")

passwordLabel=Label(miFrame,text="contraseña")
passwordLabel.grid(row=3,column=0)

cuadroApellido=Entry(miFrame,textvariable=miApellido)
cuadroApellido.grid(row=4,column=1)

apellidoLabel=Label(miFrame,text="apellido")
apellidoLabel.grid(row=4,column=0)

cuadroDireccion=Entry(miFrame,textvariable=miDireccion)
cuadroDireccion.grid(row=5,column=1)

direccionLabel=Label(miFrame,text="direccion")
direccionLabel.grid(row=5,column=0)

cuadroComentarios=Text(miFrame,width=20,height=5)
cuadroComentarios.grid(row=6,column=1)

comentariosLabel=Label(miFrame,text="comentarios")
comentariosLabel.grid(row=6,column=0)

scrollVert=Scrollbar(miFrame,command=cuadroComentarios.yview)
scrollVert.grid(row=6,column=2,sticky="nsew")

cuadroComentarios.config(yscrollcommand=scrollVert.set)

miFrame2=Frame(root)

botonCrear=Button(miFrame2,text="crear",command=lambda:crearCampo())
botonCrear.grid(row=8,column=0)

botonLeer=Button(miFrame2,text="leer",command=lambda:leerCampo())
botonLeer.grid(row=8,column=1)

botonUpdate=Button(miFrame2,text="actualizar",command=lambda:updateCampo())
botonUpdate.grid(row=8,column=2)

botonDelete=Button(miFrame2,text="borrar",command=lambda:borrarCampo())
botonDelete.grid(row=8,column=3)

miFrame.pack()

miFrame2.pack()


root.mainloop() 

