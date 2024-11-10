import tkinter as tk
#-------------------------#

fenetre = tk.Tk()            # -> creation de la fenetre de travaille 
fenetre.geometry("900x650")
fenetre.configure(bg="lightblue")
fenetre.title("Task Manager")


def canva_script():
   zone_texte = tk.Text(fenetre, width=100, height=5000)
   zone_texte.pack(expand=True) 


btn_creat = tk.Button(fenetre, text="creat", command=canva_script) # -> boutton de creation du canva 
btn_creat.pack()

fenetre.mainloop()           # -> permet a la fenetre de rester fige