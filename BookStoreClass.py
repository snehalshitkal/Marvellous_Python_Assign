class BookStore:
    NoofBooks = 0
    def __init__(self, nm,aut):
        self.Name = nm
        self.Author = aut
        #BookStore.NoofBooks = 1

    def Display(self):
        print("Inside display method:")
        print("Name:"+self.Name)
        print("Author:"+self.Author)
       # NoofBooks = NoofBooks+1
        print("NoofBook:",BookStore.NoofBooks)


def main():
    obj1 = BookStore("Linux system Programming","Robert Love")
    obj1.Display()

    obj2 = BookStore("C Programming","Dennis Ritchie")
    obj2.Display()


if __name__=="__main__":
    main()