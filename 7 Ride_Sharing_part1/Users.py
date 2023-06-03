from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, email, nid) -> None:
        self.name = name
        self.email = email
        # TODO: set user id dynamically 
        self.__id = 0
        self.__nid = nid
        self.wallet = 0
    
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    

class Rider(User):
    def __init__(self, name, email, nid) -> None:
        self.current_ride = None
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f'Rider: with name: {self.name} and email: {self.email}') 

    def request_ride(self, location, destination):
        if not self.current_ride:
            # TODO: set ride properly
            # TODO: set current ride via ride match 
            ride_request = None
            self.current_ride = None

