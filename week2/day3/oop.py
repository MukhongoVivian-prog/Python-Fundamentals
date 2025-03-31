"""
we are orgnisers of an event, we want to collect the attendance of the event
wit 4 tracks
dsign, tailoring, tech ad agriculture
"""
"""
Name |Address | phone number|email address|track
John Doe |123 Main St | 555-123-4567 | johndoe@example.com | design
Jane Smith |456 Elm St | 555-987-6543 | janesmith@example.com | tailoring
"""

class Attendance():
    def __init__(self, name, address, phone_number, age, track):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.age = age
        self.track = track

    def displayinfo(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Phone number: {self.phone_number}")
        print(f"Age: {self.age}")
        print(f"Track: {self.track}")

    def Adult(self):
        if self.age >= 20:
         print("Adult")
        else:
            print("Young")
    
     
attendance1 = Attendance("Dabel","Lugbe","08976655535",12,"tech")

attendance1.displayinfo()
# checking whether the attendee is an adult
 