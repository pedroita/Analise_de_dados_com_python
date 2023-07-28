import tkinter as tk

def create_item():
    print("Criando")

def read_item():
    print ("lendo item")

def atulizar_item():
    print ("atulizar_item")

def Deletar_item():
    print ("Deletar item")

root =  tk.Tk()
root.title("Crud em python")

btn_create = tk.Button(root,text="Criar", command=create_item)
btn_create.pack()

btn_read = tk.Button(root,text="Ler", command=read_item)
btn_read.pack()

btn_update = tk.Button(root,text="Atulizar", command=atulizar_item)
btn_update.pack()

btn_delete = tk.Button(root,text="Deletar", command=Deletar_item)
btn_delete.pack()

root.mainloop()
