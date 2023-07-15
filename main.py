
import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})


class Hotel:

    def __init__(self,hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = df.loc[df['id']==self.hotel_id,"name"].squeeze()

    def book(self):
        """book a hotel and change availability to no"""
        df.loc[df['id']==self.hotel_id,"available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        availablity = df.loc[df['id']==self.hotel_id,"available"].squeeze()
        if availablity == "yes":
            return True
        else:
            return False



class Ticket():

    def __init__(self,customer_name,hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object
    def reserve(self,customer_name,hotel_object):
        pass
    def generate(self):
        content = f"""
                 Thank you for your reservation.
                 your information is:
                 name : {self.customer_name}
                 hotel : {self.hotel_object.hotel_name}"""
        return content

hotel_ID = input("Enter the ID of hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = Ticket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("hotel is not free")
