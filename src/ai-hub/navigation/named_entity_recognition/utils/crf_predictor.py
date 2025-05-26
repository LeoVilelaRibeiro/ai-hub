import os
import pycrfsuite
import re


def tokenize(text):
    return re.findall(r"\w+|[^\w\s]", text)


def word2features(sent, i):
    word = sent[i].strip()

    features = {
        "bias": 1.0,
        "word.lower()": word.lower(),
        "word.isupper()": word.isupper(),
        "word.istitle()": word.istitle(),
        "word.isdigit()": word.isdigit(),
        "prefix-1": word[0] if len(word) >= 1 else "",
        "suffix-1": word[-1] if len(word) >= 1 else "",
        "prefix-2": word[:2] if len(word) >= 2 else word,
        "suffix-2": word[-2:] if len(word) >= 2 else word,
        "prefix-3": word[:3] if len(word) >= 3 else word,
        "suffix-3": word[-3:] if len(word) >= 3 else word,
    }

    if i > 0:
        prev_word = sent[i - 1].strip()
        features.update(
            {
                "-1:word.lower()": prev_word.lower(),
                "-1:word.istitle()": prev_word.istitle(),
                "-1:word.isupper()": prev_word.isupper(),
            }
        )
    else:
        features["BOS"] = True

    if i < len(sent) - 1:
        next_word = sent[i + 1].strip()
        features.update(
            {
                "+1:word.lower()": next_word.lower(),
                "+1:word.istitle()": next_word.istitle(),
                "+1:word.isupper()": next_word.isupper(),
            }
        )
    else:
        features["EOS"] = True

    return features


def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]


def predict(text: str) -> dict:
    tokens = tokenize(text)
    features = sent2features(tokens)

    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    MODEL_PATH = os.path.join(CURRENT_DIR, "../models/ner-crf.model")

    tagger = pycrfsuite.Tagger()
    tagger.open(MODEL_PATH)

    predictions = tagger.tag(features)

    result = {}
    for token, label in zip(tokens, predictions):
        if label != "LX":
            if label in result:
                result[label] += f" {token}"
            else:
                result[label] = token

    return {k: v.strip() for k, v in result.items()}
