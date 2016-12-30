# Lower case of the text
def _lcase(text):
    text = text.lower()
    print(text)

# Upper case of the text
def _ucase(text):
    text = text.upper()
    print(text)     

# Make each letter alternate in case with first letter capitalized
def _alt(text):
    ref = ""
    for i in range(len(text)):
        if (i % 2) == 0:
           ref += text[i].upper()
        else:
           ref += text[i].lower()
    text = ref
    print(text)

# Convert the string to leet-speak
def _1377(text):
    text = text.replace('l', '1')
    text = text.replace('L', '1')
    text = text.replace('E', '3')
    text = text.replace('e', '3')
    text = text.replace('T', '7')
    text = text.replace('t', '7')
    text = text.replace('O', '0')
    text = text.replace('o', '0')
    text = text.replace('S', '$')
    text = text.replace('s', '$')
    print(text)

# Reverse order of the characters in the string
def _rev(text):
    text = text[::-1]
    print(text)

# Undo all changes and restore the string as the user entered it
def _restore(text):
    text = textOrigin
    print(text)

# Remove white space 
def _remspace(text):
    text.replace(" ","")
    print(text)


print ("Welcome to the text converter. Your options are to:")
print ("(lcase) make each letter lowercase")
print ("(ucase) make each letter uppercase")
print ("(alt) make each letter alternate in case, with first letter capitalized")
print ("(remspace) remove all white space")
print ("(1337) convert to l337-speak")
print ("(rev) reverse the string")
print ("(new) enter a new string")
print ("(restore) replace string with last one entered")
print ("(quit) exit the program")
print ("------------------------------")


text = raw_input ("Please enter a string: ")        #Prompt user to input text message
textOrigin = text

while 1:

      action = raw_input ("Action (lcase, ucase, alt, remspace, 1337, rev, new, restore, quit): ")

      if action == "lcase":
         _lcase(text)

      elif action == "ucase":
         _ucase(text)

      elif action == "alt":
         _alt(text)

      elif action == "remspace":
         _remspace(text)

      elif action == "1377":
         _1377(text)

      elif action == "rev":
         _rev(text)

      elif action == "new":
         text = raw_input ("Please enter a string: ")

      elif action == "restore":
         _restore(text)

      elif action == "quit":
         print ("See you next time!")
         exit()

      else:
         print ("Invalid Command!")
