import os
import time

def get_current_directory():
    print("Current Working Directory:", os.getcwd())

def change_directory():
    # Uncomment and set a valid path to test
    # os.chdir("/path/to/directory")
    pass

def list_files():
    print("Files in Current Directory:", os.listdir("."))

def create_remove_directories():
    os.mkdir("test_folder")
    os.makedirs("parent_folder/child_folder")
    print("Created directories: test_folder and parent_folder/child_folder")
    os.rmdir("test_folder")  # Remove empty directory
    os.removedirs("parent_folder/child_folder")  # Remove nested directories
    print("Removed test_folder and parent_folder/child_folder")

def check_file_or_directory():
    path = "example.txt"
    print(f"Does {path} exist?:", os.path.exists(path))

def rename_delete_files():
    # Uncomment after creating a file
    # os.rename("old_name.txt", "new_name.txt")
    # os.remove("new_name.txt")
    pass

def get_file_information():
    # Uncomment after creating example.txt
    # if os.path.exists("example.txt"):
    #     file_info = os.stat("example.txt")
    #     print("File Size:", file_info.st_size, "bytes")
    pass

def execute_system_commands():
    print("System Command Output:")
    os.system("ls" if os.name != "nt" else "dir")

def access_environment_variables():
    print("Home Directory:", os.environ.get("HOME"))
    print("Username:", os.environ.get("USERNAME"))

def get_process_ids():
    print("Process ID:", os.getpid())
    print("Parent Process ID:", os.getppid())

def join_split_paths():
    path = os.path.join("folder", "file.txt")
    dirname, filename = os.path.split(path)
    print("Joined Path:", path)
    print("Directory Name:", dirname)
    print("File Name:", filename)

def check_path_type():
    print("Is 'example.txt' a file?", os.path.isfile("example.txt"))
    print("Is 'folder' a directory?", os.path.isdir("folder"))

def get_absolute_path():
    print("Absolute Path of example.txt:", os.path.abspath("example.txt"))

def walk_through_directory():
    print("Walking through current directory:")
    for root, dirs, files in os.walk("."):
        print(f"Root: {root}, Directories: {dirs}, Files: {files}")


def get_recently_modified_files(days):
    current_time = time.time()
    cutoff_time = current_time - (days * 86400)  # Convert days to seconds
    print(f"\n{'='*40}\nFiles modified in the last {days} days:\n{'='*40}")
    for file in os.listdir("."):
        if os.path.isfile(file):
            file_mtime = os.path.getmtime(file)
            if file_mtime >= cutoff_time:
                modified_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(file_mtime))
                print(f"\n📄 File: {file}\n🕒 Last Modified: {modified_time}\n{'-'*40}")



def os_module_examples():
    # print("--- OS Module Examples ---")
    # get_current_directory()
    # change_directory()
    # list_files()
    # create_remove_directories()
    # check_file_or_directory()
    # rename_delete_files()
    # get_file_information()
    # execute_system_commands()
    # access_environment_variables()
    # get_process_ids()
    # join_split_paths()
    # check_path_type()
    # get_absolute_path()
    # walk_through_directory()
    get_recently_modified_files(2)  # Example: Files modified in the last 7 days

if __name__ == "__main__":
    os_module_examples()
