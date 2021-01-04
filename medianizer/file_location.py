from pathlib import Path


class FileLocation:
    """Represent a media file locations"""
    def __init__(self, path):
        self.path = path

    def verify_path(self, path):
        """Verify existence of provided path"""
        if Path(path).exists():
            return True
        return False

    def locate_jpg_files(self, path):
        """Look for the jpg files in a path and return them as a list"""
        return list(Path(path).glob('**/*.[jJ][pP]*[gG]'))

    def media_sort(self, media_file, dir=None, manual_sort=False):
        """Place the media file in specified path"""
        if dir:
            dir_path = Path(dir)
        elif manual_sort:
            dir_path = Path(self.path, 'medianizer_manual_sort')
        else:
            raise ('One of the params must be specified - dir or manual')
        dir_path.mkdir(exist_ok=True, parents=True)
        media_file.replace(dir_path/media_file.name)
