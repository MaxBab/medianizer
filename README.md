# Medianizer

Medianizer is a tool to organize the media files by date structure.  
During the sort operation, media files will be placed in a date (year/month)
created directories structure.  
The media files will be renamed in a creation date format (YYYY_MM_DD-HH:MM:SS.jpg).

Medianizer works with '.jpg' and '.jpeg' files.  
The creation date of the media file fetched from the photo EXIF metadata.    
Sorted media files placed within the `medianizer_sorted` directory,
structured by the date format.  
The files that the EXIF metadata could not be read from the file,
placed with in the `medianizer_manual_sort` directory.  
The files with identical metadata, beside the first one, will be marked as
`duplicate_of_<name>` and placed under the `medianizer_manual_sort` as well.  
The output of the `medianizer`, printed to the stdout and '/tmp/medianizer.log` file.

The final structure of the `medianizer` sort may look like the following:
```
photos
├── medianizer_manual_sort
│   ├── duplicate_of_2017_04_18-03:44:30.jpg
│   ├── file1.jpg
│   ├── file2.jpg
│   ├── file3.jpg
│   └── IMG-20191112-WA0011.jpg
|
└── medianizer_sorted
    ├── 2015
    │   └── 04
    │       ├── 2015_04_21-06:42:31.jpg
    │       ├── 2015_04_21-06:42:33.jpg
    │       ├── 2015_04_21-06:43:08.jpg
    │       ├── 2015_04_22-17:06:15.jpg
    │       ├── 2015_04_22-17:06:20.jpg
    │       ├── 2015_04_23-08:54:58.jpg
    │       ├── 2015_04_23-12:09:45.jpg
    │       ├── 2015_04_23-12:10:15.jpg
    │       ├── 2015_04_23-12:10:17.jpg
    │       └── 2015_04_23-12:10:44.jpg
    └── 2017
        └── 04
            ├── 2017_04_18-02:32:14.jpg
            ├── 2017_04_18-02:32:38.jpg
            ├── 2017_04_18-02:33:47.jpg
            ├── 2017_04_18-03:44:30.jpg
            ├── 2017_04_18-03:44:33.jpg
            └── 2017_04_18-04:14:58.jpg
```

## Installation
Install the package by:
```
$ python setup.py install
```

## Usage
The medianizer accepts custom path of the directory and works on the provided path.

```
$ medianizer --path <path_to_media_files>
```

By default, medianizer fetch the EXIF metadata of the media file.  
But if needed, the "--from-name" flag will try to fetch the creation date from the
media file name.

```
$ medianizer --path <path_to_media_files> --from-name
```
