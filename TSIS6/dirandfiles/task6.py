import os
def generate_text_files(directory):
    for i in range(26):
        file_name = f'{chr(65 + i)}.txt'
        with open(os.path.join(directory, file_name), 'w') as f:
            f.write(f'File {file_name} created.')