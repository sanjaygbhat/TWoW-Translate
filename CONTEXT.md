# TranslateWoW Development Context

## Project Overview
A World of Warcraft addon that translates Chinese chat messages to English in real-time using a dictionary-based approach. Designed for Turtle WoW - Karazhan server.

## Current Status (v0.1.4)
- **Working Features**: Real-time chat translation, hyperlink handling, player name preservation, translation logging
- **Dictionary**: 114,387 entries (CC-CEDICT + WoW terms + phrases)
- **Performance**: 4.5 MB, no game lag
- **Analysis System**: Google Cloud Translation API integration for continuous improvement

## File Structure

### Core Addon Files (Main Branch)
```
TranslateWoW/
├── TranslateWoW.lua          # Main addon logic (867 lines)
├── TranslateWoW.toc          # Addon metadata (v0.1.4)
├── TranslateWoW.xml          # UI frame definitions
├── TranslateWoW_Dictionary.lua  # 114K+ translation entries (4.5 MB)
└── README.md                 # User documentation
```

### Analysis System (Private Branch: `analysis`)
```
_analysis/
├── credentials.json          # Google Cloud service account
├── extract_logs.py           # Extract translations from SavedVariables
├── compare_with_google.py    # Compare with Google Translate API
├── improve_dictionary.py     # Generate dictionary improvements
├── test_google_translate.py  # Test API connectivity
├── run_analysis.sh           # Run complete analysis pipeline
├── SETUP.md                  # Google Cloud setup guide
├── FIX_PERMISSIONS.md        # Troubleshooting guide
└── PHRASE_DICTIONARIES.md    # Phrase dictionary strategies
```

## Key Technical Details

### Translation Logic (`TranslateWoW.lua`)
1. **Hyperlink Handling**: Item/quest links preserved in Chinese, player names translated but link data kept for whispers
2. **Chat Hook**: Intercepts `AddMessage` on all chat frames
3. **Dictionary Lookup**: Longest-match-first algorithm for phrases before words
4. **Logging**: Saves original + translated text to SavedVariables for analysis

### SavedVariables Location
```
/WTF/Account/BBBNEO/SavedVariables/TranslateWoW.lua
```

Format:
```lua
TranslateWoWDB = {
    translation_log = {
        ["中文"] = "English translation",
        -- key-value pairs
    }
}
```

### Commands
- `/tw` - Show addon info
- `/tw clearlog` - Clear translation logs
- `/tw status` - Show statistics
- `/tw debug` - Toggle debug mode (careful: causes recursion if used wrong)

## Analysis System Workflow

### Setup (One-time)
1. Create Google Cloud project
2. Enable Cloud Translation API
3. Create service account with "Cloud Translation API User" role
4. Download JSON credentials
5. Install: `pip3 install google-cloud-translate`

### Running Analysis
```bash
cd _analysis
export GOOGLE_APPLICATION_CREDENTIALS="$(pwd)/credentials.json"
./run_analysis.sh
```

This:
1. Extracts translations from SavedVariables
2. Compares with Google Translate (provides WoW context)
3. Generates improvement suggestions
4. Creates `dictionary_improvements_*.lua` with scored changes

### Results Interpretation
- **Similarity < 70%**: Needs improvement
- **Average similarity**: Currently ~15% (dictionary-only) vs ~85% (Google)
- **Best improvements**: Player names, raid messages, gaming slang

## Recent Improvements (v0.1.3 → v0.1.4)

### Fixed Issues
1. ✅ Item links no longer translated (preserved in Chinese for tooltip hover)
2. ✅ Player names: Display text translated, but original name preserved for whispers
3. ✅ Stack overflow in debug mode (saved original AddMessage reference)
4. ✅ Translation logging (key-value format with timestamps)
5. ✅ In-game log clearing command (`/tw clearlog`)

### Dictionary Updates
- Added 30 WoW-specific terms (classes, roles, raid terms)
- Added 13 common phrases from actual server chat
- Updated mistranslations: "奶萨" = "resto shaman" (was "breast Bodhisattva")

