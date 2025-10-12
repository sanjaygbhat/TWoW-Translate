# Installation Guide

Complete installation instructions for **CN to EN Translate WoW**

---

## 📋 Requirements

- **World of Warcraft 1.12** (Vanilla client)
- **Compatible Servers**: Turtle WoW, Kronos, or any 1.12 private server
- **Disk Space**: ~6 MB free space
- **No external dependencies required**

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Download the Addon

**Option A: Download Release (Recommended)**
1. Go to [Releases](../../releases)
2. Download the latest `CNtoENTranslateWoW-v0.1.0.zip`
3. Extract the ZIP file

**Option B: Clone Repository**
```bash
git clone https://github.com/YOUR_USERNAME/CNtoENTranslateWoW.git
```

### Step 2: Install to WoW

1. Locate your WoW installation directory:
   ```
   Windows: C:\Program Files\World of Warcraft\
   Mac: /Applications/World of Warcraft/
   Linux: ~/Games/World of Warcraft/
   ```

2. Navigate to the AddOns folder:
   ```
   World of Warcraft/Interface/AddOns/
   ```

3. Copy the **entire** `CNtoENTranslateWoW` folder here
   
   ✅ Correct structure:
   ```
   World of Warcraft/
   └── Interface/
       └── AddOns/
           └── CNtoENTranslateWoW/
               ├── TranslateWoW.toc
               ├── TranslateWoW.lua
               ├── TranslateWoW.xml
               └── TranslateWoW_Dictionary.lua
   ```

### Step 3: Enable in Game

1. **Start** World of Warcraft
2. At the **character select screen**, click **AddOns** (bottom-left)
3. **Check** "CN to EN Translate" to enable it
4. **Select** your character and enter the game
5. Wait **5-10 seconds** for the dictionary to load (one-time)

### Step 4: Verify Installation

Type in chat:
```
/tw status
```

You should see:
```
TranslateWoW Status:
- Translation: ON
- Cache: 0 entries
- Dictionary: Loaded
```

---

## ✅ Testing the Addon

### Test 1: Chat Translation
1. Find a Chinese chat message
2. It should display with English translation

### Test 2: Item Tooltip
1. Hover over an item with Chinese text
2. Tooltip should show English translation

### Test 3: NPC Names
1. Target or mouseover an NPC with Chinese name
2. Name should translate to English

---

## 🔧 Troubleshooting

### Addon Not Appearing in List

**Problem**: Addon doesn't show at character select screen

**Solutions**:
1. Check folder name is exactly `CNtoENTranslateWoW` (case-sensitive on Linux/Mac)
2. Verify files are in correct location:
   ```
   Interface/AddOns/CNtoENTranslateWoW/TranslateWoW.toc
   ```
3. Restart WoW completely (don't just reload UI)
4. Check `TranslateWoW.toc` file exists and is not corrupted

### Long Load Time

**Problem**: Game takes 10+ seconds to load character

**Expected**: First load takes 5-10 seconds (dictionary loading)
- This is normal! The 5.2 MB dictionary must load once
- Subsequent logins are instant (dictionary stays in memory)

**If loading takes 30+ seconds**:
1. Check if other addons are conflicting
2. Disable other addons temporarily to isolate issue
3. Verify your HDD/SSD is not failing

### Translations Not Working

**Problem**: Chinese text still shows as Chinese

**Solutions**:
1. Check addon is enabled: `/tw status`
2. If OFF, enable it: `/tw on`
3. Reload UI: `/reload`
4. Check for Lua errors:
   - Type: `/console scriptErrors 1`
   - Reload and watch for error messages
5. Verify `TranslateWoW_Dictionary.lua` exists and is ~5.2 MB

### Lua Errors

**Problem**: Red error messages appear on screen

**Solutions**:
1. Take a screenshot of the error
2. Report on [GitHub Issues](../../issues)
3. Include:
   - Error message
   - What you were doing when it occurred
   - Other addons you're using
   - WoW version and server

### Performance Issues

**Problem**: Game feels laggy with addon enabled

**Unlikely**: Addon has zero FPS impact after initial load

**If experiencing lag**:
1. Check FPS: `/fps`
2. Disable addon: `/tw off`
3. Test if FPS improves
4. If yes, report the issue with system specs

---

## 🗑️ Uninstallation

### To Temporarily Disable
```
/tw off
```

### To Fully Remove
1. Close World of Warcraft
2. Navigate to:
   ```
   World of Warcraft/Interface/AddOns/
   ```
3. Delete the `CNtoENTranslateWoW` folder

4. (Optional) Clean up saved settings:
   ```
   World of Warcraft/WTF/Account/YOUR_ACCOUNT/SavedVariables/
   ```
   Delete `TranslateWoW.lua` if it exists

---

## 🔄 Updating to New Version

### Manual Update
1. **Download** new version
2. **Delete** old `CNtoENTranslateWoW` folder
3. **Copy** new folder to AddOns directory
4. **Restart** WoW (do NOT just reload UI)

### Git Update
```bash
cd "World of Warcraft/Interface/AddOns/CNtoENTranslateWoW"
git pull origin main
```

**Note**: Always restart WoW completely after updating!

---

## 📁 File Structure

```
CNtoENTranslateWoW/
├── README.md                    # Main documentation
├── INSTALL.md                   # This file
├── CHANGELOG.md                 # Version history
├── LICENSE                      # GPL v2.0 license
├── TranslateWoW.toc            # Addon metadata (573 bytes)
├── TranslateWoW.lua            # Core logic (24 KB)
├── TranslateWoW.xml            # UI definitions (374 bytes)
└── TranslateWoW_Dictionary.lua # Dictionary data (5.2 MB)
```

---

## 💾 SavedVariables Location

Translation logs and settings are saved to:

```
World of Warcraft/WTF/Account/YOUR_ACCOUNT/SavedVariables/TranslateWoW.lua
```

This file grows over time as translations are logged (~1-2 KB per gaming session).

---

## 🌐 Multi-Account Setup

To use on multiple WoW accounts:
1. Install once in `Interface/AddOns/` (shared by all accounts)
2. Enable separately for each account/character
3. Each account maintains separate translation logs

---

## 🔒 Permissions

The addon requires **no special permissions**:
- ✅ Reads game UI text (standard)
- ✅ Writes to SavedVariables (standard)
- ❌ No network access
- ❌ No file system access outside WoW
- ❌ No external programs required

---

## 📞 Support

- **Issues**: [GitHub Issues](../../issues)
- **Questions**: [GitHub Discussions](../../discussions)
- **Discord**: Coming soon

---

## ✨ First-Time Setup Tips

1. **Wait for load**: First login takes 5-10 seconds (normal!)
2. **Test it**: Type `/tw status` to confirm it's working
3. **Explore**: Hover over Chinese items, read chat, target NPCs
4. **Customize**: Use `/tw off` if you want translation disabled temporarily
5. **Report**: Found untranslated text? It helps to report it!

---

**Installation complete!** Enjoy playing WoW with instant Chinese-to-English translation! 🎮🌏→🌍

