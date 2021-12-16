import gp

praveen=gp.pay("praveen01@gmail.com","9965879085","praveen","3020102010")
praveen.open_gpay()
praveen.email_verification()
praveen.mobile_verification()
praveen.name_verification()
praveen.otp_verification(15698,15698)
praveen.Bank_verification()
praveen.set_Pin("5384")
praveen.Enter_your_Pin(5465,5465)

class Phone_pe(gp.pay):                                                                                                                            
    def _init_(self,Email_ID,Phone_number,Name,Account_number):
        
        super()._init_(Email_ID,Phone_number,Name,Account_number)

    def open_phonepe(self):
        print("Phone pe")
        
karthikraja=Phone_pe("karthikraja023@gmail.com","7705877142","karthi","5060406090")
karthikraja.open_phonepe()
karthikraja.mobile_verification()
karthikraja.name_verification()
karthikraja.otp_verification(780965,780965)
karthikraja.Bank_verification()
karthikraja.set_Pin("2387")
karthikraja.Enter_your_Pin(3564,3564)