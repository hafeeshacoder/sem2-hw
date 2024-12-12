class Password:
    def valid(text):
        u_count=0
        l_count=0
        d_count=0
        s_count=0
        length=len(text)
        for i in text:
            if i.isupper():
                u_count+=1
            elif i.islower():
                l_count+=1
            elif i.isdigit():
               d_count+=1
            else:
               s_count+=1
        if u_count>=1 and l_count>=1 and d_count>=1 and s_count>1:
            print("Password is valid")
        else:
            print("Print is invalid")
user=input()
Password.valid(user)
            
