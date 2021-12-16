class payment:                                                                                  
    
    def _init_(self,Email_ID,Phone_number,Name,Account_number):                                                                 
        self.email_id=Email_ID
        self.mobile_phone=Phone_number
        self.name=Name
        self.Account=Account_number
        
    def open_gpay(self):
        
        print("Welcome to pay")
        def _init_(self,Email_ID,Phone_number,Name,Account_number):                                                                 
        self.email_id=Email_ID
        self.mobile_phone=Phone_number
        self.name=Name
        self.Account=Account_number
        
    def open_gpay(self):
        
        print("Welcome to pay")
        
        
    def email(self):
         email_id=input("Enter the email-id:")
         print("The email-id is:"+email_id)
         if type(email_id) == str:
            if len(email_id)<= 25:                                                                              
                print("email_id is verified")
            else:
                raise ValueError("email id should not be beyond 25 letters")
         else:
            raise TypeError("Invalid email-id")
    def mobilenumber(self):
        mobile=input("Enter the phone number:")
        print("The Phone number is:"+mobile)
                  
        if (len(mobile)==10) :
            if (type(mobile) == int):                                                                            
                print("phone-number verified")
        else:
            raise TypeError("The phone-number should contain only integers ")
                
    def name_verify(self):
        username=input("Enter the username:")
        print("username is:"+username)
        if type(username)==str:
            if len(username)<= 20:                                                                                #LEN FUNCTION
                print("name verified")
            else:
                raise ValueError("The name should contain only lesser than or equal to 20 letters")
        else:
            raise TypeError("The name should contain letters only")

    def otp_verify(self,code,otp):
        if(otp==code):
            print("Otp is verified")
        else:
            raise ValueError("The OTP you are entered is not correct")

    def Bank_authentication(self):
        Account=input("Enter the account number:")
        print("Account number is:"+Account)
        if type(Account)==str:
            if(len(Account)==10):
                 print("Bank account is Verified")
            else:
                raise TypeError("The number should be =10")
        else:
            raise TypeError("This is an invalid bank account number")
           
           
       

    def Pin_generate(self,number):
        self.pin=number
        if (len(self.pin)==4):
            print("pin is successfully created")
        else:
            raise ValueError("Invalid pinnumber")

    def Pin_update(self,match,Pin):
        self.match=match
        self.pinno=Pin
        if self.match==self.pinno:
            print("pin is matched")
            print("Transaction done successful")
        else:
            raise ValueError("pin is not matched")
            print("Transaction is failed")
[1:24 AM, 12/17/2021] Preethika.......✨: data = {"customer": {"1000": {"ID": "1000", "name": "John Smith ", "DOB": "01/01/2000",
                            "Gender": "F", "Age": "20","Zip code": "08122-2324", "Amount ": "1500.20"},
                   "2000": {"ID": "2000", "name": "Jim McDonald ", "DOB": "02/02/2020",
                            "Gender": "M", "Age": "25","Zip code": "08136-2324","Amount ": "1500.20"},
                   "20": {"ID": "20", "name": "Jim McDonald", "DOB": "02/02/1999",
                          "Gender": "M", "Age": "25","Zip code": "08124-6565","Amount ": "1500.20"}}}
        
for i in data.values():
    for j in i.values():
        for k,l in j.items():
            if(k=="name"):
                temp=l
            if(k=="Age" and int(l)<25):
                print(temp,k,l)