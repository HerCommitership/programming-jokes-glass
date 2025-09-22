# 🥃 Programming Jokes Glass

> A beautiful Python GUI that fills a virtual glass with humor as you collect programming jokes!

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

<div align="center">
  <img src="assets/demo.png" alt="Programming Jokes Glass Demo" width="600">
</div>

## ✨ Features

- 🎭 **Interactive Glass Animation** - Watch the glass fill up with colorful humor blocks
- 🌈 **Dynamic Theme Evolution** - Interface brightens and becomes more colorful with each joke
- 💡 **Progressive Visual Feedback** - From dark and empty to bright and overflowing
- 🎯 **Simple & Clean Interface** - Minimalist design focused on the experience
- 🔄 **Reset Functionality** - Empty the glass and start fresh anytime
- 🖥️ **Cross-Platform** - Works on Windows, Linux, and macOS

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- Tkinter (usually included with Python)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/programming-jokes-glass.git
cd programming-jokes-glass

# Install dependencies
pip install pyjokes

# Run the application
python my_gui.py
```

### Alternative Installation

```bash
# Using pip for dependencies
pip install -r requirements.txt
python my_gui.py
```

## 🎮 How to Use

1. **Launch the app** - Run `python my_gui.py`
2. **Add jokes** - Click "Add Joke" to fill the glass with humor
3. **Watch the magic** - See the glass fill up and interface brighten
4. **Reset when full** - Click "Empty Glass" to start over

### Visual Journey

| Jokes Count | Glass State | Interface Color |
|-------------|-------------|-----------------|
| 0 | Empty glass | Dark & moody |
| 1-2 | First drops | Deep blue tones |
| 3-4 | Quarter filled | Brighter blues |
| 5-6 | Half full | Colorful blues |
| 7-8 | Almost full | Bright & vibrant |
| 9+ | Overflowing! | Pure light & joy |

## 🛠️ Technical Details

### Architecture

```
programming-jokes-glass/
├── my_gui.py           # Main application
├── requirements.txt    # Dependencies
├── README.md          # This file
├── LICENSE            # MIT license
└── assets/            # Screenshots and media
```

### Key Components

- **JokeApp Class** - Main application controller
- **Theme System** - Dynamic color and visual management
- **Glass Animation** - ASCII art-based filling visualization
- **pyjokes Integration** - Programming humor source

### Dependencies

- `tkinter` - GUI framework (built-in with Python)
- `pyjokes` - Programming jokes library

## 🎨 Design Philosophy

This app embodies the metaphor that **humor brightens life**. Starting with a dark, empty glass in a somber interface, each joke adds visual "liquid" to the glass while simultaneously brightening the entire application's color scheme. It's a playful representation of how laughter can transform our mood and perspective.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Ideas for Contributions

- 🎨 New visual themes or color schemes
- 🥃 Alternative container shapes (bottle, cup, etc.)
- 🎵 Sound effects for joke additions
- 📱 Mobile/web version adaptation
- 🌍 Internationalization support

## 📋 Development

### Setting up Development Environment

```bash
# Clone and setup
git clone https://github.com/yourusername/programming-jokes-glass.git
cd programming-jokes-glass

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

### Testing

```bash
# Run the application in debug mode
python my_gui.py --debug

# Test different screen resolutions
python my_gui.py --resolution 800x600
```

## 📖 API Reference

### JokeApp Class

```python
class JokeApp:
    def __init__(self)
    def generate_joke(self)          # Add a new joke
    def clear_jokes(self)            # Reset the glass
    def update_theme(self)           # Refresh visual theme
    def get_glass_visual(self)       # Get current glass state
    def get_theme_colors(self)       # Get current color scheme
```

## 🐛 Troubleshooting

<details>
<summary>Common Issues</summary>

**Tkinter not found**
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# macOS with Homebrew
brew install python-tk

# Windows
# Tkinter comes with Python installer
```

**Application won't start**
- Ensure Python 3.11+ is installed
- Check that pyjokes is installed: `pip install pyjokes`
- Try running with: `python -v my_gui.py` for verbose output

</details>

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- 🎭 **pyjokes** - For the endless supply of programming humor
- 🐍 **Python/Tkinter** - For making GUI development accessible
- 🎨 **ASCII Art Community** - For inspiration on text-based graphics
- ☕ **Coffee** - For powering late-night coding sessions

## 🌟 Star History

If you found this project helpful or entertaining, please consider giving it a star! ⭐

---

<div align="center">
  <p>Made with ❤️ and lots of ☕</p>
  <p>© 2025 Programming Jokes Glass</p>
</div>