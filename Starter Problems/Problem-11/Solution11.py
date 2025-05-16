rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'

char_count = {}
for char in rhyme:
    char = char.lower()
    if char.isalpha():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
            
max_char = None
max_freq = 0




for char in char_count:
    if char_count[char] > max_freq:
        max_freq = char_count[char]
        max_char = char
print(f"The most frequent character is '{max_char}' with frequency {max_freq}")
