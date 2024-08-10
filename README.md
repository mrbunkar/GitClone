
# Light weight GitClone

This project is a Python implementation of some fundamental Git commands. The goal is to create a lightweight version of Git with core functionalities implemented in Python.

## Features

Currently, the following commands have been implemented:

- **init**: Initializes a new Git repository.
- **hash-file**: Computes the SHA-1 hash of a file.
- **cat-file**: Displays the content of a specific object.

## Installation

To clone and set up the project locally, use the following commands:

```bash
git clone <repository-url>
cd gitlib
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Usage

You can use the following commands to interact with the project:

### Initialize a new repository
```bash
./lgit init
```

### Compute the hash of a file
```bash
./lgit hash-file -t <file-type> -w <file-name>
Use -w to store the file
```

### Display the content of an object
```bash
./lgit cat-file <type> <filename>
```

## Upcoming Features

This project is still under active development. The following features are planned:

- **add**: Add file contents to the index.
- **commit**: Record changes to the repository.
- **log**: Show commit logs.
- **branch**: List, create, or delete branches.
- **checkout**: Switch branches or restore working tree files.

Stay tuned for more updates!

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.