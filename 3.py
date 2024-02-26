delimiter = ";"

# не очень понятно, к примеру запискй Специя в категории Масло больше чем одна
# в таких ситуациях надо счетать сумму продаж Специя или минимальную запись?    
def printCategoryLeast(input_csv_file):
    """ printCategoryLeast выводит продукт с наименьшим кол-вом проданных единиц 
    в заданной категории
    Описание аргументов:
    input_csv_file - файл откуда надо брать информацию по продажам
    """
    f = open(input_csv_file, "r", encoding="utf8")
    tittle = f.readline()
    data = [[i for i in row[:-1].split(delimiter)] for row in f]
    f.close()

    categories = {}
    for row in data:
        if(row[0] in categories.keys()):
            categories[row[0]].append(row)
        else:
            categories[row[0]] = [row]

    while(True):
        inp = input()

        if(inp == "молоко"):
            break

        if(inp in categories.keys()):
            min_row = ["100000000000.0"]
            for row in categories[inp]:
                if(float(row[-1]) < float(min_row[-1])):
                    min_row = row.copy()
            print("В категории: {0} товар: {1} был куплен {2} раз".format(inp, min_row[1], min_row[-1]))
        else:
            print("Такой категории не существует в нашей БД")