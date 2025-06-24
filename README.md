# 🏍️ Wasteland Rider

**A post-apocalyptic text adventure built with Amazon Q Developer CLI for the #BuildGamesChallenge**

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Amazon Q](https://img.shields.io/badge/built%20with-Amazon%20Q-orange.svg)](https://aws.amazon.com/q/developer/)

## 🎮 About

Wasteland Rider is a gritty survival text adventure where you play as a lone motorcycle rider crossing 2,500 miles of post-apocalyptic wasteland from Washington DC to Los Angeles. Manage your fuel, maintain your bike, and survive the harsh world of 2087.

**🤖 Built entirely through conversation with Amazon Q Developer CLI in under 2 hours!**

## ⚡ Quick Start

```bash
git clone https://github.com/yotastalker/wasteland-rider.git
cd wasteland-rider
python3 game.py
```

**No dependencies required - just Python 3.7+!**

## 🎯 Game Features

- **🛣️ Epic Journey**: 2,500 miles from Washington DC to Los Angeles
- **⛽ Survival Mechanics**: Manage fuel, health, and bike condition
- **🗺️ Rich World**: 12 detailed locations across post-apocalyptic America  
- **🎒 Resource Management**: Scavenge for fuel, food, and repair parts
- **⚡ Random Encounters**: Face raiders, radiation storms, and mechanical failures
- **💾 Save/Load System**: Continue your journey across multiple sessions
- **🗣️ Natural Language**: Intuitive text-based interface with smart parsing

## 🏆 Amazon Q Build Games Challenge

This game was created for the **Amazon Q Build Games Challenge**, demonstrating the power of conversational AI development. The entire game - from concept to completion - was built through natural language conversation with Amazon Q Developer CLI.

### 📊 Development Stats:
- **⏱️ Time**: Under 2 hours
- **📝 Lines of Code**: 800+
- **💰 Cost**: $0 (Free with Amazon Q)
- **📦 External Dependencies**: None
- **🎯 Approach**: Pure conversational development

## 🎮 How to Play

### 🎯 Your Mission
Survive the 2,500-mile journey from Washington DC to Los Angeles on your dual-sport motorcycle. Your bike is your lifeline, fuel is your blood, and the wasteland is unforgiving.

### 🕹️ Basic Commands:
- **🛣️ Movement**: `ride north`, `west`, `east` (or `n`, `s`, `e`, `w`)
- **🎒 Items**: `take gas_can`, `use jerky`, `examine toolkit`
- **🔧 Bike Care**: `refuel gas_can`, `repair toolkit`, `rest`
- **📊 Information**: `look`, `inventory`, `status`
- **💾 Game**: `save`, `load`, `help`, `quit`

### 💡 Survival Tips:
- ⛽ Keep your fuel tank full - running out means death
- 🔧 Maintain your bike - breakdowns are fatal  
- 🏕️ Rest when injured, but watch fuel consumption
- ⚠️ Dangerous areas have better loot but higher risks
- 🗺️ Plan your route - some paths use more fuel than others

## 🗺️ The Journey

Your epic cross-country adventure takes you through:

### 🏛️ **Eastern Wasteland**
- **Washington DC Ruins** - Skeletal remains of the nation's capital
- **Interstate 66 Wasteland** - Endless cracked asphalt heading west
- **Abandoned Truck Stop** - Scavenge supplies in dangerous territory
- **Potomac Bridge** - Radioactive crossing over glowing waters

### ⛰️ **Mountain Region**
- **Shenandoah Wasteland** - Twisted remains of the Blue Ridge Mountains
- **Hidden Valley Settlement** - Trade with fellow survivors
- **Appalachian Pass** - High altitude challenges for your bike
- **Kentucky Border** - Face the raider checkpoint

### 🌾 **The Great Plains**
- **Louisville Ruins** - Gateway to the endless western expanse
- **Missouri Plains** - The long haul across grasslands
- **Los Angeles** - Your ultimate destination... if you make it

## 🛠️ Technical Details

Built with modern Python practices and powered by Amazon Q Developer CLI:

```python
# Clean object-oriented design
@dataclass
class Rider:
    inventory: List[str]
    fuel: int = 50
    bike_condition: int = 100
    health: int = 100

# Smart resource management
def use_fuel(self, amount: int):
    self.fuel = max(0, self.fuel - amount)
    
# Dynamic status display
fuel_bar = "█" * (fuel // 10) + "░" * (10 - fuel // 10)
```

### 🏗️ Architecture Features:
- **Object-oriented design** with dataclasses and type hints
- **JSON-based world data** for easy modification and expansion
- **Comprehensive error handling** with immersive responses
- **Natural language parsing** with command aliases
- **Resource management systems** for fuel, health, and bike condition
- **Random event engine** for dynamic encounters
- **Save/load functionality** with JSON serialization

## 🎨 Customization & Modding

The game world is defined in `wasteland.json`, making it incredibly easy to customize:

```json
{
  "locations": {
    "new_location": {
      "name": "Your Custom Location",
      "description": "A place of your imagination...",
      "exits": {"north": "another_location"},
      "items": ["custom_item"],
      "dangerous": false,
      "fuel_cost": 3
    }
  }
}
```

### 🔧 What You Can Modify:
- **🗺️ Add new locations** and routes
- **🎒 Create custom items** with different properties  
- **⚡ Adjust fuel costs** and danger levels
- **📝 Write new encounter text** and descriptions
- **🎲 Modify random event** probabilities

## 🤝 Contributing

This project was built for the Amazon Q Build Games Challenge, but contributions are welcome! 

### 🚀 Ways to Contribute:
- 🗺️ Add new locations or expand the world
- 🎒 Create new items and survival mechanics
- 📖 Improve the narrative and descriptions
- 🐛 Fix bugs or optimize performance
- 📚 Enhance documentation

## 🏆 Challenge Submission Details

**Amazon Q Build Games Challenge Entry**
- **🎮 Game Type**: Text Adventure (Retro-inspired)
- **🛠️ Development Tool**: Amazon Q Developer CLI
- **🎨 Theme**: Post-apocalyptic survival adventure
- **💡 Inspiration**: Classic Zork-style interactive fiction

### 📝 Development Story:
1. **Started with**: "Make a Zork-like game" 
2. **Refined to**: "Post-apocalyptic motorcycle adventure"
3. **Result**: Complete genre transformation in real-time
4. **Outcome**: Professional-quality game in under 2 hours

## 🔗 Links & Resources

- 🤖 [Amazon Q Developer CLI](https://aws.amazon.com/q/developer/)
- 🏆 [Build Games Challenge](https://community.aws/build-games-challenge)
- 📝 [My Development Blog Post](CHALLENGE_BLOG_POST.md)
- 🎬 [Video Development Story](VIDEO_SCRIPT.md)
- 📱 [Social Media Content](SOCIAL_MEDIA_POSTS.md)

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🏷️ Tags

`#BuildGamesChallenge` `#AmazonQDevCLI` `#TextAdventure` `#PostApocalyptic` `#RetroGaming` `#Python` `#GameDev` `#AI` `#ConversationalDevelopment`

---

## 🎯 Game Stats

```
🏍️  WASTELAND RIDER - DEVELOPMENT METRICS
═══════════════════════════════════════════════════════════════
📊 Lines of Code: 800+
⏱️  Development Time: < 2 hours  
💰 Development Cost: $0
🎮 Locations: 12 unique areas
🎒 Items: 20+ survival items
🔧 Dependencies: 0 external
🤖 AI Assistance: 100% Amazon Q
```

**Built with ❤️ and Amazon Q Developer CLI**

*May your fuel tank stay full and your engine never die! 🏍️💨*
