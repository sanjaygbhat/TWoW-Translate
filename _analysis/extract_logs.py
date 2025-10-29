#!/usr/bin/env python3
"""
Extract translation logs from WoW SavedVariables file.
Outputs the translations for analysis.
"""

import json
import os
import re
from pathlib import Path

# Paths
SAVEDVARIABLES_PATH = "/Users/sanjaybhat/Downloads/twmoa_1180/WTF/Account/BBBNEO/SavedVariables/TranslateWoW.lua"
OUTPUT_FILE = "translations_extracted.json"

def parse_lua_table(content):
    """Parse Lua table from SavedVariables file."""
    translations = {}
    
    # Find the translation_log table
    match = re.search(r'\["translation_log"\]\s*=\s*\{([^}]*)\}', content, re.DOTALL)
    if not match:
        print("⚠️  No translation_log found in SavedVariables")
        return translations
    
    table_content = match.group(1)
    
    # Extract key-value pairs
    # Format: ["中文"] = "English",
    pattern = r'\["([^"]+)"\]\s*=\s*"([^"]*)"'
    matches = re.findall(pattern, table_content)
    
    for chinese, english in matches:
        # Unescape any escaped characters
        chinese = chinese.replace('\\"', '"').replace('\\\\', '\\')
        english = english.replace('\\"', '"').replace('\\\\', '\\')
        translations[chinese] = english
    
    return translations

def main():
    print("=" * 70)
    print("Extract Translation Logs")
    print("=" * 70)
    print()
    
    # Check if SavedVariables file exists
    if not os.path.exists(SAVEDVARIABLES_PATH):
        print(f"❌ ERROR: SavedVariables file not found:")
        print(f"   {SAVEDVARIABLES_PATH}")
        print("\nMake sure you've:")
        print("  1. Played WoW and seen Chinese chat")
        print("  2. Exited WoW completely (so it saves)")
        return 1
    
    print(f"✓ Found SavedVariables file")
    
    # Read the file
    try:
        with open(SAVEDVARIABLES_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ ERROR reading file: {e}")
        return 1
    
    print(f"✓ Read {len(content)} characters")
    
    # Parse translations
    translations = parse_lua_table(content)
    
    if not translations:
        print("\n⚠️  No translations found!")
        print("   Make sure you've used /tw to translate some messages in-game")
        return 1
    
    print(f"✓ Extracted {len(translations)} translations")
    
    # Save to JSON
    output_path = os.path.join(os.path.dirname(__file__), OUTPUT_FILE)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(translations, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Saved to: {OUTPUT_FILE}")
    
    # Show some examples
    print("\n" + "=" * 70)
    print("Sample Translations (first 5):")
    print("=" * 70)
    for i, (chinese, english) in enumerate(list(translations.items())[:5]):
        print(f"{i+1}. '{chinese}' → '{english}'")
    
    print("\n" + "=" * 70)
    print(f"✅ Successfully extracted {len(translations)} translations")
    print("=" * 70)
    print(f"\nNext: Run 'python3 compare_with_google.py' to analyze")
    
    return 0

if __name__ == "__main__":
    exit(main())

