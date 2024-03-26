from movie_rental import  CinemaHouse
 

# Create a rental store
RentMovies = CinemaHouse.RentalStore
KIRK = CinemaHouse.Customer


# Add movies to the store
RentMovies.addToStore('The Dark Knight','18', 'Comedy','2016','GH₵10.00','Old','This is a new movie', 1,'100%')
RentMovies.addToStore('Ariel','1', 'Action','2017','GH₵20.00','New','This is a new movie', 2, '10%')
RentMovies.addToStore('Jungle Story','1', 'Animation','2015','GH₵30.00','New','This is a new movie', 3, '50%')
RentMovies.addToStore('Fight Club','1', 'Action','2014','GH₵10.00','New','This is a new movie', 4, '60%')
RentMovies.addToStore('The Shawshank Redemption','1', 'Horror','2015','GH₵20.00','Old','This is a new movie', 5, '70%')
RentMovies.addToStore('The Shawshank Redemption','1', 'Drama','2015','GH₵20.00','New','This is an old movie', 6, '80%')
RentMovies.addToStore('The Dark Knight','1', 'Fantasy','2017','GH₵40.00','New','This is a new movie', 7, '90%')
RentMovies.addToStore('The Shawshank Redemption','1', 'Romance','2016','GH₵40.00','New','This is an old movie', 8, '10%')
RentMovies.addToStore('The Dark Knight','1', 'Fantasy','2018','GH₵20.00','New','This is a new movie', 9, '5%')
RentMovies.addToStore('The Matrix','1', 'Romance','2019','GH₵35.00','New','This is an old movie', 10, '4%')

# Add customers to the store
RentMovies.addCustomer('Alice', 'Mandy','16', 'Female', '8458092682',0)
RentMovies.addCustomer( 'Uma', 'Wendy','24', 'Female', '7061293115',1)       
RentMovies.addCustomer( 'Isabel', 'Vicky','23', 'Female', '2310456043',2)    
RentMovies.addCustomer( 'Alice', 'Yvonne','14', 'Female', '7394355151',3)    
RentMovies.addCustomer( 'Xavier', 'Bernard','15', 'Male', '7488790731',4)    
RentMovies.addCustomer( 'Ivan', 'Yvonne','20', 'Female', '3342957117',5)     
RentMovies.addCustomer( 'Uma', 'Terry','19', 'Female', '3342957117',6)       
RentMovies.addCustomer( 'Emma', 'Carter','15', 'Female', '3342957117',7)     
RentMovies.addCustomer( 'Jenny', 'Uma','19', 'Female', '8458092682',8)       
RentMovies.addCustomer( 'Xavier', 'Carter','25', 'Male', '2310456043',9) 

def InitialDisplay():
    print("Hello , Welcome to CinemaHouseX2")
    type = chooseWhoYouAre()
    if type == 1:
        CustomerDisplay()
        
    elif type == 2:
        adminDisplay()

    else:
        exit()


def CustomerDisplay():
    print("Hello Customer, Welcome to CinemaHouseX2")
    print("Please select an option from the menu below")
    print("1. Display all movies")
    print("2. Rent a movie")
    print("3. Return a movie")
    userInput = int(input("What is your choice: "))
    if userInput == 1:
            DisplayMovies()
    elif userInput == 2:
            RentMovie()
    elif userInput== 3:
            ReturnMovie()
    

def adminDisplay():
    print("Hello Admin, Welcome to CinemaHouseX2")
    print("Please select an option from the menu below")
    print("1. Display all movies")
    print("2. Display all customers")
    userInput = int(input("What is your choice: "))
    if userInput == 1:
            DisplayMovies()
    elif userInput == 2:
            DisplayCustomers()

def chooseWhoYouAre():
    print("Who are you? ")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    userInput = int(input("What is your choice: "))
    return userInput

def DisplayMovies():
    RentMovies.getMovieDetails()

def DisplayCustomers():
    RentMovies.getCustomers()


def RentMovie():
    print("Please select a movie from the list below")
    DisplayMovies()
    movieChoice = input("What is your choice: ")
    print("Please select a customer from the list below")
    DisplayCustomers()
    customerChoice = input("What is your choice: ")
    print("Please enter the price of the movie")
    price = input("What is your choice: ")
    print("Please enter the duration of the rental")
    duration = input("What is your choice: ")
    RentMovies.rentMovie(movieChoice,customerChoice,price,duration)
    print("Movie Rented")

def ReturnMovie():
    print("Please select a movie from the list below")
    DisplayMovies()
    movieChoice = input("What is your choice: ")
    if movieChoice not in RentMovies.Movies:
        raise ValueError("Movie not found")
    print("Please select a customer from the list below")
    DisplayCustomers()
    customerChoice = input("What is your choice: ")
    if customerChoice not in RentMovies.Customers:
        raise ValueError("Customer not found")
    
    RentMovies.returnMovie(movieChoice,customerChoice)
    print("Movie Returned")

def exit():
    print("Goodbye")
    exit()

def main():
    InitialDisplay()


if __name__ == "__main__":
    main()

