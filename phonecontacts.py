import datetime

class mobilecontact:

    def _init_ (self,uname,kname,num1,num2,email,dob):
        self.first_name=uname
        self.last_name=kname
        self.phone_number1=num1
        self.phone_number2=num2
        self.emailid=email
        self.inputDate=dob
        

    def contact(self):
        print("!!!!!!!phone_contacts details!!!!!!!")
        print("""_
              1.first_name
              2.nick_name
              3.phone_number_1
              4.phone_number_2
              5.email_id
              5.inputDate
              __""")
        
    def firstname(self):
        first_name=input("Enter the contact name:")
        print("contact is:"+first_name)
        if type(self.first_name)==str:
            if len(self.first_name)<= 20:                                                                                
                print("name verified")
        else:
            raise TypeError("The name should not contain numbers and symbols")

    def lastname(self):
        last_name=input("Enter the last name:")
        print("lastname is:"+last_name)
        if type(self.last_name)==str:
            if len(self.last_name)<= 20:                                                                                
                print("name verified")
        else:
            raise TypeError("The name should not contain numbers and symbols")
    

    def phone_number_1(self):
        phone_number1=input("Enter the phone number:")
        print("The Phone number is:"+phone_number1)
        if (len(phone_number1)==10):
            if type(phone_number1)==int:
                print("phone-number 1 verified")
        else:
            raise ValueError("The phone-number should not letters and symbols")

        

    def phone_number_2(self):

       phone_number2=input("Enter the phone number:")
       print("The Phone number is:"+phone_number2)
       if (len(phone_number2)==10):
           if type(phone_number2)==int:                                                                            
                print("phone-number 2 verified")
       else:
           raise ValueError("The phone-number should not contain letters and symbols")
    

    def email_id(self):
        emailid=input("Enter the email id:")
        print("The email id is:"+emailid)
        if type(emailid)==str:
            if len(emailid)<= 30: 
                print("email_id is verified")
        else:
            raise TypeError("Invalid email-id")

    def Date_Of_birth(self):
        self.inputDate = input("Enter the date of birth : ")
        day,month,year = inputDate.split('/')
        isValidDate = True
        try :
            datetime.datetime(int(year),int(month),int(day))
            datetime.datetime(int(day), int(month), int(year))
            datetime.datetime(int(year), int(month),int(day))
        except ValueError :
            isValidDate = False
        if(isValidDate):
            print ("The date of birth is valid ..")
        else:
            print ("The date of birth is not valid..")
            
        
    

    

    def _del_(self):
        del self.first_name
        del self.last_name
        del self.phonenumber1
        del self.phonenumber2
        del self.emailid
        del self.inputDate