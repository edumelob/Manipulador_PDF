from PyPDF2 import PdfReader, PdfWriter

class PDFUtils:
    @staticmethod
    def merge_pdfs(pdf_list, output_name):
        """Junta vários PDFs em um único arquivo."""
        writer = PdfWriter()

        for pdf in pdf_list:
            reader = PdfReader(pdf)
            for page in reader.pages:
                writer.add_page(page)

        with open(output_name, "wb") as file:
            writer.write(file)

    @staticmethod
    def split_pdf(pdf_name):
        """Divide um PDF em arquivos separados por página."""
        reader = PdfReader(pdf_name)

        for index, page in enumerate(reader.pages):
            writer = PdfWriter()
            writer.add_page(page)

            output = f"pagina_{index + 1}.pdf"
            with open(output, "wb") as file:
                writer.write(file)

    @staticmethod
    def extract_text(pdf_name):
        """Extrai texto de um PDF."""
        reader = PdfReader(pdf_name)
        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        return text
