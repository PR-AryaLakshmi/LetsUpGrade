import random

def fortune_cookie():

    messages=['Today Will Be A Lucky Day','You Will Meet Someone New And Interesting','Watch Out For Obstacles In Your Path']

    message=random.choice(messages)
    print(message)

if __name__ == "__main__" :
    fortune_cookie()