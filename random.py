import random

# List of categories
categories = [
    "Exhibit or museum",
    "Clothing store",
    "Book store",
    "Food store",
    "Sporting goods store"
]

# Select one category randomly 200 times
random_categories = [random.choice(categories) for _ in range(200)]

# Count occurrences of each category
category_counts = {category: random_categories.count(category) for category in categories}

print(category_counts)
