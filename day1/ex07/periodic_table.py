def get_data(line):
    elem_dict = [line.split("=")[0].strip()]
    elem_data = []
    data = line.split("=")[1].strip()
    for elem_line in data.split(","):
        elem_data.append(elem_line[elem_line.find(":") + 1:].strip())
    elem_dict.append(elem_data)
    return elem_dict


def get_elements():
    f = open("periodic_table.txt", "r")
    elem_list = []
    for line in f.readlines():
        elem = get_data(line)
        elem_list.append(elem)
    f.close()
    return elem_list


def write_elements_to_file(elements: list, f):
    prev = 0
    line = "<table>"
    for elem in elements:
        cur = int(elem[1][0])
        if cur == 0:
            line += "<tr>"
        if cur - prev > 1:
            line += "<td colspan='" + str(cur - prev - 1) + "'></td>"
        line += "<td>\n<h4>" + elem[0] + "</h4>\n"
        line += "<ul><li>" + elem[1][1] + "</li>\n<li>" + elem[1][2] + "</li>\n<li>" + \
                elem[1][3] + "</li>\n<li>" + elem[1][4] + "</li>\n</ul></td>"
        if cur == 17:
            line += "</tr>"
            cur = 0
        prev = cur
    line += "</table>"
    f.write(line)


def write_to_html(elements: list):
    f = open("periodic_table.html", "w")
    f.write("""<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<title>Periodic table</title>
<style>
table, td {
border: 1px solid black;
border-collapse: collapse;
}
</style>
</head>
<body>
""")
    write_elements_to_file(elements, f)
    f.write("    </body>\n")
    f.write("</html>\n")
    f.close()


def generate_html():
    elements = get_elements()
    write_to_html(elements)


if __name__ == '__main__':
    generate_html()
