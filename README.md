# Sentiment Analyzer for Reviews

## Project questions

- How many reviews belong to each class, and are the classes balanced?
- What accuracy and confusion matrix does the classifier produce on the held-out test set?
- What information does the model's text representation preserve, and what does it lose?
- How accurate is the classifier for negation, sarcasm, mixed sentiment, intensity, and domain shift?
- Does the model distinguish mild sentiment from strong sentiment?
- Which category was most difficult, and why?
- How does held-out test accuracy compare with accuracy in each challenge category?
- What change could improve the handling of negation, and what would it cost?
- Would you deploy this analyzer? What might happen to sarcastic customers if it routed angry customers to a human?

## Directory

```text
.
├── sentiment_analyzer.py  # Sentiment classifier
├── challenge_set.py       # Labeled challenge reviews and evaluation
├── requirements.txt       # Project dependencies
├── analysis_report.md     # Results and analysis
├── notebook/              # Notebook assignment
├── Resources/             # Assignment instructions and lecture
├── README.md              # Project questions and directory
└── LICENSE
```
