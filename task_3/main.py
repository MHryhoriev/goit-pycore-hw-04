from directory_utils import validate_input_path, list_files_and_directories

def main():
    directory_path = validate_input_path()
    list_files_and_directories(directory_path)

if __name__ == '__main__':
    main()
