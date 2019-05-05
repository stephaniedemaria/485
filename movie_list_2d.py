#!/usr/bin/env python3

def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        print(movie_list)

def add(movie_list):
    title = input("Name: ")
    year = input("Year: ")

    book = {"name": title,
            "year": year}
    movie_list[title] = book
    print(title + "was added to movie list")
    
def delete(movie_list):
    title = input("Title: ")
    if title in movie_list:
        del movie_list[title]
        print(title + "was removed from movie list")
    else:
        print(title + "doesnt exist in movie list")
        
def main():
    movie_list = {
        "Monty Python and the Holy Grail":
            {"name" : "Monty Python and the Holy Grail",
             "year" : "1975"},
        "On the Waterfront":
            {"name" : "On the Waterfront",
             "year" : "1954"},
        "Cat on a Hot Tin Roof":
            {"name" : "Cat on a Hot Tin Roof",
             "year" : "1958"}
        }
  
    display_menu()
    while True:        
        command = input("Command: ")
        if command == "list":
            list(movie_list)
        elif command == "add":
            add(movie_list)
        elif command == "del":
            delete(movie_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
