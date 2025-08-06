import sys

def get_python_version():
    print("Python Version:", sys.version)
    print("Version Info:", sys.version_info)

def get_command_line_arguments():
    print("Command Line Arguments:", sys.argv)

def exit_script():
    print("Exiting script with status code 0")
    sys.exit(0)

def get_system_platform():
    print("Platform:", sys.platform)

def get_recursion_limit():
    print("Current Recursion Limit:", sys.getrecursionlimit())

def set_recursion_limit(limit):
    sys.setrecursionlimit(limit)
    print("New Recursion Limit Set To:", sys.getrecursionlimit())

def get_system_path():
    print("System Path:")
    for path in sys.path:
        print(path)

def get_standard_streams():
    print("Standard Input:", sys.stdin)
    print("Standard Output:", sys.stdout)
    print("Standard Error:", sys.stderr)

def get_byteorder():
    print("System Byte Order:", sys.byteorder)

def check_imported_modules():
    print("Imported Modules:")
    for module in sys.modules:
        print(module)

def sys_module_examples():
    print("--- Sys Module Examples ---")
    get_python_version()
    get_command_line_arguments()
    get_system_platform()
    get_recursion_limit()
    get_system_path()
    get_standard_streams()
    get_byteorder()
    check_imported_modules()
    # Uncomment to test exit function
    # exit_script()
    # Uncomment to test recursion limit change
    # set_recursion_limit(2000)

if __name__ == "__main__":
    sys_module_examples()
