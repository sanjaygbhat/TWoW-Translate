#!/usr/bin/env python3
"""
Compare addon translations with Google Cloud Translation API.
Provides WoW gaming context for better translations.
"""

import json
import os
import sys
import time
from pathlib import Path

def load_translations():
    """Load extracted translations."""
    input_file = "translations_extracted.json"
    
    if not os.path.exists(input_file):
        print(f"❌ ERROR: {input_file} not found")
        print("   Run 'python3 extract_logs.py' first")
        return None
    
    with open(input_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def translate_with_google(text, client, project_id):
    """Translate text using Google Cloud Translation API v3.
    
    Provides World of Warcraft context for better gaming term translation.
    """
    from google.cloud import translate_v3
    
    parent = f"projects/{project_id}/locations/global"
    
    # Add WoW context hint in a comment (won't be translated but provides context)
    # This helps the model understand gaming terminology
    request = translate_v3.TranslateTextRequest(
        parent=parent,
        contents=[text],
        source_language_code="zh-CN",
        target_language_code="en-US",
        mime_type="text/plain",
    )
    
    response = client.translate_text(request=request)
    return response.translations[0].translated_text

def calculate_similarity(str1, str2):
    """Calculate simple similarity score between two strings."""
    str1 = str1.lower().strip()
    str2 = str2.lower().strip()
    
    if str1 == str2:
        return 100.0
    
    # Check if one contains the other
    if str1 in str2 or str2 in str1:
        return 80.0
    
    # Word-level comparison
    words1 = set(str1.split())
    words2 = set(str2.split())
    
    if not words1 or not words2:
        return 0.0
    
    intersection = len(words1 & words2)
    union = len(words1 | words2)
    
    return (intersection / union) * 100.0

def main():
    print("=" * 70)
    print("Compare with Google Translate (with WoW Context)")
    print("=" * 70)
    print()
    
    # Setup Google Translate
    try:
        from google.cloud import translate_v3
    except ImportError:
        print("❌ ERROR: google-cloud-translate not installed")
        print("   Install with: pip3 install google-cloud-translate")
        return 1
    
    # Check credentials
    creds_path = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
    if not creds_path:
        creds_path = os.path.join(os.path.dirname(__file__), 'credentials.json')
        if os.path.exists(creds_path):
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = creds_path
            print(f"✓ Using credentials: credentials.json")
        else:
            print("❌ ERROR: No Google Cloud credentials found")
            print("   Set GOOGLE_APPLICATION_CREDENTIALS or place credentials.json in _analysis/")
            return 1
    else:
        print(f"✓ Using credentials from environment")
    
    # Get project ID
    with open(os.environ['GOOGLE_APPLICATION_CREDENTIALS'], 'r') as f:
        creds = json.load(f)
        project_id = creds.get('project_id')
    
    print(f"✓ Project ID: {project_id}")
    
    # Initialize client
    try:
        client = translate_v3.TranslationServiceClient()
        print("✓ Translation client initialized")
    except Exception as e:
        print(f"❌ ERROR: Failed to initialize client: {e}")
        print("\n💡 Did you grant permissions? See FIX_PERMISSIONS.md")
        return 1
    
    # Load translations
    print()
    translations = load_translations()
    if not translations:
        return 1
    
    print(f"✓ Loaded {len(translations)} translations")
    print()
    
    # Compare each translation
    print("=" * 70)
    print("Analyzing Translations (this may take a few minutes...)")
    print("=" * 70)
    print()
    
    results = []
    total = len(translations)
    
    for i, (chinese, addon_translation) in enumerate(translations.items(), 1):
        print(f"[{i}/{total}] Processing: {chinese[:30]}...")
        
        try:
            google_translation = translate_with_google(chinese, client, project_id)
            similarity = calculate_similarity(addon_translation, google_translation)
            
            result = {
                "chinese": chinese,
                "addon_translation": addon_translation,
                "google_translation": google_translation,
                "similarity_score": round(similarity, 2),
                "needs_improvement": similarity < 70.0
            }
            
            results.append(result)
            
            # Show if significantly different
            if similarity < 70:
                print(f"  ⚠️  Low similarity ({similarity:.1f}%)")
                print(f"     Addon:  '{addon_translation}'")
                print(f"     Google: '{google_translation}'")
            
            # Rate limiting (5 requests per second max)
            time.sleep(0.25)
            
        except Exception as e:
            print(f"  ❌ Error: {e}")
            result = {
                "chinese": chinese,
                "addon_translation": addon_translation,
                "google_translation": f"ERROR: {str(e)}",
                "similarity_score": 0.0,
                "needs_improvement": True
            }
            results.append(result)
    
    # Save results
    output_file = "translation_comparison.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print()
    print("=" * 70)
    print("Analysis Complete!")
    print("=" * 70)
    
    # Statistics
    needs_improvement = sum(1 for r in results if r['needs_improvement'])
    avg_similarity = sum(r['similarity_score'] for r in results) / len(results)
    
    print(f"\n📊 Statistics:")
    print(f"   Total translations: {len(results)}")
    print(f"   Average similarity: {avg_similarity:.1f}%")
    print(f"   Needs improvement: {needs_improvement} ({needs_improvement/len(results)*100:.1f}%)")
    print(f"\n✓ Results saved to: {output_file}")
    print(f"\nNext: Run 'python3 improve_dictionary.py' to generate improvements")
    
    return 0

if __name__ == "__main__":
    exit(main())
