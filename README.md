# SpamShield - Complete source code

## Windows par chalane ka asaan tareeqa
1. ZIP par right-click karein aur Extract All karein.
2. Extracted SpamShield_Source_Code folder VS Code mein kholen.
3. Terminal > New Terminal kholen.
4. Yeh command chalayein (Python installed hona chahiye):

   py -m http.server 8000 --bind 127.0.0.1 --directory dist

5. Browser mein http://localhost:8000 kholen.
6. Server band karne ke liye terminal mein Ctrl+C dabayein.

Alternatively START_WINDOWS.bat ko double-click karein, phir browser mein upar wala address kholen.
Agar py command available nahin, python use karein.
HTML file ko directly double-click na karein: model.json load karne ke liye local HTTP server chahiye.

## Files
- dist/index.html: webpage structure
- dist/style.css: design and responsive styling
- dist/app.js: input, buttons and results
- dist/classifier.js: TF-IDF + Multinomial Naive Bayes inference in JavaScript
- dist/model.json: trained vocabulary, IDF values and model weights
- scripts/train.py: reproduces training from the notebook and exports model.json
- spam_classifier.ipynb: your original notebook
- spam.csv: your uploaded dataset

## Model integration
The webpage does not run the notebook on each click. The Python model was trained using the notebook's settings, then its learned weights were exported to model.json. classifier.js performs the equivalent inference in the browser. Messages stay in the browser. No API key or Python ML server is needed. Google Fonts is optional; system fonts are used if unavailable.

## Optional: retrain
Only needed if changing the data/model, not for running the website:

   py -m pip install -r requirements.txt
   py scripts/train.py spam.csv

The training script uses a deduplicated dataset, 80/20 stratified split, random_state=42, default TfidfVectorizer and default MultinomialNB. It overwrites dist/model.json. If the dataset changes, update the displayed metrics in dist/index.html too.

## Verification and limitations
1,034 held-out messages: browser inference matched all Python predictions. Accuracy 95.16%, spam precision 100%, spam recall 61.83%. These are test-set measurements, not guarantees. Training data is SMS-style; long emails and other languages may be less reliable. Browser visual testing was not performed.
