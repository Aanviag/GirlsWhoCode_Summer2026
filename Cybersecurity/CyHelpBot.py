#CyHelp Starter Code
cyberSecurityBirthYear = 1970

#Greets user
print("Hello! I'm CyHelp.")
userName = input("What is your name?\n")
print(userName)
print("Nice to meet you " + userName)

#Recounts start of Cybersecurity
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - cyberSecurityBirthYear
print("Wow! That means it has been " + str(timePassed) + " years since Cybersecurity began!" )

print("The field of Cybersecurity started in the 1970s when more and more information started being stored on computer systems and networks!")

input("Please press enter to continue.")


#Describes Cybersecurity
print("Cybersecurity refers to the practices that people use to protect computer systems and networks from cyber attacks.")

print("These people can be governments/nations, individuals, companies, community organizations, and hackers.\n")


#Introduces CIA Triad
print("The CIA Triad is the model used to discuss cybersecurity. CIA stands for confidentiality, integrity, and availability.")
print("Would you like to learn more about the CIA Triad?")
givenInfo = input("Type 'yes' or 'no'\n")


#Explains pillars of CIA Triad

while givenInfo.lower() == "yes":
    
    print("\nWhat would you like to learn more about? Enter the lowercase letter of the following options: \n (a) confidentiality, (b) integrity, (c) availability, (d) none")
    
    topic = input()
    
    if topic.lower() == "a":
        print("Confidentiality makes sure data is private")
    
    elif topic.lower() == "b":
        print("Integrity makes data has not been tampered with and can be trusted.")
    
    elif topic.lower() == "c":
        print("Availability makes sure authorized people cna access the data.")
    
    elif topic.lower() == "d":
        break;
    
    else:
        print("Sorry, I didn't catch that. Choose one of the options listed.")

input("Please press enter to continue.\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")
