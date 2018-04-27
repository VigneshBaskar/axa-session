class UnknownWordsProcessing(object):
    def __init__(self, vocab_list, replace, replace_unknow_word_with='unk'):
        self.vocab_list = vocab_list
        self.replace = replace # Boolean
        self.replace_unknow_word_with = replace_unknow_word_with #string
        
    def remove_or_replace_unkown_word_from_sentence(self, tokenized_sentence):    
        if self.replace == False:
            unknown_word_removed_sentence = [word for word in tokenized_sentence if word in self.vocab_list]
            return unknown_word_removed_sentence
        else:
            unknown_word_replaced_sentence = [word if word in self.vocab_list else self.replace_unknow_word_with for word in tokenized_sentence]
            return unknown_word_replaced_sentence

    def remove_or_replace_unkown_word_from_sentences(self, tokenized_sentences_tokenized_words):    
        unknown_word_removed_or_replaced_sentences = [self.remove_or_replace_unkown_word_from_sentence(tokenized_sentence) for tokenized_sentence in tokenized_sentences_tokenized_words]
        return unknown_word_removed_or_replaced_sentences

