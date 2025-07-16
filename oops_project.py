class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.logged_in = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Chatbook! How would you like to proceed?
                           1. Press 1 to Sign Up
                           2. Press 2 to Log In
                           3. Press 3 to Write a Post
                           4. Press 4 to Message a Friend
                           5. Press any other key to Exit
                           
                           -->   """)
        
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.my_post()
        elif user_input == '4':
            self.send_msg()
        else:
            exit("Thank you for using Chatbook! Goodbye!")
            
    def signup(self):
        email = input("Enter your email: ")
        password = input("Setup your password: ")
        self.username = email.split('@')[0]
        self.password = password
        print(f"Signed up successfully!")
        print('\n')
        self.menu()
        
    def signin(self):
        if self.username == '' and self.password == '':
            print("Please sign up first!")
        else:
            uname = input("Enter your email/username: ")
            pwd = input("Enter your password: ")
            if self.username == uname and self.password == pwd:
                print("Logged in successfully!")
                self.logged_in = True
            else:
                print("Please check your credentials and try again!")
        print('\n')
        self.menu()
        
    def my_post(self):
        if self.logged_in == True:
            txt = input("Enter your message: ")
            print(f"Following content has been posted: {txt}")
        else:
            print("You need to log in first to post any content!")
        print('\n')
        self.menu()
        
    def send_msg(self):
        if self.logged_in == True:
            txt = input("Enter your message: ")
            friend = input("Enter the username of your friend: ")
            print(f"Message sent to {friend}: {txt}")
        else:
            print("You need to log in first to send a message!")
        print("\n")
        self.menu()

        

# obj = chatbook()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        