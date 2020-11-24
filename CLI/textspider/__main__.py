import re
import argparse
from colored import fg, bg, attr


def crawl(file_obj, word):
    match_sentences = []
    _pos = []
    line_pos = []
    found = False
    pattern = re.compile(f"{word}", re.I)
    contents = file_obj.read().splitlines(True)
    for _line in contents:
        search = pattern.search(_line)
        if search:
            new_line = _line[:search.start()] + f"%s%s{search.group()}%s" % (fg(232), bg(226), attr('reset')) + \
                       _line[search.end():]
            match_sentences.append(new_line)
            _pos.append(_line.index(search.group())+1)
            line_pos.append(contents.index(_line) + 1)
            found = True
    if found:
        return match_sentences, _pos, line_pos
    else:
        return found


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Crawl a text file for any word or line matches.")
    parser.add_argument('action', help="this command is always just 'crawl' for now, "
                                       "defines the action you want to perform "
                                       "with textspider")
    parser.add_argument('filepath', type=argparse.FileType('r', 1000), help='enter the path of the '
                                                                            'text file to be crawled')
    parser.add_argument('word', help='word or sentence to search for')
    parser.add_argument('-v', '--verbose', action='store_true', help='enable verbose results')
    args = parser.parse_args()
    if args.action == 'crawl':
        results = crawl(args.filepath, args.word)
        if results:
            sentences, positions, lines = results
            if not args.verbose:
                for i in sentences:
                    print(f"\n    {i}")
            else:
                for sentence, pos, line in zip(sentences, positions, lines):
                    print(f"\n    Word found at {pos} in line {line}.\n    {sentence}")
        else:
            print(f"\n    No matches for {args.word!r} found in {args.filepath.name}.")
    else:
        print(f"\n    Invalid action please use {'crawl'!r}.")
