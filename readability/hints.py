from time import ctime


def pronounceable_names():

    generated_timestamp = ctime()
    print(f"Generated timestamp is: {generated_timestamp}")


def type_hint(name: str) -> str:
    # Make code more readable.
    # Python 3.5+
    print(f"Hello {name}")


def readability_example():
    # Improve readability of large numbers.
    # Python 3.6+
    seconds_in_a_month = 2_629_743
    million = 1000000
    print(seconds_in_a_month, million, seconds_in_a_month == million)


def print_comments_guidelines():

    comments = """
    Comments should be complete sentences.
    Comments that contradict the code are worse than no comments.
    Always make a priority of keeping the comments
    up-to-date when the code changes!

    If a comment is a phrase or sentence, its first word should be capitalized,
    unless it is an identifier that begins
    with a lower case letter (never alter the case of identifiers!).

    If a comment is short, the period at the end can be omitted.
    Block comments generally consist of one or more paragraphs
    built out of complete sentences, and each sentence should end in a period.
    You should use two spaces after a sentence-ending period.
    """

    print(comments)


def stepdown():

    comments = """
    Use the stepdown rule for class methods and other functions.
    Follow the public, private, public method and so forth arrangement in the code.
    """

    print(comments)


def main():
    pronounceable_names()
    type_hint("Anonymous")
    readability_example()
    print_comments_guidelines()
    stepdown()


if __name__ == "__main__":
    main()
