


decodeDict = {'⟐': 'a', '⟑': 'b', '⟒': 'c', '⟓': 'd', '⟔': 'e', '⟕': 'f', '⟖': 'g', '⟗': 'h', '⟘': 'i', '⟙': 'j', '⟚': 'k', '⟛': 'l', '⟜': 'm', '⟝': 'n', '⟞': 'o', '⟟': 'p', '⟠': 'q', '⟡': 'r', '⟢': 's', '⟣': 't', '⟤': 'u', '⟥': 'v', '⟦': 'w', '⟧': 'x', '⟨': 'y', '⟩': 'z', ' ': ' '}
encodeDict = {'a': '⟐', 'b': '⟑', 'c': '⟒', 'd': '⟓', 'e': '⟔', 'f': '⟕', 'g': '⟖', 'h': '⟗', 'i': '⟘', 'j': '⟙', 'k': '⟚', 'l': '⟛', 'm': '⟜', 'n': '⟝', 'o': '⟞', 'p': '⟟', 'q': '⟠', 'r': '⟡', 's': '⟢', 't': '⟣', 'u': '⟤', 'v': '⟥', 'w': '⟦', 'x': '⟧', 'y': '⟨', 'z': '⟩', ' ': ' '}

def decode(message):
    decoded = ""
    for char in message:
        decoded += decodeDict[char]
    return decoded

def encode(message):
    encoded = ""
    for char in message:
        encoded += encodeDict[char]
    return encoded
