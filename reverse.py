def reverse_sent(sentence):
    word_list = sentence.split(' ')
    word_list.reverse()
    return ' '.join(word_list)