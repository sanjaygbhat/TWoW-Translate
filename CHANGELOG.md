# Changelog

All notable changes to CN to EN Translate WoW will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] - 2025-10-12

### 🎉 Initial Release

#### Added
- **Core Translation Engine**
  - Dictionary-based translation system with 115,757 CC-CEDICT entries
  - 588 WoW-specific gaming terms (quests, items, combat, UI)
  - Smart phrase matching up to 15 Chinese characters
  - Translation caching for instant lookups
  - Greedy longest-match-first algorithm

- **Translation Coverage**
  - Item tooltips (hover over items)
  - NPC names and titles (mouseover and target)
  - Quest text and objectives
  - Chat messages (all channels)
  - UI elements and interface text
  - GameTooltip integration

- **In-Game Commands**
  - `/tw on` - Enable translation
  - `/tw off` - Disable translation
  - `/tw status` - Show addon statistics

- **Translation Logging**
  - Automatic logging of translations to SavedVariables
  - Supports future quality analysis and improvements
  - Configurable via `LOG_TRANSLATIONS` flag

- **Performance Optimization**
  - Zero FPS impact during gameplay
  - Efficient memory usage (~5.5 MB)
  - Instant cached translation lookups
  - One-time dictionary load on game start

#### Technical Details
- **Dictionary File**: 5.2 MB compressed Lua table
- **Load Time**: 5-10 seconds (one-time)
- **Compatibility**: WoW 1.12 (Vanilla)
- **SavedVariables**: TranslateWoWDB for persistent storage

#### Known Limitations
- Translations are word-by-word (no grammar reordering)
- Complex sentences may be literal
- Internet slang may not translate accurately
- Some proper names translate literally

---

## [Unreleased]

### Planned for v0.2.0
- Improved chat message phrase matching
- Expanded WoW-specific terminology
- Translation quality metrics display
- User feedback system

### Planned for v0.3.0
- User-customizable dictionary entries
- Export/import translation improvements
- Enhanced phrase recognition
- Performance profiling tools

---

## Version History

| Version | Release Date | Highlights |
|---------|--------------|------------|
| 0.1.0 | 2025-10-12 | Initial release with 115K+ dictionary |

---

**Note**: Development builds and self-improvement tools are maintained in a separate private repository.

