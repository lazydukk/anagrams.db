import re
file = input("file path: ")
text = open(file).read()

def retain_capitalized_four_letter_words(text):
    
    pattern = r'\b[A-Z]{4}\b'
    words = re.findall(pattern, text)
    result = '\n'.join(words)
    
    return result

def remove_unwanted_characters(text):
    clean_text = re.sub(r'[^A-Z\s]', '', text)
    
    result = retain_capitalized_four_letter_words(clean_text)
    
    return result

if __name__ == "__main__":
    result = remove_unwanted_characters(text)
    print(result)
    
    
open("stripped-"+file, 'w').write(str(result))

