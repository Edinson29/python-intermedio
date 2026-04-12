"""Example of using enumerate to iterate over a list with index."""

from sample_data import sample_articles

counter = 1
for article in sample_articles:
    print(f"{counter}: {article}")
    counter += 1

# Using enumerate to simplify the code, option #1
# PD: the enumerate start in 0 by default, but we can change it to start in 1
sample_articles_enum = enumerate(sample_articles, start=1)
for counter, article in sample_articles_enum:
    print(f"{counter}: {article}")

# Using enumerate to simplify the code, option #2
for counter, article in enumerate(sample_articles, start=10):
    print(f"{counter}: {article}")
