import money


praveen=money.payment("praveen0024","9965879085","praveen","3020102010")
praveen.open_gpay()
praveen.email()
praveen.mobilenumber()
praveen.name_verify()
praveen.otp_verify(15698,15698)
praveen.Bank_authentication()
praveen.Pin_generate("5384")
praveen.Pin_update(3465,3465)

class Phone_pe(gp.pay):                                                                                                                            
    def _init_(self,Email_ID,Phone_number,Name,Account_number):
        
        super()._init_(Email_ID,Phone_number,Name,Account_number)

    def open_phonepe(self):
        print("Phone pe")
        
karthik=Phone_pe("karthikeyen001","9965879086","karthikeyen","5060406090")
karthik.open_phonepe()
karthik.email()
karthik.mobilenumber()
karthik.name_verify()
karthik.otp_verify(780965,780965)
karthik.Bank_authentication()
karthik.Pin_generate("2387")
karthik.Pin_update(3564,3564)