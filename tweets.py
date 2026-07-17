import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from tqdm import tqdm

# 1. SETUP VADER
nltk.download('vader_lexicon', quiet=True)
sia = SentimentIntensityAnalyzer()
tqdm.pandas()

# 2. LOAD DATA
print(">>> Loading Data...")
files = ['data_visualization.csv', 'data_analysis.csv', 'data_science.csv']
df = pd.concat([pd.read_csv(f, low_memory=False) for f in files], ignore_index=True)

# 3. CLEAN & LABEL
print(">>> Cleaning and Labeling...")
df = df[['tweet']].dropna().drop_duplicates()

def get_label(text):
    score = sia.polarity_scores(str(text))['compound']
    return 'Positive' if score > 0 else 'Negative'

df['sentiment'] = df['tweet'].progress_apply(get_label)

# 4. SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(
    df['tweet'], df['sentiment'], test_size=0.2, random_state=42
)

# 5. VECTORIZE
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 6. TRAIN MODEL
print(">>> Training Model...")
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# 7. RESULTS
print("\n" + "="*30)
print("FINAL RESULTS")
print("="*30)
predictions = model.predict(X_test_vec)

# Print Accuracy
print(f"REAL ACCURACY: {accuracy_score(y_test, predictions) * 100:.2f}%")

# Print Confusion Matrix
print("\n--- CONFUSION MATRIX ---")
cm = confusion_matrix(y_test, predictions, labels=['Negative', 'Positive'])
cm_df = pd.DataFrame(cm, index=['Actual Negative', 'Actual Positive'], 
                         columns=['Predicted Negative', 'Predicted Positive'])
print(cm_df)

# Print Detailed Report
print("\n--- DETAILED REPORT ---")
print(classification_report(y_test, predictions))