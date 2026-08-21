#Breach Bot Starter Code
breachYear = 2019

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of Breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since Facebook data Breach in 2019.")

#Introduces Breach
print("Would you like to learn about the Facebook Data Breach that occurred in 2019?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains Breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a)Breach Details, (b) Organization's Response, or (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
     print("In summer of 2019, personal data like phone  numbers, full names, locations, email addresses, etc.. of 533 million users from accross 106 countries on Facebook was accessed by 'malicious actors' and posted onto an hacking forum. The data was scraped from a decfective feature on the Facebook platform.")
  
  elif topic.lower() == "b":
    print("In August 2019, Facebook blocked the path to accessing the private information. Although, officials didn't individually notify users claiming the information leaked wasn't sensitive. In return Facebook had to pay $5 billion in settlement to the US Federal Commission for the privacy violence.")
  
  elif topic.lower() == "c":
   break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")


#Introduces My Take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my Take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a)Relation to CIA Triad, (b) My Reaction, (c)My Advice, or (d) None")
  topic = input()
  
  if topic.lower() == "a":
    print("The Data Breach of Facebook in summer of 2019 affected the CIA Triad in all three ways. One way is INTEGRITY where the information leaked can be used to create false identities. So, the information found from the leaked data can not be considered credible.")
  
  elif topic.lower() == "b":
    print("I disagree with the organization's response as they did not view the data breach to be that harmful. Information was leaked even if a little bit, but names and phone numbers completely invades privacy protocols. They didn't notify 533 million users, which could've helped them take preventive steps.")
  
  elif topic.lower() == "c":
      print("My advice would be to change passwords to all accounts, enable two-factor authentication, and montior for any suspected action.")

  elif topic.lower() == "d":
     break
      
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")


#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")
