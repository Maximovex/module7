from pprint import pprint

class Product:
    def __init__(self,name,weight,category):
        self.name=name
        self.weight=weight
        self.category=category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    _file_name='product.txt'

    def get_products(self):
        file=open(self._file_name,'r')
        return file.read()
        file.close()

    def add(self,*products):
        file=open(self._file_name,'a')
        file_contain=self.get_products()
        for i in range(len(products)):
            if products[i].name in file_contain:
                print(f'Продукт {products[i].name} уже есть в магазине')
            else:
                file.write(f'{products[i].name} {products[i].weight} {products[i].category}\n')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

