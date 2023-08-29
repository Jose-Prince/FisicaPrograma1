import turtle
from tkinter import *
import pruebas as pr
import Figuras as fig
import CampoElectrico as campo




if __name__ == "__main__":

  
  tortugita = turtle.Turtle()
  root = Tk()
  root.geometry("960x540")
  
  tituloh = Label(root, text="Bienvenido al CALCULUS EP CAMPO ELECTRICO EN TRES FIGURAS", font=("Arial", 12)).pack()
  # Change the label text
  def show():
      label1.config( text = "Se ha elegido la figura: " + clicked.get())

      if(clicked.get()=="Cono"):
        entryradio.pack() #mayor
        labelpediradio = Label(root, text="Por favor ingresar el radio   \n**Tomar en Cuenta que cada pixel es un metro**").pack()
        entryaltura.pack() #altura
        labelpediraltura = Label(root, text="Por favor ingresar la altura   \n**Tomar en Cuenta que cada pixel es un metro**").pack()
        buttoninput = Button(root, text= "Ingresar",width= 20, command= display_texconot).pack(pady=20)
        



      if(clicked.get() == "Tronco de Cono"):
        entryradio.pack()
        labelpedirmayor = Label(root, text="Por favor ingresar el radio mayor  \n**Tomar en Cuenta que cada pixel es un metro**").pack()
        entryaltura.pack() #menor
        labelpediraltura = Label(root, text="Por favor ingresar la altura   \n**Tomar en Cuenta que cada pixel es un metro**").pack()
        entryradiomenor.pack()
        labelpediradiomenor = Label(root, text="Por favor ingresar el radio menor   \n**Tomar en Cuenta que cada pixel es un metro**").pack()
        buttoninput = Button(root, text= "Ingresar",width= 20, command= display_textron).pack(pady=20)


      if(clicked.get()== "Hemisferio"):
        entryradio.pack()
        labelpediradio = Label(root, text="Por favor ingresar el radio   \n**Tomar en Cuenta que cada pixel es un metro**").pack()
        buttoninput = Button(root, text= "Ingresar",width= 20, command= display_texhemi).pack(pady=20)
      importante = Label(root, text="EL plano cartesiano se abrió en otra pantalla").pack()



####TOdo ESTO SE DEBE DE UTILIZAR PARA CALCULAR LA TORTUGA
  def display_texconot(): #Cono radio y altura}
   stringaltura = entryaltura.get()
   string= entryradio.get()
   label2.configure(text=string)
   pr.pantalla()
   fig.cono(int(string),int(stringaltura),tortugita)
   

  def display_textron(): #Cono toncado radio 1 radio 2 y radio menor
   
   string= entryradio.get()
   radiomen = entryradiomenor.get()
   altrua = entryaltura.get()
   label2.configure(text=string)
   pr.pantalla()
   fig.conoTruncado(int(string),int(radiomen),int(altrua),tortugita)

  def display_texhemi(): #hemisferio solo el radio 
   string= entryradio.get()
   label2.configure(text=string)
   pr.pantalla()
   fig.hemisferio(int(string),turtle)
    
  # Dropdown menu options
  options = [
      "Cono",
      "Tronco de Cono",
      "Hemisferio"
  ]
    
  # datatype of menu text
  clicked = StringVar()
    
  # initial menu text
  clicked.set( "Figura" )
    
  # Create Dropdown menu
  drop = OptionMenu( root , clicked , *options)
  drop.config(width=100, height=1)
  drop.pack()
    
  # Create button, it will change label text
  button = Button( root , text = "Elegir figura Geometrica" , command = show, height=1, width=100 ).pack()
    
  # Create Label
  label1 = Label( root , text = " " )
  label1.pack()

  #Creas el label
  label2=Label(root, text="")
  label2.pack()

  entryradio= Entry(root, width= 40) #Mayor
  entryradio.focus_set()
  entryradiomenor= Entry(root, width= 40) #menor
  entryradiomenor.focus_set()
  entryaltura= Entry(root, width= 40) 
  entryaltura.focus_set()
  #Initialize a Label to display the User Input



  button = Button( root , text = "Generar Plano Cartesiano" , command = lambda: pr.pantalla(), height=1, width=75 ).pack()


      #Create an Entry widget to accept User Input


    
  # Execute tkinter
  root.mainloop()








    
    # x = 10
    
    
    # def getcoords(numero):
    #   for i in range(numero):
    #     coord = Label(root, text="Las coordenadas en X es: " + str(x)).grid(row=(i+4), column=0)
    #     elinput = Label(root, text="Se dijo esto: ").grid(row=20, column=0)
        


    # root = Tk()
    # mylabel1 = Label(root, text= "Bienvenidos al programa de Solidos").grid(row=0,column=0)
    # mylabel2 = Label(root, text= "Bienvenidos al programa de Solidos").grid(row=1,column=1) #Crea un texto
    # El grid es para su posicion
    # e = Entry(root, width=100)
    # e.grid(row=40, column=2)

    # elinput = Label(root, text="Se dijo esto: ").grid(row=30, column=0)
    


    # mybutton = Button(root, text="Click Me", command= lambda: getcoords(x)).grid(row=2,column=0)

    
  root.mainloop()