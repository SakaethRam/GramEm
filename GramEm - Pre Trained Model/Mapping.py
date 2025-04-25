# Keyword-based fallback to improve accuracy
keyword_emotion_mapping = {
    "relaxed": "relief", "calm": "relief", "serene": "calmness",
    "furious": "anger", "enraged": "anger", "annoyed": "frustration",
    "cheerful": "joy", "delighted": "happiness", "ecstatic": "joy",
    "terrified": "fear", "scared": "fear", "anxious": "anxiety"
}


emoji_mapping = {
    "joy": "😊", "happiness": "😊", "contentment": "😊", "pride": "😊",
    "awe": "🤩", "excitement": "🤩", "enthusiasm": "🤩", "wonder": "🤩",
    "anger": "😡", "frustration": "😡", "resentment": "😡", "rage": "😡",
    "sadness": "😢", "grief": "😢", "disappointment": "😢", "loneliness": "😢",
    "fear": "😨", "anxiety": "😨", "nervousness": "😨", "dread": "😨",
    "surprise": "😲", "shock": "😲", "astonishment": "😲",
    "love": "❤️", "affection": "❤️", "caring": "❤️", "gratitude": "❤️",
    "neutral": "😐", "indifference": "😐", "boredom": "😐",
    "disgust": "🤢", "revulsion": "🤢", "aversion": "🤢",
    "optimism": "🙂", "hope": "🙂", "confidence": "🙂",
    "admiration": "👏", "respect": "👏", "appreciation": "👏",
    "amusement": "😂", "humor": "😂", "fun": "😂",
    "relief": "😌", "calmness": "😌", "serenity": "😌"
}
