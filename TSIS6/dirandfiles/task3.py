import os
def path_info(path):
    if os.path.exists(path):
        return {
            'file_name': os.path.basename(path),
            'directory': os.path.dirname(path)
        }
    else:
        return {'error': 'Path does not exist'}