# Medianizer

A command line based tool to organize the photo files into a hierarchy structure.

### Features
* Organize the photo files into the folder hierarchy structure
* Create the structure of the folders by the following format - year/month
* Support `.jpg` and `.jpeg` files
* Fetch the creation date of the photo from the file EXIF metadata (using
the ExifRead tool)
* Rename the files into the `YYYY_MM_DD-HH:MM:SS.jpg` date format during
the move into the structure
* All the sorted photos will be placed into a hierarchy folders structure
undercloud `medianizer_sorted` directory
* The photos with the identical creation metadata, beside the first one,
marked as `duplicate_of_<name>` and placed under the `medianizer_manual_sort` directory
* A "--from-name" flag gives the ability to try to fetch creation date from the name of the file
* the output of the execution, printed to the stdout and '/tmp/medianizer.log' file


#### Final structure
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


### Installation
Install the package by:
```bash
$ python -m venv medianizer_venv && source medianizer_venv/bin/activate
$ python setup.py install
```

As a requirement, the 'ExifRead' pip package will be installed.


### Usage
The medianizer accepts custom path of the directory and works on the provided path.

```bash
$ medianizer --path <path_to_media_files>
```

By default, medianizer fetch the EXIF metadata of the media file.  
But if needed, the "--from-name" flag will try to fetch the creation date from the
media file name.

```bash
$ medianizer --path <path_to_media_files> --from-name
```
