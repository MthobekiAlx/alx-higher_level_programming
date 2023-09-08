#!/usr/bin/python3
import py_compile
import sys

if __name__ == "__main__":
    # Load the compiled module
    try:
        compiled_module = py_compile.compile("hidden_4.py")
        module_code = open(compiled_module, 'rb').read()
    except FileNotFoundError:
        print("Error: 'hidden_4.py' not found.")
        sys.exit(1)

    # Execute the module's code to populate its namespace
    module_namespace = {}
    exec(module_code, module_namespace)

    # Filter and print the names
    sorted_names = sorted(
        (name for name in module_namespace if not name.startswith("__"))
    )

    for name in sorted_names:
        print(name)
