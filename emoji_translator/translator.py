def translate_to_emoji(text):
    emoji_map = {
        "happy": "😊", "sad": "😔", "angry": "😠", "love": "❤️",
        "food": "🍔", "pizza": "🍕", "car": "🚗", "dog": "🐶",
        "cat": "🐱", "sun": "☀️", "moon": "🌙", "star": "⭐",
        "hello": "👋", "goodbye": "👋", "yes": "👍", "no": "👎",
        "fire": "🔥", "water": "💧", "tree": "🌳", "flower": "🌸",
        "book": "📚", "computer": "💻", "phone": "📱", "music": "🎵",
        "money": "💰", "idea": "💡", "time": "⏰", "sleep": "😴",
        "work": "💼", "play": "🎮", "run": "🏃", "walk": "🚶",
        "eat": "🍽️", "drink": "🍹", "party": "🎉", "dance": "💃",
        "fun": "😄", "cool": "😎", "wow": "😮", "oops": "😅",
        "thank you": "🙏", "please": "🥺", "sorry": "😔", "congratulations": "🎉",
        "birthday": "🎂", "christmas": "🎄", "new year": "🎆", "halloween": "🎃",
        "summer": "☀️", "winter": "❄️", "spring": "🌷", "autumn": "🍂",
        "hot": "🥵", "cold": "🥶", "rain": "🌧️", "snow": "🌨️",
        "cloud": "☁️", "wind": "🌬️", "storm": "⛈️", "rainbow": "🌈",
        "earth": "🌍", "world": "🌎", "globe": "🌐", "map": "🗺️",
        "home": "🏠", "school": "🏫", "hospital": "🏥", "bank": "🏦",
        "store": "🏪", "restaurant": "🍽️", "cafe": "☕", "bar": "🍻",
        "movie": "🎬", "game": "🎮", "sport": "⚽", "travel": "✈️",
        "beach": "🏖️", "mountain": "⛰️", "city": "🏙️", "countryside": "🏞️",
        "morning": "🌅", "evening": "🌆", "night": "🌃", "day": "☀️",
        "friend": "👫", "family": "👨‍👩‍👧‍👦", "couple": "💑", "baby": "👶",
        "man": "👨", "woman": "👩", "boy": "👦", "girl": "👧",
        "old": "👴", "young": "👶", "beautiful": "💖", "ugly": "👹",
        "strong": "💪", "weak": " कमजोर", "fast": "⚡", "slow": "🐌",
        "big": "🐘", "small": "🐜", "tall": "🦒", "short": "矮",
        "clean": "🧼", "dirty": "💩", "new": "✨", "old": "👴",
        "open": "🔓", "close": "🔒", "on": "🔛", "off": "📴",
        "up": "⬆️", "down": "⬇️", "left": "⬅️", "right": "➡️",
        "in": "📥", "out": "📤", "start": "▶️", "stop": "⏹️",
        "pause": "⏸️", "next": "⏭️", "previous": "⏮️", "shuffle": "🔀",
        "repeat": "🔁", "volume up": "🔊", "volume down": "🔉", "mute": "🔇",
        "search": "🔍", "settings": "⚙️", "info": "ℹ️", "help": "❓",
        "ok": "👌", "cancel": "❌", "check": "✅", "cross": "❌",
        "warning": "⚠️", "error": "🚫", "success": "🎉", "fail": "❌",
        "question": "❓", "answer": "💡", "idea": "💡", "light": "💡",
        "dark": "🌑", "bright": "🌟", "dim": "🕯️", "loud": "🔊",
        "quiet": "🔇", "fast": "⚡", "slow": "🐌", "hot": "🥵",
        "cold": "🥶", "wet": "💧", "dry": "🏜️", "full": "🌕",
        "empty": "🗑️", "good": "👍", "bad": "👎", "great": "🤩",
        "terrible": "🤮", "happy": "😊", "sad": "😔", "angry": "😠",
        "excited": "🤩", "bored": "😑", "tired": "😴", "hungry": " cravings",
        "thirsty": "💧", "sick": "🤢", "healthy": "💪", "strong": "💪",
        "weak": " कमजोर", "smart": "🧠", "stupid": "🤪", "funny": "😂",
        "serious": "😐", "kind": "😇", "mean": "😈", "brave": "🦁",
        "scared": "😱", "shy": "😳", "confident": "😎", "proud": "🤩",
        "humble": "😌", "generous": "🤗", "selfish": "😒", "honest": "😇",
        "dishonest": "🤥", "loyal": "🐕", "disloyal": "🐍", "patient": "🧘",
        "impatient": "😤", "calm": "😌", "stressed": "😩", "relaxed": "😌",
        "busy": "🐝", "free": "🕊️", "rich": "💰", "poor": "乞丐",
        "clean": "🧼", "dirty": "💩", "new": "✨", "old": "👴",
        "beautiful": "💖", "ugly": "👹", "big": "🐘", "small": "🐜",
        "tall": "🦒", "short": "矮", "long": "📏", "short": "✂️",
        "wide": "↔️", "narrow": "↕️", "thick": "🍞", "thin": "📏",
        "hard": "💎", "soft": "☁️", "smooth": "✨", "rough": "🪨",
        "light": "💡", "dark": "🌑", "bright": "🌟", "dim": "🕯️",
        "loud": "🔊", "quiet": "🔇", "fast": "⚡", "slow": "🐌",
        "hot": "🥵", "cold": "🥶", "wet": "💧", "dry": "🏜️",
        "full": "🌕", "empty": "🗑️", "good": "👍", "bad": "👎",
        "great": "🤩", "terrible": "🤮", "happy": "😊", "sad": "😔",
        "angry": "😠", "excited": "🤩", "bored": "😑", "tired": "😴",
        "hungry": " cravings", "thirsty": "💧", "sick": "🤢", "healthy": "💪",
        "strong": "💪", "weak": " कमजोर", "smart": "🧠", "stupid": "🤪",
        "funny": "😂", "serious": "😐", "kind": "😇", "mean": "😈",
        "brave": "🦁", "scared": "😱", "shy": "😳", "confident": "😎",
        "proud": "🤩", "humble": "😌", "generous": "🤗", "selfish": "😒",
        "honest": "😇", "dishonest": "🤥", "loyal": "🐕", "disloyal": "🐍",
        "patient": "🧘", "impatient": "😤", "calm": "😌", "stressed": "😩",
        "relaxed": "😌", "busy": "🐝", "free": "🕊️", "rich": "💰",
        "poor": "乞丐", "clean": "🧼", "dirty": "💩", "new": "✨",
        "old": "👴", "beautiful": "💖", "ugly": "👹", "big": "🐘",
        "small": "🐜", "tall": "🦒", "short": "矮", "long": "📏",
        "short": "✂️", "wide": "↔️", "narrow": "↕️", "thick": "🍞",
        "thin": "📏", "hard": "💎", "soft": "☁️", "smooth": "✨",
        "rough": "🪨",
    }

    words = text.lower().split()
    translated_words = []
    for word in words:
        if word in emoji_map:
            translated_words.append(emoji_map[word])
        else:
            translated_words.append(word)
    return " ".join(translated_words)

if __name__ == "__main__":
    sentence = "I am very happy to eat pizza and drink water."
    translated_sentence = translate_to_emoji(sentence)
    import sys

    def print_unicode(text):
        sys.stdout.buffer.write((text + '\n').encode('utf-8'))

    sentence = "I am very happy to eat pizza and drink water."
    translated_sentence = translate_to_emoji(sentence)
    print_unicode(f"Original: {sentence}")
    print_unicode(f"Translated: {translated_sentence}")

    sentence2 = "The sun is bright and the sky is blue."
    translated_sentence2 = translate_to_emoji(sentence2)
    print_unicode(f"Original: {sentence2}")
    print_unicode(f"Translated: {translated_sentence2}")
