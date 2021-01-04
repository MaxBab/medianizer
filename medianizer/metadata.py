import exifread
import random
import re
import string

from datetime import datetime


class Metadata:
    """Fetch media files metadata"""
    def __init__(self):
        pass

    def fetch_date(self, media_file, fetch_date_from_name=None):
        """Fetch the date from the media file

        Try to fetch the creation date from the file metadata.
        If not available, try to get it from the file name.
        """
        date = self._fetch_date_from_metadata(media_file)
        if not date and fetch_date_from_name:
            date = self._fetch_date_from_name(media_file)
        if date:
            return date
        else:
            raise KeyError('Unable to read EXIF metadata')

    def _fetch_date_from_metadata(self, media_file):
        """Fetch metadata and extract creation date from media file"""
        exif = exifread.process_file(media_file)
        if exif:
            full_date = str(exif['EXIF DateTimeOriginal'])
            date, date_time = full_date.split(" ", 1)
            date = date.replace(':', '_')
            year, month, _ = date.split('_')
            return {'date_time': date_time,
                    'date': date,
                    'month': month,
                    'year': year}
        return False

    def _fetch_date_from_name(self, media_file):
        """Fetch creation date from the file name if available"""
        # The date from file name fetch will not contain time.
        # So in order to differentiate between the images, generate random str.
        letters = string.ascii_lowercase
        random_str = ''.join(random.choice(letters) for i in range(4))

        possible_dates = []
        date = None
        numbers = re.findall(r'\b\d+\b', str(media_file))
        for num in numbers:
            if len(num) == 8:
                possible_dates.append(num)
        for pdate in possible_dates:
            try:
                date = datetime.strptime(pdate, '%Y%m%d').date()
            except ValueError:
                pass
            if date:
                date = str(date).replace('-', '_')
                year, month, _ = date.split('_')
                return {'date_time': random_str,
                        'date': date,
                        'month': month,
                        'year': year}
        return False
