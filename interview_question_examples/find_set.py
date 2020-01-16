from collections import Counter

def get_set(paragraph):
    output = []
    counter = Counter(paragraph)
    paragraph_size = len(paragraph)
    max_frequency = max(counter.values())
    frequency_count = 1
    done = False
    while not done and frequency_count < max_frequency:
        next_letters = [letter for letter in counter if counter[letter] == frequency_count]
        for letter in next_letters:
            paragraph_size -= frequency_count
            if paragraph_size < 50:
                done = True
            output.append(letter)
        
        frequency_count += 1
    return output
    
paragraph = """We are an independent division within Spotify, we have the ability to move fast combined with the resources of the world's most forward-thinking audio company Come help us build the future of podcasting! If you want to jumpstart the process of talking to us about this role, here’s a little challenge: write a program that outputs the largest unique set of characters that can be removed from this paragraph without letting its length drop below 50."""
