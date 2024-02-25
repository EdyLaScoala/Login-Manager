from Requests.requests import regRequest, logoutRequest

logged = False

if __name__ == '__main__':
    while True:
        if logged == "quit":
            break
        elif not logged:
            logged = regRequest(input("Login or Register?\n"))
        else:
            logged = logoutRequest(input("Do you want to log out?\n"))
