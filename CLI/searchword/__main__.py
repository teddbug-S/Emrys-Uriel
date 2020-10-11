import os
from colored import fg, attr, bg


# asking for file we'll be working with
def ask_file():
    user_input = input(r'File: ')
    return user_input

# takes search query and file content
def do_search(query, con):
    # for veryfying search result
    found = False
    # if search in the file content
    if query in con:
        # getting the position
        position = con.index(query) + 1
        # printing it
        print(f'{query} found at line {position}.')
    else:
        # getting each line
        for line in con:
            # else if query in a line maybe a word
            if query in (listed_line := line.split()):
                # getting word in line position
                word_pos = listed_line.index(query)
                # getting line position in content or file
                line_pos = con.index(line)+1
                # changing or coloring the found word in the line
                listed_line[word_pos] = "%s%s{}%s".format(query) % (bg(226), fg(232), attr('reset'))
                # finally printing it
                print(f"\nWord found at {word_pos + 1} in line {line_pos}.")
                print("'{}'".format(" ".join(listed_line)))
                found = True
    if not found:
        print('No matches found')


def main():
    file_path = ask_file()
    while True:
        quest = input('\nSearch line or word: ').strip()
        with open(file_path, 'r') as f:
            contents = f.read()
            lines = contents.split('\n')
            do_search(quest, lines)


if __name__ == '__main__':
    main()
