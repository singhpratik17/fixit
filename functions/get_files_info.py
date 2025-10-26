import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(os.path.join(working_directory, directory))

    print(abs_working_directory)
    print(abs_directory)

    if not abs_directory.startswith(abs_working_directory):
        return f'Error: {directory} is not in the working directory.'
    
    contents = os.listdir(abs_directory)
    content_info = ""
    for content in contents:
        content_path = os.path.join(abs_directory, content)
        is_dir = os.path.isdir(content_path)
        content_size = os.path.getsize(content_path)

        content_info += f"- {content}: file_size: {content_size} bytes, is_dir: {is_dir}\n"
    
    return content_info

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)