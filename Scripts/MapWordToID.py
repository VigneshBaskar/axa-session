class MapWordToID(object):
    def __init__(self, vocab_dict):
        self.vocab_dict = vocab_dict
      
    def word_list_to_id_list(self, word_list):
        # It is necessary that the unknown word should be present in the vocab_dict
        id_list = [self.vocab_dict[word] for word in word_list if word in self.vocab_dict.keys()]
        return id_list

    def word_lists_to_id_lists(self, word_lists):
        id_lists = [self.word_list_to_id_list(word_list) for word_list in word_lists]
        return id_lists
