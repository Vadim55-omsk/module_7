
from pprint import pprint

name = '2Products.txt'
file = open(name, 'r') # r - read, w - write, a - append
pprint(file.read())
file.close()

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__ (self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    # def __init__(self):
    __file_name = '2Products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products


    def add(self, *products):
        _products = self.get_products()
        for product in products:
            if str(product) not in _products:
                file = open(self.__file_name, 'a')
                file.write(f"{product}\n")
                file.close()
        # for product in products:
        #     if product.name not in self.get_products():
        #         file = open(self.__file_name, 'a')
        #         # file.writelines(f'{product }\n' )
        #         file.write(f"{product}\n")
        #         # file = str(product() +'\n')
        #         file.close()

            #     self.file = open(self.__file_name, 'r')
            # if product.name not in self.file.read():
            #     self.file = open(self.__file_name, 'a')
                  # добавлен \n для разделения
                                                          # строки в файле 2Products

            else:
                print(f'Продукт {product.name},{product.weight}, {product.category} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__


s1.add(p1, p2, p3)

print(s1.get_products())
