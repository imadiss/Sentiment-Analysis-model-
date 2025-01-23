import csv
import random

# Define the number of datasets and rows per dataset
num_datasets = 10  # Number of small datasets to generate
rows_per_dataset = 10000  # Rows per dataset

# Define the sentiment labels
sentiments = [1, -1, 0]  # 1 for positive, -1 for negative, 0 for neutral

# Define a larger set of sample phrases for each sentiment
positive_phrases = [
    "I love this product!", "This is amazing!", "Great experience!", "Highly recommended!", "Fantastic service!",
    "Excellent quality!", "Very satisfied!", "Wonderful product!", "Impressive work!", "Top-notch service!",
    "Absolutely brilliant!", "Couldn't be happier!", "Perfect in every way!", "Exceeded my expectations!",
    "Best purchase ever!", "Truly outstanding!", "Superb quality!", "A joy to use!", "Incredible value!",
    "Highly impressed!", "Simply the best!", "Absolutely delightful!", "Worth every penny!", "Flawless performance!",
    "A game-changer!", "Exceptional service!", "Pure perfection!", "A must-have!", "Beyond amazing!",
    "Unbelievable quality!", "A dream come true!", "Absolutely stunning!", "Perfectly executed!", "A true gem!",
]

negative_phrases = [
    "I hate this product!", "This is terrible!", "Awful experience!", "Would not recommend!", "Poor service!",
    "Very disappointed!", "Waste of money!", "Horrible quality!", "Unacceptable service!", "Frustrating to use!",
    "Not worth it!", "Complete garbage!", "Extremely dissatisfied!", "Regret buying this!", "A total disaster!",
    "Worst experience ever!", "Broken on arrival!", "Terrible customer service!", "Not as described!",
    "Avoid at all costs!",
    "Extremely poor quality!", "A huge letdown!", "Unreliable product!", "Not functional!", "A complete waste!",
    "Utterly disappointed!", "Shockingly bad!", "Unusable product!", "Extremely frustrating!",
    "A nightmare to deal with!",
]

neutral_phrases = [
    "This is okay.", "It's just average.", "Not bad, not great.", "It's fine.", "Nothing special.",
    "Meets basic expectations.", "Decent product.", "Neither good nor bad.", "Average quality.", "Fairly standard.",
    "Does the job.", "Not particularly impressive.", "Mediocre at best.", "Acceptable but not great.", "Just alright.",
    "Not remarkable.", "Fairly average.", "Neither here nor there.", "Passable quality.", "Not outstanding.",
    "Does what it needs to.", "Not exceptional.", "Fairly ordinary.", "Not amazing, not terrible.", "Just so-so.",
    "Not the best, not the worst.", "Fairly unremarkable.", "Not particularly noteworthy.", "Just average.", "Not bad.",
]

# Define negation phrases to handle negations
negation_phrases = [
    "not ", "isn't ", "aren't ", "don't ", "doesn't ", "can't ", "couldn't ", "won't ", "wouldn't ", "shouldn't ",
]


# Function to generate a random sentence with possible negation
def generate_sentence(sentiment):
    if sentiment == 1:
        phrase = random.choice(positive_phrases)
    elif sentiment == -1:
        phrase = random.choice(negative_phrases)
    else:
        phrase = random.choice(neutral_phrases)

    # Randomly add a negation to the sentence
    if random.random() < 0.2:  # 20% chance of adding a negation
        negation = random.choice(negation_phrases)
        phrase = negation + phrase.lower()

    return phrase


# Generate multiple datasets
for dataset_num in range(1, num_datasets + 1):
    data = []
    for _ in range(rows_per_dataset):
        sentiment = random.choice(sentiments)
        sentence = generate_sentence(sentiment)
        data.append([sentence, sentiment])

    # Write the dataset to a CSV file
    csv_filename = f"sentiment_analysis_dataset_{dataset_num}.csv"
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["text", "sentiment"])  # Write the header
        writer.writerows(data)  # Write the data

    print(f"Generated dataset {dataset_num} with {rows_per_dataset} rows in '{csv_filename}'.")

print("All datasets generated successfully!")