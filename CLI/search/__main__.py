import argparse
import os.path

current_dir = os.curdir


def search(path, *, filename=None, extension=None):
    sizes = []
    r_files = []
    for root, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if not extension:
                if filename == file:
                    r_files.append(file) if root == path else r_files.append(os.path.join(root, file))
                    size = os.path.getsize(os.path.join(root, file))
                    sizes.append(f"{size / 1000 / 1000:.2f} MB") if size / 1000 / 1000 >= 0.10 else sizes.append(
                        f"{size / 1000:.2f} KB")
            elif extension and not filename:
                if file.endswith(extension):
                    r_files.append(file) if root == path else r_files.append(os.path.join(root, file))
                    size = os.path.getsize(os.path.join(root, file))
                    sizes.append(f"{size / 1000 / 1000:.2f} MB") if size / 1000 / 1000 >= 0.10 else sizes.append(
                        f"{size / 1000:.2f} KB")

    return r_files, sizes


if __name__ == '__main__':
    # implementing python's recommended library for cli args
    parser = argparse.ArgumentParser(description="Search for files and extensions where ever you want.")  # created a
    # parser
    parser.add_argument('-p', '--path', help="specify the path in which you want to do the search\nDefault is the "
                                             "current dir",
                        default=current_dir)  # added the first command which is path
    parser.add_argument('-f', '--filename', help="name of target file")  # arg for file name
    parser.add_argument('-e', '--extension', help='specify target file extension')  # arg for file extension
    parser.add_argument('-v', '--verbose', help='enable verbose results', action='store_true')  # for verbose output
    # asking the parser to parse our args as attributes
    args = parser.parse_args()
    # passing the args to the search function
    search_result = search(args.path, filename=args.filename, extension=args.extension)
    # if the verbose flag is set...
    if args.verbose:
        if search_result[0]:
            width = (len(max(search_result[0], key=lambda x: len(x))) + 20)
            print(f"{'File':{width - 8}} Size")
            print("=" * width)
            all_files, all_sizes = search_result
            for f, s in zip(all_files, all_sizes):
                print(f"{f:{width - 8}} {s}")
        else:
            print("No results found.")
    else:
        print("")
        for _files in search_result[0]:
            print(_files)

    # boom... haha python is so cool man!
