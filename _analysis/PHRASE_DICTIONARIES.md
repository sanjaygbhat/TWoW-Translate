# Phrase Dictionary Sources for WoW Translation

## What You Already Have ✅

Your dictionary ALREADY includes phrases:
- Multi-word game terms: "团队任务" = "raid quest"
- Common expressions: "任务完成了" = "quest completed"
- WoW-specific: "英雄副本" = "heroic dungeon"

## Best Phrase Dictionary Sources

### 1. **Your Own WoW Chat Data** (BEST!) ⭐
**Already extracted:** `wow_phrases.lua` (21 real WoW phrases)

**Advantages:**
- Real phrases YOUR server uses
- Player names, guild names
- Server-specific slang
- Gaming context

**Keep running the analysis to build this over time!**

### 2. **Chinese Internet Slang Dictionaries**

Sources:
- **Chinese Gaming Slang**: Terms like "来T", "M", "DPS"
- **Internet Memes**: "6666" (amazing), "233" (laughing)
- **Common abbreviations**

Example additions:
```lua
["来T"] = "LF tank",
["来M"] = "LF healer", 
["来DPS"] = "LF DPS",
["老板"] = "raid leader",
["打金"] = "gold farming",
["摸尸"] = "looting",
["躺尸"] = "wiped",
["开荒"] = "progression",
["毕业"] = "BiS (best in slot)",
```

### 3. **Chinese Idioms (成语 Chengyu)**

Your dictionary already has some (4-character idioms):
- "君子坦荡荡，小人长戚戚" = "good people are at peace..."

**Common gaming-relevant idioms:**
```lua
["一马当先"] = "take the lead",
["勇往直前"] = "charge forward",
["全力以赴"] = "go all out",
["众志成城"] = "united we stand",
["背水一战"] = "last stand",
```

### 4. **WoW-Specific Terms Database**

Gaming databases like:
- **WoWHead** (item names, abilities)
- **WoW Wiki** (lore, locations)

Example WoW terms to add:
```lua
-- Classes
["战士T"] = "warrior tank",
["防战"] = "prot warrior",
["狂战"] = "fury warrior",
["武战"] = "arms warrior",

-- Roles  
["主T"] = "main tank",
["副T"] = "off tank",
["奶妈"] = "healer",
["输出"] = "DPS",

-- Raids
["黑翼"] = "BWL",
["黑上"] = "UBRS",
["黑下"] = "LBRS",
["斯坦"] = "Strat",
["通灵"] = "Scholo",

-- Loot
["需求"] = "need",
["贪婪"] = "greed",
["拾取"] = "loot",
["掉落"] = "drop",
```

## Recommended Two-Tier Lookup Strategy

### Update Your Translation Logic:

```lua
function translateText(text)
    -- Tier 1: Try exact phrase match (longest first)
    for phraseLen = 8, 2, -1 do
        for phrase, translation in pairs(phraseDict) do
            if #phrase == phraseLen then
                text = text:gsub(phrase, translation)
            end
        end
    end
    
    -- Tier 2: Word-by-word for remaining text
    for word, translation in pairs(wordDict) do
        text = text:gsub(word, translation)
    end
    
    return text
end
```

### Performance Optimization:

**Phrase Dict Size Recommendations:**
- Common phrases: 1,000-5,000 entries (~100-500 KB)
- WoW-specific: 500-1,000 entries (~50-100 KB)
- **Total safe limit**: ~5,000 phrase entries

**Priority Order:**
1. Longest phrases first (8+ characters)
2. Medium phrases (4-7 characters)
3. Short phrases (2-3 characters)
4. Individual words

## Building Your Custom Phrase Dictionary

### Strategy 1: Automatic (Run periodically)
```bash
# Every week, extract new phrases from logs
cd _analysis
./run_analysis.sh
# This builds wow_phrases.lua from real chat
```

### Strategy 2: Manual Curation
Add phrases you notice are commonly mistranslated:
1. Play WoW, note bad translations
2. Add them to a custom section in dictionary
3. They'll match before word-by-word translation

### Strategy 3: Community-Sourced
- Ask guildmates for common phrases
- Server-specific terminology
- Inside jokes, memes

## Practical Limits

| Dictionary Type | Entries | Size | Performance |
|----------------|---------|------|-------------|
| **Word Dict** (current) | 114K | 4.5 MB | ✅ Excellent |
| **Phrase Dict** (add) | 5K | 500 KB | ✅ No impact |
| **Combined** | 119K | 5 MB | ✅ Still great |

## Best Approach

**Keep doing what you're doing!**

1. ✅ **Word dictionary**: 114K entries (CC-CEDICT)
2. ✅ **WoW phrases**: Auto-generated from your logs
3. ✅ **Google API**: For complex sentences

This gives you:
- Fast common word lookups
- Context-aware phrase matching
- Professional sentence translation
- Growing accuracy over time

**Your hybrid system is already better than any single dictionary!** 🎯

