from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def main():
    working_directory = "calculator"
    # root_contents = get_files_info(working_directory)
    # print(root_contents)
    # pkg_contents = get_files_info(working_directory, "pkg")
    # print(pkg_contents)
    # pkg_contents = get_files_info(working_directory, "/bin")
    # print(pkg_contents)
    # pkg_contents = get_files_info(working_directory, "../")
    # print(pkg_contents)

    print(get_file_content(working_directory, "lorem.txt"))
    print(get_file_content(working_directory, "main.py"))
    print(get_file_content(working_directory, "pkg/calculator.py"))
    print(get_file_content(working_directory, "pkg/nonon.py"))
    print(get_file_content(working_directory, "/bin/cat"))


main()