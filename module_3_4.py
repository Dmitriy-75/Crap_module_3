def single_root_words(root_word,*other_words):
    same_words = []
    i = 0
    while i < len(other_words):
        if str.lower(root_word) in str.lower(other_words[i]):
            same_words.append(other_words[i])
        elif str.lower(other_words[i]) in str.lower(root_word):
            same_words.append(other_words[i])
        i += 1
    return(same_words)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)















