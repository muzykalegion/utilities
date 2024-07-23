from docx import Document

doc = Document("test.docx")
for paragraph in doc.paragraphs:
    paragraph.text = paragraph.text.replace('". ', '" ')
    doc.save("test.docx")

