import os
import json
import subprocess
import sys

def cllm_repeat(data, args):
    results = []
    cllm_command = ['cllm']
    
    for item in data:
        try:
            result = subprocess.run(cllm_command + args, input=item, text=True, capture_output=True, env=os.environ)
            # Try to parse the output as JSON
            # If it fails, just return the output as is
            try:
                parsed = json.output(result.stdout)
                results.append(parsed)
            except json.JSONDecodeError:
                results.append(result.stdout)
        except FileNotFoundError:
            results.append(f"Error: {result.stderr}")
    return results

def main():
    args = args = sys.argv[1:]
    
    input_data = sys.stdin.read()
    data = json.loads(input_data)
    
    res = cllm_repeat(data, args)
    print(json.dumps(res))

if __name__ == "__main__":
    main()
