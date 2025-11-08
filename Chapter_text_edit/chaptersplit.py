import os

def safe_split_text(text: str, max_chars: int) -> list[str]:
    """
    Splits a large string into smaller chunks of a maximum size
    without cutting words. (The core logic remains the same)
    """
    chunks = []
    current_start = 0

    while current_start < len(text):
        # 1. Remaining text is within the limit
        if len(text) - current_start <= max_chars:
            chunks.append(text[current_start:])
            break

        # 2. Find the ideal end position
        ideal_end = current_start + max_chars

        # 3. Find the last whitespace *before* the ideal end
        split_point = -1
        # Search backward from ideal_end - 1
        for i in range(ideal_end - 1, current_start - 1, -1):
            if text[i].isspace():
                split_point = i
                break

        if split_point == -1:
            # Fallback for words longer than max_chars
            print(f"⚠️ Warning: Splitting mid-word near position {ideal_end}. Word is longer than {max_chars} chars.")
            split_point = ideal_end

        # 4. Extract the chunk (up to the split_point)
        chunk = text[current_start:split_point]
        chunks.append(chunk.strip())

        # 5. Update the start position for the next iteration
        # +1 to skip the space/newline we just split on
        current_start = split_point + 1

    return chunks

def process_file_for_tts(input_filepath: str, output_filepath: str, max_chars: int = 2000):
    """
    Reads text from an input file, splits it into safe chunks,
    and writes the chunks sequentially to an output file.
    """
    # 1. READ the entire text from the input file
    try:
        with open(input_filepath, 'r', encoding='utf-8') as f:
            full_text = f.read()
    except FileNotFoundError:
        print(f"❌ Error: Input file not found at '{input_filepath}'")
        return

    # 2. SPLIT the text
    safe_chunks = safe_split_text(full_text, max_chars)

    # 3. WRITE the chunks to the output file
    # 'w' mode overwrites the file if it exists
    with open(output_filepath, 'w', encoding='utf-8') as f:
        for i, chunk in enumerate(safe_chunks):
            # Write a header for easy manual copy-pasting
            f.write(f"--- CHUNK {i+1} (Length: {len(chunk)} / Max: {max_chars}) ---\n")
            f.write(chunk)
            f.write("\n\n") # Double newline for separation in the output file

    print(f"✅ Successfully processed and split text into {len(safe_chunks)} chunks.")
    print(f"   Output saved to: '{output_filepath}'")
    
    # You can also automatically open the output file (optional)
    # os.startfile(output_filepath) 


# --- Configuration and Execution ---

# 🛑 IMPORTANT: Replace 'input.txt' with your actual file name
INPUT_FILE = 'input.txt' 
OUTPUT_FILE = 'tts_chunks.txt'
MAX_TTS_CHARS = 2000 # The limit for your online TTS application

# Run the process
process_file_for_tts(INPUT_FILE, OUTPUT_FILE, MAX_TTS_CHARS)