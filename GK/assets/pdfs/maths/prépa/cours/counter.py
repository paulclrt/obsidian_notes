from pathlib import Path
from pypdf import PdfReader

# Folder containing the PDFs

folder = Path("./")
total_pages = 0

for pdf_file in sorted(folder.glob("*.pdf")):
    try:
        reader = PdfReader(pdf_file)
        num_pages = len(reader.pages)
        total_pages += num_pages
        print(f"{pdf_file.name}: {num_pages} pages")
    except Exception as e:
        print(f"Error reading {pdf_file.name}: {e}")

print("-" * 40)
print(f"Total pages: {total_pages}")
