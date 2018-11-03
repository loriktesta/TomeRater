class Users(object):
    def __init__(self, name, email):
        self.name = name        # string
        self.email = email      # string
        self.books = {}         # dictionary of Book objects : rating

    def get_email(self):
        return self.email

    def change_email(self, new_email):
        self.email = new_email
        print(self.name + "'s email updated to: " + self.email)
        return

    def __repr__(self):
        return "user: " + self.name + ", email:" + self.email + ", # books read: " + str(len(self.books))

    def __eq__(self, other_user):
        if other_user.name == self.name and other_user.email == self.email:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        total_rating = 0
        count = 0
        for book in self.books:
            if self.books[book] is not None:
                total_rating += self.books[book]
                count += 1
        avg_rating = total_rating / count
        return avg_rating

