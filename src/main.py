"""
use os package to iterate through files in a directory
"""
import os
import time


def main():
    """
    main function
    """
    for dirname, dirnames, filenames in os.walk('.'):
        if 'index.html' in filenames:
            print("index.html already exists")
        else:
            print("index.html does not exist")
            with open(os.path.join(dirname, 'index.html'), 'w', encoding="utf-8") as f:
                f.write("\n".join([
                    get_template_head(dirname),
                    "<tr><td><a href=\"../\">../</a></td><td>-</td><td>-</td></tr>" if dirname != "." else "",
                ]))
                for subdirname in dirnames:
                    f.write("<tr><td><a href=\"" + subdirname + "/\">" +
                            subdirname + "/</a></td><td>-</td><td>-</td></tr>\n")
                for filename in filenames:
                    path = (dirname == '.' and filename or dirname +
                            '/' + filename)
                    f.write("<tr><td><a href=\"" + filename + "\">" + filename + "</a></td><td>" +
                            get_file_size(path) + "</td><td>" + get_file_modified_time(path) + "</td></tr>\n")

                f.write("\n".join([
                    get_template_foot(),
                ]))


def get_file_size(filepath):
    """
    get file size
    """
    size = os.path.getsize(filepath)
    if size < 1024:
        return str(size) + " B"
    elif size < 1024 * 1024:
        return str(round((size / 1024), 2)) + " KB"
    elif size < 1024 * 1024 * 1024:
        return str(round((size / 1024 / 1024), 2)) + " MB"
    else:
        return str(round((size / 1024 / 1024 / 1024), 2)) + " GB"
    return str(size)


def get_file_modified_time(filepath):
    """
    get file modified time
    """
    return time.ctime(os.path.getmtime(filepath))


def get_template_head(foldername):
    """
    get template head
    """
    with open("template/head.html", "r", encoding="utf-8") as file:
        head = file.read()
    head = head.replace("{{foldername}}", foldername)
    return head


def get_template_foot():
    """
    get template foot
    """
    with open("template/foot.html", "r", encoding="utf-8") as file:
        foot = file.read()
    return foot


if __name__ == "__main__":
    main()

# for subdirname in dirnames:
#     print("FOLDER" + os.path.join(dirname, subdirname))

# for filename in filenames:
#     print("FILE" + os.path.join(dirname, filename))
