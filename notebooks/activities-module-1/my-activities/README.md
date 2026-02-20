# Activities — Module 1

Colab notebooks from the Cambridge Data Science course.

## Download from Google Drive

**Source:** [Google Drive folder](https://drive.google.com/drive/folders/17mX5ZDCexHhOiPTchzFdAYwKFdG93C1l?usp=drive_link)

### Option 1: Automated (requires public sharing)

1. In Google Drive, right-click the folder → **Share** → set to **"Anyone with the link"** (Viewer).
2. From the project root, run:
   ```bash
   python scripts/download_module1_activities.py
   ```

### Option 2: Manual download

1. Open the [Drive folder](https://drive.google.com/drive/folders/17mX5ZDCexHhOiPTchzFdAYwKFdG93C1l?usp=drive_link).
2. Select all notebooks → **Download** (or download individually).
3. Move the `.ipynb` files into this folder: `activities-module-1/`.

### Option 3: Using cookies (if Option 1 fails)

If the folder is shared but gdown still fails (e.g. due to access limits):

1. Install a browser extension like [Get cookies.txt LOCALLY](https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc).
2. Sign in to Google Drive in your browser, open the folder, export cookies as `cookies.txt`.
3. Run: `mkdir -p ~/.cache/gdown && mv cookies.txt ~/.cache/gdown/cookies.txt`
4. Run the download script again.
