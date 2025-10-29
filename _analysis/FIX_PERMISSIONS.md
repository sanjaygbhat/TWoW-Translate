# Fix Service Account Permissions

## Problem
```
403 Cloud IAM permission 'cloudtranslate.generalModels.predict' denied.
```

## Solution

Your service account (`translate@rugged-cooler-430706-j3.iam.gserviceaccount.com`) needs permissions to use the Translation API.

### Option 1: Using Google Cloud Console (Easiest)

1. Go to https://console.cloud.google.com/iam-admin/iam?project=rugged-cooler-430706-j3
2. Find your service account: `translate@rugged-cooler-430706-j3.iam.gserviceaccount.com`
3. Click the pencil icon (Edit) next to it
4. Click "ADD ANOTHER ROLE"
5. Search for and select: **Cloud Translation API User**
6. Click "SAVE"

### Option 2: Using Command Line

```bash
gcloud projects add-iam-policy-binding rugged-cooler-430706-j3 \
    --member="serviceAccount:translate@rugged-cooler-430706-j3.iam.gserviceaccount.com" \
    --role="roles/cloudtranslate.user"
```

### Verify It Works

After adding the role, run:
```bash
cd /Users/sanjaybhat/Downloads/twmoa_1180/Interface/AddOns/TranslateWoW/_analysis
export GOOGLE_APPLICATION_CREDENTIALS="$(pwd)/credentials.json"
python3 test_google_translate.py
```

You should see:
```
🎉 Google Cloud Translation API is working!
```

## What Permissions Are Needed?

The service account needs the **Cloud Translation API User** role which includes:
- `cloudtranslate.generalModels.predict` - to translate text
- `cloudtranslate.generalModels.get` - to get model info
- `cloudtranslate.operations.wait` - for long-running operations

---

**Estimated time**: 2 minutes

