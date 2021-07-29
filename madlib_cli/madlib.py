
import re
from typing import Tuple
from _pytest._code.code import TracebackEntry
# import parse


def read_template(filepath: str) -> str:
    try:
        with open(filepath, 'r') as file_1:
            file_text = file_1.read()
            return file_text.strip()
    except:
        raise


# 'It was a {Adjective} and {Adjective} {Noun}'


def parse_template(template: str) -> list:
    pattern = r'{(.*?)}'  # match everything in a non-greedy way and capture it
    striped_template = re.sub(pattern, '{}', template)
    striped_parts = tuple(re.findall(pattern, template))

    return striped_template, striped_parts


def merge(bare_template: str, language_parts: tuple) -> str:
    result = bare_template.format(*language_parts)
    return result


def writing_file(merged_template: str, filepath: str):
    with open(filepath, 'a') as new_file:
        # write the content to the file, using the write() method
        new_file.write(merged_template)
# print(merge("It was a {} and {} {}.", ("dark", "stormy", "night")))


if __name__ == "__main__":

    print(' **** Welcome to Madlib Game****\n***You need to enter a list of guessing words to play this game***\n ***and your guessed words should be an answer to the next questions and your answers should be separated by commas***\n')

    def_template = read_template('assets/template.txt')

    stripped_template, guessing_question = parse_template(def_template)

    def collecting_input(input_words):

        # input_words = ['Adjective', 'A First Name', 'Past Tense Verb', 'Plural Noun ?',
        # 'Large Animal', 'A Girl\'s Name', 'Number 1-50', 'First Name\'s']
        answers = []
        for word in input_words:

            user_input = input(f'***{word}***\n <')
            answers.append(user_input)

        return answers

    user_answers = collecting_input(guessing_question)
    print(user_answers)
    print(stripped_template)
    final_template = merge(stripped_template, user_answers)
    writing_file(final_template, 'assets/final_template.txt')
    print(final_template)


# parse_template(def_template)
# print(re.findall(r'?<=\{).+?(?=\}',
# 'It was a {Adjective} and {Adjective} {Noun}.'))
