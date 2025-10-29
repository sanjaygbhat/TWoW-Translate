# Translation Analysis Tools

This folder contains scripts to analyze and improve the TranslateWoW dictionary using Google Translate API.

## Setup

1. Install Python dependencies:
```bash
pip install google-cloud-translate difflib pandas requests
```

2. Set up Google Cloud Translation API:
   - Create a Google Cloud project
   - Enable the Cloud Translation API
   - Create a service account and download the JSON key
   - Set environment variable: `export GOOGLE_APPLICATION_CREDENTIALS="path/to/key.json"`
   
   OR use the simpler API key method:
   - Get an API key from Google Cloud Console
   - Set: `export GOOGLE_TRANSLATE_API_KEY="your-api-key"`

## Scripts

### 1. `extract_translations.py`
Extracts translations from SavedVariables and prepares them for analysis.

```bash
python extract_translations.py
```

Output: `translations_extracted.csv`

### 2. `compare_with_google.py`
Compares dictionary translations with Google Translate and calculates accuracy scores.

```bash
python compare_with_google.py
```

Output:
- `translation_comparison.csv` - Full comparison with scores
- `low_accuracy.csv` - Translations needing improvement (score < 70%)

### 3. `improve_dictionary.py`
Generates dictionary improvements based on Google Translate suggestions.

```bash
python improve_dictionary.py
```

Output:
- `dictionary_suggestions.txt` - New entries to add to dictionary
- `dictionary_fixes.txt` - Existing entries that need correction

### 4. `analyze_all.sh`
Runs the complete analysis pipeline.

```bash
bash analyze_all.sh
```

## Workflow

1. Play WoW and let translations log naturally
2. Run `/tw clearlog` after saving a backup if needed
3. Extract translations: `python extract_translations.py`
4. Compare with Google: `python compare_with_google.py`
5. Review `low_accuracy.csv` for problems
6. Generate improvements: `python improve_dictionary.py`
7. Manually review and apply suggestions to `TranslateWoW_Dictionary.lua`

## Notes

- Google Translate API costs ~$20 per 1 million characters
- Results are cached to avoid duplicate API calls
- The comparison uses fuzzy matching to handle minor differences
- Focus on improving low-accuracy translations first
