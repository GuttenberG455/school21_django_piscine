import sys
import os
import re
import settings


def create_html(path):
    regex = re.compile(".*\.template")
    if not regex.match(path):
        return print("wrong extension, (required: .template)")
    if not os.path.isfile(path):
        return print("does not exit file... : {}".format(path))
    f = open(path, "r")
    template = "".join(f.readlines())
    f.close()
    file = template.format(
        name=settings.name, surname=settings.surname, title=settings.title, age=settings.age,
        profession=settings.profession, phone=settings.phone, email=settings.email, skype=settings.skype)
    regex = re.compile("(\.template)")
    path = "".join([path[0:regex.search(path).start()], ".html"])
    f = open("myCV.html", "w")
    f.write(file)
    f.close()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        create_html(sys.argv[1])
