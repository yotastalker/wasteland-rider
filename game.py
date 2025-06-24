#!/usr/bin/env python3
"""
Wasteland Rider - Post-Apocalyptic Adventure Game
Navigate the dangerous wasteland from Washington DC to Los Angeles
on your trusty dual-sport motorcycle
"""

import json
import os
import pickle
import random
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum


class GameState(Enum):
    PLAYING = "playing"
    GAME_OVER = "game_over"
    WON = "won"


@dataclass
class Item:
    name: str
    description: str
    takeable: bool = True
    useable: bool = False
    use_message: str = ""
    aliases: List[str] = None
    fuel_value: int = 0  # For fuel items
    food_value: int = 0  # For food items
    repair_value: int = 0  # For repair items
    
    def __post_init__(self):
        if self.aliases is None:
            self.aliases = []


@dataclass
class Location:
    name: str
    description: str
    exits: Dict[str, str]
    items: List[str]
    visited: bool = False
    dangerous: bool = False
    fuel_cost: int = 1  # Fuel cost to leave this location
    
    def __post_init__(self):
        if not hasattr(self, 'items'):
            self.items = []


class Rider:
    def __init__(self):
        self.inventory: List[str] = ["toolkit", "water_bottle", "jerky"]
        self.current_location: str = "dc_ruins"
        self.health: int = 100
        self.fuel: int = 50
        self.bike_condition: int = 100
        self.miles_traveled: int = 0
        self.days_survived: int = 0
    
    def add_item(self, item_name: str):
        self.inventory.append(item_name)
    
    def remove_item(self, item_name: str):
        if item_name in self.inventory:
            self.inventory.remove(item_name)
            return True
        return False
    
    def has_item(self, item_name: str) -> bool:
        return item_name in self.inventory
    
    def use_fuel(self, amount: int):
        self.fuel = max(0, self.fuel - amount)
    
    def add_fuel(self, amount: int):
        self.fuel = min(100, self.fuel + amount)
    
    def repair_bike(self, amount: int):
        self.bike_condition = min(100, self.bike_condition + amount)
    
    def damage_bike(self, amount: int):
        self.bike_condition = max(0, self.bike_condition - amount)


