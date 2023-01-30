## P2P bank app written in python

# Requirements
```
User A is added to the app
User A deposits 10 dollars

User B is added to the app
User B deposits 20 dollars

User B sends 15 dollars to User A
User A checks their balance and has 25 dollars
User B checks their balance and has 5 dollars

User A transfers 25 dollars from their account
User A checks their balance and has 0 dollars

SUMMARY:
add user
user deposits money
user checks their balance
user withdraw money fron their account
user A send money to use B
```

## to run the app:
# make sure you have python 3 installed.
```
- open file (main.py) with IDLE (or terminal)

- EXAMPLE: 
- add a new user to the app: userA = Bank('john') 
- deposite money into users account: userA.deposite(5000)
- withdraw money from users account: userA.withdraw(350) 
- check users account balance: userA.check_balance()
- transfer money between users: userA.transfer(userB, 200)
```

# running test cases
- for testing, we will be using pytest framework

```
- on your console and on the project directory
- pytest
```
