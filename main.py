import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_files_info import schema_get_files_info

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    
    if len(sys.argv) < 2:
        print("Usage: python main.py '<your prompt here>'")
        sys.exit(1)
    prompt = sys.argv[1]

    verbose = False
    if len(sys.argv) == 3 and sys.argv[2]=="--verbose":
        verbose = True


    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    available_functions = types.Tool(
        function_declarations = [
            schema_get_files_info,
        ]
    )

    config = types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt
    )

    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=messages,
        config=config,
    )

    if verbose and response.usage_metadata:
        print(f"User Prompt: {prompt}")
        print(f"Prompt Tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response Tokens: {response.usage_metadata.candidates_token_count}")

    if response.function_calls:
        print(response.function_calls)
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print("Response:", response.text)

main()