class MovieTicket:
    cinema_name = "Rustaveli Cinema"
    total_tickets_sold = 0
    
    def __init__(self, movie_title, seat_number, price):
        self.movie_title = movie_title
        self.seat_number = seat_number
        self.price = price

        MovieTicket.total_tickets_sold += 1

ticket1 = MovieTicket("Avatar: The Way of Water", 12, 25.0)
ticket2 = MovieTicket("The Batman", 5, 20.0)
ticket3 = MovieTicket("Top Gun: Maverick", 18, 30.0)

print("---- Movie Ticket Information --")
print(f"Cinema: {MovieTicket.cinema_name}")
print(f"Ticket 1 - Movie: {ticket1.movie_title}, Seat: {ticket1.seat_number}, Price: ${ticket1.price}")
print(f"Ticket 2 - Movie: {ticket2.movie_title}, Seat: {ticket2.seat_number}, Price: ${ticket2.price}")
print(f"Ticket 3 - Movie: {ticket3.movie_title}, Seat: {ticket3.seat_number}, Price: ${ticket3.price}")
print(f"Total Tickets Sold: {MovieTicket.total_tickets_sold}")