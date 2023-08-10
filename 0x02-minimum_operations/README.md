# Minimum Operations

This project contains a Python script that calculates the minimum number of operations required to obtain number 'H' characters in a text file using the Copy All and Paste operations.

## Table of Contents
- [Minimum Operations](#minimum-operations)
  - [Table of Contents](#table-of-contents)
  - [Requirements](#requirements)
  - [Getting Started](#getting-started)

## Requirements

- Allowed editors: vi, vim, emacs
- All files are interpreted/compiled on Ubuntu 14.04 LTS using Python 3 (version 3.4.3)
- All files end with a new line
- The first line of all files is `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should be documented
- Code should use the PEP 8 style (version 1.7.x)
- All files must be executable

## Getting Started

1. Clone this repository into your local storage.
```sh
$ git clone https://github.com/Ngwanatuka/0x02-minimum_operations.git
```
2. Change directories into the repository.
```sh
$ cd 0x02-minimum_operations
```
3. Run the script.
```sh
$ ./0-main.py
```

Usage

The  script '0-minoperations.py' contains the 'minOperations' function that calculates the fewest number of operations needed to result in exactly 'H' characters in the file.
To use the 'minOperations' function follow the steps below:

1. Import the 'minOperations' function into your script.
```sh
$ from 0-minoperations import minOperations
```
2. Call the 'minOperations' function with the desired number of 'H' charracters.
```sh
n = 9
min_operations = minOperations(n)
print(f"Minimum number of operations to reach {n} characters: {min_operations}")
```
3. Run your script.
```sh
$ ./main.py
```

Example

```sh
n = 4
min_operations = minOperations(n)
print(f"Minimum number of operations to reach {n} characters: {min_operations}")

n = 12
min_operations = minOperations(n)
print(f"Minimum number of operations to reach {n} characters: {min_operations}")
```

Output
```sh
Minimum number of operations to reach 4 characters: 4
Minimum number of operations to reach 12 characters: 7
```

Contributing

Contributions are welcome! if you find any issues or want to enhance something, create an issue and feel free to make any changes.

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin 0x02-minimum_operations/<location>`
5. Create the pull request.