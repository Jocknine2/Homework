class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        # self.favourite_song = favourite_song

    def pay_entry_fee(self, room):
        self.wallet -= room.entry_fee
