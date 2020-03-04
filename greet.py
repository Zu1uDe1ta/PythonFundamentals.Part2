def name_input():
"""
WILL PROVIDE THE PROMPT TO INPUT NAME
"""
  name = input("What is your name?!")
  return(name)

def greet(name):
"""
WILL GIVE THE GREET WITH THE PREVIOUS NAME
"""
    print("Hello " + name)

greet(name_input())
