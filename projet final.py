

import tkinter as tk
from tkinter import messagebox

class ProjectIdeaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Idée de projet et Case Utilisateur")
        
        # Project Idea
        self.idea_label = tk.Label(root, text="Idée de Projet:")
        self.idea_label.grid(row=0, column=0, padx=10, pady=5)
        self.idea_entry = tk.Entry(root, width=50)
        self.idea_entry.grid(row=0, column=1, padx=10, pady=5)
        
        # Use Cases
        self.use_cases_label = tk.Label(root, text="Explication du Projet:")
        self.use_cases_label.grid(row=1, column=0, padx=10, pady=5)
        self.use_cases_text = tk.Text(root, height=10, width=50)
        self.use_cases_text.grid(row=1, column=1, padx=10, pady=5)
        
        # Actors
        self.actors_label = tk.Label(root, text="Acteur Potentiel:")
        self.actors_label.grid(row=2, column=0, padx=10, pady=5)
        self.actors_text = tk.Text(root, height=10, width=50)
        self.actors_text.grid(row=2, column=1, padx=10, pady=5)
        
        # Submit Button
        self.submit_button = tk.Button(root, text="Soumettre", command=self.submit)
        self.submit_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")
        
    def submit(self):
        idea = self.idea_entry.get()
        use_cases = self.use_cases_text.get("1.0", tk.END).strip()
        actors = self.actors_text.get("1.0", tk.END).strip()
        
        if not idea or not use_cases or not actors:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
        else:
            summary = f"Project Idea: {idea}\n\nUse Cases:\n{use_cases}\n\nPotential Actors:\n{actors}"
            messagebox.showinfo("Project Summary", summary)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectIdeaApp(root)






    root.mainloop()