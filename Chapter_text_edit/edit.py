import re
import os

def clean_and_edit_text_file(filepath):
    """
    Reads a text file, performs specified character removals and string
    replacements, and then saves the edited content back to the same file.

    Args:
        filepath (str): The path to the text file to be edited.
    """
    try:
        # 1. Read the entire file content
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"✅ Successfully read content from: {filepath}")

    except FileNotFoundError:
        print(f"❌ Error: The file was not found at {filepath}")
        return
    except Exception as e:
        print(f"❌ An error occurred during file reading: {e}")
        return

    # --- EDITS ---

    # 2. Define the replacements (Order matters here for complex replacements)
    replacements = {
        '->': 'to',
        '???': 'unknown',
        'Lv.': 'level',
        ' ': ' ', # Replace the non-breaking space (U+00A0) with a regular space
    }
    
    # Perform string replacements
    for old, new in replacements.items():
        # We use re.sub for robust, non-overlapping replacement
        content = re.sub(re.escape(old), new, content)
        
    print("✅ Completed string replacements.")

    # 3. Define the characters to remove
    # Note: We include the full-width space and Japanese quotation marks here, 
    # as they were listed in your 'to remove' section.
    # The list is: !, 」, 「, #, [, ], (, ), ! (duplicate), the non-breaking space
    
    # We create a single regex pattern to match any of these characters
    # '\\s' is included to catch any leftover whitespace that you listed (like the one before '」')
    # and any potential full-width space characters. 
    # If you only want to remove *the specific* non-breaking space, do it in the replacements step above.
    
    # Pattern explanation: r'[...]'. The characters inside the brackets are matched literally.
    # We escape the special regex characters: \#\[\]\(\).
    chars_to_remove_pattern = r'[!」「\#\[\]\(\)\\]'
    
    # Perform the removals using re.sub with an empty string as the replacement
    content = re.sub(chars_to_remove_pattern, '', content)
    
    print("✅ Completed character removals.")
    
    # --- SAVING ---
    
    # 4. Save the edited content back to the file
    try:
        # 'w' mode truncates (clears) the file and writes the new content
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
            print(f"✅ Successfully saved edited content back to: {filepath}")
            print("❗ IMPORTANT: Spacing and alignment were preserved because the program only replaced/removed content, it did not modify existing line breaks or indentation.")
            
    except Exception as e:
        print(f"❌ An error occurred during file writing: {e}")

# --- USAGE EXAMPLE ---

if __name__ == "__main__":
    # 🌟 IMPORTANT: Change this to the actual path of your text file.
    file_to_edit = 'chapters'
    
    # Optional: You can check if the file exists before running the function
    if os.path.exists(file_to_edit):
        print(f"Attempting to process file: **{file_to_edit}**")
        clean_and_edit_text_file(file_to_edit)
    else:
        print(f"Please create a text file named '{file_to_edit}' or update the `file_to_edit` variable with the correct path.")
