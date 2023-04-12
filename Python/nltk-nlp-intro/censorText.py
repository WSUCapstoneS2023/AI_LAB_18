#import nltk 
#import tkinter as tk
#from nltk.tokenize import word_tokenize
#from nltk.corpus import stopwords
#from nltk.stem import WordNetLemmatizer
import re

# run 'python -m spacy download en_core_web_md' before trying
import spacy

#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download("maxent_ne_chunker")
#nltk.download("words")
#nltk.download('wordnet')

#stop_words = set(stopwords.words("english"))

spacy_md = spacy.load('en_core_web_md')


#def toWordNetLabel(pos_label):
#    if pos_label.startswith('R'):
#        return "r"
#    if pos_label.startswith('J'):
#        return "a"
#    if pos_label.startswith('V'):
#        return "v"
#    if pos_label.startswith('N'):
#        return "n"
#    # default return noun
#    return "n"


#def lemmatize_words(pos_tagged_words):
#    lemmatizer = WordNetLemmatizer()
#
#    pos_tagged_words_converted = [(word, toWordNetLabel(p)) for word,p in pos_tagged_words]
#    lemmatized_words = [lemmatizer.lemmatize(word, pos=p) for word,p in pos_tagged_words_converted]
#    return lemmatized_words


#def get_filtered_tokenization(text):
#    tokenized_words = word_tokenize(text)
#    filtered_tokenization = [word for word in tokenized_words if word not in stop_words]
#    return filtered_tokenization


def regex_phone_numbers(text, censor_replacement):
    result = re.finditer(r"\(?\d{3}\)?[- .]\d{3}[- .]\d{4}", text, re.MULTILINE)
    ret, prevend = '', 0
    for match in result:
        sStart, sEnd = match.span()
        pNumber = text[sStart:sEnd]
                                                # replace with commented out if format/length dont need to be censored
        ret += text[prevend:sStart] + censor_replacement #''.join("*" if c.isdigit() else c for c in pNumber)
        prevend = sEnd
    ret += text[prevend:]
    return ret


def censor_text(text):
    censor_replacement = "-REDACTED-"
    current_text = regex_phone_numbers(text, censor_replacement)
    
    doc = spacy_md(current_text)
    entities_removed = " ".join([entity.text if not entity.ent_type_ else censor_replacement for entity in doc])
    return entities_removed


if __name__ == "__main__":
    example_text = """Gazprom 'in $36m back-tax claim' 333-333-3333

    The nuclear unit of Russian energy giant Gazprom is reportedly facing a 1bn rouble ($35.7m; £19.1m) back-tax claim for the 2001-2003 period.

    Vedomosti newspaper reported that Russian authorities made the demand at the end of last year. The paper added that most of the taxes claimed are linked to the company's export activity. Gazprom, the biggest gas company in the world, took over nuclear fuel giant Atomstroieksport in October 2004. The main project of Atomstroieksport is the building of a nuclear plant in Iran, which has been a source of tension between Russia and the US.

    Gazprom is one of the key players in the complex Russian energy market, where the government of Vladimir Putin has made moves to regain state influence over the sector. Gazprom is set to merge with state oil firm Rosneft, the company that eventually acquired Yuganskneftegas, the main unit of embattled oil giant Yukos. Claims for back-taxes was a tool used against Yukos, and led to the enforced sale Yuganskneftegas. Some analysts fear the Kremlin will continue to use these sort of moves to boost the efforts of the state to regain control over strategically important sectors such as oil."""

    censored_text = censor_text(example_text)
    print(example_text)
    print(censored_text)