# importing modules
import os
import sys

def search_extension(path, ext):
    """Searches for extensions in the path"""
    output = []
    for root, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if file.endswith(ext):
                path = os.path.join(root, file)
                output.append(path)

    return output


def search_file(path, f):
    """Searches for files in the path"""
    output = []
    for root, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if file == f:
                path = os.path.join(root, file)
                output.append(path)

    return output


def main():
    # arguments passed in the command line
    args = sys.argv[1:]
    # if there's only one argument passed, the directory is goint to be the cwd
    if len(args) == 1:
        # the directory where we are executing the command
        dir = os.getcwd()
        # to know if the argument is an extension or a file
        if args[0].startswith('.'):
            ext = arg
            output = search_extension(dir, ext)

        else:
            file = args[0]
            output = search_file(dir, file)

        if len(output) == 0:
            print("Couldn't find that file.")

        else:
            print(f'Found {len(output)} matches.\n')
            [print(x) for x in output]

    # is there's two arguments passed, the first one is the directory to search, and the other one is the file/ext
    elif len(args) == 2:
        dir = args[0]
        arg = args[1]
        # checking if the directory exists
        if os.path.exists(dir):
            # checking if it's an extension or file
            if arg.startswith('.'):
                output = search_extension(dir, arg)

            else:
                output = search_file(dir, arg)

            if len(output) == 0:
                print("Couldn't find that file.")

            else:
                print(f'Found {len(output)} matches.\n')
                [print(x) for x in output]

        else:
            print("Directory does not exist.")

    else:
        print('The syntax of the command is incorrect.')



if __name__ == '__main__':
    main()
