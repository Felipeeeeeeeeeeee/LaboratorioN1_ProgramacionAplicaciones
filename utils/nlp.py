import spacy

class NLP:
    def __init__(self, sentence: str):
        self.nlp = spacy.load("es_core_news_md")
        self.doc = self.nlp(sentence)
        self.nouns = sum(1 for token in self.doc if token.pos_ == "NOUN")
        self.verbs = sum(1 for token in self.doc if token.pos_ == "VERB")


    def get_num_of_verbs_and_nouns(self) -> tuple:
        """
        Retorna en una tupla en la primera posición los sustantivos y en la segunda los verbos.
        """
        return (self.nouns, self.verbs)


    def get_word_labels(self) -> dict:
        """
        Retorna un diccionario donde cada palabra está etiquetada como "VERB", "NOUN" o "WORD".
        """
        word_labels = {}
        for token in self.doc:
            if token.pos_ == "VERB":
                word_labels[token.text] = "VERB"
            elif token.pos_ == "NOUN":
                word_labels[token.text] = "NOUN"
            else:
                word_labels[token.text] = "WORD"
        return word_labels
