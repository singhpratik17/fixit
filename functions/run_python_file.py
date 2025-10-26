import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    absolute_working_directory = os.path.abspath(working_directory)
    absolute_file_path = os.path.abspath(os.path.join(absolute_working_directory, file_path))

    if not absolute_file_path.startswith(absolute_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(absolute_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not absolute_file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        final_args = ["python3", file_path]
        final_args.extend(args)
        output = subprocess.run(final_args, cwd=absolute_working_directory, timeout=30, capture_output=True)
        final_string = f"""
        STDOUT: {output.stdout}
        STDERR: {output.stderr}
        """
        if output.stdout == "" and output.stderr == "":
            final_string = "No output produced.\n"
        if output.returncode !=0:
            final_string = f"Process exited with code {output.returncode}"
        return final_string
    except Exception as e:
        return f'Exception running file: {e}'
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a Python file with the specified arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Arguments to pass to the Python script.",
                ),
            ),
        },
    ),
)