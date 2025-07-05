import re

def find_and_highlight(pattern, text, highlight_char='*'):
    matches = list(re.finditer(pattern, text))
    if not matches:
        return text, []

    highlighted_text = list(text)
    found_matches = []

    offset = 0
    for match in matches:
        start, end = match.span()
        
        # Insert highlight characters
        highlighted_text.insert(end + offset, highlight_char)
        highlighted_text.insert(start + offset, highlight_char)
        
        # Adjust offset for next insertions
        offset += 2
        
        found_matches.append(match.group(0))

    return "".join(highlighted_text), found_matches

if __name__ == "__main__":
    text = "The quick brown fox jumps over the lazy dog. The fox is quick."
    
    # Test 1: Simple word search
    pattern1 = r"fox"
    highlighted_text1, matches1 = find_and_highlight(pattern1, text)
    print(f"Text: {text}")
    print(f"Pattern: {pattern1}")
    print(f"Highlighted: {highlighted_text1}")
    print(f"Matches: {matches1}")
    print("\n" + "-"*30 + "\n")

    # Test 2: Case-insensitive search
    pattern2 = r"the"
    highlighted_text2, matches2 = find_and_highlight(pattern2, text, highlight_char='_')
    print(f"Text: {text}")
    print(f"Pattern: {pattern2} (case-insensitive)")
    print(f"Highlighted: {highlighted_text2}")
    print(f"Matches: {matches2}")
    print("\n" + "-"*30 + "\n")

    # Test 3: Digits
    text3 = "My phone number is 123-456-7890 and my age is 30."
    pattern3 = r"\d+"
    highlighted_text3, matches3 = find_and_highlight(pattern3, text3, highlight_char='#')
    print(f"Text: {text3}")
    print(f"Pattern: {pattern3}")
    print(f"Highlighted: {highlighted_text3}")
    print(f"Matches: {matches3}")
    print("\n" + "-"*30 + "\n")

    # Test 4: No match
    pattern4 = r"zebra"
    highlighted_text4, matches4 = find_and_highlight(pattern4, text)
    print(f"Text: {text}")
    print(f"Pattern: {pattern4}")
    print(f"Highlighted: {highlighted_text4}")
    print(f"Matches: {matches4}")
    print("\n" + "-"*30 + "\n")

