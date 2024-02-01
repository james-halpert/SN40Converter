import os
import easygui
from tkinter import filedialog, Tk
from tkinter import messagebox

def modify_hex_properties(input_file, output_file):
    # Hexadecimal values to search for and replace
    original_hex = "534E3430"  # hex for "SN40"
    new_hex = "48323633"      # hex for "H263"

    try:
        with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
            # Read the file as binary and replace hex values
            file_data = infile.read()
            modified_data = file_data.replace(bytes.fromhex(original_hex), bytes.fromhex(new_hex))
            outfile.write(modified_data)

        # Display success message
        messagebox.showinfo("Success", f"Hex properties modified. Output file: {output_file}")

    except Exception as e:
        # Display error message if an exception occurs
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    Tk().withdraw()  # Hide the main window

    # Ask the user to select a file
    file_path = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video files", "*.avi")])

    if file_path:
        # Get the directory and filename separately
        directory, filename = os.path.split(file_path)

        # Set the default output file in the same directory
        output_file = os.path.join(directory, "modified_" + filename)

        # Modify hex properties
        modify_hex_properties(file_path, output_file)
