import smtplib
import time
from bsedata.bse import BSE

b = BSE()
b = BSE(update_codes = True)

# codes of stocks to be tracked are stored in codelist 
codelist = ['500570','500400','532540', '500770', '500470', '512599', '532921','533096', '539254','500820', '532977', '532281', '500180', '507685', '500875']
profit_percent = 0.40
stoploss_percent = 0.30

# for every company we will create a stock initialized with following attributes
class stock:
    def __init__(self, code):
        st = b.getQuote(code)
        self.name = st["companyName"]
        self.code = code
        current_price = float(st["currentValue"])
        self.sell_price = current_price + profit_percent * current_price
        self.buy_price = current_price - stoploss_percent * current_price

# codes of some of the companies

# '500570': 'Tata Motors Ltd.'
# '500400': 'Tata Power Co.ltd.'
# '532540': 'Tata Consultancy Services Ltd.' 
# '500770': 'Tata Chemicals Ltd.'
# '500470': 'Tata Steel'
# '512599': 'Adani Enterprises Ltd.'
# '532921': 'Adani Ports And Special Economic Zone Ltd.'
# '533096': 'Adani Power Ltd.'
# '539254': 'Adani Transmission Ltd'              
# '500820': 'Asian Paints Ltd.'
# '532977': 'Bajaj Auto Ltd.'
# '532281': 'Hcl Technologies Ltd.'
# '500180': 'Hdfc Bank Ltd'
# '507685': 'Wipro Ltd.'    
# '500875': 'Itc Ltd.'

        
#storing the stocks to be tracked in my_stocks list
my_stocks = []
for s in codelist:
    t = stock(s)   #create a stock object for each company
    my_stocks.append(t)


#following code runs all the time 
while True:
    time.sleep(3600) #after every one hour it fetches the details of the my_stock prices and checks if target or stoploss is hit
    try:
        for st in my_stocks:
            t = b.getQuote(st.code)
            current_price = float(t["currentValue"])
            if current_price >= sell_price:
                notify("sell", st.name, current_price)
            elif current_price <= buy_price:
                notify("buy", st.name, current_price)
    
    except Exception as e: 
        print ("Error occured: Below are the details")
        print (e)

def notify(notification_type, name, code):
    if notification_type == sell:
        message = "Hi ! Congratulations. Its selling time. the price of share of "+name+" has reached the target price."
    else:
        message = "Hi! Its buying time !! the price of share of "+name+" has reached the low point you had set."
    
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("sender_email_id", "sender_email_id_password")
  
    # sending the mail
    s.sendmail("sender_email_id", "receiver_email_id", message)

    # terminating the session
    s.quit()