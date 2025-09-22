import tkinter as tk
from tkinter import scrolledtext
import pyjokes

class JokeApp:
    def __init__(self):
        self.joke_count = 0
        self.root = tk.Tk()
        self.root.title("Programming Jokes")
        self.root.geometry("650x550")
        
        try:
            self.root.wm_attributes('-toolwindow', True)
            self.root.wm_attributes('-toolwindow', False)
        except:
            pass
            
        self._create_interface()
        self.update_theme()
        
    def _create_interface(self):
        self.main_frame = tk.Frame(self.root, padx=25, pady=20)
        self.main_frame.pack(fill="both", expand=True)
        
        self.title_label = tk.Label(self.main_frame, text="Programming Jokes", 
                                   font=("Segoe UI", 22, "bold"))
        self.title_label.pack(pady=(0, 20))
        
        # Glass container for visual effect
        self.glass_frame = tk.Frame(self.main_frame, relief="ridge", bd=2)
        self.glass_frame.pack(pady=(0, 15))
        
        self.glass_label = tk.Label(self.glass_frame, font=("Courier", 10, "bold"), 
                                   justify="center", width=20, height=8)
        self.glass_label.pack(padx=10, pady=5)
        
        # Buttons
        button_frame = tk.Frame(self.main_frame)
        button_frame.pack(pady=(0, 15))
        
        self.generate_btn = tk.Button(button_frame, text="Add Joke", 
                                     command=self.generate_joke,
                                     font=("Segoe UI", 12, "bold"), 
                                     relief="flat", padx=20, pady=8)
        self.generate_btn.pack(side="left", padx=(0, 10))
        
        self.clear_btn = tk.Button(button_frame, text="Empty Glass", 
                                  command=self.clear_jokes,
                                  font=("Segoe UI", 10), 
                                  relief="flat", padx=15, pady=8)
        self.clear_btn.pack(side="left")
        
        # Text area
        self.text_area = scrolledtext.ScrolledText(self.main_frame, wrap=tk.WORD,
                                                  font=("Consolas", 10), 
                                                  relief="flat", bd=0, 
                                                  padx=10, pady=10)
        self.text_area.pack(fill="both", expand=True)
        self.text_area.insert(tk.END, "Click 'Add Joke' to fill the glass of humor!\n\n")
    
    def get_glass_visual(self):
        levels = [
            # Empty glass
            """    ┌─────────┐
    │         │
    │         │
    │         │
    │         │
    │         │
    │         │
    └─────────┘""",
            
            # 1-2 jokes - drops at bottom
            """    ┌─────────┐
    │         │
    │         │
    │         │
    │         │
    │    ∼∼   │
    │  ∼∼∼∼∼  │
    └─────────┘""",
            
            # 3-4 jokes - quarter full
            """    ┌─────────┐
    │         │
    │         │
    │         │
    │  ∼∼∼∼∼  │
    │  ░░░░░  │
    │  ░░░░░  │
    └─────────┘""",
            
            # 5-6 jokes - half full  
            """    ┌─────────┐
    │         │
    │         │
    │  ∼∼∼∼∼  │
    │  ░░░░░  │
    │  ░░░░░  │
    │  ▓▓▓▓▓  │
    └─────────┘""",
            
            # 7-8 jokes - three quarters
            """    ┌─────────┐
    │         │
    │  ∼∼∼∼∼  │
    │  ░░░░░  │
    │  ░░░░░  │
    │  ▓▓▓▓▓  │
    │  █████  │
    └─────────┘""",
            
            # 9+ jokes - overflowing!
            """    ┌─────────┐
    │  ∼∼∼∼∼  │
    │  ░░░░░  │
    │  ░░░░░  │
    │  ▓▓▓▓▓  │
    │  █████  │
    │  █████  │
    └─────────┘"""
        ]
        
        level_index = min(self.joke_count // 2, len(levels) - 1)
        return levels[level_index]
    
    def get_theme_colors(self):
        # Theme gets brighter and more colorful with more jokes
        themes = [
            {"bg": "#0a0a0a", "fg": "#666666", "text_bg": "#1a1a1a", "text_fg": "#999999", "glass_fg": "#444444"},
            {"bg": "#1a1a2e", "fg": "#888888", "text_bg": "#16213e", "text_fg": "#aaaaaa", "glass_fg": "#3498db"},
            {"bg": "#16537e", "fg": "#bbbbbb", "text_bg": "#1e5f8b", "text_fg": "#dddddd", "glass_fg": "#2ecc71"},
            {"bg": "#3d5a80", "fg": "#dddddd", "text_bg": "#4a6fa5", "text_fg": "#eeeeee", "glass_fg": "#f39c12"},
            {"bg": "#98c1d9", "fg": "#2c3e50", "text_bg": "#b8d4ea", "text_fg": "#34495e", "glass_fg": "#e74c3c"},
            {"bg": "#e0fbfc", "fg": "#2c3e50", "text_bg": "#f0ffff", "text_fg": "#2c3e50", "glass_fg": "#9b59b6"}
        ]
        
        theme_index = min(self.joke_count // 2, len(themes) - 1)
        return themes[theme_index]
    
    def update_theme(self):
        colors = self.get_theme_colors()
        glass_visual = self.get_glass_visual()
        
        # Update all colors
        self.root.configure(bg=colors["bg"])
        self.main_frame.configure(bg=colors["bg"])
        self.title_label.configure(bg=colors["bg"], fg=colors["fg"])
        
        self.glass_frame.configure(bg=colors["bg"])
        self.glass_label.configure(bg=colors["bg"], fg=colors["glass_fg"], text=glass_visual)
        
        self.generate_btn.configure(bg=colors["glass_fg"], fg="#ffffff", 
                                   activebackground=colors["fg"])
        self.clear_btn.configure(bg=colors["fg"], fg="#ffffff", 
                                activebackground=colors["glass_fg"])
        
        self.text_area.configure(bg=colors["text_bg"], fg=colors["text_fg"])
        
    def generate_joke(self):
        joke = pyjokes.get_joke()
        self.joke_count += 1
        self.text_area.insert(tk.END, f"Joke #{self.joke_count}: {joke}\n\n")
        self.text_area.see(tk.END)
        self.update_theme()
        
    def clear_jokes(self):
        self.text_area.delete(1.0, tk.END)
        self.joke_count = 0
        self.text_area.insert(tk.END, "Click 'Add Joke' to fill the glass of humor!\n\n")
        self.update_theme()
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = JokeApp()
    app.run()