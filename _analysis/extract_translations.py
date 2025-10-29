#!/usr/bin/env python3
"""
Extract translations from TranslateWoW SavedVariables for analysis.
"""

import re
import os
import csv
from pathlib import Path

def find_savedvariables_file():
    """Find the TranslateWoW SavedVariables file."""
    # Look for WTF folder relative to addon directory
    addon_dir = Path(__file__).parent.parent
    wtf_path = addon_dir.parent.parent.parent / "WTF"
    
    if not wtf_path.exists():
        print(f"Error: WTF folder not found at {wtf_path}")
        return None
    
    # Find TranslateWoW.lua in SavedVariables
    for sv_file in wtf_path.rglob("TranslateWoW.lua"):
        if "SavedVariables" in str(sv_file):
            return sv_file
    
    print("Error: TranslateWoW.lua not found in SavedVariables")
    return None

def parse_lua_table(content):
    """Parse Lua table format to extract translation_log entries."""
    translations = {}
    
    # Find translation_log section
    log_match = re.search(r'\["translation_log"\]\s*=\s*\{(.*?)\n\t\}', content, re.DOTALL)
    if not log_match:
        print("Warning: No translation_log found")
        return translations
    
    log_content = log_match.group(1)
    
    # Extract key-value pairs: ["chinese"] = "english",
    pattern = r'\["(.+?)"\]\s*=\s*"(.+?)"(?:,|\n)'
    matches = re.finditer(pattern, log_content, re.DOTALL)
    
    for match in matches:
        chinese = match.group(1)
        english = match.group(2)
        
        # Unescape Lua strings
        chinese = chinese.replace(r'\"', '"').replace(r'\\', '\\')
        english = english.replace(r'\"', '"').replace(r'\\', '\\')
        
        translations[chinese] = english
    
    return translations

def clean_text(text):
    """Remove WoW markup and hyperlinks for clean analysis."""
    # Remove WoW color codes
    text = re.sub(r'\|c[0-9a-fA-F]{8}', '', text)
    text = re.sub(r'\|r', '', text)
    
    # Remove texture codes
    text = re.sub(r'\|T[^|]+\|t', '', text)
    
    # Extract text from hyperlinks but keep the display text
    text = re.sub(r'\|H[^|]+\|h\[([^\]]+)\]\|h', r'\1', text)
    
    # Remove placeholder patterns
    text = re.sub(r'<<WOW\d+>>', '', text)
    text = re.sub(r'<<HYPERLINK\d+>>', '', text)
    
    # Remove channel prefixes
    text = re.sub(r'^\[\d+\.\s*\w+\]\s*', '', text)
    text = re.sub(r'<\w+>', '', text)
    
    return text.strip()

def extract_chinese_segments(text):
    """Extract pure Chinese text segments from mixed content."""
    # Find Chinese character sequences
    chinese_pattern = r'[\u4e00-\u9fff，。！？、；：]+'
    segments = re.findall(chinese_pattern, text)
    return segments

def main():
    print("=" * 70)
    print("TranslateWoW Translation Extractor")
    print("=" * 70)
    
    # Find SavedVariables file
    sv_file = find_savedvariables_file()
    if not sv_file:
        return 1
    
    print(f"\nFound SavedVariables: {sv_file}")
    
    # Read file
    with open(sv_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse translations
    translations = parse_lua_table(content)
    print(f"Extracted {len(translations)} translation pairs")
    
    if not translations:
        print("No translations found. Play the game to generate translation logs.")
        return 1
    
    # Prepare output data
    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)
    
    # Full translations (with markup)
    full_csv = output_dir / "translations_full.csv"
    with open(full_csv, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Chinese (Original)', 'English (Dictionary)', 'Chinese Length', 'English Length'])
        for chinese, english in translations.items():
            writer.writerow([chinese, english, len(chinese), len(english)])
    
    print(f"Saved full translations to: {full_csv}")
    
    # Clean translations (markup removed)
    clean_csv = output_dir / "translations_clean.csv"
    clean_pairs = []
    
    for chinese, english in translations.items():
        chinese_clean = clean_text(chinese)
        english_clean = clean_text(english)
        
        if chinese_clean and english_clean:
            clean_pairs.append((chinese_clean, english_clean))
    
    # Remove duplicates
    clean_pairs = list(set(clean_pairs))
    clean_pairs.sort(key=lambda x: len(x[0]), reverse=True)
    
    with open(clean_csv, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Chinese', 'English'])
        for chinese, english in clean_pairs:
            writer.writerow([chinese, english])
    
    print(f"Saved clean translations to: {clean_csv}")
    print(f"Total unique clean pairs: {len(clean_pairs)}")
    
    # Extract Chinese-only segments for dictionary analysis
    segments_csv = output_dir / "chinese_segments.csv"
    all_segments = set()
    
    for chinese, _ in translations.items():
        segments = extract_chinese_segments(chinese)
        all_segments.update(segments)
    
    all_segments = sorted(all_segments, key=len, reverse=True)
    
    with open(segments_csv, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Chinese Segment', 'Length'])
        for segment in all_segments:
            writer.writerow([segment, len(segment)])
    
    print(f"Saved Chinese segments to: {segments_csv}")
    print(f"Total unique segments: {len(all_segments)}")
    
    # Summary
    print("\n" + "=" * 70)
    print("Extraction Complete!")
    print("=" * 70)
    print(f"Output directory: {output_dir}")
    print(f"\nFiles created:")
    print(f"  1. {full_csv.name} - Full translations with WoW markup")
    print(f"  2. {clean_csv.name} - Clean translations ready for Google API")
    print(f"  3. {segments_csv.name} - Chinese segments for dictionary mining")
    print(f"\nNext step: Run compare_with_google.py to analyze accuracy")
    
    return 0

if __name__ == "__main__":
    exit(main())

