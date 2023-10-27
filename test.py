import tkinter as tk

liste_tache = []  # Utiliser une liste de paires (tâche, statut)
liste_terminee = []
status = True

def ajout():
    taches = tache_entree.get()
    nouvelles_taches = [(t.strip(), False) for t in taches.split(',')]  # Nouvelles tâches sont marquées comme non terminées
    liste_tache.extend(nouvelles_taches)
    tache_entree.delete(0, 'end')
    mise_a_jour_label()

def supprimer():
    taches_a_supprimer = tache_entree.get()
    taches_a_supprimer = [t.strip() for t in taches_a_supprimer.split(',')]    #strip supprime les espace, split sépare a la ,
    
    for tache in taches_a_supprimer:
        for task, status in liste_tache:
            if tache == task:
                liste_tache.remove((task, status))
                tache_entree.delete(0, 'end')
    mise_a_jour_label()

def MaJ():
    mise_a_jour_label()

def terminee():
    tache_terminee = tache_entree.get()
    for i, (task, status) in enumerate(liste_tache):    # parcours indice valeur dans l'énumaration de la liste de tache valeur status    
        if tache_terminee == task:
            liste_tache[i] = (task, True)               # Marquer la tâche comme terminée
    tache_entree.delete(0, 'end')                      
    mise_a_jour_label()
    
def mise_a_jour_label():                                # mis a jour status 
    text = "Tâches restantes :\n"                     
    for task, status in liste_tache:                    # parcours indice valeur 
        if status:                                   
            text += f"[Terminée] {task}\n"              # renvoie le texte "terminé" avec la variable task de l'occurence
        else:
            text += f"[En cours] {task}\n"              # par défaut en cours 
    label_taches.config(text=text)                      # mis à jour auto du texte status 

window = tk.Tk()                                        # init fenetre
window.title("Gestionnaire de tâches")                  # titre 
window.geometry("1080x720")                             # taille de la fenêtre
window.config(background="#77AF9C")                     # couleur bg

label_instruction = tk.Label(window, text="Que souhaitez-vous faire ?", font=('Open Sans',30), bg="#77AF9C", pady=45)
label_instruction.pack()

tache_entree = tk.Entry(window, bg="#8CD790", width=60,highlightcolor="#D7FFF1")
tache_entree.pack(pady=100)

ajout_bouton = tk.Button(window, text="Ajouter", command=ajout, bg= "#8CD790" ,activebackground="#D7FFF1",height=2, width=20)
ajout_bouton.pack(side=tk.LEFT, padx=30)

#exemple d'explication : command --> fonction appelée, bg = background color, activebackground = couleur au clic, height = hauteur, width = largeur)


################################
#les boutons sont placés en ligne
################################
supprimer_bouton = tk.Button(window, text="Supprimer", command=supprimer, bg="#8CD790",activebackground="#D7FFF1",height=2, width=20)
supprimer_bouton.pack(side=tk.LEFT, padx=30)

maj_bouton = tk.Button(window, text="Mise à jour", command=MaJ, bg ="#8CD790",activebackground="#D7FFF1",height=2, width=20)
maj_bouton.pack(side=tk.LEFT, padx=30)

terminee_bouton = tk.Button(window, text="Terminée", command=terminee, bg ="#8CD790",activebackground="#D7FFF1", height=2, width=20)
terminee_bouton.pack(side=tk.LEFT, padx=30)

label_taches = tk.Label(window, text="Tâches restantes :",bg='#8CD790', padx=40, border=5)
label_taches.pack()
#label different de button, ici c'est de l'affichage, la des taches restantes, placé à droite de la ligne de bouton

window.mainloop() #lancement