class WastelandEngine:
    def __init__(self):
        self.rider = Rider()
        self.locations: Dict[str, Location] = {}
        self.items: Dict[str, Item] = {}
        self.state = GameState.PLAYING
        self.load_world_data()
        
    def load_world_data(self):
        """Load world data from JSON file"""
        world_file = os.path.join(os.path.dirname(__file__), 'wasteland.json')
        try:
            with open(world_file, 'r') as f:
                data = json.load(f)
                
            # Load locations
            for location_id, location_data in data.get('locations', {}).items():
                self.locations[location_id] = Location(**location_data)
                
            # Load items
            for item_id, item_data in data.get('items', {}).items():
                self.items[item_id] = Item(**item_data)
                
        except FileNotFoundError:
            print("Wasteland data file not found. Creating default world...")
            self.create_default_world()
    
    def create_default_world(self):
        """Create a default post-apocalyptic world if no wasteland.json exists"""
        # Default locations
        self.locations = {
            "dc_ruins": Location(
                name="Washington DC Ruins",
                description="The skeletal remains of the Capitol dome pierce the smoky sky. Your dual-sport motorcycle idles among the rubble-strewn streets. The Potomac River glows with an unnatural green hue to the south. Interstate 66 stretches west toward the wasteland.",
                exits={"west": "highway_66", "south": "potomac_bridge"},
                items=["gas_can"],
                fuel_cost=2
            ),
            "highway_66": Location(
                name="Interstate 66 Wasteland",
                description="Cracked asphalt stretches endlessly west. Abandoned vehicles rust in the median, their metal skeletons picked clean by scavengers. Your bike's engine echoes across the desolate landscape. A side road leads north to an old truck stop.",
                exits={"east": "dc_ruins", "west": "shenandoah", "north": "truck_stop"},
                items=["spare_tire"],
                fuel_cost=3
            ),
            "truck_stop": Location(
                name="Abandoned Truck Stop",
                description="Rusted fuel pumps stand like metal tombstones. The convenience store's windows are shattered, but the structure might still hold supplies. A faded sign reads 'Last Gas for 50 Miles' - if only that were still true.",
                exits={"south": "highway_66"},
                items=["fuel_siphon", "canned_food", "road_map"],
                dangerous=True,
                fuel_cost=1
            ),
            "potomac_bridge": Location(
                name="Potomac River Bridge",
                description="The bridge spans the irradiated waters below. Geiger counter clicks echo in your helmet. The metal structure groans ominously in the radioactive wind. Best not to linger here long.",
                exits={"north": "dc_ruins", "west": "virginia_hills"},
                items=["rad_pills"],
                dangerous=True,
                fuel_cost=2
            ),
            "shenandoah": Location(
                name="Shenandoah Wasteland",
                description="What once were the beautiful Blue Ridge Mountains are now twisted, blackened peaks. Your dual-sport handles the rough terrain well. A hidden valley to the south might offer shelter.",
                exits={"east": "highway_66", "south": "hidden_valley", "west": "appalachian_pass"},
                items=["mountain_gear"],
                fuel_cost=4
            ),
            "hidden_valley": Location(
                name="Hidden Valley Settlement",
                description="Smoke rises from chimneys built into hillsides. Survivors have carved out a life here, trading supplies and information. Your motorcycle draws curious but wary glances.",
                exits={"north": "shenandoah"},
                items=["trade_goods", "fuel_barrel", "repair_kit"],
                fuel_cost=1
            ),
            "virginia_hills": Location(
                name="Virginia Hills",
                description="Rolling hills stretch toward the horizon, dotted with the remains of small towns. Your bike climbs steadily westward. The air tastes of ash and distant storms.",
                exits={"east": "potomac_bridge", "west": "appalachian_pass"},
                items=["binoculars"],
                fuel_cost=3
            ),
            "appalachian_pass": Location(
                name="Appalachian Mountain Pass",
                description="The highest point for hundreds of miles. From here you can see the long road ahead - thousands of miles of wasteland between you and Los Angeles. Your bike's engine strains against the altitude.",
                exits={"east": "shenandoah", "south": "virginia_hills", "west": "kentucky_border"},
                items=["high_octane_fuel"],
                fuel_cost=5
            ),
            "kentucky_border": Location(
                name="Kentucky Border Crossing",
                description="A checkpoint from the old world, now manned by raiders who demand tribute from travelers. Your bike could probably outrun them, but negotiation might be wiser.",
                exits={"east": "appalachian_pass", "west": "louisville_ruins"},
                items=["ammunition"],
                dangerous=True,
                fuel_cost=2
            ),
            "louisville_ruins": Location(
                name="Louisville Ruins",
                description="The Ohio River flows past the skeletal remains of the city. Your destination of Los Angeles feels impossibly far from here. But your bike is strong, and the road calls westward.",
                exits={"east": "kentucky_border"},
                items=["victory_flag"],
                fuel_cost=1
            )
        }
        
        # Default items
        self.items = {
            "toolkit": Item(
                name="Motorcycle Toolkit",
                description="A well-worn set of tools for maintaining your dual-sport bike. Essential for survival in the wasteland.",
                takeable=False,
                useable=True,
                use_message="You perform basic maintenance on your bike, improving its condition.",
                repair_value=15,
                aliases=["tools", "wrench", "kit"]
            ),
            "water_bottle": Item(
                name="Water Bottle",
                description="A metal water bottle, dented but functional. Clean water is precious in the wasteland.",
                useable=True,
                use_message="You drink deeply, feeling refreshed and ready to continue.",
                food_value=10,
                aliases=["water", "bottle", "drink"]
            ),
            "jerky": Item(
                name="Beef Jerky",
                description="Dried meat that's seen better days, but it's protein and it's yours.",
                useable=True,
                use_message="The salty meat gives you energy for the road ahead.",
                food_value=15,
                aliases=["meat", "food", "beef"]
            ),
            "gas_can": Item(
                name="Jerry Can",
                description="A red metal gas can, about half full. Fuel is life in the wasteland.",
                useable=True,
                use_message="You pour the precious fuel into your bike's tank.",
                fuel_value=25,
                aliases=["fuel", "gas", "gasoline", "petrol"]
            ),
            "spare_tire": Item(
                name="Motorcycle Tire",
                description="A knobby dual-sport tire, perfect for your bike. Still has good tread.",
                useable=True,
                use_message="You replace a worn tire, improving your bike's handling.",
                repair_value=20,
                aliases=["tire", "wheel", "rubber"]
            ),
            "fuel_siphon": Item(
                name="Fuel Siphon Hose",
                description="A length of rubber hose for extracting fuel from abandoned vehicles.",
                useable=True,
                use_message="You siphon fuel from a nearby wreck, adding to your reserves.",
                fuel_value=15,
                aliases=["siphon", "hose", "tube"]
            ),
            "canned_food": Item(
                name="Canned Beans",
                description="A dented can of beans. The label is faded but it's still sealed.",
                useable=True,
                use_message="You eat the beans cold. Not gourmet, but filling.",
                food_value=25,
                aliases=["beans", "can", "food"]
            ),
            "road_map": Item(
                name="Pre-War Road Atlas",
                description="A road atlas from before the bombs fell. Some routes may still be passable.",
                useable=True,
                use_message="You study the map, planning your route to Los Angeles.",
                aliases=["map", "atlas", "directions"]
            ),
            "rad_pills": Item(
                name="Rad-Away Pills",
                description="Anti-radiation medication. Essential for traveling through hot zones.",
                useable=True,
                use_message="You take a pill, feeling the radiation sickness subside.",
                food_value=5,
                aliases=["pills", "medicine", "radaway"]
            ),
            "mountain_gear": Item(
                name="Climbing Gear",
                description="Ropes, pitons, and carabiners. Useful for navigating treacherous terrain.",
                aliases=["rope", "climbing", "gear"]
            ),
            "trade_goods": Item(
                name="Trade Supplies",
                description="Miscellaneous items valuable for bartering with other survivors.",
                aliases=["supplies", "barter", "goods"]
            ),
            "fuel_barrel": Item(
                name="Fuel Barrel",
                description="A large barrel of high-quality gasoline. This could get you far.",
                useable=True,
                use_message="You fill your tank and spare containers with premium fuel.",
                fuel_value=50,
                aliases=["barrel", "drum", "gasoline"]
            ),
            "repair_kit": Item(
                name="Advanced Repair Kit",
                description="Professional-grade tools and parts for major motorcycle repairs.",
                useable=True,
                use_message="You perform extensive repairs, bringing your bike back to peak condition.",
                repair_value=40,
                aliases=["parts", "kit", "repairs"]
            ),
            "binoculars": Item(
                name="Military Binoculars",
                description="High-quality optics for scouting the road ahead and spotting danger.",
                useable=True,
                use_message="You scan the horizon, noting safe routes and potential hazards.",
                aliases=["scope", "optics", "glasses"]
            ),
            "high_octane_fuel": Item(
                name="High-Octane Racing Fuel",
                description="Premium racing fuel that will make your bike purr like a mountain cat.",
                useable=True,
                use_message="Your bike's engine roars with newfound power from the premium fuel.",
                fuel_value=35,
                aliases=["racing", "premium", "octane"]
            ),
            "ammunition": Item(
                name="Ammunition Box",
                description="A box of mixed ammunition. Useful for trading or protection.",
                aliases=["ammo", "bullets", "rounds"]
            ),
            "victory_flag": Item(
                name="California Republic Flag",
                description="A tattered flag from the old California Republic. A symbol of hope and your destination.",
                aliases=["flag", "banner", "california"]
            )
        }
    
    def get_current_location(self) -> Location:
        return self.locations[self.rider.current_location]
    
    def display_location(self):
        location = self.get_current_location()
        
        print("\n" + "="*60)
        print(f"🏍️  {location.name}")
        print("-" * len(location.name))
        print(location.description)
        
        if not location.visited:
            location.visited = True
            self.rider.miles_traveled += 50  # Each new location is ~50 miles
        
        # Show exits
        if location.exits:
            print(f"\n🛣️  Routes: {', '.join(location.exits.keys())}")
        
        # Show items
        if location.items:
            print(f"\n🎒 You spot: {', '.join([self.items[item].name for item in location.items])}")
        
        # Show status warnings
        if location.dangerous:
            print("⚠️  DANGER: This area looks hazardous!")
        
        self.show_status_brief()
    
    def show_status_brief(self):
        """Show brief status info"""
        fuel_bar = "█" * (self.rider.fuel // 10) + "░" * (10 - self.rider.fuel // 10)
        bike_bar = "█" * (self.rider.bike_condition // 10) + "░" * (10 - self.rider.bike_condition // 10)
        
        print(f"\n⛽ Fuel: [{fuel_bar}] {self.rider.fuel}%")
        print(f"🔧 Bike: [{bike_bar}] {self.rider.bike_condition}%")
        if self.rider.health < 100:
            health_bar = "█" * (self.rider.health // 10) + "░" * (10 - self.rider.health // 10)
            print(f"❤️  Health: [{health_bar}] {self.rider.health}%")
    
    def process_command(self, command: str) -> bool:
        """Process user command and return False if game should quit"""
        command = command.lower().strip()
        self.rider.days_survived += 0.1  # Each command represents time passing
        
        if not command:
            return True
            
        parts = command.split()
        verb = parts[0]
        
        # Movement commands
        if verb in ['ride', 'go', 'move', 'drive'] and len(parts) > 1:
            return self.move_rider(parts[1])
        elif verb in ['north', 'n', 'south', 's', 'east', 'e', 'west', 'w', 'up', 'down']:
            return self.move_rider(verb)
        
        # Item commands
        elif verb in ['take', 'get', 'pick', 'grab'] and len(parts) > 1:
            return self.take_item(' '.join(parts[1:]))
        elif verb in ['drop', 'leave'] and len(parts) > 1:
            return self.drop_item(' '.join(parts[1:]))
        elif verb in ['use', 'consume', 'drink', 'eat'] and len(parts) > 1:
            return self.use_item(' '.join(parts[1:]))
        
        # Bike-specific commands
        elif verb in ['refuel', 'fuel'] and len(parts) > 1:
            return self.refuel_bike(' '.join(parts[1:]))
        elif verb in ['repair', 'fix'] and len(parts) > 1:
            return self.repair_bike_with(' '.join(parts[1:]))
        elif verb in ['rest', 'sleep', 'camp']:
            return self.rest()
        
        # Information commands
        elif verb in ['look', 'l']:
            self.display_location()
        elif verb in ['inventory', 'i', 'inv', 'pack']:
            self.show_inventory()
        elif verb in ['examine', 'x', 'inspect'] and len(parts) > 1:
            self.examine_item(' '.join(parts[1:]))
        elif verb in ['status', 'stats', 'condition']:
            self.show_full_status()
        
        # Game commands
        elif verb in ['help', 'h']:
            self.show_help()
        elif verb in ['save']:
            self.save_game()
        elif verb in ['load']:
            self.load_game()
        elif verb in ['quit', 'q', 'exit']:
            return False
        
        else:
            responses = [
                "Your bike's engine idles as you consider that command...",
                "The wasteland wind carries away your words...",
                "That doesn't seem possible in this harsh world.",
                "Your survival instincts suggest trying something else."
            ]
            print(random.choice(responses))
            print("Type 'help' for available commands.")
        
        # Check for game over conditions
        if self.rider.fuel <= 0:
            print("\n💀 Your bike runs out of fuel in the middle of the wasteland...")
            print("Without transportation, you become another casualty of the apocalypse.")
            self.state = GameState.GAME_OVER
            return False
        
        if self.rider.bike_condition <= 0:
            print("\n💀 Your motorcycle breaks down beyond repair...")
            print("Stranded in the wasteland, your journey ends here.")
            self.state = GameState.GAME_OVER
            return False
        
        return True
    
    def move_rider(self, direction: str) -> bool:
        # Handle direction aliases
        direction_map = {
            'n': 'north', 's': 'south', 'e': 'east', 'w': 'west'
        }
        direction = direction_map.get(direction, direction)
        
        location = self.get_current_location()
        
        if direction in location.exits:
            # Check if bike can make the journey
            fuel_needed = location.fuel_cost
            if self.rider.fuel < fuel_needed:
                print(f"⛽ You don't have enough fuel to travel {direction}.")
                print(f"Need {fuel_needed} fuel, but only have {self.rider.fuel}.")
                return True
            
            # Use fuel and potentially damage bike
            self.rider.use_fuel(fuel_needed)
            
            # Rough terrain damages bike
            if fuel_needed > 3:
                damage = random.randint(1, 5)
                self.rider.damage_bike(damage)
                print(f"🔧 The rough terrain damages your bike (-{damage} condition)")
            
            # Move to new location
            self.rider.current_location = location.exits[direction]
            print(f"🏍️  You ride {direction}, engine roaring across the wasteland...")
            
            # Random events in dangerous areas
            new_location = self.get_current_location()
            if new_location.dangerous and random.random() < 0.3:
                self.random_encounter()
            
            self.display_location()
            
            # Check win condition (reached Los Angeles)
            if self.rider.current_location == "los_angeles":
                print("\n🎉 INCREDIBLE! You've made it to Los Angeles!")
                print("Against all odds, you've crossed the wasteland and reached the City of Angels!")
                print(f"Miles traveled: {self.rider.miles_traveled}")
                print(f"Days survived: {int(self.rider.days_survived)}")
                self.state = GameState.WON
                return False
        else:
            print(f"🚫 You can't ride {direction} from here.")
            print("Check your map and try a different route.")
        
        return True
    
    def random_encounter(self):
        """Handle random encounters in dangerous areas"""
        encounters = [
            "🏴‍☠️ Raiders spot you! You gun the engine and escape, but not without some bike damage.",
            "☢️ You ride through a radiation pocket. You feel sick but push through.",
            "🌪️ A dust storm hits! Visibility drops to zero, but you navigate by instinct.",
            "🐺 A pack of mutant wolves howls in the distance. You rev the engine to scare them off.",
            "⚡ Your bike hits a pothole hard. The suspension takes a beating."
        ]
        
        encounter = random.choice(encounters)
        print(f"\n{encounter}")
        
        # Apply random effects
        if "damage" in encounter.lower():
            damage = random.randint(5, 15)
            self.rider.damage_bike(damage)
        elif "sick" in encounter.lower():
            health_loss = random.randint(5, 10)
            self.rider.health = max(0, self.rider.health - health_loss)
    
    def refuel_bike(self, item_name: str) -> bool:
        """Refuel bike with fuel items"""
        item_id = self.find_item_by_name(item_name, self.rider.inventory)
        
        if item_id:
            item = self.items[item_id]
            if item.fuel_value > 0:
                old_fuel = self.rider.fuel
                self.rider.add_fuel(item.fuel_value)
                self.rider.remove_item(item_id)
                gained = self.rider.fuel - old_fuel
                print(f"⛽ You add fuel to your tank (+{gained} fuel)")
                print(f"Current fuel: {self.rider.fuel}%")
            else:
                print(f"❌ The {item.name} can't be used as fuel.")
        else:
            print(f"❌ You don't have any {item_name}.")
        
        return True
    
    def repair_bike_with(self, item_name: str) -> bool:
        """Repair bike with repair items"""
        item_id = self.find_item_by_name(item_name, self.rider.inventory)
        
        if item_id:
            item = self.items[item_id]
            if item.repair_value > 0:
                old_condition = self.rider.bike_condition
                self.rider.repair_bike(item.repair_value)
                if item.name == "Motorcycle Toolkit":
                    # Toolkit is reusable but less effective each time
                    print(f"🔧 You perform maintenance with your toolkit.")
                else:
                    self.rider.remove_item(item_id)
                    print(f"🔧 You use the {item.name} to repair your bike.")
                
                gained = self.rider.bike_condition - old_condition
                print(f"Bike condition improved by {gained}% (now {self.rider.bike_condition}%)")
            else:
                print(f"❌ The {item.name} can't be used for repairs.")
        else:
            print(f"❌ You don't have any {item_name}.")
        
        return True
    
    def rest(self) -> bool:
        """Rest to recover health but use time and fuel"""
        print("🏕️ You make camp and rest for the night...")
        print("The wasteland is quiet except for distant howls and the wind.")
        
        # Recover health
        health_gain = random.randint(10, 20)
        self.rider.health = min(100, self.rider.health + health_gain)
        
        # Use some fuel (bike idles for warmth/power)
        self.rider.use_fuel(2)
        
        # Advance time
        self.rider.days_survived += 1
        
        print(f"❤️  You feel refreshed (+{health_gain} health)")
        print(f"⛽ Your bike used some fuel overnight (-2 fuel)")
        
        return True
    
    def take_item(self, item_name: str) -> bool:
        location = self.get_current_location()
        
        # Find item by name or alias
        item_id = self.find_item_by_name(item_name, location.items)
        
        if item_id:
            item = self.items[item_id]
            if item.takeable:
                location.items.remove(item_id)
                self.rider.add_item(item_id)
                print(f"📦 You secure the {item.name} in your pack.")
            else:
                print(f"❌ You can't take the {item.name}.")
        else:
            print(f"❌ There's no {item_name} here to take.")
        
        return True
    
    def drop_item(self, item_name: str) -> bool:
        item_id = self.find_item_by_name(item_name, self.rider.inventory)
        
        if item_id:
            item = self.items[item_id]
            self.rider.remove_item(item_id)
            self.get_current_location().items.append(item_id)
            print(f"📦 You drop the {item.name} here.")
        else:
            print(f"❌ You don't have a {item_name} to drop.")
        
        return True
    
    def use_item(self, item_name: str) -> bool:
        item_id = self.find_item_by_name(item_name, self.rider.inventory)
        
        if item_id:
            item = self.items[item_id]
            if item.useable:
                print(f"🔧 {item.use_message}")
                
                # Apply item effects
                if item.fuel_value > 0:
                    old_fuel = self.rider.fuel
                    self.rider.add_fuel(item.fuel_value)
                    gained = self.rider.fuel - old_fuel
                    print(f"⛽ Fuel increased by {gained}% (now {self.rider.fuel}%)")
                
                if item.food_value > 0:
                    old_health = self.rider.health
                    self.rider.health = min(100, self.rider.health + item.food_value)
                    gained = self.rider.health - old_health
                    print(f"❤️  Health increased by {gained}% (now {self.rider.health}%)")
                
                if item.repair_value > 0:
                    old_condition = self.rider.bike_condition
                    self.rider.repair_bike(item.repair_value)
                    gained = self.rider.bike_condition - old_condition
                    print(f"🔧 Bike condition improved by {gained}% (now {self.rider.bike_condition}%)")
                
                # Remove consumable items
                if item.fuel_value > 0 or item.food_value > 0:
                    if item.name != "Motorcycle Toolkit":  # Toolkit is reusable
                        self.rider.remove_item(item_id)
                
            else:
                print(f"❌ You can't use the {item.name} right now.")
        else:
            print(f"❌ You don't have a {item_name} in your pack.")
        
        return True
    
    def find_item_by_name(self, name: str, item_list: List[str]) -> Optional[str]:
        """Find item by name or alias"""
        name = name.lower()
        for item_id in item_list:
            item = self.items[item_id]
            if (name in item.name.lower() or 
                name == item_id.lower() or 
                any(alias.lower() == name for alias in item.aliases)):
                return item_id
        return None
    
    def examine_item(self, item_name: str):
        # Check inventory first
        item_id = self.find_item_by_name(item_name, self.rider.inventory)
        if not item_id:
            # Check current location
            location = self.get_current_location()
            item_id = self.find_item_by_name(item_name, location.items)
        
        if item_id:
            item = self.items[item_id]
            print(f"\n🔍 {item.name}")
            print(f"   {item.description}")
            
            # Show item stats
            if item.fuel_value > 0:
                print(f"   ⛽ Fuel value: +{item.fuel_value}")
            if item.food_value > 0:
                print(f"   ❤️  Health value: +{item.food_value}")
            if item.repair_value > 0:
                print(f"   🔧 Repair value: +{item.repair_value}")
        else:
            print(f"❌ You don't see a {item_name} here.")
    
    def show_inventory(self):
        if self.rider.inventory:
            print("\n🎒 SURVIVAL PACK:")
            for item_id in self.rider.inventory:
                item = self.items[item_id]
                print(f"  • {item.name}")
                if item.fuel_value > 0 or item.food_value > 0 or item.repair_value > 0:
                    values = []
                    if item.fuel_value > 0:
                        values.append(f"⛽{item.fuel_value}")
                    if item.food_value > 0:
                        values.append(f"❤️{item.food_value}")
                    if item.repair_value > 0:
                        values.append(f"🔧{item.repair_value}")
                    print(f"    ({' '.join(values)})")
        else:
            print("\n🎒 Your pack is empty.")
    
    def show_full_status(self):
        print(f"\n📊 RIDER STATUS:")
        print(f"🏍️  Location: {self.get_current_location().name}")
        print(f"🛣️  Miles Traveled: {self.rider.miles_traveled}")
        print(f"📅 Days Survived: {int(self.rider.days_survived)}")
        print(f"❤️  Health: {self.rider.health}%")
        print(f"⛽ Fuel: {self.rider.fuel}%")
        print(f"🔧 Bike Condition: {self.rider.bike_condition}%")
        
        # Distance to LA (rough estimate)
        distance_remaining = 2500 - self.rider.miles_traveled
        print(f"🎯 Estimated miles to Los Angeles: {max(0, distance_remaining)}")
    
    def show_help(self):
        print("""
🏍️  WASTELAND RIDER COMMANDS:
═══════════════════════════════════════════════════════════════

🛣️  MOVEMENT:
   ride <direction> | north/n, south/s, east/e, west/w
   
🎒 ITEMS:
   take <item>     - Pick up items from the wasteland
   drop <item>     - Drop items from your pack
   use <item>      - Consume food, fuel, or medicine
   examine <item>  - Get detailed information about items
   
🔧 BIKE MAINTENANCE:
   refuel <item>   - Add fuel to your tank
   repair <item>   - Fix your bike with tools/parts
   rest            - Make camp and recover health
   
📊 INFORMATION:
   look/l          - Look around your current location
   inventory/i     - Check your survival pack
   status          - View detailed rider and bike status
   
💾 GAME:
   save            - Save your progress
   load            - Load saved game
   help/h          - Show this help
   quit/q          - End your journey

💡 SURVIVAL TIPS:
• Keep your fuel tank full - running out means death
• Maintain your bike - breakdowns are fatal
• Rest when injured, but watch your fuel consumption
• Dangerous areas have better loot but more risks
• Your goal: Reach Los Angeles alive!
        """)
    
    def save_game(self):
        try:
            save_data = {
                'rider': {
                    'inventory': self.rider.inventory,
                    'current_location': self.rider.current_location,
                    'health': self.rider.health,
                    'fuel': self.rider.fuel,
                    'bike_condition': self.rider.bike_condition,
                    'miles_traveled': self.rider.miles_traveled,
                    'days_survived': self.rider.days_survived
                },
                'locations': {loc_id: asdict(location) for loc_id, location in self.locations.items()}
            }
            
            with open('wasteland_save.json', 'w') as f:
                json.dump(save_data, f, indent=2)
            print("💾 Game saved successfully!")
        except Exception as e:
            print(f"❌ Error saving game: {e}")
    
    def load_game(self):
        try:
            with open('wasteland_save.json', 'r') as f:
                save_data = json.load(f)
            
            # Restore rider state
            rider_data = save_data['rider']
            self.rider.inventory = rider_data['inventory']
            self.rider.current_location = rider_data['current_location']
            self.rider.health = rider_data['health']
            self.rider.fuel = rider_data['fuel']
            self.rider.bike_condition = rider_data['bike_condition']
            self.rider.miles_traveled = rider_data['miles_traveled']
            self.rider.days_survived = rider_data['days_survived']
            
            # Restore location states
            for loc_id, loc_data in save_data['locations'].items():
                self.locations[loc_id] = Location(**loc_data)
            
            print("💾 Game loaded successfully!")
            self.display_location()
        except FileNotFoundError:
            print("❌ No saved game found.")
        except Exception as e:
            print(f"❌ Error loading game: {e}")
    
    def run(self):
        print("🏍️  WASTELAND RIDER")
        print("=" * 50)
        print("The year is 2087. The bombs fell decades ago.")
        print("You're a lone rider on a dual-sport motorcycle,")
        print("trying to get from Washington DC to Los Angeles")
        print("across 2,500 miles of post-apocalyptic wasteland.")
        print("\nYour bike is your lifeline. Your fuel is your blood.")
        print("The road is long, dangerous, and unforgiving.")
        print("\nType 'help' for commands. Good luck, rider.")
        print("=" * 50)
        
        self.display_location()
        
        while self.state == GameState.PLAYING:
            try:
                command = input("\n🏍️ > ").strip()
                if not self.process_command(command):
                    break
            except KeyboardInterrupt:
                print("\n\n🏍️ Safe travels, wasteland rider!")
                break
            except EOFError:
                break
        
        if self.state == GameState.WON:
            print(f"\n🎉 VICTORY! You've conquered the wasteland!")
            print(f"Miles traveled: {self.rider.miles_traveled}")
            print(f"Days survived: {int(self.rider.days_survived)}")
            print("You are a true wasteland legend!")
        elif self.state == GameState.GAME_OVER:
            print(f"\n💀 GAME OVER")
            print(f"Miles traveled: {self.rider.miles_traveled}")
            print(f"Days survived: {int(self.rider.days_survived)}")
            print("The wasteland claims another soul...")
        else:
            print(f"\n🏍️ Thanks for riding! Miles traveled: {self.rider.miles_traveled}")


if __name__ == "__main__":
    game = WastelandEngine()
    game.run()
