def main():
    try:
        # Creating a new text file named "my_file.txt" in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file
            file.write("Hello, this is line 1.\n")
            file.write("12345\n")
            file.write("This is line 3.\n")

        # File Reading and Display
        with open("my_file.txt", "r") as file:
            # Read the contents of "my_file.txt"
            file_contents = file.read()
            print("Contents of my_file.txt:")
            print(file_contents)

        # File Appending
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text to the existing content
            file.write("This is line 4.\n")
            file.write("67890\n")
            file.write("Appending line 6.\n")

    except FileNotFoundError:
        print("File not found or unable to create the file.")
    except PermissionError:
        print("Permission denied to open or write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("End of program.")


if __name__ == "__main__":
    main()
