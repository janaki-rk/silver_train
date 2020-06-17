# DAILY CODING CHALLENGE 17
# Question asked by: GOOGLE
# Given a string representing the file system in the above format, return the length of the longest absolute path to
# a file in the abstracted file system. If there is no file in the system, return 0. For example, in the second
# example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including
# the double quotes).


# Step 1: Parsing the file system
def build_fs(input_value):
    fs = {}
    files = input_value.split('\n')

    current_path = []
    for f in files:
        indentation = 0
        while '\t' in f[:2]:
            indentation += 1
            f = f[1:]

        current_node = fs
        for subdir in current_path[:indentation]:
            current_node = current_node[subdir]

        if '.' in f:
            current_node[f] = True
        else:
            current_node[f] = {}

        current_path = current_path[:indentation]
        current_path.append(f)

    return fs


# Step 2: Computing the longest path
def longest_path(root):
    paths = []
    for key, node in root.items():
        if node == True:
            paths.append(key)
        else:
            paths.append(key + '/' + longest_path(node))
    # filter out unfinished paths
    paths = [path for path in paths if '.' in path]
    if paths:
        return max(paths, key=lambda path: len(path))
    else:
        return ''


# Step 3: Putting it together
def longest_absolute_path(s):
    return len(longest_path(build_fs(s)))


# Step 4: Calling the main function which calls these above functions and displays the result
result = longest_absolute_path(
    "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
print(result)
