class Washer:
    def __init__(self, brand, prod_name, size):
        self.__brand = brand
        self.__prod_name = prod_name
        self.__size = size

    def washing(self):
        print("{} {} 세탁기가 {}킬로그램의 빨래를 합니다.".format(self.__brand, self.__prod_name, self.__size))
