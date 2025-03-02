import os
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        return f'File {path} deleted successfully.'
    else:
        return f'Cannot delete file {path}. Check if it exists and you have write permissions.'