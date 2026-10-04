from pathlib import Path

from pypdf import PdfReader


def is_pdf(file_path: str) -> bool:
    with open(file_path, "rb") as file:
        return file.read(5) == b"%PDF-"


def extract_text(pdf_path: str) -> str:
    if not is_pdf(pdf_path):
        raise ValueError(f"File is not a valid PDF: {pdf_path}")

    reader = PdfReader(pdf_path)

    pages = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages.append(text)

    return "\n".join(pages)