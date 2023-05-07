import random

# Initialise variables
article = ['a','the', 'an']
subject = ['man', 'women', 'bird', 'person', 'alien', 'dog', 'driver', 'cat', 'mouse']
verb = ['jump', 'join', 'sprint', 'skulk', 'fly', 'sramble', 'scramp', 'waddle']
adverb = ['loudly', 'quickly','stupidly', 'badly', 'quietly', 'soundly', 'slowly']

# function to pick a word
def pick(words):
    i = random.randint(0, len(words) - 1)
    return words[i]



# Request user input number od sentences generated
limit = 5 # default
try:
    limit = int(input("Enter the number of sentences to generate: "))
except ValueError as err:
    print(err, "five sentences will be generated")

# Iterate and create sentences
count = 0
while count < limit:
    if random.randint(1,2) == 2:
        print(pick(article), pick(subject), pick(verb))
    else:
        print(pick(article), pick(subject), pick(verb), pick(adverb))
    count += 1