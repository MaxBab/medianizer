from argparse import ArgumentParser
from pathlib import Path

import medianizer.app_logger as app_logger
from medianizer.file_location import FileLocation
from medianizer.metadata import Metadata

logger = app_logger.get_logger(__name__)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--path', help='Specify the path of the media files',
                        required=True)
    parser.add_argument('--from-name', required=False, action='store_true',
                        help='Try to fetch creation date from name. By default'
                             ', creation date fetched from metadata only')
    return parser.parse_args()


class Executor:
    def __init__(self, path, date_from_name=None):
        self.path = path
        self.date_from_name = date_from_name
        self.location = FileLocation(self.path)
        self.metadata = Metadata()

    def process_image(self):
        for image in self.location.locate_jpg_files(self.path):
            try:
                with open(image, 'rb') as img:
                    date = self.metadata.fetch_date(img, self.date_from_name)
                    file_name = f'{date["date"]}-{date["date_time"]}.jpg'
                    new_image_path = Path(self.path, 'medianizer_sorted',
                                          date['year'], date['month'],
                                          file_name).resolve()
                    if image.name == file_name:
                        continue
                    logger.info(f'Rename file {image} to {file_name}')
                    if self.location.verify_path(new_image_path):
                        logger.info('The image with the same metadata '
                                    'already exists in the dest path. Moving '
                                    f'the {image} to "manual_sort" directory')
                        file_name = f'duplicate_of_{file_name}'
                        image.rename(image.parent/file_name)
                        self.location.media_sort(image.parent/file_name,
                                                 manual_sort=True)
                        continue
                    image.rename(image.parent/file_name)
                    self.location.media_sort(image.parent/file_name,
                                             dir=new_image_path.parent)
            except IOError:
                logger.error(f'Unable to open the {image} file.')
            except KeyError:
                logger.error(f'Unable to read the {image} EXIF metadata. '
                             'Moving the image to the "manual_sort" directory')
                self.location.media_sort(image, manual_sort=True)


def main():
    args = parse_args()
    executor = Executor(args.path, args.from_name)
    logger.info('Start medianizer app')
    if not executor.location.verify_path(args.path):
        raise ValueError('The given path does not exist')
    logger.info(f'The given path has been found: {args.path}')
    executor.process_image()


if __name__ == '__main__':
    main()
