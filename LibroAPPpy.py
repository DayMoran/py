from tkinter import *
from tkinter.ttk import Treeview
from Libro import Libro

#######################OPERACIONES####################
def borrar_libro():
    item = tree.selection()[0]
    tree.delete(item)
    
def btnG_click():
    milibro=Libro(textid.get(),texttitulo.get(),textautor.get(),textisbn.get(),textpaginas.get(),textedicion.get(),texteditorial.get(),textlugar.get(),"SI" if dis.get() else "NO",textprecio.get())
    tree.insert("",END,values=(milibro.id_Libro, milibro.Titulo, milibro.Autor, milibro.ISBN, milibro.Paginas, milibro.Edicion, milibro.Editorial, milibro.Pais, milibro.Disponible,milibro.Precio,milibro.precio_mas_iva()))
    clear()
def btnM_click():
    item=tree.selection()[0]
    tree.item(item, values=(textid.get(),texttitulo.get(),textautor.get(),textisbn.get(),textpaginas.get(),textedicion.get(),texteditorial.get(),textlugar.get(),"SI" if dis.get() else "NO"))
    btnG.config(state=NORMAL)
    btnB.config(state=NORMAL)
    textid.config(state=NORMAL)
    tree.config(selectmode=BROWSE)
    clear()
    pass
def onDoubleClick(event):
    item=tree.selection()[0]
    clear()
    textid.insert(0, tree.item(item)['values'][0])
    texttitulo.insert(0, tree.item(item)['values'][1])
    textautor.insert(0, tree.item(item)['values'][2])
    textisbn.insert(0, tree.item(item)['values'][3])
    textpaginas.insert(0, tree.item(item)['values'][4])
    textedicion.insert(0, tree.item(item)['values'][5])
    texteditorial.insert(0, tree.item(item)['values'][6])
    textlugar.insert(0, tree.item(item)['values'][7])
    dis.set(1 if tree.item(item) ['values'][8]=="SI" else 0)
    btnG.config(state=DISABLED)
    btnB.config(state=DISABLED)
    textid.config(state=DISABLED)
    tree.config(selectmode=NONE)
    pass

def clear():
    textid.delete(0,END)
    texttitulo.delete(0,END)
    textautor.delete(0,END)
    textisbn.delete(0,END)
    textpaginas.delete(0,END)
    textedicion.delete(0,END)
    texteditorial.delete(0,END)
    textlugar.delete(0,END)
    dis.set(0)
    pass
def salir():
    ventana.destroy()

######################################################

#######################DISENIO########################

ventana = Tk()
ventana.title("Imagen de fondo")
#ventana.geometry("1280x720")
#ventana.resizable(False, False)  # Desactiva la capacidad de cambiar el tamanio de la ventana
color_fondo = "#18171c"  # Color de fondo en formato hexadecimal
color_texto="#F6f6f6"
ventana.configure(bg=color_fondo)

######################################################

################VARIABLES DE CONTROL##################
dis = IntVar()
######################################################

#####################INSERCION DE CONTROLES###########
labelid=Label(text="ID",bg=color_fondo, highlightbackground=color_fondo,fg=color_texto)
labelid.grid(column=0,row=0,padx=10,pady=10,sticky=E)
textid=Entry()
textid.grid(column=1,row=0,padx=10,pady=10,sticky=W)

labelcolor=Label(text="TITULO",bg=color_fondo, highlightbackground=color_fondo,fg=color_texto)
labelcolor.grid(column=0,row=1,padx=10,pady=10,sticky=E)
texttitulo=Entry()
texttitulo.grid(column=1,row=1,padx=10,pady=10,sticky=W)

labelautor=Label(text="AUTOR",bg=color_fondo, highlightbackground=color_fondo,fg=color_texto)
labelautor.grid(column=0,row=2,padx=10,pady=10,sticky=E)
textautor=Entry()
textautor.grid(column=1,row=2,padx=10,pady=10,sticky=W)

