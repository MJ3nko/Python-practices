#!/bin/python3


def first_solution(line: str):
    words = line.split(sep=" ")
    sentence = []
    for word in words:
        sentence.append(word.capitalize())
    sentence = " ".join(sentence)
    return sentence


def second_solution(line: str):
    words = line.split(sep=" ")
    sentence = []
    for word in words:
        word = word[:1].upper() + word[1:]
        sentence.append(word)
    sentence = " ".join(sentence)
    return words


if __name__ == "__main__":
    line = input()
    result = first_solution(line)
    print(result)
