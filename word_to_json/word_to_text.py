from docx import Document

# Function to extract text from a Word document
def docx_to_text(file_path):
    document = Document(file_path)
    doc_text = []

    # Iterate through paragraphs in the document and add the text
    for para in document.paragraphs:
        doc_text.append(para.text)
    
    # Join the text into a single string with newlines
    return '\n'.join(doc_text)

# Function to save the extracted text to a .txt file
def save_text_output(file_path, output_txt_path):
    text = docx_to_text(file_path)
    with open(output_txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

# Example usage
file_path = 'Workforce.Miami Organizing Document_X.docx'  # Replace with your Word file path
output_txt_path = 'output.txt'  # Output text file path

save_text_output(file_path, output_txt_path)
print(f"Word document has been converted to text and saved to {output_txt_path}")
