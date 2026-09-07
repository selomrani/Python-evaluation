# 1.1
print("Block 1.1")
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.availability = "Available"
    def book_infos(self):
        print(f"'{self.title}' de {self.author} etat : {self.availability}")

book1 = Book(title="Dune",author="Frank herbert")
book2 = Book(title="Darkly dreamer dexter ",author="Jeff lindsay")
#book1.book_infos()

#1.2
print("Block 1.2")

class Adherant:
    def __init__(self,name):
        self.name = name
        self.books = []
    def emprunter_livre(self,book):
        if book.availability != "Available":
            print(f"Error book {book.title} is not available")
        else:
            book.availability = "emprunte"
            self.books.append(book)
    def render_un_livre(self,book):
        if(book.availability != "Available"):
            book.availability = "Available"
    def consulter_number_des_livres_emprente(self):
        rented_books = []
        for book in self.books:
            if book.availability == "emprunte":
                rented_books.append(book)
        return len(rented_books)




ali = Adherant("Ali")




#1.3

print("Block 1.3")
sara = Adherant("Sara")
#sara.emprunter_livre(book1)


#1.4


ali.emprunter_livre(book1)
ali.emprunter_livre(book2)
book1.book_infos()
ali.render_un_livre(book1)
ali.render_un_livre(book2)
book1.book_infos()

print(ali.consulter_number_des_livres_emprente())
