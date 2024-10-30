def single_root_words(root_word, *other_words):
    root_word_lower = root_word.lower()
    same_words = []

    for word in other_words:
        word_lower = word.lower()
        if root_word_lower in word_lower or word_lower in root_word_lower:

            same_words.append(word)

    print(same_words)

single_root_words('Six',
                  'five', 'six', 'seven', 'fifteen', 'sixteen', 'seventeen', 'fifty', 'sixty', 'seventy')
single_root_words('apple', 'Apple_juice', 'pineapple', 'PLUM', 'apple', 'orange')