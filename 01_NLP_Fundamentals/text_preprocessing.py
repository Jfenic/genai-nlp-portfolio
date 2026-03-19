"""
Project: NLP Fundamentals - Text Preprocessing Pipeline
Author: [Your Name]
Description: This script demonstrates how to clean raw text, remove stop words,
             and compares Stemming (cutting) vs. Lemmatization (root finding).
"""

import re
import nltk
import spacy
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# --- 1. SETUP & DOWNLOADS ---
# Download NLTK data (only needs to be done once)
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")
    nltk.download("stopwords")

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")
stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))


# --- 2. THE CLEANING FUNCTION ---
def clean_text(text):
    """
    Takes raw text and performs:
    1. Lowercasing
    2. Noise removal (special chars)
    3. Tokenization
    4. Stopword removal
    """
    # 1. Convert to lowercase
    text = text.lower()

    # 2. Remove special characters and numbers using Regex
    # Keep only letters (a-z) and spaces
    text = re.sub(r"[^a-z\s]", "", text)

    # 3. Tokenization (Split into words)
    tokens = word_tokenize(text)

    # 4. Remove Stop Words (e.g., 'the', 'is', 'in')
    clean_tokens = [word for word in tokens if word not in stop_words]

    return clean_tokens


# --- 3. COMPARISON: STEMMING VS LEMMATIZATION ---
def compare_stem_lemma(text):
    """
    Compares how NLTK (Stemming) and SpaCy (Lemmatization) handle the same words.
    """
    tokens = clean_text(text)

    results = []

    # Process with SpaCy for Lemmatization
    doc = nlp(" ".join(tokens))

    for token in doc:
        # Append data to results list
        results.append(
            {
                "Original": token.text,
                "Stemming (NLTK)": stemmer.stem(token.text),
                "Lemmatization (SpaCy)": token.lemma_,
            }
        )

    return pd.DataFrame(results)


# --- 4. EXECUTION ---
if __name__ == "__main__":
    # Example raw text (Messy input)
    raw_text = """
    The striped bats are hanging on their feet for best sleep! 
    Running, swam, and eating are basic survival skills in 2025.
    """

    print("--- RAW TEXT ---")
    print(raw_text.strip())

    print("\n--- 1. CLEANED TOKENS ---")
    cleaned = clean_text(raw_text)
    print(cleaned)

    print("\n--- 2. STEMMING VS LEMMATIZATION COMPARISON ---")
    df_comparison = compare_stem_lemma(raw_text)
    print(df_comparison.to_string(index=False))

    print("\n--- CONCLUSION ---")
    print(
        "Notice how 'hanging' becomes 'hang' in both, but 'swam' remains 'swam' in Stemming"
    )
    print("while Lemmatization correctly identifies the root verb 'swim'.")
