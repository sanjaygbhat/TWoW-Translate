#!/usr/bin/env python3
"""
Generate dictionary improvements from translation comparison.
Creates Lua code to update the TranslateWoW_Dictionary.lua file.
"""

import json
import os
from datetime import datetime

def load_comparison():
    """Load comparison results."""
    input_file = "translation_comparison.json"
    
    if not os.path.exists(input_file):
        print(f"❌ ERROR: {input_file} not found")
        print("   Run 'python3 compare_with_google.py' first")
        return None
    
    with open(input_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def escape_lua_string(s):
    """Escape string for Lua."""
    s = s.replace('\\', '\\\\')
    s = s.replace('"', '\\"')
    s = s.replace('\n', '\\n')
    s = s.replace('\r', '\\r')
    return s

def main():
    print("=" * 70)
    print("Generate Dictionary Improvements")
    print("=" * 70)
    print()
    
    # Load comparison results
    results = load_comparison()
    if not results:
        return 1
    
    print(f"✓ Loaded {len(results)} comparison results")
    
    # Filter items that need improvement
    improvements = [r for r in results if r['needs_improvement']]
    
    if not improvements:
        print("\n🎉 No improvements needed! Dictionary is already accurate.")
        return 0
    
    print(f"✓ Found {len(improvements)} items to improve")
    print()
    
    # Generate Lua dictionary updates
    print("=" * 70)
    print("Generating Dictionary Updates")
    print("=" * 70)
    print()
    
    lua_updates = []
    for item in improvements:
        chinese = escape_lua_string(item['chinese'])
        google_trans = escape_lua_string(item['google_translation'])
        addon_trans = escape_lua_string(item['addon_translation'])
        score = item['similarity_score']
        
        lua_updates.append({
            'chinese': chinese,
            'old_translation': addon_trans,
            'new_translation': google_trans,
            'score': score
        })
    
    # Create output file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"dictionary_improvements_{timestamp}.lua"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("-- Dictionary Improvements\n")
        f.write(f"-- Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"-- Total improvements: {len(lua_updates)}\n")
        f.write("--\n")
        f.write("-- Instructions:\n")
        f.write("--   1. Open TranslateWoW_Dictionary.lua\n")
        f.write("--   2. Find each Chinese phrase below\n")
        f.write("--   3. Update its translation to the suggested version\n")
        f.write("--\n\n")
        
        for i, update in enumerate(lua_updates, 1):
            chinese = update['chinese']
            old_trans = update['old_translation']
            new_trans = update['new_translation']
            score = update['score']
            
            f.write(f"-- Entry {i}/{len(lua_updates)} (Similarity: {score:.1f}%)\n")
            f.write(f'-- Chinese: "{chinese}"\n')
            f.write(f'-- OLD: "{old_trans}"\n')
            f.write(f'-- NEW: "{new_trans}"\n')
            f.write(f'["{chinese}"] = "{new_trans}",\n\n')
    
    print(f"✓ Generated: {output_file}")
    print()
    
    # Create a summary report
    summary_file = f"improvement_summary_{timestamp}.txt"
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("=" * 70 + "\n")
        f.write("Translation Improvement Summary\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total entries analyzed: {len(results)}\n")
        f.write(f"Entries needing improvement: {len(improvements)}\n")
        f.write(f"Average similarity of improved entries: {sum(u['score'] for u in lua_updates) / len(lua_updates):.1f}%\n\n")
        
        f.write("=" * 70 + "\n")
        f.write("Top 10 Most Different Translations\n")
        f.write("=" * 70 + "\n\n")
        
        sorted_updates = sorted(lua_updates, key=lambda x: x['score'])[:10]
        for i, update in enumerate(sorted_updates, 1):
            f.write(f"{i}. Similarity: {update['score']:.1f}%\n")
            f.write(f"   Chinese: {update['chinese']}\n")
            f.write(f"   Addon:   {update['old_translation']}\n")
            f.write(f"   Google:  {update['new_translation']}\n\n")
    
    print(f"✓ Created summary: {summary_file}")
    print()
    
    # Final summary
    print("=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"\n📊 Statistics:")
    print(f"   Total translations: {len(results)}")
    print(f"   Need improvement: {len(improvements)} ({len(improvements)/len(results)*100:.1f}%)")
    print(f"   Already good: {len(results) - len(improvements)} ({(len(results)-len(improvements))/len(results)*100:.1f}%)")
    
    print(f"\n📝 Files created:")
    print(f"   {output_file} - Lua dictionary entries to update")
    print(f"   {summary_file} - Human-readable summary")
    
    print(f"\n✅ Done! Review the files and update your dictionary.")
    
    return 0

if __name__ == "__main__":
    exit(main())

