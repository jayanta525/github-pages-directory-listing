"""import os.path"""
import os
import sys


def main():
    """
    main function
    """
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = os.getcwd()

    print("cleaning up " + path)
    try:
        os.chdir(path)
    except OSError:
        print("Cannot change the current working Directory")
        sys.exit()
    for dirname, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            if filename == "index.html":
                print("removing leftover index.html")
                os.remove(os.path.join(dirname, filename))

main()