
#S-here I'm using a dictionary and key : value pairs to map the stock name to price
stocks = {
'amazon' : 3000,
'apple' : 100,
'fb' : 250,
'google' : 1400,
'msft' : 200
}

def stock_purchases():

    # Given the prices above and a client's investment budget, how much stock can they buy?
    # 1.1 TODO: Ask the client's name (use the string: "What is your name? ") and save it into a variable
    user_input1 = input("what is your name?")
    name = user_input1
    # 1.2 TODO: Ask the client how many dollars they would like to invest (use the string: "How much would you like to invest? $")
    user_input2 = int(input("How much would you like to invest? $"))
    # and save it into a variable
    dollars = user_input2
    # NOTE: When you use the `input` function to get user input, what do numbers get saved as?
    # 1.3 TODO: Uncomment the line below to ask the client which stock they're interested in.
    # NOTE: Take a look at how this input string prints out
    stock_name = input(f"\nWhich stock are you interested in? Enter the full name:\nAmazon\nApple\nFacebook\nGoogle\nMicrosoft\nStock Name: ")
    stock_price = stocks.get(stock_name.lower())  
    # Now that you have all of the client info, you can check how much they can purchase of the stock
    # they're interested in.

    # 1.4 TODO: Use `if/elif/else` conditional logic to determine how much stock the client can buy,
    # and save it in a variable
    if dollars > stock_price:
        share = int(dollars / stock_price)
    elif dollars < stock_price:
        print("You can't buy one full share.")
    # 1.5 TODO: Once you've calculated the number of stocks that can be purchased,
    # Use an f-string to print the result for the client, ala:
    # Alex has $5000 to invest and can buy 50 shares of Apple at the current price of $100.
    
    print(f'{name} has ${dollars} to invest and can buy {share} shares of {stock_name} at the current price of ${stock_price}.')

#stock_purchases()