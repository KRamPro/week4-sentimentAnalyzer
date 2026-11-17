"""Labeled reviews for testing the sentiment analyzer."""

from sentiment_analyzer import classifier, vectorizer

challenge_reviews = {
    "negation": [
        ("The movie was not nearly as funny as the trailer.", "neg"),
        ("I didn't enjoy watching any of these characters.", "neg"),
        ("The ending wasn't bad at all; it pulled the story together.", "pos"),
        ("I can't say I hated it. I'd watch it again.", "pos"),
        ("The plot never gets interesting, even near the end.", "neg"),
    ],
    "sarcasm": [
        ("Wonderful, another movie where everyone whispers in the dark for two hours.", "neg"),
        ("Just what I wanted: a plot that explains itself three times.", "neg"),
        ("The dialogue was a real treat, especially the five speeches about friendship.", "neg"),
        ("Great, they saved the best part for the credits.", "neg"),
        ("I loved paying to watch the camera shake while nothing happened.", "neg"),
    ],
    "mixed sentiment": [
        ("The sets looked lovely, but the story bored me the whole time.", "neg"),
        ("The acting was uneven, but the story kept me hooked.", "pos"),
        ("I liked the music, though it couldn't save the terrible dialogue.", "neg"),
        ("The beginning dragged, but the ending made the wait worthwhile.", "pos"),
        ("Some jokes landed, but most of the movie felt like a chore.", "neg"),
    ],
    "intensity": [
        ("It was fine. I enjoyed it enough.", "pos"),
        ("I liked the movie quite a bit.", "pos"),
        ("I absolutely loved every minute of it.", "pos"),
        ("I didn't care much for it.", "neg"),
        ("I hated every single minute and couldn't wait for it to end.", "neg"),
    ],
    "domain shift": [
        ("The soup arrived cold, and the bread was stale.", "neg"),
        ("My new headphones fit comfortably and sound great on the bus.", "pos"),
        ("The hotel room was clean, and the staff helped us find a late dinner.", "pos"),
        ("The zipper broke the first time I wore the jacket.", "neg"),
        ("Our server forgot half the order and never came back with water.", "neg"),
    ],
}

print("\nChallenge set accuracy:")
for category, reviews in challenge_reviews.items():
    correct = 0

    for review, label in reviews:
        review_vector = vectorizer.transform([review])
        prediction = classifier.predict(review_vector)[0]
        if prediction == label:
            correct += 1

    accuracy = correct / len(reviews)
    print(f"{category}: {correct}/{len(reviews)} ({accuracy:.0%})")
