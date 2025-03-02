import os
def list_files_and_dirs(path):
    all_items = os.listdir(path)
    files = [f for f in all_items if os.path.isfile(os.path.join(path, f))]
    directories = [d for d in all_items if os.path.isdir(os.path.join(path, d))]
    return {'files': files, 'directories': directories, 'all': all_items}