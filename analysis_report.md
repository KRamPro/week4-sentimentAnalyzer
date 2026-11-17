# Sentiment analysis report

## Held-out test results

The dataset contains 1,000 positive and 1,000 negative movie reviews. The model was trained on 1,600 reviews and tested on 400. Its accuracy was 81.75%.

The model sees word counts, but it doesn't see the order those words came in.

| Actual / predicted | Negative | Positive |
| --- | ---: | ---: |
| Negative | 162 | 38 |
| Positive | 35 | 165 |

## Challenge set results

| Category | Correct | Accuracy |
| --- | ---: | ---: |
| Negation | 3/5 | 60% |
| Sarcasm | 2/5 | 40% |
| Mixed sentiment | 3/5 | 60% |
| Intensity | 4/5 | 80% |
| Domain shift | 4/5 | 80% |

Sarcasm was the hardest category at 40%, compared with 81.75% on the chunk of the training data we set aside to test with. With only five reviews in each category, these results show where the model struggled on this set, not how it will perform on every review.

### Negation

Both reviews were labeled positive but predicted negative:

- "The ending wasn't bad at all; it pulled the story together."
- "I can't say I hated it. I'd watch it again."

The model cannot identify combinations of words that might identify the sentiment better for negation. It likely learned that "bad" and "Hated" appear in negative sentiment reviews. To fix this we could take in combinations of words. we could identify those major sentiment identifiers and then take in words before and after them for additional context during training. One way to do this is with bigrams, so "not good" can be treated differently from how the individual words would be treated. This would mean having a larger vocabulary to train off of though.

### Sarcasm

All three reviews were labeled negative but predicted positive:

- "Wonderful, another movie where everyone whispers in the dark for two hours."
- "The dialogue was a real treat, especially the five speeches about friendship."
- "Great, they saved the best part for the credits."

The model predicted positive for three negative reviews that had words like "wonderful" and "A Real Treat". Those positive words may have influenced its predictions. Since the model sees word counts instead of word order, it can miss the context that makes the praise sarcastic.

### Mixed sentiment

Both reviews were labeled positive but predicted negative:

- "The acting was uneven, but the story kept me hooked."
- "The beginning dragged, but the ending made the wait worthwhile."

These two were positive over-all but included criticisms. I suspect that the model gave the negative words more weight than the positive ones, and that there are other constructions of sentences like "but" that might be included to logically extend or modify the sentiment.

### Intensity

The following review was labeled positive but predicted negative:

- "I absolutely loved every minute of it."

This one was predicted as negative despite saying explicitly that they loved it. I suspect the model may not have learned enough from intense phrasing in the training set. The model doesn't distinguish mild from strong sentiment. The 80% result only measures positive and negative labels.

### Domain shift

The following review was labeled negative but predicted positive:

- "The zipper broke the first time I wore the jacket."

The model predicted positive for this complaint about a jacket zipper. It was trained on movie reviews so it may not have learned how the state of a zipper relates at all to positive or negative sentiment since there are no pure indicator words like loved or hated to latch on to.

## Deployment

I would train this model on more granular data with potentially a mixed sentiment or unsure sentiment output so that it could be clarified. If we provided the ability for a model to take in extra combinations of words also we could get better performance on negation tasks and other forms of complaints. I would not depoy this model as is, especially if I wanted to deal with angry customers, because it seemed to do poorly on sarcastic comments and negation tasks. That would mean that there is a margin of error for customers to get routed incorrectly, or sarcastic or negative comments to be reported as praise and throw off other systems reliant on that information.
