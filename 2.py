delimiter = ";"

def insertSort(data, index):
    """ insertSort сортирует список методом вставки
    Описание аргументов:
    data - список
    index - по какой части елемента идет сортировка
    """
    res = data.copy()

    for i in range(1, len(res)):
        while(i>=1 and float(res[i][index]) < float(res[i-1][index])):
            res[i][index], res[i-1][index] = res[i-1][index], res[i][index] 
            i -= 1

    return res

def printCategoryChart(input_csv_file):
    """ printCategoryChart находит самый дорогой товар внутри категории
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
    
    for category in categories.keys():
        new_rows = insertSort(categories[category], 3)[::-1]
        print("В категории: {0} самый дорогой товар: {1} его цена за единицу товара составляет {2}".format(category, new_rows[0][1], new_rows[0][-2]))
