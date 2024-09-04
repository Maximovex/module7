
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
        with open(self._file_name,'r') as file:
            return file.read()

    def add(self,*products):
        with open(self._file_name,'a+') as file:
            file_contain=self.get_products()
            for product in products:
                if str(product) in file_contain:
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    file.write(f'{str(product)}\n')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p1) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

