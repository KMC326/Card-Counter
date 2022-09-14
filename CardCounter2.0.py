from tkinter import *
from tkinter.ttk import *
import sv_ttk

count = 0
trueCount = float(0.00)
cardsRemaining = 0
loseCount = 0
winCount = 0
percentWon = 0
percentDecksUsed = 0
cardsUsed = 0
decks = 0

def updateDisplays():
    global percentDecksUsed, deckQty, cardsRemaining, cardsUsed
    countDisplay.configure(text=count)
    trueCountDisplay.configure(text="{:.2f}".format(trueCount))
    cardsRemainingDisplay.configure(text=str(cardsRemaining))

    try:
        percentDecksUsed = (1 -(int(cardsRemaining)/(int(decks) * 52))) * 100
        percentDeckUsedDisplay.configure(text="{:.1f}".format(percentDecksUsed) + "%")
    except:
        percentDeckUsedDisplay.configure(text=0)
    cardsUsed = (int(decks)*52) - int(cardsRemaining)
    cardsUsedDisplay.configure(text=int(cardsUsed))

def decksSetEvent():
    global decks, cardsRemaining
    decks = deckCountEntry.get()
    deckQty.configure(text=str(decks) + " Decks Entered", font=("Arial Bold", 12))
    deckCountEntry.delete(0, END)

    cardsRemaining = int(decks) * 52
    updateDisplays()

def cardTwoThruSix():
    global decks
    if (decks==0):
        deckQty.configure(text="Set Number of Decks First!!", font=("Arial Bold", 16), background="yellow")
    else:
        global count
        count = count + 1

        global trueCount
        trueCount = count / int(decks)

        global cardsRemaining
        cardsRemaining = cardsRemaining - 1
        updateDisplays()

def cardSevenThruNine():
    global decks
    if (decks==0):
        deckQty.configure(text="Set Number of Decks First!!", font=("Arial Bold", 16), background="yellow")
    else:
        global cardsRemaining
        cardsRemaining = cardsRemaining - 1
        updateDisplays()

def cardTensandAce():
    global decks
    if (decks==0):
        deckQty.configure(text="Set Number of Decks First!!", font=("Arial Bold", 16), background="yellow")
    else:
        global count
        count = count - 1
        countDisplay.configure(text=count)

        global trueCount
        trueCount = count / int(decks)

        global cardsRemaining
        cardsRemaining = cardsRemaining - 1
        updateDisplays()

def resetAll():
    global decks
    global count
    global trueCount
    global cardsRemaining
    decks = 0
    count = 0
    trueCount = 0
    cardsRemaining = 0
    deckQty.configure(text="Set Number of Decks", font=("Arial Bold", 16))
    updateDisplays()

def percentWonUpdate():
    global percentWon, loseCount, winCount
    percentWon = (int(winCount)/(int(winCount)+int(loseCount))) * 100
    percentWonLabel.configure(text="Percent Won: " + "{:.0f}".format(percentWon) + "%", justify='center', wraplength=75)

def lostRound():
    global loseCount
    loseCount = loseCount+1
    loseCountLabel.configure(text="Lose Count: "+str(loseCount))
    percentWonUpdate()

def winRound():
    global winCount
    winCount = winCount+1
    winCountLabel.configure(text="Win Count: "+str(winCount))
    percentWonUpdate()


window = Tk()
window.title("Card Counter 2.0")

deckCountFrame = Frame(window)
deckCountText = Label(deckCountFrame, text="Deck Count:", font=16)
deckCountEntry = Entry(deckCountFrame, width=10)
deckCountButton = Button(deckCountFrame, text="Set Quantity", command=decksSetEvent)
deckQty = Label(deckCountFrame, text="Set Number of Decks", foreground="red", justify="center", font=("Arial Bold",16))

cardButtonFrame = Frame(window)
buttonTwoThruSix = Button(cardButtonFrame, text="2 - 6", command=cardTwoThruSix)
buttonSevenThruNine = Button(cardButtonFrame, text="7 - 9", command=cardSevenThruNine)
buttonTensandAce = Button(cardButtonFrame, text="10s - Ace", command=cardTensandAce)

countFrame = Frame(window)
countLabel = Label(countFrame, text="Count:", font="14")
countDisplay = Label(countFrame, text=str(count), font=("Arial Bold", 14))
trueCountLabel = Label(countFrame, text="True Count:", font="14")
trueCountDisplay = Label(countFrame, text=str(trueCount), font=("Arial Bold", 14))


cardsUsedFrame = Frame(window)
cardsUsedLabel = Label(cardsUsedFrame, text="Cards Used:", font="14")
cardsUsedDisplay = Label(cardsUsedFrame, text=str(cardsUsed), font=("Arial Bold", 14))
cardsRemainingLabel = Label(cardsUsedFrame, text="Cards Remaining:", font="14")
cardsRemainingDisplay = Label(cardsUsedFrame, text=str(cardsRemaining), font=("Arial Bold", 14))
percentDeckUsedLabel = Label(cardsUsedFrame, text="Percent of Decks Used: ", font="14")
percentDeckUsedDisplay = Label(cardsUsedFrame, text=str(percentDecksUsed), font=("Arial Bold", 14))

winLossFrame = Frame(window)
roundLabel = Label(winLossFrame, text="Round Counter", font=("Bold", 20))
winButton = Button(winLossFrame, text="Won Round", command=winRound)
winCountLabel = Label(winLossFrame, text="Win Count: " + str(winCount))
loseButton = Button(winLossFrame, text="Lost Round", command=lostRound)
loseCountLabel = Label(winLossFrame, text="Lose Count: " + str(loseCount))
percentWonLabel = Label(winLossFrame, text="Percent Won: -", justify='center', wraplength=75, font=("Arial Bold", 10))

resetAllButton = Button(window, text="Reset Counter (Keeps Win/Loss)", command=resetAll)



#pack/gridding below
deckCountFrame.grid(row=0,column=0, columnspan=3, padx=10, pady=5)
deckCountText.grid(row=0, column=0)
deckCountEntry.grid(row=0, column=1, padx=8)
deckCountButton.grid(row=0, column=3)
deckQty.grid(row=1, column=0, columnspan=4)

cardButtonFrame.grid(row=4, column=0, columnspan=1, pady=10)
buttonTwoThruSix.grid(row=0, column=0)
buttonSevenThruNine.grid(row=2, column=0)
buttonTensandAce.grid(row=4, column=0)

countFrame.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
countLabel.grid(row=0, column=0)
countDisplay.grid(row=0, column=1)
trueCountLabel.grid(row=1, column=0)
trueCountDisplay.grid(row=1, column=1)

cardsUsedFrame.grid(row=5, column=0, columnspan=3)
cardsUsedLabel.grid(row=0, column=0)
cardsUsedDisplay.grid(row=0, column=1)
cardsRemainingLabel.grid(row=1, column=0)
cardsRemainingDisplay.grid(row=1, column=1)
percentDeckUsedLabel.grid(row=2, column=0)
percentDeckUsedDisplay.grid(row=2, column=1)

winLossFrame.grid(row=6, column=0, columnspan=3, pady=10)
roundLabel.grid(row=0, column=0, columnspan=4, pady=10)
winButton.grid(row=1, column=0, padx=5)
loseButton.grid(row=1, column=1, padx=5)
winCountLabel.grid(row=2, column=0)
loseCountLabel.grid(row=2, column=1)
percentWonLabel.grid(row=1, column=2, rowspan=2)


resetAllButton.grid(row=7, column=0, columnspan=3, pady=10)

sv_ttk.set_theme("dark")

window.mainloop()
