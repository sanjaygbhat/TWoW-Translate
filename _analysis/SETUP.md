# Google Cloud Translation API Setup Guide

## Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Google Cloud account

## Step 1: Google Cloud Setup

### 1.1 Create a Google Cloud Project
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click "Select a project" → "New Project"
3. Enter project name (e.g., "wow-translator")
4. Click "Create"

### 1.2 Enable Billing
1. Go to [Billing](https://console.cloud.google.com/billing)
2. Link a billing account (Google gives $300 free credit for new users!)
3. **Cost**: ~$20 per 1 million characters
   - For testing: A few hundred translations will cost < $1
   - For full analysis: Estimate based on your log size

### 1.3 Enable Cloud Translation API
1. Go to [APIs & Services > Library](https://console.cloud.google.com/apis/library)
2. Search for "Cloud Translation API"
3. Click on it and press "Enable"

### 1.4 Create Service Account & Credentials
1. Go to [IAM & Admin > Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
2. Click "Create Service Account"
3. Enter name: `translate-wow-analyzer`
4. Click "Create and Continue"
5. Grant role: Select "Basic" → "Editor" (or "Cloud Translation API User")
6. Click "Continue" → "Done"
7. Click on the created service account
8. Go to "Keys" tab
9. Click "Add Key" → "Create New Key"
10. Choose "JSON" format
11. Click "Create" - A JSON file will be downloaded

### 1.5 Save the Credentials File
1. Move the downloaded JSON file to a secure location
2. Rename it to something memorable, e.g., `wow-translator-key.json`
3. **IMPORTANT**: Never commit this file to git or share it publicly!

## Step 2: Python Environment Setup

### 2.1 Create Virtual Environment (Recommended)
```bash
# Navigate to the _analysis folder
cd /Users/sanjaybhat/Downloads/twmoa_1180/Interface/AddOns/TranslateWoW/_analysis

# Create virtual environment
python3 -m venv venv

# Activate it
# On Mac/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 2.2 Install Required Packages
```bash
pip install google-cloud-translate pandas
```

## Step 3: Set Environment Variable

### On Mac/Linux (Temporary - Current Session)
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/wow-translator-key.json"
```

### On Mac/Linux (Permanent - Add to ~/.zshrc or ~/.bash_profile)
```bash
echo 'export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/wow-translator-key.json"' >> ~/.zshrc
source ~/.zshrc
```

### On Windows (Temporary - Current Session)
```cmd
set GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your\wow-translator-key.json"
```

### On Windows (Permanent - System Properties)
1. Search for "Environment Variables" in Start menu
2. Click "Edit the system environment variables"
3. Click "Environment Variables" button
4. Under "User variables", click "New"
5. Variable name: `GOOGLE_APPLICATION_CREDENTIALS`
6. Variable value: `C:\path\to\your\wow-translator-key.json`
7. Click OK

## Step 4: Test Your Setup

Run the test script:
```bash
cd /Users/sanjaybhat/Downloads/twmoa_1180/Interface/AddOns/TranslateWoW/_analysis
python test_google_translate.py
```

Expected output:
```
======================================================================
Google Cloud Translation API Test
======================================================================

✓ Credentials file found: /path/to/your-key.json
✓ google-cloud-translate library imported successfully
✓ Translation client initialized

======================================================================
Testing Translations
======================================================================

✓ '你好' → 'Hello'
  (Expected context: Hello)
  Detected source: zh-CN

✓ '世界' → 'World'
  (Expected context: World)
  Detected source: zh-CN

...

======================================================================
Results: 5/5 translations successful
======================================================================

🎉 All tests passed! Your Google Cloud Translation API is working correctly.
You can now run the full analysis scripts.
```

## Troubleshooting

### Error: "GOOGLE_APPLICATION_CREDENTIALS environment variable not set"
- Solution: Follow Step 3 to set the environment variable
- Make sure you're using the correct path to your JSON key file

### Error: "Credentials file not found"
- Solution: Check the path in your environment variable is correct
- Use absolute path, not relative path

### Error: "Permission denied" or "403 Forbidden"
- Solution: Make sure you've enabled the Cloud Translation API in Step 1.3
- Check that your service account has the correct permissions

### Error: "Quota exceeded"
- Solution: You've hit the free tier limit
- Check your quota at: https://console.cloud.google.com/apis/api/translate.googleapis.com/quotas
- Consider enabling billing or waiting for quota reset

### Error: "google.cloud not found"
- Solution: Install the library: `pip install google-cloud-translate`
- Make sure your virtual environment is activated if using one

## Next Steps

Once the test passes:
1. Play WoW and let translations accumulate (aim for 50-100+ entries)
2. Run `/tw status` to check log count
3. Run the analysis scripts (coming next!)

## Cost Estimation

Google Cloud Translation API pricing (as of 2024):
- **$20 per 1 million characters**
- Chinese characters count as 1 character each
- Example: 100 chat messages averaging 50 characters = 5,000 characters = **$0.10**

For testing with 100-500 translations, expect to spend less than $1.

