# Simple AI Agent that checks and fixes python code

#### Model - gemini-2.5-flash

## Sample prompt and response:

```
(fixit) fixit % uv run calculator/main.py "3 + 7 * 2"                                           
{
  "expression": "3 + 7 * 2",
  "result": 20
}

(fixit) fixit % uv run main.py "The calculator is broken 3 + 7 * 2 shouldn't be 20. Fix the bug"
 - Calling function: get_files_info
 - Calling function: get_file_content
 - Calling function: get_files_info
 - Calling function: get_file_content
 - Calling function: write_file
The calculator's operator precedence was incorrect. I've updated `pkg/calculator.py` to correctly prioritize multiplication and division over addition and subtraction by changing the precedence of `+` and `-` to `1`.

(fixit) fixit % uv run calculator/main.py "3 + 7 * 2"                                           
{
  "expression": "3 + 7 * 2",
  "result": 17
}

```

`/calculator` directory contains a sample calculator app to which the agent has access to.