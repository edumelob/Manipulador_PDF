from pdf_utils import PDFUtils

def main():
    print("📑 PDF TOOLKIT 📑")
    print("1 - Juntar PDFs")
    print("2 - Dividir PDF")
    print("3 - Extrair texto")
    print("4 - Sair")

    option = input("\nEscolha uma opção: ")

    if option == "1":
        pdfs = input("Digite os nomes dos PDFs separados por vírgula: ")
        pdf_list = [pdf.strip() for pdf in pdfs.split(",")]
        output = input("Nome do PDF final: ")
        PDFUtils.merge_pdfs(pdf_list, output)
        print("✅ PDFs unidos com sucesso!")

    elif option == "2":
        pdf = input("Nome do PDF para dividir: ")
        PDFUtils.split_pdf(pdf)
        print("✅ PDF dividido com sucesso!")

    elif option == "3":
        pdf = input("Nome do PDF: ")
        text = PDFUtils.extract_text(pdf)
        print("\n📄 TEXTO EXTRAÍDO:\n")
        print(text)

    elif option == "4":
        print("Encerrando...")
    else:
        print("❌ Opção inválida.")

if __name__ == "__main__":
    main()
