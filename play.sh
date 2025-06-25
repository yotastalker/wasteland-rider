#!/bin/bash
# Wasteland Rider - Easy Game Launcher

echo "🏍️  WASTELAND RIDER - Starting Game..."
echo "====================================="
echo

# Check if Python is available
if command -v python3 &> /dev/null; then
    python3 game.py
elif command -v python &> /dev/null; then
    python game.py
else
    echo "❌ Python not found!"
    echo "Please install Python from https://python.org"
    echo
    echo "On Mac, you can also install via:"
    echo "• App Store (search for Python)"
    echo "• Homebrew: brew install python"
    echo
    read -p "Press Enter to exit..."
    exit 1
fi

echo
echo "Thanks for playing Wasteland Rider!"
read -p "Press Enter to exit..."
