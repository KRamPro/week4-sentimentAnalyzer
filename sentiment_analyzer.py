"""Train and evaluate a movie-review sentiment classifier."""

import nltk
from nltk.corpus import movie_reviews
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

nltk.download("movie_reviews", quiet=True)

positive_reviews = movie_reviews.fileids("pos")
negative_reviews = movie_reviews.fileids("neg")

positive_count = len(positive_reviews)
negative_count = len(negative_reviews)

print(f"Positive reviews: {positive_count}")
print(f"Negative reviews: {negative_count}")

# Numbers beat vibes when checking class balance.
if positive_count > negative_count:
    print("There are more positive reviews.")
elif positive_count < negative_count:
    print("There are more negative reviews.")
else:
    print("The classes are balanced.")

review_ids = positive_reviews + negative_reviews
reviews = [movie_reviews.raw(review_id) for review_id in review_ids]
labels = [movie_reviews.categories(review_id)[0] for review_id in review_ids]

# Keep the same split each time, and save a fair share of each class.
train_reviews, test_reviews, train_labels, test_labels = train_test_split(
    reviews, labels, test_size=0.2, random_state=42, stratify=labels
)

print(f"\nTraining reviews: {len(train_reviews)}")
print(f"Test reviews: {len(test_reviews)}")

vectorizer = CountVectorizer()
train_vectors = vectorizer.fit_transform(train_reviews)
test_vectors = vectorizer.transform(test_reviews)

classifier = MultinomialNB()
classifier.fit(train_vectors, train_labels)
predictions = classifier.predict(test_vectors)

accuracy = accuracy_score(test_labels, predictions)
matrix = confusion_matrix(test_labels, predictions, labels=["neg", "pos"])

print(f"\nAccuracy: {accuracy}")
print("Confusion matrix (rows: actual; columns: predicted)")
print("Order: negative, positive")
print(matrix)
