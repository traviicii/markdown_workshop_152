
# For loop Review

stuff = ['item1', 'item2', 'item3', 'item4']

for thing in stuff:
    if thing == 'item3':
        print(thing.upper())
    else:
        print(f"The thing my for loop is currently looking at is: {thing}")

def d():
    print('='*50)

flavors = ['chocolate', 'vanilla', 'strawberry', 'pistachio']
toppings = ['sprinkles', 'chocolate syrup', 'whipped cream', 'cherry']
sizes = ['small', 'medium', 'large']


for flavor in flavors:
    for topping in toppings:
        print(f"Outer Loop: {flavor}, Inner Loop: {topping}")

d()

python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

keywords = ["good", "excellent", "bad", "poor", "average"]

for review in python_reviews:
    for word in keywords:
        if word in review:
            x = review.replace(word, word.upper())
            print(x)

python_positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

for review in python_reviews:
    pos_count = 0
    neg_count = 0
    for word in python_positive_words:
        if word in review:
            pos_count += 1
    for word in negative_words:
        if word in review:
            neg_count += 1
    d()
    print(review)
    print(f"Positive words: {pos_count}")
    print(f"Negative words: {neg_count}")
    d()


d()

how_many_times = 0

for i in range(0, 20, 2):
    how_many_times += 1
    print(f"i = {i} and I've done this {how_many_times} times now.")