def write_string_to_file(string_to_file, file_path):
    with open(file_path, 'a') as f:
        f.write(string_to_file + "\n")
