# def write_file(file_name, file_content):
#     # with open('big_file.txt', encoding='utf-8') as text_file:
#     #     for line in text_file:
#     #         # Process the individual line
#     #         print(line)
#     with open(f"{file_name}".txt, "w") as file:
#         file.write(file_content)
#         print(file_name)
#         print(file)


# write_file("test_file", "This is a test content.")

# write_file(file_name="file_name".txt, file_content="This is a test content.")


# def append_file(file_name, append_content):
#     pass


# def read_file(file_name):
#     print(file_name.read())
#     pass


# read_file("file_name.txt")
# file_io.py


def write_file(file_path, content):
    """Write content to a file"""
    with open(f"{file_path}.txt", "w") as file:
        file.write(content)


def append_file(file_path, content):
    """Append content to an existing file"""
    with open(f"{file_path}.txt", "a") as file:
        file.write(content)


def read_file(file_path):
    """Read content from a file"""
    with open(f"{file_path}.txt", "r") as file:
        content = file.read()
    return content
