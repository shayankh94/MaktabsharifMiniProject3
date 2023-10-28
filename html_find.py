from pathlib import Path
from bs4 import BeautifulSoup

directory_path = Path('front')
html_files = directory_path.glob('*.html')

for file_path in html_files:
    with open(file_path, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    image_tags = soup.find_all('img', src=lambda src: src and 'images' in src)

    for image_tag in image_tags:
        current_src = image_tag['src']
        new_src = current_src.replace('images', 'Icons')
        image_tag['src'] = new_src

    with open(file_path, 'w') as file:
        file.write(str(soup))