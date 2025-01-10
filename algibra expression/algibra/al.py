import re

# Input string
input_str = 'Layla is a good data scientist'

# Regular expression to find words with exactly two 'a's
pattern = r'\b\w*[aA]\w*[aA]\w*\b'

# Find all matching words
matching_words = re.findall(pattern, input_str)

# Print the result
print(matching_words)
