import random
import string

def generate_random_string(length):
    """Generates a random string of letters and digits."""
    characters = string.ascii_letters 
    return ''.join(random.choice(characters) for i in range(length))

# Generate a random string of length 10
random_string = generate_random_string(10)
print(random_string)