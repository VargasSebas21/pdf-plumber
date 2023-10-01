import csv
import pdfplumber


def extract_titles_and_images(pdf_path, output_csv):
    with pdfplumber.open(pdf_path) as pdf:
        rows = []
        for i, page in enumerate(pdf.pages):
            titles = []
            images = []
            for obj in page.extract_objects():
                if obj["object_type"] == "char" and obj["fontname"].endswith("Bold"):
                    titles.append(obj["text"].strip())
                elif obj["object_type"] == "image":
                    images.append(obj)
            
            titles_str = ", ".join(titles)
            images_count = len(images)
            
            row = {
                "Page": i + 1,
                "Titles": titles_str,
                "Images": images_count
            }
            rows.append(row)
        
        fieldnames = ["Page", "Titles", "Images"]
        
        with open(output_csv, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)


pdf_path = "\Desktop\python\1624copia.pdf"
output_csv = "\Desktop\python\1624.csv"

extract_titles_and_images(pdf_path, output_csv)

                                                   