labelisbn=Label(text="ISBN",bg=color_fondo, highlightbackground=color_fondo,fg=color_texto)
labelisbn.grid(column=0,row=3,padx=10,pady=10,sticky=E)
textisbn=Entry()
textisbn.grid(column=1,row=3,padx=10,pady=10,sticky=W)

labelpaginas=Label(text="PAGINAS",bg=color_fondo, highlightbackground=color_fondo,fg=color_texto)
labelpaginas.grid(column=0,row=4,padx=10,pady=10,sticky=E)
textpaginas=Entry()
textpaginas.grid(column=1,row=4,padx=10,pady=10,sticky=W)

labeledicion=Label(text="EDICION",bg=color_fondo, highlightbackground=color_fondo,fg=color_texto)
labeledicion.grid(column=0,row=5,padx=10,pady=10,sticky=E)
textedicion=Entry()
textedicion.grid(column=1,row=5,padx=10,pady=10,sticky=W)

labeleditorial=Label(text="EDITORIAL",bg=color_fondo, highlightbackground=color_fondo,fg=color_texto)
labeleditorial.grid(column=0,row=6,padx=10,pady=10,sticky=E)
texteditorial=Entry()
texteditorial.grid(column=1,row=6,padx=10,pady=10,sticky=W)

labellugar=Label(text="LUGAR",bg=color_fondo, highlightbackground=color_fondo,fg=color_texto)
labellugar.grid(column=0,row=7,padx=10,pady=10,sticky=E)
textlugar=Entry()
textlugar.grid(column=1,row=7,padx=10,pady=10,sticky=W)

labelprecio=Label(text="PRECIO",bg=color_fondo, highlightbackground=color_fondo,fg=color_texto)
labelprecio.grid(column=0,row=8,padx=10,pady=10,sticky=E)
textprecio=Entry()
textprecio.grid(column=1,row=8,padx=10,pady=10,sticky=W)


disp= Checkbutton(text="DISPONIBLE",variable=dis, highlightbackground=color_fondo)
disp.grid(column=1,row=9,padx=10,pady=10,sticky=W)
#PARTE DEL TREEVIEW
columns = ("id","titulo","autor","isbn","paginas","edicion","editorial","lugar","disponible","precio","precio_mas_iva")

tree=Treeview(ventana, columns=columns, show="headings")
tree.heading("id",text="ID")
tree.heading("titulo",text="Titulo")
tree.heading("autor",text="Autor")
tree.heading("isbn",text="ISBN")
tree.heading("paginas",text="Paginas")
tree.heading("edicion",text="Edicion")
tree.heading("editorial",text="Editorial")
tree.heading("lugar",text="Lugar")
tree.heading("disponible",text="Disponible")
tree.heading("precio",text="Precio")
tree.heading("precio_mas_iva",text="Precio + IVA")

tree.grid(column=0,row=10,columnspan=2,padx=80)

tree.column("id", width=50)
tree.column("titulo", width=100)
tree.column("autor", width=200)
tree.column("isbn", width=100)
tree.column("paginas", width=100)
tree.column("edicion", width=80)
tree.column("editorial", width=150)
tree.column("lugar", width=180)
tree.column("disponible", width=80)
tree.column("precio", width=70)
tree.column("precio_mas_iva", width=100)
#treeBind
tree.bind("<Double-1>",onDoubleClick)
#Botones
btnG=Button(text="Guardar",command=btnG_click)
btnG.grid(column=0,row=11, pady=30)

btnM=Button(text="Modificar",command=btnM_click)
btnM.grid(column=1,row=11, pady=30,sticky=W)

btnB=Button(text="Borrar",command=borrar_libro)
btnB.grid(column=1,row=11, pady=30)

btnSalir = Button(text="Salir", command=salir)
btnSalir.grid(column=1, row=11, pady=30,padx=20,sticky=E)

######################################################
ventana.mainloop()