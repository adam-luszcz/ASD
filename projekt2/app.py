from heap import heap_deq, heap_enq, is_min_heap


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


def build_tree(queue: list):
    while len(queue) > 1:
        a = heap_deq(queue)
        b = heap_deq(queue)
        heap_enq(queue, (a[0] + b[0], '', a, b))
    return heap_deq(queue)


def encode(n, binary_rep, txt):
    if n[1] != '':
        with open('output.txt', 'a') as f:
            f.write(f'{n[1]}: {binary_rep}\n')
        print(f'{n[1]}: {binary_rep}')
        txt = txt.replace(n[1], binary_rep)
        return txt
    txt = encode(n[2], binary_rep + '1', txt)
    txt = encode(n[3], binary_rep + '0', txt)
    return txt


def main():
    with open('input_text.txt', 'r') as f:
        text = f.read()

    occurrence_dict = build_occurrence_dict(text)
    queue = build_priority_queue(occurrence_dict)
    # print(queue)
    # print(is_min_heap([n[0] for n in queue]))
    # print(occurrence_dict)
    print('\nTablica kodowania: ')
    root_node = build_tree(queue)

    result = encode(root_node, '', text)
    print(f'\nZakodowany tekst: {result}')

    with open('output.txt', 'a', encoding='utf-8') as f:
        for i in range(0, len(result), 8):
            f.write(chr(int(result[i:8+i], 2)))


if __name__ == '__main__':
    main()
