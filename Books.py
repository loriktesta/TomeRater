class Books(object):
    def __init__(self, title, isbn):
        self.title = title       # string
        self.isbn = isbn         # number
        self.ratings = []   # list of ratings

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print(self.title + "'s ISBN updated to: " + str(self.isbn))
        return

    def add_rating(self, rating):
        if rating in range(0, 5):
            self.ratings.append(rating)
        else:
            print("Invalid rating")
        return

    def __eq__(self, other_book):
        if other_book.title == self.title and other_book.isbn == self.isbn:
            return True
        else:
            return False

    def __repr__(self):
        return "title: " + self.title + ", isbn:" + str(self.isbn) + ", Ratings: " + str(len(self.ratings))

    def get_average_rating(self):
        total_rating = 0
        for item in range(0, len(self.ratings)):
            total_rating += self.ratings[item]
        avg_rating = total_rating / len(self.ratings)
        return avg_rating

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Books):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author      # string

    def get_author(self):
        return self.author

    def __repr__(self):
        return self.title + " by " + self.author + ", Ratings:" + str(len(self.ratings))

class Non_Fiction(Books):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject      # string
        self.level = level         # string

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return self.title + " a " + self.level + " manual on " + self.subject + ", Ratings:" + str(len(self.ratings))
