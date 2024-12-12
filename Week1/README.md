# Document Search Tool

A simple Python-based tool for searching text documents stored in a directory. The program allows users to search for documents by file name or search for specific words within the documents. The word search functionality ignores short words (3 characters or fewer) and is case-insensitive.

## Features

- **Document Search**: Search and display the content of a document by its file name.
- **Word Search**: Search for a specific word across multiple documents and see which documents contain that word.
- **Case-Insensitive Search**: The word search ignores case, treating 'Word' and 'word' as the same.
- **Word Filtering**: Words of 3 characters or fewer are ignored during indexing.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/KhadimHussainDev/indexer
   cd indexer
   ```

2. **Prepare the environment**:

   Ensure you have Python 3 installed. You can check the version with:

   ```bash
   python --version
   ```

3. **Create the documents folder**:

   Create a directory named `documents` in the project root and add your `.txt` files there.

## Usage

1. **Run the application**:

   ```bash
   python main.py
   ```

2. **Choose an option**:

   - **1**: Search for a document by name.
   - **2**: Search for a word in all documents.
   - **e**: Exit the application.

3. **Document Search**:

   When choosing option `1`, enter the exact file name (including extension) to view the document's content.

4. **Word Search**:

   When choosing option `2`, enter a word to find out which documents contain that word. The search ignores case and filters out short words (length 3 or less).

## Project Structure

```
.
├── documents/       # Directory containing all text documents
├── main.py          # Main application script
└── README.md        # Project documentation
```

## Example

If your `documents` folder contains files such as `science.txt`, `history.txt`, and `sports.txt`, you can:

- **Search for 'science.txt'** to display its content.
- **Search for the word 'solar'** to see a list of documents that mention 'solar'.

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a new branch** for your feature:
   
   ```bash
   git checkout -b feature-branch
   ```
3. **Commit your changes**:

   ```bash
   git commit -m "Add a new feature"
   ```
4. **Push the changes** to your fork:

   ```bash
   git push origin feature-branch
   ```
5. **Create a pull request** to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

- **Khadim Hussain** - [GitHub Profile](https://github.com/KhadimHussainDev/)

## Acknowledgements

- Python's built-in libraries: `os`, `re`, `collections`.
- A special thanks to all contributors and users.

## Future Improvements

- Add functionality to search phrases.
- Implement a web-based interface for easier access.
- Add support for other file formats (e.g., PDF, DOCX).

## Contact

Feel free to reach out with suggestions or questions:

- **Email**: DevKhadimHussain@gmail.com
- **GitHub**: [https://github.com/KhadimHussainDev](https://github.com/KhadimHussainDev)
