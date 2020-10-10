# importing modules
import os
import sys

def main():
    output = []
    # arguments passed in the command line
    args = sys.argv[1:]
    # the directory where we are executing the command
    dir = os.getcwd()
    # thanks to this, we ensure that there is only one argument passed
    if len(args) == 1:
        arg = args[0]
        # to know if the argument is an extension or a file
        if arg.startswith('.'):
            # is an extension
            ext = arg
            for root, dirs, files in os.walk(dir, topdown=True):
                for _file in files:
                    if _file.endswith(ext):
                        path = os.path.join(root, _file)
                        output.append(path)
        else:
            # is a file
            file = arg
            for root, dirs, files in os.walk(dir, topdown=True):
                for _file in files:
                    if _file == file:
                        path = os.path.join(root, _file)
                        output.append(path)

        if len(output) == 0:
            print("Couldn't find that file")
        else:
            [print(x) for x in output]
    else:
        print('The syntax of the command is incorrect')



if __name__ == '__main__':
    main()
