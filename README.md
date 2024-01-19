# Toolbox
#### Some very simple python classes or 'Tools'

All current `classes` are made in `python 3.12` and require no 3rd-party packages.

## UrlString
The `UrlString` class is a utility designed for handling URL-related string checks in Python. It provides methods to 
check whether a given string is safe, contains reserved URL characters, or contains unsafe URL characters.

### usage
Import the `UrlString` class and you can use it's provided methods, all methods return a `bool`:
```python
from url_string import url_string

# Check if the string is URL-safe
print(url_string.is_url_safe('some_string'))

# Check if the string contains reserved URL characters
print(url_string.is_url_reserved('some_string'))

# Check if the string contains unsafe URL characters
print(url_string.is_url_unsafe('some_string'))
```

## FileCounter
the `FileCounter` class is a python utility designed for counting files in a specified folder based on their file 
extensions. It counts files recursively and utilizes the `Path` module for clean and concise path manipulation.

### usage
Initialize the `FileCounter` object with the desired folder path as a `str`.
```python
from file_count import FileCounter

file_count = FileCounter('path/to/your/folder')

# Or, disable the automatic print. True by default
FileCounter('path/to/your/folder', False)

# access the dict
file_dict = file_count.start_count() # will print the result if automatic print is True
# or
file_count.start_count() # will print the result if automatic print is True
file_dict = file_count.file_counts

# the file_dict value now contains the returned dict
```

### example
Imagine you have a folder like this:
* pictures
  * poems
    * flower.txt
    * dog.jpg
  * dog.jpg
  * dog2.jpg
  * cat.png

When using the code it could look something like this:
```python
from file_count import FileCounter

file_count = FileCounter('./pictures', True)
file_count.start_count()
```

This will print:
```json
{
    '.jpg': 2,
    '.png': 1,
    'poems': {
        '.txt': 1,
        '.jpg': 1
    }
}
```