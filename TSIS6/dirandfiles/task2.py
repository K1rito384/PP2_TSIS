import os
def check_access(path):
    return {
        'exists': os.path.exists(path),
        'readable': os.access(path, os.R_OK),
        'writable': os.access(path, os.W_OK),
        'executable': os.access(path, os.X_OK)
    }