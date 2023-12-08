from pypdf import PdfReader

TABLE_SEPARATOR: str = "Indexes"

file_name: str = r".\pdf_reading\modelagem_dw.pdf"
page_content: str = ""
tables_list: list[str] = []

with open(f"{file_name}", "rb") as file:
    reader = PdfReader(file, strict=False)
    page = reader.pages[0]
    page_content = page.extract_text()

# print(page_content)

print(len(page_content))

ft_table = page_content[:page_content.find(TABLE_SEPARATOR)]
# print(ft_table)

page_content = page_content[page_content.find(TABLE_SEPARATOR)+len(TABLE_SEPARATOR):]

print(len(page_content))
# print(tables_list)
