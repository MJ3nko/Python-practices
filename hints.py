def type_hint(name: str) -> str:
    # Make code more readable.
    # Python 3.5+
    print(f"Hello {name}")


def readability():
    # Improve readability of large numbers.
    # Python 3.6+
    x = 1_000_000
    y = 1000000
    print(x, y, x == y)


def comments():

    comments = """
    Comments should be complete sentences.
    Comments that contradict the code are worse than no comments. 
    Always make a priority of keeping the comments up-to-date when the code changes!    
    
    If a comment is a phrase or sentence, its first word should be capitalized, 
    unless it is an identifier that begins with a lower case letter (never alter the case of identifiers!).

    If a comment is short, the period at the end can be omitted.
    Block comments generally consist of one or more paragraphs built out of complete sentences, and each sentence should end in a period.
    You should use two spaces after a sentence-ending period.
    """

    print(comments)


type_hint("Anonymous")
readability()
comments()
