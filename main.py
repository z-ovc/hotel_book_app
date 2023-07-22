
import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype = str).to_dict(orient= 'records')
df_cards_security = pd.read_csv("card-security.csv", dtype=str)




print(df_cards)

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
    
class Credit_card:
    
    def __init__(self, number):
        self.number = number

    def validate(self, expiration_date, cvc, holder):
        card_data = {"number":self.number, "expiration":expiration_date,"holder":holder, "cvc":cvc}
        if card_data in df_cards:
            return True
        else:
            return False

class SecureCreditCard(Credit_card):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security['number'] == self.number, "password"].squeeze()
        print(password,'*****************************')
        if password == given_password:
            return True
        else:
            return False

        
        



hotel_ID = input("Enter the ID of hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    card_number = input("Enter your card Number: ")
    credit_card = SecureCreditCard(number = card_number)
    if credit_card.validate(expiration_date="12/26", holder="JOHN SMITH",cvc="123"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = Ticket(name, hotel)
            print(reservation_ticket.generate())
        else:
            print("card is not authenticated...")
    else:
        print("we cant validate your card...")
else:
    print("hotel is not free")