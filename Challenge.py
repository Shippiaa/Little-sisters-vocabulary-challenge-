# Function to add 'un' to the beginning of a word
def add_prefix_un(word):
    # Combine 'un' with the original word
    new_word = 'un' + word
    # Print and return the new word
    print(new_word)
    return new_word

# Function to create new words with a common prefix
def make_word_groups(vocab_words):
    # Extract the prefix which is the first word in the list
    prefix = vocab_words[0]
    # Create a list to hold the new words, starting with the prefix itself
    new_list = [vocab_words[0]]
    # Loop over the rest of the words and add the prefix to each
    for word in vocab_words[1:]:
        new_word = prefix + word
        new_list.append(new_word)
    # Print and return the list of new words
    print(new_list)
    return new_list

# Function to remove the suffix 'ness' from words
def remove_suffix_ness(word):
    # Check if the word ends with 'ness'
    if word.endswith('ness'):
        # Cut off the last 4 characters ('ness')
        base_word = word[:-4]
        # If the remaining word ends with 'i', change it to 'y'
        if base_word[-1] == 'i':
            new_word = base_word[:-1] + 'y'
        else:
            new_word = base_word
        # Print and return the new word
        print(new_word)
        return new_word
    # If there's no 'ness' suffix, print and return the word as is
    print(word)
    return word

# Function to change adjectives to verbs
def adjective_to_verb(sentence, index):
    # Split the sentence into words
    words = sentence.split()
    # Select the word at the specified index
    adjective = words[index].strip('.,!?')
    # If the adjective ends with 'e', just add 'n' to make it a verb
    if adjective[-1] == 'e':
        verb = adjective + 'n'
    else:
        # Otherwise, add 'en' to make it a verb
        verb = adjective + 'en'
    # Print and return the new verb
    print(verb)
    return verb

# Testing the functions with example inputs
add_prefix_un("happy")               
add_prefix_un("manageable")           

make_word_groups(['en', 'close', 'joy', 'lighten'])
make_word_groups(['pre', 'serve', 'dispose', 'position'])

remove_suffix_ness("heaviness")
remove_suffix_ness("sadness")

adjective_to_verb("I need to make that bright.", -1)

