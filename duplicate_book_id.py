class DuplicateBookIdError(Exception):
    def __init__(self, book_id):
        self.book_id = book_id

    def __str__(self):
        return str(self.book_id)
