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

# тоже не очень понятно что надо, по коду видно
def chartLeastProducts(input_csv_file):
    """ chartLeastProducts по возрастанию выводит категорию и кол-во продаж в ней
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
            categories[row[0]] += float(row[-1])
        else:
            categories[row[0]] = float(row[-1])
    
    sorted_vals = insertSort([[i] for i in categories.values()], 0)

    for i in range(10):
        for category in categories.keys():
            if(categories[category] == sorted_vals[i][0]):
                print("{0}, {1}.".format(category, categories[category]))