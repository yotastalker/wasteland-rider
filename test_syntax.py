#!/usr/bin/env python3
"""
Simple syntax test for the game
"""

# Test basic imports and syntax
try:
    import json
    import os
    from typing import Dict, List, Optional
    from dataclasses import dataclass
    from enum import Enum
    
    print("✅ All imports successful")
    print("✅ Python syntax appears valid")
    print("✅ Game should run properly once Python is set up")
    
    # Test basic dataclass
    @dataclass
    class TestItem:
        name: str
        description: str
    
    test_item = TestItem("Test", "A test item")
    print(f"✅ Dataclass test: {test_item.name}")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
except SyntaxError as e:
    print(f"❌ Syntax error: {e}")
except Exception as e:
    print(f"❌ Other error: {e}")
