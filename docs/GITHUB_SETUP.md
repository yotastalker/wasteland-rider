# GitHub Repository Setup for Wasteland Rider

## 📁 Repository Structure

```
wasteland-rider/
├── README.md                 # Main project documentation
├── game.py                   # Main game engine
├── wasteland.json           # World data (locations, items)
├── requirements.txt         # Python dependencies (empty - no external deps)
├── LICENSE                  # MIT License
├── .gitignore              # Python gitignore
├── screenshots/            # Gameplay screenshots
│   ├── gameplay1.png
│   ├── gameplay2.png
│   └── status_bars.png
├── docs/                   # Additional documentation
│   ├── CHALLENGE_BLOG_POST.md
│   ├── VIDEO_SCRIPT.md
│   └── DEVELOPMENT_LOG.md
└── examples/               # Example save files and mods
    ├── sample_save.json
    └── custom_world.json
```

## 📝 Repository README.md

```markdown
# 🏍️ Wasteland Rider

A post-apocalyptic text adventure built with Amazon Q Developer CLI for the #BuildGamesChallenge

![Wasteland Rider Screenshot](screenshots/gameplay1.png)

## 🎮 About

Wasteland Rider is a gritty survival text adventure where you play as a lone motorcycle rider crossing 2,500 miles of post-apocalyptic wasteland from Washington DC to Los Angeles. Manage your fuel, maintain your bike, and survive the harsh world of 2087.

**Built entirely through conversation with Amazon Q Developer CLI in under 2 hours!**

## ⚡ Quick Start

```bash
git clone https://github.com/[your-username]/wasteland-rider.git
cd wasteland-rider
python3 game.py
```

No dependencies required - just Python 3.7+!

## 🎯 Game Features

- **Survival Mechanics**: Manage fuel, health, and bike condition
- **Rich World**: 12 detailed locations across post-apocalyptic America  
- **Resource Management**: Scavenge for fuel, food, and repair parts
- **Random Encounters**: Face raiders, radiation storms, and mechanical failures
- **Save/Load System**: Continue your journey across multiple sessions
- **Natural Language Commands**: Intuitive text-based interface

## 🏆 Amazon Q Build Games Challenge

This game was created for the Amazon Q Build Games Challenge, demonstrating the power of conversational AI development. The entire game - from concept to completion - was built through natural language conversation with Amazon Q Developer CLI.

### Development Stats:
- **Time**: Under 2 hours
- **Lines of Code**: 800+
- **Cost**: $0 (Free with Amazon Q)
- **External Dependencies**: None

## 🎮 How to Play

### Basic Commands:
- **Movement**: `ride north`, `west`, `east` (or `n`, `s`, `e`, `w`)
- **Items**: `take gas_can`, `use jerky`, `examine toolkit`
- **Bike Care**: `refuel gas_can`, `repair toolkit`, `rest`
- **Information**: `look`, `inventory`, `status`
- **Game**: `save`, `load`, `help`, `quit`

### Survival Tips:
- Keep your fuel tank full - running out means death
- Maintain your bike - breakdowns are fatal  
- Rest when injured, but watch fuel consumption
- Dangerous areas have better loot but higher risks

## 🗺️ The Journey

Your epic 2,500-mile journey takes you through:

- **Washington DC Ruins** - Your starting point in the devastated capital
- **Interstate 66 Wasteland** - Endless cracked asphalt heading west
- **Abandoned Truck Stop** - Scavenge for supplies in dangerous territory
- **Shenandoah Wasteland** - Navigate the twisted mountain terrain
- **Hidden Valley Settlement** - Trade with fellow survivors
- **Appalachian Pass** - High altitude challenges for your bike
- **Kentucky Border** - Face the raider checkpoint
- **Louisville Ruins** - Gateway to the Great Plains
- **Missouri Plains** - The long haul across endless grasslands
- **Los Angeles** - Your ultimate destination (if you make it!)

## 🛠️ Technical Details

Built with modern Python practices:
- Object-oriented design with dataclasses
- JSON-based world data for easy modification
- Comprehensive error handling
- Natural language command parsing
- Resource management systems
- Random event engine

## 🎨 Customization

The game world is defined in `wasteland.json`, making it easy to:
- Add new locations and routes
- Create custom items with different properties
- Modify fuel costs and danger levels
- Write new encounter text and descriptions

## 📸 Screenshots

![Game Start](screenshots/gameplay1.png)
*Starting your journey in the ruins of Washington DC*

![Status System](screenshots/status_bars.png)  
*Resource management with visual fuel and condition bars*

![Dangerous Encounter](screenshots/gameplay2.png)
*Surviving random encounters in the wasteland*

## 🤝 Contributing

This project was built as part of the Amazon Q Build Games Challenge, but contributions are welcome! Feel free to:
- Add new locations or items
- Improve the narrative
- Add new game mechanics
- Fix bugs or improve code quality

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🏆 Challenge Submission

**Amazon Q Build Games Challenge Entry**
- **Game Type**: Text Adventure (Retro-inspired)
- **Development Tool**: Amazon Q Developer CLI
- **Theme**: Post-apocalyptic survival
- **Inspiration**: Classic Zork-style adventures

### Blog Post: [Link to your blog post]
### Video Demo: [Link to your video]

## 🔗 Links

- [Amazon Q Developer CLI](https://aws.amazon.com/q/developer/)
- [Build Games Challenge](https://community.aws/build-games-challenge)
- [My Development Blog Post](docs/CHALLENGE_BLOG_POST.md)
- [Video Script](docs/VIDEO_SCRIPT.md)

## 🏷️ Tags

`#BuildGamesChallenge` `#AmazonQDevCLI` `#TextAdventure` `#PostApocalyptic` `#RetroGaming` `#Python` `#GameDev` `#AI`

---

*Built with ❤️ and Amazon Q Developer CLI*
*May your fuel tank stay full and your engine never die! 🏍️*
```

## 🔧 Additional Files to Create

### .gitignore
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Game saves
*_save.json
savegame.json

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

### LICENSE (MIT)
```
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### requirements.txt
```
# No external dependencies required
# Python 3.7+ standard library only
```

## 🚀 Repository Setup Commands

```bash
# Initialize repository
cd /Users/chrismckearn/zork_modern
git init
git add .
git commit -m "Initial commit: Wasteland Rider - Post-apocalyptic text adventure built with Amazon Q"

# Create GitHub repository (using GitHub CLI)
gh repo create wasteland-rider --public --description "Post-apocalyptic text adventure built with Amazon Q Developer CLI for #BuildGamesChallenge"

# Push to GitHub
git branch -M main
git remote add origin https://github.com/[your-username]/wasteland-rider.git
git push -u origin main
```
