from pypdf import PdfReader
from pydantic import BaseModel


class DataBaseTable(BaseModel):
    tbl_name: str
    columns: list[str]


TABLE_SEPARATOR: str = "Indexes"

file_name: str = r".\pdf_reading\modelagem_dw.pdf"
page_content: str = ""
tables_list: list[str] = []

with open(f"{file_name}", "rb") as file:
    reader = PdfReader(file, strict=False)
    page = reader.pages[0]
    page_content = page.extract_text()

# print(page_content)

# print(len(page_content))

first_table = page_content[:page_content.find(TABLE_SEPARATOR)].split('\n')
# print(first_table)


# print(first_table)
pydantic_test = DataBaseTable(
    tbl_name=first_table[0],
    columns=first_table[1:-1])

print(pydantic_test)

# page_content = page_content[page_content.find(TABLE_SEPARATOR)+len(TABLE_SEPARATOR):]


# print(len(page_content))
# print(tables_list)
