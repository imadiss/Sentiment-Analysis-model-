import pandas as pd
import joblib

import re


def preprocess_text(text):
    text = text.lower()

    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    return text


def handle_negation(text):
    # List of negation patterns to handle
    negation_patterns = [
        # Handle multi-word negations (e.g., "not really", "not at all")
        (
        r'\b(not\s+really|not\s+at\s+all|not\s+exactly|not\s+so|not\s+very|not\s+too|not\s+much|not\s+any|not\s+quite)\b',
        lambda match: "NOT_" + match.group(0).replace(" ", "_")),

        # Handle "don't/doesn't/didn't + verb + object" (e.g., "I don't feel great")
        (r"\b(don't|doesn't|didn't)\s+(think|believe|feel|hope|know)\s+([\w\s]+)",
         lambda match: "NOT_" + match.group(2) + "_" + match.group(3).replace(" ", "_")),

        # Handle auxiliary verbs + "not" + verb (e.g., "I do not want", "You did not see")
        (r"\b(are|is|am|was|were|be|been|have|has|had)\s+not\s+(\w+)",
         r"NOT_\2"),

        # Handle general negations (e.g., "not happy", "never go")
        (r"\b(not|no|never|n't|don't|doesn't|didn't|can't|won't|wouldn't|wasn't|isn't|aren't|hasn't|haven't)\s+(\w+)",
         r"NOT_\2"),

        # Handle double negatives (e.g., "I don't need no help")
        (r"\b(no|not|never)\s+(.*?)(\bno\b|\bnot\b|\bnever\b)",
         r"NOT_\2 NOT_\3"),

        # Handle implicit negations (e.g., "hardly", "without", "any")
        (r'\b(hardly|barely|scarcely|rarely|few|little|without|none|nobody|nothing|neither|nor|any)\b',
         lambda match: "NOT_" + match.group(0)),

        # Handle punctuation immediately after negations (e.g., "not!")
        (r"\b(not|no|never|n't|don't|doesn't|didn't|can't|won't|wouldn't|isn't|aren't|hasn't|haven't)\b([^\w\s])",
         r"NOT\2")
    ]

    # Apply all negation patterns
    for pattern, replacement in negation_patterns:
        text = re.sub(pattern, replacement, text)

    # Replace spaces after 'NOT_' with underscores for consistent formatting
    text = re.sub(r'NOT_(\S+)', lambda match: 'NOT_' + match.group(1).replace(" ", "_"), text)

    return text









v=joblib.load("vectorizer3.pkl")
model=joblib.load("sentiment_analysis_model3.pkl")





def prediction(text):
    text = handle_negation(text)
    text = preprocess_text(text)
    t=v.transform([text])
    res=model.predict(t)
    if res[0]==1:
        return "Postive"
    elif res[0]==0:
        return "Neutral"
    else: return "Negative"


