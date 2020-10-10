# importing modules
import os


# import sys


def search_extension(path, ext):
    """Searches for extensions in the path"""
    output = {}
    for root, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if file.endswith(ext):
                output.setdefault(root, []).append(file)
    print("\n{:-^50}\n".format("Search results"))
    for key, value in output.items():
        print("Path\n{}\n\nFiles\n{}".format(key, "\n".join(value)))
    if not output:
        print('\nNo match found.')


def search_file(path, f):
    """Searches for files in the path"""
    output = False
    for root, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if file == f:
                path = os.path.join(root, file)
                file_size_b = os.path.getsize(path)
                file_size_kb = file_size_b / 1024
                file_size_mb = file_size_b / 1024 / 1024
                print("\n{:-^50}\nFile\t\tSize".expandtabs(28).format("Search results"))
                if file_size_mb >= 0.10:
                    print("{}\t{:.2f} MB".format(file, file_size_mb).expandtabs(28))
                elif file_size_mb < 0.10:
                    print("{}\t{:.2f} KB".format(file, file_size_kb).expandtabs(28))
                elif file_size_kb < 0.10:
                    print("{}\t{:.2f} B".format(file, file_size_b).expandtabs(28))
            else:
                output = False
    if not output:
        print("No matches found.")


def main():
    while True:
        current_dir = os.getcwd()
        # this is the command prompt
        user_input = input(f'\n{current_dir} $ ').lower()
        # analyzing the input to get command and args
        analyze = user_input.split()
        # first input is command
        command = analyze[0]
        # args
        args = " ".join(analyze[1:])
        # defining the set of commands we have
        commands = {
            'searchext': "search_extension({!r}, {!r})".format(current_dir, args),
            'searchfile': "search_file({!r}, {!r})".format(current_dir, args),
            'cd': "os.chdir({!r})".format(args),
            'ls': r"print('\n'+'\n'.join(os.listdir()))".format(args)

                    }

        if command in commands.keys():
            eval(commands[command])
        else:
            print('\ncommand not found\n')


if __name__ == '__main__':
    main()
