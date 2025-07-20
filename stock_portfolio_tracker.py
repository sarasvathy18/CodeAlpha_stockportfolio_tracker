stock_prices={"AAPL": 228,
              "TSLA": 265,
              "GOOGL": 3065,
              "AMZN": 3700,
              "NFLX": 635,
              "META": 520}#stock name : price
portfolio={}
total=0 #intialisation of while loop (to be found)
print("STOCK PORTFOLIO TRACKER!!!")
print("Available stocks are : ",', ' .join(stock_prices.keys()))
while True:
    stock=input("Enter stock name (or type DONE to finish) :  ").upper()
    if stock == "DONE": #give as string
        break
    if stock not in stock_prices:
        print("Stock not found , try again!")
        continue
    try:
        quantity=int(input(f"Enter quantity for {stock} : "))
        price=stock_prices[stock]
        amount=price*quantity
        total += amount     #increment of while loop
        portfolio[stock]=quantity   #update portfolio-empty dictionary  in each loop with stock name and quantity as key and value pair
    except ValueError:
        print("Enter a valid number for qunatity:")
    print("\n INVESTMENT SUMMARY")
    for stock,quantity in portfolio.items():
        price=stock_prices[stock]    #again define formatting string inside summary loop to run otherwise same cost folows for all stock name
        amount=price*quantity
        print(f"{stock}:{quantity} shares x ₹{price} = ₹{amount}")
    print(f"TOTAL INVESTMENT IS : ₹{total}")
save = input("Do you need to save the portfolio (y/n) : ").lower()
if save == "y":  #give as string
    with open("portfolio.txt","w",encoding="utf-8")as file:  #file name and mode within string  and ₹ (Indian Rupee symbol) is a Unicode character which your system’s default encoding
        for stock,quantity in portfolio.items():              #UTF-8 supports ₹ and all Unicode characters. instead we can use $ without using utf
            price=stock_prices[stock]    
            amount=price*quantity
            file.write(f"{stock}:{quantity} shares x ₹{price} = ₹{amount}\n")  #this gives well arranged result -\n
        file.write(f"TOTAL INVESTMENT IS : ₹{total}\n")

    print("PORTFOLIO SAVED SUCCESSFULLY AS portfolio.txt!")    
                    
        
