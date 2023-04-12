class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self, iata_codes, flight_details):
        self.IATA_codes = iata_codes
        self.flight_details = flight_details
        self.user_list = {}
        self.user_emails = []


    def get_users(self):

        import requests

        request = requests.get(url="https://api.sheety.co/353d19f8a7f5fadb98f15932efe6c05b/flightdeals/users")
        print(request.status_code)
        user_list = request.json()["users"]

        for user in user_list:
            self.user_list[f"{user['first']}_{user['last']}"] = user['email']

        print (self.user_list)

        for name, email in self.user_list.items():
            self.user_emails.append(email)

    def send_infos(self):

        import smtplib




        for destination in self.IATA_codes:


                # ----------- Accessing Individual Flight Details ---------- #
            print(destination)
            flight_data = self.flight_details[destination]

            formatted_departure_time = flight_data["route"][0]
            formatted_departure_time = formatted_departure_time["local_departure"]
            formatted_departure_time = formatted_departure_time.split("T")
            departure_date = formatted_departure_time[0]
            departure_time = formatted_departure_time[1][:8]

            formatted_return_time = flight_data["route"][1]
            formatted_return_time = formatted_return_time["local_departure"]
            formatted_return_time = formatted_return_time.split("T")
            return_date = formatted_return_time[0]
            return_time = formatted_return_time[1][:8]

            print(departure_time)
            print(departure_date)
            print(return_time)
            print(return_date)

            #----------- Formatting Flight Data for Text -----------#

            formatted_flight_data = f"""
                
            Departure City: {flight_data["cityFrom"]}\n
            Arrival City: {flight_data["cityTo"]}({flight_data["flyTo"]})\n
            Departure: {departure_date} / {departure_time}\n
            Return: {return_date} / {return_time}\n
            Nights at Destination: {flight_data["nightsInDest"]}\n
            Price: {flight_data["price"]}€\n
                
            """

            #------------ Sending Trip Information via Text --------- #

                # from twilio.rest import Client
                #
                # API_KEY_TWILIO = "29ab14e21da397b163590918e0d4da11"
                # SID_TWILIO = "AC85b4dccb465482509b8b7dc2d653e166"
                #
                # client = Client(SID_TWILIO, API_KEY_TWILIO)
                #
                # message = client.messages.create(
                #     to="+4915123916438",
                #     from_="+19127158761",
                #     body= f"{formatted_flight_data}"
                # )
                # print(message.status)

                # ----------- Sending Trip Information Via Email --------------- #
            for email in self.user_emails:

                    MY_EMAIL = "konstantin.kotschenreuther1@gmail.com"

                    with smtplib.SMTP("smtp.gmail.com") as connection:
                        connection.starttls()
                        connection.login(user=MY_EMAIL, password="Kotschi.123")
                        connection.sendmail(from_addr=MY_EMAIL, to_addrs=email,
                                            msg=f"Subject:Your Daily Flight Deals Have Just Landed!\n\n"
                                                f"{formatted_flight_data}")
                        connection.close()



nm = NotificationManager(iata_codes=[], flight_details=[])
nm.get_users()