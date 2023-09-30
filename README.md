#Spam Bot
##Python
###Modules:
- pyautogui
- os
- time

##Spam_bot
```bash
def Spam(txt, rep, tim):
# Seconds needed to start the Spamming
    sleep(tim)
    
    # loop will keep Spamming untl the wanted Spams is done
    for _ in range(rep):
        pink.write(txt)
        # Second for the code to breath before continuing
        sleep(0.2)
        # Press "Enter" for the next spam to begin
        pink.press('Enter')
```

