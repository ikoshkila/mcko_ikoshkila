delimiter = ";"

def makeTotal(input_csv_file, output_csv_file, find_category):
    """ makeTotal счетает на какую цену товара было продано
    для каждой отдельной записи и записывает ее в поле total
    а также выводит сумму total в заданной категории
    Описание аргументов:
    input_csv_file - файл откуда надо брать информацию по продажам
    output_csv_file - файл куда надо сохрать итог
    find_category - категория по которой надо посчитать сумму total
    """
    f = open(input_csv_file, "r", encoding="utf8")
    tittle = f.readline()
    data = [[i for i in row[:-1].split(delimiter)] for row in f]
    f.close()

    fout = open(output_csv_file, "w", encoding="utf8")
    fout.write(tittle[:-1] + ";total\n")

    find_category_sum = 0
    for row in data:
        total = float(row[-1]) * float(row[-2])
        row.append(str(total))
        if(row[0] == find_category):
            find_category_sum += total
        fout.write(delimiter.join(row) + "\n")

    fout.close()