## Known Limitations

### Dictionary Approach
- **Word-by-word translation** can't handle context
- **Grammar differences** between Chinese and English
- **Slang & idioms** often mistranslated
- **Player/guild names** need manual addition to dictionary

### Performance Limits
- **Current**: 114K entries (4.5 MB) → No lag
- **Safe maximum**: 250K entries (~10 MB) before noticeable delay
- **Hard limit**: ~50 MB before UI freezes

## Future Improvement Strategy

### Short-term (Dictionary)
1. Run weekly analysis to extract new phrases
2. Add top 50 most common mistranslations
3. Community-source server-specific terms

### Long-term (Hybrid Approach)
1. Keep dictionary for fast word lookups
2. Use Google API for complex sentences (if online integration possible)
3. Build phrase dictionary from real server chat over time

## API & Services

### Google Cloud Translation API v3
- **Model**: Standard NMT (Neural Machine Translation)
- **Location**: `global` for NMT
- **Language pair**: `zh-CN` → `en-US`
- **Cost**: ~$20 per 1M characters (~$0.10 for 100 messages)
- **Rate limit**: 5 requests/sec (handled with 0.25s sleep)

### Translation LLM
- **Status**: Doesn't support zh-CN → en-US yet
- **Location**: Would use `us-central1` if supported
- **Fallback**: Use standard NMT model

## Git Repository
- **Main branch**: Clean addon files only
- **Analysis branch**: Private branch with analysis tools and credentials
- **Repo**: https://github.com/sanjaygbhat/TWoW-Translate

## Development Environment
- **WoW Version**: 1.12.1 (Vanilla)
- **Server**: Turtle WoW - Karazhan (Chinese)
- **Python**: 3.9+ (for analysis tools)
- **OS**: macOS (paths use absolute paths to Downloads folder)

## Common Issues & Solutions

### "Stack overflow at line 75"
**Cause**: Debug mode calls AddMessage inside hooked AddMessage
**Fix**: Save original AddMessage reference before hooking:
```lua
originalChatAddMessage = DEFAULT_CHAT_FRAME.AddMessage
-- Then use originalChatAddMessage in debug()
```

### "Translation logs cleared but reappear"
**Cause**: WoW saves in-memory data on exit/reload
**Solution**: 
1. Clear with `/tw clearlog` in-game (updates memory)
2. OR exit WoW completely, clear file, restart

### "403 Permission denied"
**Cause**: Service account lacks Translation API permissions
**Fix**: Add "Cloud Translation API User" role in IAM console

### "Syntax error in dictionary"
**Cause**: Missing comma or line break between entries
**Fix**: Ensure each entry has format:
```lua
["中文"] = "English",
```

## Performance Optimization Tips

1. **Phrase Priority**: Longer phrases match first (8+ chars → 2 chars → words)
2. **Regex Caching**: Don't create regex patterns in hot loops
3. **Table Size**: Pre-allocate tables when possible
4. **String Operations**: Use gsub for batch replacements
5. **Logging**: Only log if logging enabled (check flag first)

## Testing Checklist

Before release:
- [ ] `/reload` works without errors
- [ ] Chat translation works (Chinese → English)
- [ ] Item links clickable and show English tooltips on hover
- [ ] Player names clickable for whispers
- [ ] `/tw clearlog` works
- [ ] `/tw status` shows correct counts
- [ ] No UI lag with large dictionary

## Next Session TODO

1. Run analysis on accumulated logs (need 50-100+ translations)
2. Review `improvement_summary_*.txt` for patterns
3. Add top mistranslated phrases to dictionary
4. Test performance with larger phrase dictionary
5. Consider community feedback for server-specific terms

## Useful References
- CC-CEDICT: https://cc-cedict.org/
- WoW Addon API: https://wowpedia.fandom.com/wiki/World_of_Warcraft_API
- Google Cloud Translation: https://cloud.google.com/translate/docs
- Turtle WoW: https://turtle-wow.org/

---
**Last Updated**: October 29, 2025
**Version**: 0.1.4
**Maintainer**: sanjaygbhat

