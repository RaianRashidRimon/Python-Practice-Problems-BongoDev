def capitalize(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

input_sentence = "python for web developers"
output_sentence = capitalize(input_sentence)
print(output_sentence)