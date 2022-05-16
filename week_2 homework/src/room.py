class Room:
    def __init__(self, room_num, capacity, entry_fee):
        self.room_num = room_num
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.guests = []
        self.songs = []

    def get_guest_count(self):
        return len(self.guests)

    def check_in_guest(self, guest):
        self.guests.append(guest)

    def check_out_guest(self, guest):
        guest_list = []
        for gst in self.guests:
            if gst != guest:
                guest_list.append(gst)
        self.guests = guest_list

    def song_count(self):
        return len(self.songs)

    def add_song(self, song):
        self.songs.append(song)
