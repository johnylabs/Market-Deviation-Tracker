# REQUIRES INSTALL YFINANCE!! IF RAN IN a good IDE like PyCharm it will prompt you to add the dependency after running!!
# USER IS ASKED WHAT FOOD THEY WANT TO MONITOR
import yfinance as yf
print("PLEASE SELECT YOUR COMMODITY")
print("a. COFFEE")
print("b. ORANGE_JUICE")
print("c. CORN")

choice = input()

if choice == "a":
    food = "KC=F"
elif choice == "b":
    food = "OJ=F"
elif choice == "c":
    food = "ZC=F"
else:
    print("A VALID OPTION WAS NOT SELECTED, DEFAULTING TO COFFEE")
    food = "KC=F"

data = yf.download(food, period="5d", interval="1d")

if not data.empty:
    latest = data["Close"].iloc[-1]
    print("Latest closing price:", latest)

    yesterday = data["Close"].iloc[-2]
    change = ((latest.iloc[0] - yesterday.iloc[0]) / yesterday.iloc[0]) * 100

    if change > 5:
        print("PRICE SENSITIVITY EVENT DETECTED")
    else:
        print("NO PRICE SENSITIVITY EVENT DETECTED")

else:
    print("Could not get data, try again later")