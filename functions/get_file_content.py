import os
from config import MAX_CHARACTERS
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    file_content_string = ""
    try:
        with open(abs_file_path, 'r') as file:
            file_content_string = file.read(MAX_CHARACTERS)
            if len(file_content_string) >= MAX_CHARACTERS:
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARACTERS} characters]'

        return file_content_string
    except Exception as e:
        return f'Exception reading file {e}'
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists the file content for the specified file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory.",
            ),
        },
    ),
)