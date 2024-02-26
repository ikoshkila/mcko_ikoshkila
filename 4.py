delimiter = ";"

def makePromocodes(input_csv_file, output_csv_file):
    """ makePromocodes создает промокоды для каждого продукта
    Описание аргументов:
    input_csv_file - файл откуда надо брать информацию по продажам
    output_csv_file - файл куда надо сохрать итог
    """
    f = open(input_csv_file, "r", encoding="utf8")
    tittle = f.readline()
    data = [[i for i in row[:-1].split(delimiter)] for row in f]
    f.close()

    fout = open(output_csv_file, "w", encoding="utf8")
    fout.write(tittle[:-1] + ";promocode\n")

    for row in data:
        splited_date = row[2].split(".")
        promocode = row[1][:2] + splited_date[0] + row[1][-2:][::-1] + splited_date[1][::-1]
        row.append(promocode.upper())
        fout.write(delimiter.join(row) + "\n")

    fout.close()