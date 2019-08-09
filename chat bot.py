from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup
from csv import writer


from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"my name is (.*)",
        ["Sophie: Hello %1, How are you today ?",]
    ],
     [
        r"You: what is your name ?",
        ["Sophie: My name is Sophie and I'm a chatbot ?",]
    ],
    [
        r"Sophie:  how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
        
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*) created ?",
        ["I was created by Annu, Anna, Swathi and Kavya","top secret ;)",]
    ],
        [
        r"(.*) are you wearing?",
        ["Aluminosilicate silicate glass and steel, nice huh?",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Chennai, Tamil Nadu',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
     [
        r"(.*) joke",
        ['A guy in a plane stood up & shouted: “HIJACK!”\nAll passengers got scared\nFrom the other end of the plane, a guy shouted back “HI JOHN”.',' Maybe math teachers are pirates in disguise. They seem suspiciously interested in finding the X.',' Why don’t scientists trust atoms?\nBecause they make up everything! ',' why Wall of China is the wonder of the world!\nIt’s the only thing made in China that lasted years.','PUPIL: Would you punish me for something I didn`t do?\nTEACHER: Of course not.\nPUPIL: Good, because I haven`t done my homework.',]
    ],
    [
        r"who (.*) (movie|film)?",
        ["I’ve heard that Blade Runner is a very realistic and intelligent depiction of intelligent assistants"]
],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
],
    [
        r"which (.*) (music|song)?",
        ["Bohemian Rhapsod"]
],
    [
        r"quit",
        [" Sophie : Bye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]


def mean():
        my_url = "https://www.urbandictionary.com/define.php?term="+name
        uClient = uReq(my_url)
        page_soup = soup(uClient.read(), "html.parser")
        uClient.close()
        meaning= page_soup.findAll("div", {"class": "meaning"})  
        print("\n Sophie :  People with the name  * ",name, " * generally have the following personsality \n \n")
        for i in range(0,1):
         print(meaning[i].text),   
        print("\n Sophie : Is my analysis corrected?") 
        input("\n You : ")
        print("\n Sophie : Ok! \n ") 
        print(" Sophie : Btw ",name, " feel free to ask me anything ")
        pairs= input("\n You : ")

def chatty():
    chat = Chat(pairs, reflections)
    chat.converse()


 

if __name__ == "__main__":
    print("\n\n\n\n Sophie :  Hi there, I'm Sophie, the chat bot.  \n\t\t\t Type  quit to leave ") #default message at the start
    name= input("\n\n Sophie :  May I know your good name ?\n\n You:  ")
    print(" Sophie : Mmmm...\n\t\t That is a great name")
    print(" Sophie : Hey",name, " would you like to know more about your name?\n\t\t\t(y or n)" )
    choice=input("\n You : ")
    if choice=='y':
      print(".... Please wait while I analysis your personality ....\n")
      mean()
    else:
        print("\n Sophie : Ok! \n ") 
        print(" Sophie : Btw ",name, " feel free to ask me anything ")
        pairs= input("\n You : ")
    chatty()
    
