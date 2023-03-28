from docxtpl import DocxTemplate
from docx2pdf import convert
import jinja2


def multiply_by(value, by):
    return value * by


doc = DocxTemplate("my_word_template.docx")
context = {'price_dollars': 100.00}
doc.render(context)
doc.save("generated_doc.docx")

convert("generated_doc.docx", "generated.pdf")

