from pathlib import Path
import re

class Front:
    def sortUrl(self):
        images_folder = Path("images")
        files = sorted(images_folder.glob("*"))
        self.file_name = [file.name for file in files]
        for name in self.file_name:
            print(name)

    def showIIcon(self):
        pattern = r"(.+)-icon(-1)?\.[a-z]+"
        match_urls = list(filter(lambda x: re.match(pattern, x), self.file_name))
        with open("icons.txt", "a+") as file:
            for url in match_urls:
                print("hi")
                file.write(f'images/{url}' + "\n")
        print("Ok")


def main():
    front = Front()
    front.sortUrl()
    front.showIIcon()


if __name__ == '__main__':
    main()
