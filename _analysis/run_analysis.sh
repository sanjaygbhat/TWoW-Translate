#!/bin/bash
# Master script to run the complete translation analysis pipeline

echo "======================================================================"
echo "TranslateWoW Translation Analysis Pipeline"
echo "======================================================================"
echo ""

# Set credentials
export GOOGLE_APPLICATION_CREDENTIALS="$(pwd)/credentials.json"

# Step 1: Extract translations
echo "STEP 1: Extracting translations from SavedVariables..."
python3 extract_logs.py
if [ $? -ne 0 ]; then
    echo "❌ Failed to extract translations"
    exit 1
fi
echo ""

# Step 2: Compare with Google Translate
echo "STEP 2: Comparing with Google Cloud Translation API..."
python3 compare_with_google.py
if [ $? -ne 0 ]; then
    echo "❌ Failed to compare translations"
    exit 1
fi
echo ""

# Step 3: Generate improvements
echo "STEP 3: Generating dictionary improvements..."
python3 improve_dictionary.py
if [ $? -ne 0 ]; then
    echo "❌ Failed to generate improvements"
    exit 1
fi
echo ""

# Done!
echo "======================================================================"
echo "✅ Analysis Complete!"
echo "======================================================================"
echo ""
echo "📁 Output files:"
echo "   - translations_extracted.json (extracted from WoW)"
echo "   - translation_comparison.json (comparison results)"
echo "   - dictionary_improvements_*.lua (suggested dictionary updates)"
echo "   - improvement_summary_*.txt (human-readable summary)"
echo ""
echo "📝 Next steps:"
echo "   1. Review the improvement_summary_*.txt file"
echo "   2. Apply updates from dictionary_improvements_*.lua"
echo "   3. Test in-game with /reload"
echo ""

