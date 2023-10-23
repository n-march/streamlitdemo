import streamlit as st
import PyPDF2
from io import BytesIO


def read_pdf(file):
    pdfReader = PyPDF2.PdfFileReader(file)
    pages_info = {}
    for i in range(pdfReader.numPages):
        page = pdfReader.getPage(i)
        text = page.extractText().lower()
        pages_info[i] = text
    return pages_info


def main():
    st.title("PDF Text Search with Langchain")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        pdf_bytes = BytesIO(uploaded_file.read())
        extracted_pages = read_pdf(pdf_bytes)

        search_term = st.text_input("Enter the word you're looking for:")

        if st.button('Search'):
            search_term_lower = search_term.lower()
            found_pages = []

            for page_num, text in extracted_pages.items():
                if search_term_lower in text:
                    found_pages.append(page_num + 1)  # Page numbers usually start from 1

            if found_pages:
                st.success(f"The word '{search_term}' was found on pages {found_pages} in the uploaded PDF.")
            else:
                st.warning(f"The word '{search_term}' was not found in the uploaded PDF.")


if __name__ == "__main__":
    main()
