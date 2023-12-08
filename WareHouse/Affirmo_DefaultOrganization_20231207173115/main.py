'''
This is the main file of the subliminal app. It contains the GUI implementation and handles user interactions.
'''
import tkinter as tk
from subliminal_generator import SubliminalGenerator
class SubliminalApp(tk.Tk):
    def __init__(self, api_key):
        super().__init__()
        self.title("Subliminal App")
        self.geometry("800x600")
        self.subliminal_generator = SubliminalGenerator(api_key)
        self.create_widgets()
    def create_widgets(self):
        # GUI elements creation and layout
        # GPT prompt input
        self.prompt_label = tk.Label(self, text="GPT Prompt:")
        self.prompt_label.pack()
        self.prompt_entry = tk.Entry(self, width=50)
        self.prompt_entry.pack()
        # Waves selection
        self.waves_label = tk.Label(self, text="Select Waves:")
        self.waves_label.pack()
        self.waves_options = ["Theta", "Gamma", "Beta", "Alpha"]
        self.waves_vars = []
        for wave in self.waves_options:
            var = tk.BooleanVar()
            checkbutton = tk.Checkbutton(self, text=wave, variable=var)
            checkbutton.pack()
            self.waves_vars.append(var)
        # Background music selection
        self.music_label = tk.Label(self, text="Select Background Music:")
        self.music_label.pack()
        self.music_options = ["Music 1", "Music 2", "Music 3"]
        self.music_var = tk.StringVar()
        self.music_var.set(self.music_options[0])
        self.music_dropdown = tk.OptionMenu(self, self.music_var, *self.music_options)
        self.music_dropdown.pack()
        # Generate button
        self.generate_button = tk.Button(self, text="Generate Subliminal", command=self.generate_subliminal)
        self.generate_button.pack()
        # Output text
        self.output_text = tk.Text(self, height=10, width=80)
        self.output_text.pack()
    def generate_subliminal(self):
        # Get user inputs
        prompt = self.prompt_entry.get()
        waves = [self.waves_options[i] for i, var in enumerate(self.waves_vars) if var.get()]
        music = self.music_var.get()
        # Generate subliminal message
        subliminal_message = self.subliminal_generator.generate_subliminal(prompt, waves, music)
        # Display output
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, subliminal_message)
if __name__ == "__main__":
    api_key = "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"
    app = SubliminalApp(api_key)
    app.mainloop()