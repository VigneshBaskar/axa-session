class SentenceProcessing(object):
    def pad_truncate_sent(self, tokenized_sentences_tokenized_words, chosen_sent_len, dummy_token='my_dummy'):
        preprocessed_documents = []
        for sent in tokenized_sentences_tokenized_words:
            if len(sent) <= chosen_sent_len:
                sent = sent + ['my_dummy'] * (chosen_sent_len-len(sent))

            if len(sent) > chosen_sent_len:
                sent = sent[:chosen_sent_len]
            preprocessed_documents.append(sent)
        return preprocessed_documents


