import tkinter as tk
from tkinter import ttk

def validate_float(value_if_allowed):
    """Validation pour permettre les valeurs flottantes avec ',' ou '.'"""
    if value_if_allowed == "":
        return True
    try:
        float(value_if_allowed.replace(',', '.'))
        return True
    except ValueError:
        return False

def calculate_volumes():
    """Calcule les volumes d'éthanol et d'eau pour atteindre la concentration souhaitée"""
    try:
        current_concentration = float(entry_current.get().replace(',', '.'))
        desired_concentration = float(entry_desired.get().replace(',', '.'))
        final_volume = float(entry_volume.get().replace(',', '.'))

        if desired_concentration > current_concentration:
            result_label.config(text="Erreur : La concentration souhaitée ne peut pas être supérieure à la concentration actuelle.")
            return

        # Calcul du volume d'éthanol à mélanger
        volume_ethanol = (desired_concentration / current_concentration) * final_volume
        volume_water = final_volume - volume_ethanol

        result_label.config(
            text=f"Volume d'éthanol : {volume_ethanol:.2f} mL\nVolume d'eau : {volume_water:.2f} mL"
        )
    except ValueError:
        result_label.config(text="Erreur : Veuillez entrer des valeurs valides !")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Calculateur de concentration d'éthanol")
root.geometry("400x400")

# Validation pour les champs d'entrée
vcmd = root.register(validate_float)

# Label et entrée pour la concentration actuelle
label_current = tk.Label(root, text="Concentration actuelle (g/mL ou %):")
label_current.pack(pady=(10, 0))

frame_current = tk.Frame(root)
frame_current.pack(pady=(0, 10))

entry_current = tk.Entry(frame_current, validate="key", validatecommand=(vcmd, '%P'))
entry_current.pack(side=tk.LEFT)

unit_var_current = tk.StringVar(value="g/mL")
dropdown_current = ttk.OptionMenu(frame_current, unit_var_current, "g/mL", "g/mL", "%", "mg/mL")
dropdown_current.pack(side=tk.LEFT, padx=(5, 0))

# Label et entrée pour la concentration souhaitée
label_desired = tk.Label(root, text="Concentration souhaitée (g/mL ou %):")
label_desired.pack(pady=(10, 0))

frame_desired = tk.Frame(root)
frame_desired.pack(pady=(0, 10))

entry_desired = tk.Entry(frame_desired, validate="key", validatecommand=(vcmd, '%P'))
entry_desired.pack(side=tk.LEFT)

unit_var_desired = tk.StringVar(value="g/mL")
dropdown_desired = ttk.OptionMenu(frame_desired, unit_var_desired, "g/mL", "g/mL", "%", "mg/mL")
dropdown_desired.pack(side=tk.LEFT, padx=(5, 0))

# Label et entrée pour le volume final souhaité
label_volume = tk.Label(root, text="Volume final souhaité (mL):")
label_volume.pack(pady=(10, 0))

entry_volume = tk.Entry(root, validate="key", validatecommand=(vcmd, '%P'))
entry_volume.pack(pady=(0, 10))

# Bouton pour calculer
submit_button = tk.Button(root, text="Calculer", command=calculate_volumes)
submit_button.pack(pady=(10, 0))

# Label pour afficher le résultat
result_label = tk.Label(root, text="", fg="blue")
result_label.pack(pady=(10, 0))

# Boucle principale
root.mainloop()

