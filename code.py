import time
import random


def play():
    req = []
    corp = random.choice(["Google", "Netflix", "Amazon", "Uber",
                          "Tesla"])
    first_text(req, corp)
    election(req, corp)


def play_again():
    new = input("Play again? Yes/No\n").lower()
    if "yes" in new:
        play()
    else:
        text("\nOK, see you!!\n")


def text(intro_text):
    print(intro_text)
    time.sleep(1)


def first_text(req, corp):
    text("\nYou are a guy who doesn't feel confortable with "
         "his actual job possition and ready to change it.\n")
    text("You heard about that " + corp + " need people to "
         "work on their projects.\n")
    text("So you decide to take a steep and create an opportunity.\n")
    text("The first is obtain the formation and knowledge.\n")


def selector_movement():
    print("Press 1 to move to formation.")
    print("Press 2 to move to offert.")
    print("Press 3 to move to the job.\n")


def election(req, corp):
    selector_movement()
    movement = int(input("Enter what yo want to do:\n"))
    if movement == 1:
        formation(req, corp)
    elif movement == 2:
        find_offer(req, corp)
    elif movement == 3:
        interview(req, corp)
    else:
        wrong_input_text()
        election(req, corp)


def wrong_input_text():
    text("\nYou have entered a wrong indication\n")
    text("Please, introduce one from the list\n")


def formation(req, corp):
    if "cert" in req:
        text("\nYour formation center it's still how's you remember it. "
             "You salute to your mentors, but you have successfully passed "
             "and it's no more to do here for now.\n")
    else:
        text("\nYou work hard and learn so much, with that all,"
             " just make look it easy adn pass the formation.\n")
        text("Your mentors congratulate you and they give you the "
             "certificate.\n")
        req.append("cert")
    election(req, corp)


def find_offer(req, corp):
    if "offer" in req:
        text("\nYou already found the offer from " + corp + " corporation.\n")
        text("And you have a meeting with a recruiter very soon.\n")
    else:
        text("\nYou start looking for a offers in the browser or "
             "thru your contacts and creating perfiles in different sites.\n")
        if "cert" in req:
            text("Your profile is checked by one recruiter from "
                 + corp + " and he likes it.\n")
            text("Then he calls you for a interview.\n")
            req.append("offer")
        else:
            text("But first you should have the necessary skills to look "
                 "for a new job.\n")
    election(req, corp)


def interview(req, corp):
    if "cert" in req:
        if "offer" in req:
            text("\nThe day of the interview happen.\n")
            text("You feel confident about the tecnical part.\n")
            text("The interview goes very well, the recruiter is "
                 "delighted with you and hires you for the job.\n")
            text("Congratulations, you reach your meta..!!\n")
            play_again()
        else:
            text("\nSorry, you failed.\n")
            text("Without any offer you can not do too much.\n")
            play_again()
    else:
        text("\nSorry, you failed.\n")
        text("You should have the certificate proving you knowledge "
             "and offer to sign up for.\n")
        play_again()


play()
