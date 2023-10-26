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

search_terms = ["term1", "term2", "term3"]
file_count_dict = {term: 0 for term in search_terms}

for excel, temp_df in dfs.items():
    for term in search_terms:
        if temp_df['key'].str.contains(term, case=False).any():
            file_count_dict[term] += 1

st.write(file_count_dict)

import streamlit as st

# Assuming you already have your dfs dictionary and file_count_dict from previous steps

# Total number of unique files in the dataset
total_files = len(dfs)

for term in search_terms:
    # Display section title for the term
    st.subheader(f"Statistics for '{term}':")

    # 1. Calculate and display the metric
    percent_files = (file_count_dict[term] / total_files) * 100
    st.metric(label="# of docs containing term", value=f"{percent_files:.2f}%", delta=None)

    # 2. List the file names and content for files containing the term
    st.write(f"Files containing '{term}':")
    for excel, temp_df in dfs.items():
        if temp_df['key'].str.contains(term, case=False).any():
            st.write(f"File: {excel}")
            for content in temp_df[temp_df['key'].str.contains(term, case=False)]['content']:
                st.write(content)
