def split_words(text: str) -> set:
    """
    take a string and make a set of words (or quasi-words) used in it.
    :param text: Text to be broken down into discreet words based on space characters.
    :return: set of words in text
    """

    return set(text.split())


text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here.

preps_used = prepositions & split_words(text)
print(preps_used)