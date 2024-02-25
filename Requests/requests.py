from Login.Registration import registerUser, loginUser

def regRequest(request):
        if request == "register":
            return registerUser()
        elif request == "login":
            return loginUser()
        elif request == "quit":
            return "quit"
        else:
            print("Invalid request. Please try again.\n")
            return False
def logoutRequest(request):
    if "yes" in request:
        print("Logout succesful.\n")
        return False
    elif "no" in request:
        print("Ok.\n")
        return True
    else:
        print("Unknown command. Please try again.")
        return logoutRequest(input("Do you want to log out?\n"))