from python import Choose
from sport import Play
from capital import Cities
from politics import Department
from movies import Action
from colorama import Fore
import pyodbc


def app():
    while True:
        print(Fore.BLUE + "\t\tWELLCOME TO TRIVIA QUIZ GAME: ")
        print(Fore.GREEN + "\tSelect the Category")
        print("Enter 1 For Python ")
        print("Enter 2 For Sport ")
        print("Enter 3 For Capital cities ")
        print("Enter 4 For Politics ")
        print("Enter 5 For Movies ")
        stid = int(input("Enter id: "))
        fname = input("Enter your fname: ")
        choice = input(Fore.LIGHTWHITE_EX + "In which topic  you interested : ")
        if choice == "python":
            print("Welcome to python quiz")
            program = Choose()
            program.oop()
        elif choice == "2":
            print("Welcome to  sport quiz")
            gym = Play()
            gym.games()
        elif choice == "3":
            print("Welcome to Capital cities quiz")
            city = Cities()
            city.down_town()
        elif choice == "4":
            print("Welcome to Politics quiz")
            part = Department()
            part.party()
        elif choice == "5":
            print("Welcome to Movies quiz")
            series = Action()
            series.films()

        def select():
            conn = pyodbc.connect("DRIVER={SQL Server};"
                                  "SERVER=GMAN-2121;"
                                  " DATABASE=tech;"
                                  "Trusted_connection = yes;"
                                  )
            pas = conn.cursor()
            pas.execute("insert into [tec_tbl] ([studid], [FirstName],[Choice])"
                        "values(?,?,?)", (stid, fname, choice))
            pas.execute("select * from tec_tbl")
            while True:
                row = pas.fetchone()
                if not row:
                    break
            pas.commit()
            pas.close()
            conn.close()

        con = input("Do you want continue? Y/N: ")
        if con == "N".casefold():
            break

        select()
