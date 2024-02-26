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
        


if __name__ == "__main__":
    makeTotal("products.csv", "products_new.csv", "Закуски")
    printCategoryChart("products.csv")
    printCategoryLeast("products.csv")
    makePromocodes("products.csv", "product_promo.csv")
    chartLeastProducts("products.csv")