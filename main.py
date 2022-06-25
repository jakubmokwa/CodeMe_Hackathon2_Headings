def init_heading_sets():
    heading_set1 = [{id: 1, 'title': "heading1", 'heading_level': 0},
                    {id: 2, 'title': "heading2", 'heading_level': 2},
                    {id: 3, 'title': "heading3", 'heading_level': 1},
                    {id: 4, 'title': "heading4", 'heading_level': 1}]

    heading_set2 = [{id: 1, 'title': "heading1", 'heading_level': 0},
                    {id: 2, 'title': "heading2", 'heading_level': 3},
                    {id: 3, 'title': "heading3", 'heading_level': 4},
                    {id: 4, 'title': "heading4", 'heading_level': 1},
                    {id: 5, 'title': "heading5", 'heading_level': 0}]

    heading_set3 = [{id: 1, 'title': "heading1", 'heading_level': 3},
                    {id: 2, 'title': "heading2", 'heading_level': 2},
                    {id: 3, 'title': "heading3", 'heading_level': 1},
                    {id: 4, 'title': "heading4", 'heading_level': 5},
                    {id: 5, 'title': "heading5", 'heading_level': 0}]

    return heading_set1, heading_set2, heading_set3


def write_md(heading_set, filename):
    with open(filename + '.md', 'w') as f:
        for i in heading_set:
            line = ''.join('#' * (i['heading_level'] + 1))
            line = line + ' ' + i['title'] + '\n'
            f.write(line)


def main():
    heading_set1, heading_set2, heading_set3 = init_heading_sets()
    list_heading_sets = [heading_set1, heading_set2, heading_set3]
    for index, h_set in enumerate(list_heading_sets):
        filename = 'heading' + str(index + 1)
        write_md(h_set, filename)


if __name__ == '__main__':
    main()
