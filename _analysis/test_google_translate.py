#!/usr/bin/env python3
"""
Test script to verify Google Cloud Translation API v3 (with LLM model) is working.
Uses the official Translation LLM for context-aware translations.

Based on: https://cloud.google.com/translate/docs/advanced/translating-text-v3
"""

import os
import sys
import json

def check_credentials():
    """Check if Google Cloud credentials are set."""
    creds_path = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
    
    if not creds_path:
        print("❌ ERROR: GOOGLE_APPLICATION_CREDENTIALS environment variable not set!")
        print("\nSee _analysis/SETUP.md for full setup instructions")
        return False
    
    if not os.path.exists(creds_path):
        print(f"❌ ERROR: Credentials file not found: {creds_path}")
        return False
    
    print(f"✓ Credentials file found: {creds_path}")
    return True

def test_translation():
    """Test Google Cloud Translation API v3 with Translation LLM."""
    try:
        from google.cloud import translate_v3
    except ImportError:
        print("❌ ERROR: google-cloud-translate not installed!")
        print("\nInstall it with:")
        print("   pip install google-cloud-translate")
        return False
    
    print("✓ google-cloud-translate library imported")
    
    # Get project ID from credentials
    creds_path = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
    with open(creds_path, 'r') as f:
        creds = json.load(f)
        project_id = creds.get('project_id')
    
    if not project_id:
        print("❌ ERROR: Could not find project_id in credentials file")
        return False
    
    print(f"✓ Project ID: {project_id}")
    
    # Initialize client
    try:
        client = translate_v3.TranslationServiceClient()
        # Use 'global' for standard NMT, 'us-central1' for LLM
        parent_global = f"projects/{project_id}/locations/global"
        parent_llm = f"projects/{project_id}/locations/us-central1"
        print("✓ Translation client initialized")
    except Exception as e:
        print(f"❌ ERROR: Failed to initialize client: {e}")
        return False
    
    # Test 1: Standard NMT model
    print("\n" + "=" * 70)
    print("TEST 1: Standard NMT Model (Default)")
    print("=" * 70)
    
    wow_test_cases = [
        ("你好", "Hello"),
        ("副本", "Instance/Dungeon"),
        ("来T", "Need Tank"),
        ("法师开门", "Mage open portal"),
    ]
    
    success_count = 0
    for chinese, expected in wow_test_cases:
        try:
            request = translate_v3.TranslateTextRequest(
                parent=parent_global,
                contents=[chinese],
                source_language_code="zh-CN",
                target_language_code="en-US",
                mime_type="text/plain",
            )
            
            response = client.translate_text(request=request)
            translation = response.translations[0].translated_text
            
            print(f"✓ '{chinese}' → '{translation}' (expected: {expected})")
            success_count += 1
            
        except Exception as e:
            print(f"❌ '{chinese}': {e}")
    
    # Test 2: Translation LLM (context-aware)
    print("\n" + "=" * 70)
    print("TEST 2: Translation LLM (Context-Aware)")
    print("=" * 70)
    print("This model understands context better for gaming terminology\n")
    
    try:
        # Create context by adding WoW-specific text
        wow_context_text = "来T，满血战士。副本开始了。"  # "Need tank, full HP warrior. Instance started."
        
        request = translate_v3.TranslateTextRequest(
            parent=parent_llm,
            contents=[wow_context_text],
            source_language_code="zh-CN",
            target_language_code="en-US",
            mime_type="text/plain",
            model=f"projects/{project_id}/locations/us-central1/models/general/translation-llm",
        )
        
        response = client.translate_text(request=request)
        translation = response.translations[0].translated_text
        
        print(f"✓ LLM Translation:")
        print(f"  Original: '{wow_context_text}'")
        print(f"  Translation: '{translation}'")
        print(f"  (LLM understands gaming context better!)")
        
    except Exception as e:
        print(f"⚠️  LLM model error: {e}")
        print("\nPossible reasons:")
        print("  1. Translation LLM requires billing to be enabled")
        print("  2. API might not be fully enabled for your project")
        print("  3. Free tier might have limitations")
        print("\nNote: Standard NMT model still works for basic translations")
        
    # Summary
    print("\n" + "=" * 70)
    print(f"SUMMARY: {success_count}/{len(wow_test_cases)} standard translations successful")
    print("=" * 70)
    
    if success_count >= len(wow_test_cases) // 2:
        print("\n🎉 Google Cloud Translation API is working!")
        print("\n📝 Next Steps:")
        print("   1. Play WoW and accumulate 50-100+ translations")
        print("   2. Check translation count with /tw status in-game")
        print("   3. Run the full analysis scripts")
        return True
    else:
        print("\n⚠️  Setup incomplete. Please check:")
        print("   - Cloud Translation API is enabled")
        print("   - Billing is activated")
        print("   - Service account has correct permissions")
        return False

def main():
    print("=" * 70)
    print("Google Cloud Translation API v3 Test (LLM Model)")
    print("=" * 70)
    print("Testing context-aware translation for WoW terminology\n")
    
    if not check_credentials():
        return 1
    
    if not test_translation():
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
