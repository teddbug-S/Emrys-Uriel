# importing modules
import os
import sys


def search_extension(path, ext):
    """Searches for extensions in the given path"""
    output = []
    for root, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if file.endswith(ext):
                path = os.path.join(root, file)
                output.append(path)

    return output


def search_file(path, f):
    """Searches for files in the given path"""
    output = []
    for root, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if file == f:
                path = os.path.join(root, file)
                output.append(path)

    return output


def search_dir(path, dir):
    """Searchs for directories in the given path"""
    output = []
    for root, dirs, files in os.walk(path, topdown=True):
        for _dir in dirs:
            if _dir == dir:
                path = os.join.path(root, _dir)
                output.append(path)

    return output


def main():
    # arguments passed in the command prompt
    args = sys.argv[1:]
    # to check whether we have the path specified or not
    if len(args) == 1:
        dir = os.getcwd()
        arg = args[0]
        # checking whether the argument passed is an extension, file or dir
        if arg.startswith('.'):
            # It's an ext
            output = search_extension(dir, arg)
        elif '.' in arg:
            # It's a file
            output = search_file(dir, arg)
        else:
            # It's a dir
            output = search_dir(dir, arg)

        if len(output) == 0:
            print("Couldn't find that file.")

        else:
            print(f'Found {len(output)} matches.\n')
            [print(x) for x in output]

    elif len(args) == 2:
        dir = args[0]
        arg = args[1]
        # checking whether the argument passed in as extension, file or dir
        if os.path.exists(dir):
            if arg.startswith('.'):
                # It's an ext
                output = search_extension(dir, arg)
            elif '.' in arg:
                # It's a file
                output = search_file(dir, arg)
            else:
                # It's a dir
                output = search_dir(dir, arg)

            if len(output) == 0:
                print("Couldn't find that file.")

            else:
                print(f'Found {len(output)} matches.\n')
                [print(x) for x in output]

        else:
            print('Directory does not exist.')

    else:
        print("The syntax of the command is incorrect.")


if __name__ == '__main__':
    main()
