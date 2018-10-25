class MyStack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def getItems(self):
        for k in self.items:
            print k

class bh:
    def __init__(self):

        self.__current = ""
        self.__back = MyStack()
        self.__forward = MyStack()

    def open(self, url):
        if self.__current != "":
            self.__back.push(self.__current)
            self.__forward = MyStack()

        self.__current = url

    def back(self):
        if self.__back.isEmpty():
            print "History doesn't exist"
        else:
            print "Moving back <--"
            self.__forward.push(self.__current)
            self.__current = self.__back.pop()


    def forward(self):
        if self.__forward.isEmpty():
            print "History doesn't exist"
        else:
            self.__back.push(self.__current)
            print "Moving forward -->"
            self.__current = self.__forward.pop()

    def getCurrent(self):
        print self.__current





def main():
    history = bh()
    history.open("www.a.com")
    history.open("www.b.com")
    history.open("www.c.com")
    history.getCurrent()
    history.back()
    history.getCurrent()
    history.forward()
    history.getCurrent()

main()