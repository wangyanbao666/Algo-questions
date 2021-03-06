#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.order=[]

    def Push(self, a):
        self.__stack.append(a)
        if len(self.order)==0:
            self.order.append(a)
        elif a>=self.order[-1]:
            self.order.append(a)


    def Pop(self):
        assert(len(self.__stack))
        a=self.__stack.pop()
        if a==self.order[-1]:
            self.order.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.order[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
