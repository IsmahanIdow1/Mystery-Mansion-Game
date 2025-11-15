import string

# List of "unimportant" words (feel free to add more)
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']


def filter_words(words, skip_words):
    """This function takes a list of words and returns a copy of the list from
    which all words provided in the list skip_words have been removed.
    For example:

    >>> filter_words(["help", "me", "please"], ["me", "please"])
    ['help']

    >>> filter_words(["go", "south"], skip_words)
    ['go', 'south']

    >>> filter_words(['how', 'about', 'i', 'go', 'through', 'that', 'little', 'passage', 'to', 'the', 'south'], skip_words)
    ['go', 'passage', 'south']

    In Mystery Mansion, this helps the game ignore filler words like "the" or "please".
    """
    filtered = [word for word in words if word not in skip_words]
    return filtered
    
def remove_punct(text):
    """This function is used to remove all punctuation
    marks from a string. Spaces do not count as punctuation and should
    not be removed. The funcion takes a string and returns a new string
    which does not contain any puctuation. For example:
    """

    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char

    return no_punct.strip()

def normalise_input(user_input):
    """This function removes all punctuation from the string and converts it to
    lower case. It then splits the string into a list of words (also removing any extra
    spaces between words) and futher remove all "unimportant" 
    words from the list of words using the filter_words() function.
    The resulting list of "important" word is returned. For example:

    >>> normalise_input("Go East to the Dining Room!")
    ['go', 'east', 'dining', 'room']
    >>> normalise_input("Take the Silver Key please ")
    ['take', 'silver', 'key']
    >>> normalise_input("Go down to the cellar now!")
    ['go', 'down', 'cellar']
    >>> normalise_input("Drop the key in the grand hall")
    ['drop', 'key', 'grand', 'hall']
    >>> normalise_input("I wish to go north to the library.")
    ['go', 'north', 'library']
    """
    # Remove punctuation and convert to lower case
    no_punct = remove_punct(user_input).lower()
    words = no_punct.split()
    important_words = filter_words(words, skip_words)

    return important_words