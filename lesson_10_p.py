class Counter(object):
    def __init__(self, counts=0):
        self.counts = counts

    def __call__(self, *args, **kwargs):
        self.counts += 1
        self.p_print()

    def p_print(self):
        print(self.counts)


class Count2(Counter):
    def __call__(self, *args, **kwargs):
        print("__call__ Counter2:", self.counts)

    def ppr(self):
        super().p_print()

# asd = Counter       # переопределение имени класса
asd1 = Counter()        # Создал объект класса
asd2 = Count2()
counter2 = Count2(100)

aaa = super(object, asd2)
# counter2.__call__()
#
# counter2.ppr()
# counter2.p_print()
#
# counter2()
#
# asd = Counter
# asd = Counter()
# asd.p_print()
# asd
# count = Counter()

print()
