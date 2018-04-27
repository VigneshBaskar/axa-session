class VocabDict(object):
    @staticmethod
    def create_vocab_dict(all_documents_tokenized_words, min_doc_count=30):
        # all_documents_tokenized_words is a list of list of strings. Each document is word tokenized resulting in a list of strings.
        # All these list of strings is concatentated into one single list
        vocab_dict = {}
        for one_document_tokenized_words in all_documents_tokenized_words:
            for word in one_document_tokenized_words:
                if word not in vocab_dict.keys():
                    vocab_dict[word] = 1
                else:
                    vocab_dict[word] += 1
        vocab_dict = dict((k, v) for k, v in vocab_dict.items() if v >= min_doc_count)
        vocab_dict = dict((k, i) for k, i in zip(vocab_dict.keys(), range(len(vocab_dict))))
        rev_vocab_dict = dict(zip(vocab_dict.values(), vocab_dict.keys()))
        return vocab_dict, rev_vocab_dict
