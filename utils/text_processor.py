def process_text(text):
    return text.replace("\n", " ")

def truncate_text(text, max_length):
    text = process_text(text)
    text_label = text[:max_length] + '...' if len(text) > max_length else text
    return text_label
    