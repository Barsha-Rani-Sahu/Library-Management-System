class NegativeDateError(Exception):
    def __init__(self,return_date):
        self.return_date = return_date

    def __str__(self):
        return str(self.return_date)