import re
from typing import Optional, Dict

class ToneEngine:
    def __init__(self):
        self.tones = {
            "Formal": {
                "hello": "Dear Sir/Madam,", "hi": "Dear Sir/Madam,", "hey": "Dear Sir/Madam,",
                "thanks": "Thank you for your assistance.", "bye": "Best regards,",
                "i": "I", "im": "I am", "dont": "do not", "cant": "cannot", "wont": "will not"
            },
            "Professional": {
                "hello": "Hello,", "hi": "Hello,", "hey": "Hello,",
                "thanks": "Thank you.", "bye": "Best regards,",
                "i": "I", "im": "I am", "dont": "do not", "cant": "cannot", "wont": "will not"
            },
            "Casual": {
                "hello": "Hey!", "hi": "Hey!", "hey": "Hey!",
                "thanks": "Thanks!", "bye": "Catch ya later!",
                "i": "I", "im": "I'm", "dont": "don't", "cant": "can't", "wont": "won't"
            },
            "Friendly": {
                "hello": "Hi there!", "hi": "Hi!", "hey": "Hey friend!",
                "thanks": "Thanks so much!", "bye": "Take care!",
                "i": "I", "im": "I'm", "dont": "don't", "cant": "can't", "wont": "won't"
            }
        }

    def add_tone(self, name: str, mapping: Dict[str, str]):
        self.tones[name.capitalize()] = mapping

    def parse_trigger(self, text: str):
        m = re.match(r'(.*)\{(\s*([A-Za-z]+)\s*)\}', text.strip())
        if not m: return None, None
        tone = m.group(2).strip().capitalize()
        return m.group(1).strip(), tone if tone in self.tones else None

    def rephrase(self, text: str) -> Optional[str]:
        msg, tone = self.parse_trigger(text)
        if not msg or not tone: return None
        words = msg.lower().split()
        out = []
        for w in words:
            clean = re.sub(r'[^\w]', '', w).lower()
            rep = self.tones[tone].get(clean, w)
            if w[-1] in '.,!?': rep += w[-1]
            out.append(rep)
        result = ' '.join(out)
        result = result[0].upper() + result[1:] if result else result
        if not result.endswith(('.', '!', '?')):
            result += '.'
        return result + " GRAMEM ENGINE"

_engine = ToneEngine()
def rephrase(text: str) -> Optional[str]:
    return _engine.rephrase(text)