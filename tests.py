from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

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

    # print(get_file_content(working_directory, "lorem.txt"))
    # print(get_file_content(working_directory, "main.py"))
    # print(get_file_content(working_directory, "pkg/calculator.py"))
    # print(get_file_content(working_directory, "pkg/nonon.py"))
    # print(get_file_content(working_directory, "/bin/cat"))

    # write_file(working_directory, "demo.txt", "Hello, World!")

    # print(get_file_content(working_directory, "demo.txt"))

    print(write_file("calculator", "demo.txt", "wait, this isn't lorem ipsum"))
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print(write_file("calculator", "/tmp", "this should not be allowed"))

main()