from collections import defaultdict
import os
import re

# Dictionary to store the index of words in documents.
dic = defaultdict(set)
path = './documents'  # Directory containing all documents to be indexed and searched.

def main():
    # Main function to control the menu-driven interaction with the user.
    readAllDocument()  # Reads all documents and indexes them before user interaction.
    while True:
        os.system('cls')  # Clears the console 
        print("1. Search document")
        print("2. Search word")
        print("e. Exit")
        op = input("Choose an option: ")
        if op == '1':
            searchDocument()  # Searches for and displays a document by its name.
        elif op == '2':
            searchWord()  # Searches for documents that contain a specific word.
        elif op == 'e':
            break  # Exit the program.
        else:
            print("Choose correct option")
        input("Press Enter to continue...")  # Waits for user input to continue.

def searchDocument():
    # Function to search and display the content of a document by its name.
    name = input("Enter name of document : ")
    
    files = os.listdir(path)  # Retrieves the list of all document names in the directory.
    if name in files:
        file_path = os.path.join(path, name)
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)  # Displays the content of the specified document.
    else:
        print(f"Document '{name}' not found in '{path}'.")

def searchWord():
    # Function to search for documents that contain a specific word.
    word = input("Enter word to search : ")
    word = re.sub(r'[^\w\s]', '', word)
    if word.lower() in dic:
        print(f"{word} is in these files : {dic[word.lower()]}")  # Display documents containing the word.
    else:
        print(f"{word} is not found in any file.")
    return 0

def readAllDocument():
    # Function to read and index all documents in the specified directory.
    files = os.listdir(path)  # Retrieves all document file names in the directory.
    for f_path in files:
        file_path = os.path.join(path, f_path)
        with open(file_path, 'r') as file:
            content = file.read()
            # Clean the content to remove punctuation using regular expressions.
            cleaned_content = re.sub(r'[^\w\s]', '', content)
            # Convert content to lowercase and split it into words, ignoring short words.
            words = [word.lower() for word in cleaned_content.split() if len(word) > 3]
            for word in words:
                # Indexing: Storing each word along with the document it appeared in.
                dic[word].add(f_path)

if __name__ == '__main__':
    main()  
