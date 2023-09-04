import spacy
import re
from unidecode import unidecode

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


    def get_cleaned_words(self) -> str:
        """
        Retorna una lista de palabras de la oración sin acentos ni símbolos, en minúsculas.
        """
        cleaned_words = []
        for token in self.doc:
            cleaned_word = unidecode(token.text.lower())
            cleaned_word = re.sub(r'[^a-z ]', '', cleaned_word)
            cleaned_words.extend(cleaned_word.split())
        return ' '.join(cleaned_words)


    def count_words(self) -> list[tuple[str, str]]:
        """
        Cuenta la frecuencia de cada palabra en la oración y devuelve una lista de tuplas
        donde cada tupla contiene la palabra y su frecuencia.
        """
        word_counts = {}
        for token in self.doc:
            cleaned_word = unidecode(token.text)
            if cleaned_word in word_counts:
                word_counts[cleaned_word] += 1
            else:
                word_counts[cleaned_word] = 1
        word_frequency_list = [(word, count) for word, count in word_counts.items()]
        return word_frequency_list
