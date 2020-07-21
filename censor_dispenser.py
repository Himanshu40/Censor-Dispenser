# These are the emails you will be censoring. 
# The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# Words and phrases from email_two
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

# Negative words from email_three
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

# Censor a specific word or phrase from a body of text and then return the text
def censor_email_one(email, word):
    censor_word = ""
    for i in range(len(word)):
        censor_word += "X"
    return email.replace(word, censor_word)

# Censor whole list of words from a body of text and then return the text
def censor_email_two(email, terms_list):
    email_lst    = ['']
    email_lst[0] = email
    for items in terms_list:
        if items in email_lst[0]:
            email_lst[0] = email_lst[0].replace(items, "REDACTED")
    return email_lst[0]

# Censor whole negative words from a body of text and then return the text
def censor_email_three(email, terms_list):
    email_lst    = ['']
    email_lst[0] = email
    for items in terms_list:
        if items in email_lst[0]:
            objectVar = email_lst[0].find(items)
            for items2 in terms_list:
                if items2 in email_lst[0][objectVar + 1:]:
                    email_lst[0] = email_lst[0][:objectVar + 1] + email_lst[0][objectVar + 1:].replace(items, "REDACTED")
    return censor_email_two(email_lst[0], proprietary_terms)  

# Censors not only all of the words from the negative_words and proprietary_terms lists, but also censor any words that come before AND after a term from those two lists
def censor_email_four(email):
    email_lst1 = ['']
    email_lst2 = ['']
    email_lst3 = []
    email_lst1[0] = email
    email_lst1[0] = censor_email_two(email_lst1[0], proprietary_terms)
    email_lst1[0] = censor_email_two(email_lst1[0], negative_words)
    email_lst2[0] = email_lst1[0].replace("\n", " lineBreak ")
    email_lst3    = email_lst2[0].split(" ")
    y = 0
    while y < (len(email_lst3) - 1):
        if (email_lst3[y] == "REDACTED") or (email_lst3[y] == "REDACTEDe") or (email_lst3[y] == "REDACTEDous") or (email_lst3[y] == "REDACTEDly") or (email_lst3[y] == "REDACTED\'s") or (email_lst3[y] == "REDACTED.") or (email_lst3[y] == "REDACTEDs") or (email_lst3[y] == "REDACTED!") or (email_lst3[y] == "REDACTEDe."):
            if y == 0 and (not email_lst3[1] == "lineBreak"):
                email_lst3[y + 1] = "REDACTED"
                continue
            if not y == (email_lst3.index(email_lst3[-1])):
                if not email_lst3[y + 1] == "lineBreak":
                    email_lst3[y + 1] = "REDACTED"
                if not email_lst3[y - 1] == "lineBreak":
                    email_lst3[y - 1] = "REDACTED"
            y += 2
        y += 1
    email_lst1[0] = " ".join(email_lst3)
    email_lst1[0] = email_lst1[0].replace("lineBreak", "\n")
    return email_lst1[0]

print(censor_email_four(email_four))