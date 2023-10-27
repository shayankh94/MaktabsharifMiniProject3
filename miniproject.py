from pathlib import Path
import re


class Front:
    def sortUrl(self):
        images_folder = Path("front/images")
        files = sorted(images_folder.glob("*"))
        self.file_name = [file.name for file in files]

    def showIIcon(self):
        pattern = r"(.+)-icon(-1)?\.[a-z]+"
        match_url = list(filter(lambda x: re.match(pattern, x), self.file_name))
        with open("url_file.txt", "a+") as file:
            [file.write(i + "\n") for i in match_url]
        print("Ok")


def main():
    front = Front()
    front.sortUrl()
    front.showIIcon()


if __name__ == '__main__':
    main()
