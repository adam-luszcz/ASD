from projekt2.heap import *


def build_occurrence_dict(text: str) -> dict:
    occurrence_dict = {}
    for el in text:
        if el in occurrence_dict:
            occurrence_dict[el] += 1
        else:
            occurrence_dict[el] = 1
    return occurrence_dict


def build_priority_queue(occurrence_dict: dict) -> list:
    queue = []
    for key, val in occurrence_dict.items():
        heap_enq(queue, (val, key))
    return queue


def main():
    with open('input_text.txt', 'r') as f:
        text = f.read()

    # print(build_occurrence_dict(text))
    occurrence_dict = build_occurrence_dict(text)
    print(build_priority_queue(occurrence_dict))


if __name__ == '__main__':
    main()
