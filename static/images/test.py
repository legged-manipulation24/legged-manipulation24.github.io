from pdf2image import convert_from_path

# 指定PDF文件路径和输出目录
pdf_path = "/Users/mulinjiu/Desktop/HXL/UCSD/ICRA2024/website/hacleg.github.io/static/images/system_overview.pdf"
output_folder = "/Users/mulinjiu/Desktop/HXL/UCSD/ICRA2024/website/hacleg.github.io/static/images/"

# 转换PDF到PNG
images = convert_from_path(pdf_path)

# 保存每一页作为PNG
for i, image in enumerate(images):
    image.save(f"{output_folder}/output_page_{i + 1}.png", "PNG")
