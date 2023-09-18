print("Captain Rainbow's Color Checklist")

checklist = list()


def create(item):
    checklist.append(item)

"""
def read(index):
    item = checklist[index]
    return item
"""

""" 
def update(index, item):
    checklist[index] = item
"""

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

# Available items will show up with an checkmark "√".
# Unavailble items will appear with an "X".

def mark_completed(index):
    checkmark = "√"
    unavailable_mark = "X"
    if index == "purple socks":
        print(checkmark + " " + index)
    elif index == "red cloak":
        print(checkmark + " " + index)
    elif index == "yellow shoes":
        print(checkmark + " " + index)
    else:
        print(unavailable_mark + " " + "Item unavailable")

# Select functionality will allow you to create "C" items on the fly.
# You can also search item by index "R".
# "P" will you to list all items.

def select(function_code):
    #Create item
    if function_code == "C".lower():
        input_item = user_input("Input item: ")
        create(input_item)
    

    elif function_code == "R".lower():
        item_index = user_input("Index number? ")
       # I completed the task of catching errors
       # TO DO:
       # Get the value of the index with the item instead of just printing it.
       # What I tried:
       # passing looping through checklist
       # I was able to display all the objects in an array form
       # However, I only want one item based on the index i type in. 

        try:

            print(item_index)
        except: 
            print("An error occured")
            read(item_index)
            
           

    elif function_code == "P".lower():
        list_all_items()
    
    elif function_code == "Q".lower():
        return False
     
    else:
        print("Unknown Option")
    return True
    
def user_input(prompt):
    user_input = input(prompt)
    return user_input

def read(index):
    item = checklist[index]
    return item

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)



def test():
    create("purple sox")
    create("yellow shoes")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    print(read(0))
    print(read(1))

    list_all_items()

    mark_completed("purple socks")
    mark_completed("red cloak")
    mark_completed("yellow shoes")
    mark_completed("black boats")

    select("c")

    list_all_items()

    # select("r")

    # list_all_items()
    user_value = user_input("Please Enter a value: ")
    print(user_value)

test()

running = True

while running:
    selection = user_input(
        "pres C to add to list, R to Read from list, P to display list, and Q to quit: ")
    running = select(selection)