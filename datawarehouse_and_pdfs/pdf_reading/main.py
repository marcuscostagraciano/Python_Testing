from pypdf import PdfReader
from pydantic import BaseModel

from typing import List


class DataBaseTable(BaseModel):
    tbl_name: str
    columns: List[str]


class DataBaseSchema(BaseModel):
    # schema_name: str
    tables: List[DataBaseTable]


TABLE_SEPARATOR: str = "Indexes"

file_name: str = r".\pdf_reading\modelagem_dw.pdf"
page_content: str = ""

with open(f"{file_name}", "rb") as file:
    reader = PdfReader(file, strict=False)
    page = reader.pages[0]
    page_content = page.extract_text()

schema = DataBaseSchema(tables=[])

while len(page_content) > 0:
    table = page_content[:page_content.find(TABLE_SEPARATOR)].splitlines()
    schema.tables.append(
        DataBaseTable(tbl_name=table[0],
                      columns=table[1:])
    )
    page_content = page_content[
        page_content.find(TABLE_SEPARATOR) + len(TABLE_SEPARATOR) + 1:]

print(schema)
