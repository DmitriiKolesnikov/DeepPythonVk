
class MyList(list):

    def __init__(self, data):
        super(MyList, self).__init__()
        self.list = []
        if data:
            self.list = list(data)

    def __str__(self):
        summa = 0
        for i in self.list:
            if not isinstance(i, int):
                pass
            else:
                summa += i
        return f'{self.list}, {summa}'

    def __add__(self, other):
        lst1_ch = []
        for i in self.list:
            lst1_ch.append(i)
        if isinstance(other, MyList):
            lst2_ch = []
            for i in other.list:
                lst2_ch.append(i)
            dif = abs(len(lst1_ch) - len(lst2_ch))
            if len(lst1_ch) > len(lst2_ch):
                for i in range(dif):
                    lst2_ch.append(0)
            else:
                for i in range(dif):
                    lst1_ch.append(0)
            sum_list = [x + y for x, y in zip(lst1_ch, lst2_ch)]
            return sum_list
        if isinstance(other, list):
            lst2_ch = []
            for i in other:
                lst2_ch.append(i)
            dif = abs(len(lst1_ch) - len(lst2_ch))
            if len(lst1_ch) > len(lst2_ch):
                for i in range(dif):
                    lst2_ch.append(0)
            else:
                for i in range(dif):
                    lst1_ch.append(0)
            sum_list = [x + y for x, y in zip(lst1_ch, lst2_ch)]
            return sum_list

    def __sub__(self, other):
        lst1_ch = []
        for i in self.list:
            lst1_ch.append(i)
        if isinstance(other, MyList):
            lst2_ch = []
            for i in other.list:
                lst2_ch.append(i)
            dif = abs(len(lst1_ch) - len(lst2_ch))
            if len(lst1_ch) > len(lst2_ch):
                for i in range(dif):
                    lst2_ch.append(0)
            else:
                for i in range(dif):
                    lst1_ch.append(0)
            sub_list = [x - y for x, y in zip(lst1_ch, lst2_ch)]
            return sub_list
        if isinstance(other, list):
            lst2_ch = []
            for i in other:
                lst2_ch.append(i)
            dif = abs(len(lst1_ch) - len(lst2_ch))
            if len(lst1_ch) > len(lst2_ch):
                for i in range(dif):
                    lst2_ch.append(0)
            else:
                for i in range(dif):
                    lst1_ch.append(0)
            sub_list = [x - y for x, y in zip(lst1_ch, lst2_ch)]
            return sub_list

    def __eq__(self, other):
        summa1 = sum(self.list)
        if isinstance(other, MyList):
            summa2 = sum(other.list)
            return summa1 == summa2
        if isinstance(other, list):
            summa2 = sum(other)
            return summa1 == summa2

    def __ne__(self, other):
        summa1 = sum(self.list)
        if isinstance(other, MyList):
            summa2 = sum(other.list)
            return summa1 != summa2
        if isinstance(other, list):
            summa2 = sum(other)
            return summa1 != summa2

    def __lt__(self, other):
        summa1 = sum(self.list)
        if isinstance(other, MyList):
            summa2 = sum(other.list)
            return summa1 < summa2
        if isinstance(other, list):
            summa2 = sum(other)
            return summa1 < summa2

    def __le__(self, other):
        summa1 = sum(self.list)
        if isinstance(other, MyList):
            summa2 = sum(other.list)
            return summa1 <= summa2
        if isinstance(other, list):
            summa2 = sum(other)
            return summa1 <= summa2

    def __gt__(self, other):
        summa1 = sum(self.list)
        if isinstance(other, MyList):
            summa2 = sum(other.list)
            return summa1 > summa2
        if isinstance(other, list):
            summa2 = sum(other)
            return summa1 > summa2

    def __ge__(self, other):
        summa1 = sum(self.list)
        if isinstance(other, MyList):
            summa2 = sum(other.list)
            return summa1 >= summa2
        if isinstance(other, list):
            summa2 = sum(other)
            return summa1 >= summa2


if __name__ == "__main__":
    list1 = MyList([1])
    list2 = MyList([2, 3, 4, 5])
    print(list1 == list2)
    print(list1 + list2)
    print(list2 - list1)