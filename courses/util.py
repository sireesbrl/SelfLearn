from django.core.files.storage import default_storage

def get_chapter(file_path):
    """
    A function that reads and decodes the content of a file located at the specified file path.
    
    Parameters:
        file_path (str): The path of the file to read.
    
    Returns:
        str: The decoded content of the file if the file is successfully read, None otherwise.
    """

    # check if the file exists
    try:
        with default_storage.open(file_path) as f:
            return f.read().decode("utf-8")
    except FileNotFoundError:
        return None





    