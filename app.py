#Importando as libs (tkinter para a GUI)

import tkinter as tk
from tkinter import filedialog, Text
import os

#inicializando o tkinter
root = tk.Tk()

#array dos arquivos localizados e selecionados
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(",")
        apps = [x for x in tempApps if x.strip()]

#definindo função que encontrará os arquivos e irá mostrá-los
def addApp():
    #Destrutor, que pegara o item no array e o removerá
    for widget in frame.winfo_children():
        widget.destroy()

    #Realiza a chamada de abertura do seletor
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("Executable", "*.exe"), ("all files", "*.")))

    #Adiciona itens ao array
    apps.append(filename)
    print(filename) #log do arquivo no terminal

    #Mostra na janela do GUI o que foi selecionado
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

def clearApps():
    size = len(apps)

    if size != None:
        apps.clear()
        print(apps)
        root.mainloop()

#O canvas dará estilo para a janela
canvas = tk.Canvas(root, height=500, width=500, bg="#263042")
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.7, relheight=0.75, relx= 0.15, rely=0.05)

#Buttons
openFile = tk.Button(root, text="Open file", padx=10, pady=5, fg="white", bg="#263042", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run", padx=10, pady=5, fg="white", bg="#263042", command=runApps)
runApps.pack()

for app in apps: 
    label = tk.Label(frame, text=app)
    label.pack()

clearFiles = tk.Button(root, text="Clear", padx=10, pady=5, fg="white", bg="#263042", command=clearApps)
clearFiles.pack()

#Realiza o loop para manter a janela ativa
root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
