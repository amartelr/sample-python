class User:
    def __init__(self, name, email):
        self._name = name
        self._email = email

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def do_something(self):
        print("Hi from " + str(self))
        ##raise ValueError()
        ## pass
        ##

    def __str__(self):
        return self._name + ", " + self._email


users = [User("Testuser", "test@gmail.com"), User("User2", "user2@gmail.com")]

for user in users:
    user.do_something()
