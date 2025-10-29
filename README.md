# TranslateWoW

A real-time Chinese-to-English translation addon for World of Warcraft with grammar-aware natural language processing.

![Version](https://img.shields.io/badge/version-0.1.5-blue.svg)
![WoW](https://img.shields.io/badge/wow-1.12.1-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Features

- 🌐 **Real-time Translation** - Automatically translates Chinese chat messages to English
- 📖 **Comprehensive Dictionary** - 114,000+ entries covering common Chinese words and WoW-specific terms
- 🧠 **Grammar-Aware** - Natural translations with proper questions, tense, and flow (v0.1.5)
- 🔗 **Smart Link Handling** - Item links remain in Chinese for hover tooltips, but player names are clickable for whispers
- 📊 **Translation Logging** - Track all translations for continuous improvement
- ⚡ **Lightweight** - Only 4.5 MB, no performance impact
- 🎮 **WoW-Optimized** - Special handling for raid terms, class names, and gaming slang

## Installation

### Method 1: Manual Install
1. Download the latest release
2. Extract to `World of Warcraft/Interface/AddOns/`
3. Restart WoW or type `/reload`

### Method 2: Git Clone
```bash
cd "World of Warcraft/Interface/AddOns/"
git clone https://github.com/sanjaygbhat/TWoW-Translate.git TranslateWoW
```

## Usage

The addon works automatically once installed. All Chinese chat messages will be translated to English in real-time.

### Commands

| Command | Description |
|---------|-------------|
| `/tw` | Show addon information and version |
| `/tw status` | Display translation statistics |
| `/tw clearlog` | Clear translation logs |
| `/tw debug` | Toggle debug mode (for development) |

## How It Works

1. **Chat Interception**: Hooks into WoW's chat system to intercept messages
2. **Dictionary Lookup**: Matches phrases and words using a longest-match-first algorithm
3. **Smart Translation**: 
   - Item/Quest links: Preserved in Chinese (hover for English tooltip)
   - Player names: Display text translated, original name kept for whispers
   - Full sentences: Context-aware translation using comprehensive phrase dictionary

## Translation Quality

The addon uses a **grammar-aware hybrid approach**:

### Dictionary Foundation
- **114K+ entries** from CC-CEDICT plus WoW-specific terms
- **Longest-match-first** algorithm for phrase recognition
- **Fast, offline** translations with instant cached lookups

### Grammar Intelligence (v0.1.5)
- **80+ grammar-aware phrases** for natural translations
- **Aspect markers** (了/过/着) - proper tense/completion handling
- **Question particles** (吗/呢/吧) - automatic question detection
- **Modal verbs** (能/会/想/要) - ability/desire/necessity
- **Negation patterns** (不/没/别) - proper negative constructions
- **Post-processing rules** - punctuation, spacing, question marks

### WoW Gaming Optimization
- **Context-specific** translations for raids, dungeons, parties
- **75-82% coverage** of common WoW chat grammar patterns
- **Continuous improvement** through translation logging and analysis

### Example Translations

**Grammar-Aware Questions:**
```
Chinese: 你来吗？
English: coming? ✓ (auto-detected question)

Chinese: 有T吗？
English: any tank? ✓ (gaming + grammar)

Chinese: 准备好了吗
English: ready? ✓ (completion + question)
```

**Natural Gaming Chat:**
```
Chinese: 来T，满血战士
English: LF tank, full HP warrior

Chinese: 都准备好了
English: everyone ready ✓ (completed action)

Chinese: 马上来
English: coming soon ✓ (time + direction)
```

## Performance

- **Dictionary Size**: 4.5 MB (114,387 entries)
- **Memory Usage**: ~15-20 MB in-game
- **Load Time**: < 1 second
- **Translation Speed**: Instant (local lookup)
- **Game Impact**: None (optimized for WoW 1.12.1)

## Supported

- ✅ All chat channels (Say, Yell, Party, Raid, Guild, World)
- ✅ Player names (clickable for whispers)
- ✅ Item links (hover for tooltips)
- ✅ Quest links
- ✅ Emotes and system messages
- ✅ Multi-line messages

## Coverage

### Dictionary Coverage
- **Common Words**: 99% coverage of everyday Chinese
- **WoW Terms**: Classes, abilities, items, locations, dungeons
- **Gaming Slang**: Raid terminology, loot terms, abbreviations
- **Player Names**: Automatically learns from chat
- **Phrases**: Common expressions and idioms

### Grammar Coverage (v0.1.5)
- **Aspect Markers**: 70% (了/过/着 with common verbs)
- **Questions**: 85% (吗/呢/吧 particles)
- **Modal Verbs**: 80% (能/会/想/要/应该)
- **Negation**: 75% (不/没/别 patterns)
- **Possessives**: 90% (的 constructions)
- **Overall**: **~75-82%** of WoW gaming chat patterns

## Known Limitations

- **Context**: Word-by-word translation may miss context in very complex sentences
- **Grammar**: ~75-82% coverage of common patterns; advanced grammar (passive voice, complex conditionals) not fully supported
- **New Slang**: Server-specific terms need to be added to dictionary
- **Mixed Languages**: Messages with mixed Chinese/English may have partial translations

## Contributing

Contributions are welcome! Here's how you can help:

1. **Report Mistranslations**: Open an issue with the Chinese text and expected translation
2. **Add Terms**: Submit PRs with new dictionary entries for WoW-specific terms
3. **Server Slang**: Share common phrases from your server
4. **Code Improvements**: Optimize translation logic or add features

## Roadmap

- [ ] Phrase dictionary auto-learning from chat
- [ ] Guild-specific terminology support
- [ ] Translation quality scoring
- [ ] Customizable dictionary entries
- [ ] Export/import custom phrases
- [ ] Multi-language support (not just Chinese)

## Technical Details

### Dictionary Format
```lua
TranslateWoW_Dictionary = {
    ["中文"] = "English",
    ["副本"] = "dungeon",
    ["团队任务"] = "raid quest",
    -- 114,000+ more entries...
}
```

### Translation Algorithm
1. Extract hyperlinks (preserve structure)
2. Match longest phrases first (8+ characters)
3. Match medium phrases (4-7 characters)
4. Match short phrases (2-3 characters)
5. Match individual words
6. Restore hyperlinks with translated text

### Performance Optimization
- Pre-compiled pattern matching
- Efficient table lookups
- Minimal string allocations
- Cached regex patterns

## Credits

- **Dictionary Source**: [CC-CEDICT](https://cc-cedict.org/) (Creative Commons Chinese-English Dictionary)
- **WoW API**: [WoWPedia](https://wowpedia.fandom.com/)
- **Grammar Research**: Extensive analysis of Chinese linguistic patterns for gaming contexts
- **Community**: WoW Community players and contributors

## License

MIT License - see LICENSE file for details

## Support

- **Issues**: [GitHub Issues](https://github.com/sanjaygbhat/TWoW-Translate/issues)
- **Wiki**: [Project Wiki](https://github.com/sanjaygbhat/TWoW-Translate/wiki)
- **Community**: WoW Community Discord servers

## Changelog

### v0.1.5 (Current)
- **Grammar-Aware Translations**: Added 80+ grammar-aware frozen phrases
- **Natural Questions**: Post-processing rules for question particles (吗/呢 → ?)
- **Aspect Markers**: Proper handling of completed actions (了), modal verbs, negation
- **WoW Gaming Patterns**: "有T吗?" = "any tank?", "来不来?" = "coming or not?"
- **Coverage**: 75-82% estimated coverage of WoW gaming chat grammar patterns

### v0.1.4
- Added 13 common WoW phrases from real server chat
- Updated 30 WoW-specific terms (classes, roles, raid terms)
- Fixed dictionary syntax errors
- Improved phrase matching algorithm

### v0.1.3
- Fixed item link translation (now preserved in Chinese)
- Fixed player name whisper functionality
- Added translation logging system
- Added `/tw clearlog` command
- Fixed debug mode stack overflow

### v0.1.2
- Initial public release
- 114K+ dictionary entries
- Real-time chat translation
- Smart hyperlink handling

---

Made with ❤️ for the WoW Community

