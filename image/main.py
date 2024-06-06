import os
from pdf2image import convert_from_path

# 遍历当前目录中的所有PDF文件
for file in os.listdir('.'):
    if file.endswith('.pdf'):
        # 将PDF转换为一系列图片
        images = convert_from_path(file)

        # 遍历图片列表并保存
        for i, image in enumerate(images):
            # 创建PNG文件名
            png_filename = f"{os.path.splitext(file)[0]}_page_{i + 1}.png"

            # 保存为PNG
            image.save(png_filename, 'PNG')

        print(f"Converted {file} to PNG")
