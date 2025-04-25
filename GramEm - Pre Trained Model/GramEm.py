from flask import Flask, request, jsonify
from transformers import T5ForConditionalGeneration, T5Tokenizer, pipeline
import torch
import re
from Mapping import emoji_mapping, keyword_emotion_mapping
from spellchecker import SpellChecker

app = Flask(__name__)

# -----------------------------------
# Load ML Models & Tokenizers
# -----------------------------------
try:
    print(">> Model Initialization <<")
    t5_model = T5ForConditionalGeneration.from_pretrained("vennify/t5-base-grammar-correction")
    t5_tokenizer = T5Tokenizer.from_pretrained("vennify/t5-base-grammar-correction", legacy=False)
    emotion_pipeline = pipeline("text-classification", model="bhadresh-savani/bert-base-go-emotion", top_k=1)
    spell = SpellChecker()
    print("Models loaded successfully!")
except Exception as e:
    print(f"Model loading failed: {e}")
    exit(1)  # Stop execution if model loading fails


# -----------------------------------
# Placeholder Hive Function (Offline Mode)
# -----------------------------------
def post_to_hive(username, text, title="GramEm Grammar Correction"):
    """Simulated posting function for offline mode."""
    return "Hive posting is currently disabled (offline mode)."


# -----------------------------------
# Text Processing Functions
# -----------------------------------
def correct_spelling(text):
    """Correct spelling using SpellChecker."""
    words = text.split()
    corrected_words = [spell.correction(word) if spell.correction(word) else word for word in words]
    return " ".join(corrected_words)


def correct_grammar(text):
    """Correct grammar using T5 Transformer model."""
    input_text = "gec: " + text
    input_ids = t5_tokenizer.encode(input_text, return_tensors="pt")

    output_ids = t5_model.generate(
        input_ids,
        max_length=100,
        num_return_sequences=1,
        repetition_penalty=3.0,
        no_repeat_ngram_size=3,
        temperature=0.7,
        do_sample=True
    )

    corrected_text = t5_tokenizer.decode(output_ids[0], skip_special_tokens=True).strip()

    # Post-processing: Remove redundant words, fix punctuation spacing
    corrected_text = re.sub(r'\b(\w+)\s+\1\b', r'\1', corrected_text)
    corrected_text = re.sub(r'([.!?])\1+', r'\1', corrected_text)
    corrected_text = re.sub(r'\s([.,!?])', r'\1', corrected_text)  # Remove space before punctuation

    return corrected_text


def insert_emojis(text):
    """Enhance text with emojis based on emotions."""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    result_sentences = []

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        emotions = emotion_pipeline(sentence)
        top_emotion = emotions[0][0]['label'] if emotions else "neutral"

        # Check for keyword-based emotion mapping
        for word, mapped_emotion in keyword_emotion_mapping.items():
            if word in sentence.lower():
                top_emotion = mapped_emotion
                break

        emoji = emoji_mapping.get(top_emotion, "")
        result_sentences.append(sentence + " " + emoji)

    return " ".join(result_sentences)


# -----------------------------------
# Flask API Endpoint
# -----------------------------------
@app.route("/process", methods=["POST"])
def process_text():
    """API endpoint to process text."""
    try:
        data = request.get_json()
        user_text = data.get("text", "").strip()
        username = data.get("username", "").strip()

        if not user_text or not username:
            return jsonify({"error": "Text and username are required"}), 400

        # Process text: Spelling correction → Grammar correction → Emoji insertion
        spelled_corrected_text = correct_spelling(user_text)
        corrected_text = correct_grammar(spelled_corrected_text)
        text_with_emojis = insert_emojis(corrected_text)

        return jsonify({
            "Original Text": user_text,
            "GramEm Text": text_with_emojis,
            "Hive Post Url": post_to_hive(username, text_with_emojis)
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -----------------------------------
# Server
# -----------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

