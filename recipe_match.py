import os
import tkinter
from pint import UnitRegistry

class Recipe(object):

    def __init__(self, filename):

        # find program files' current folder
        path1 = os.getcwd()
        # add strings to get the subfolder
        path2 = "\\recipes\\"
        path = str(path1) + str(path2)
        filename = str(path) + str(filename)
        self.filename = filename
        
        # open the file to get the attribute info from
        nom = open(filename, 'r')
        nom_words = nom.read()
        # split it up into lines
        nom_lines = nom_words.split('\n')
        # access each line by list index and split into more lists
        # (unless there is only one value)
        
        # name = 0st readline (string)
        # ingredients = 1st readline (list of strings)
        # amounts = 2nd readline (list of numbers)
        # units = 3rd readline (list of strings)
        # tasty_rating = 4th readline (number)
        # prep_time = 5th readline (string)
        # cook_time = 6th readline (string)
        # match_counter = 7th line (number)
        # main_ingredient = 8th line
        # instructions = 9th line           ###how to allow paragraph formatting
        self.name = nom_lines[0]
        ingredients = nom_lines[1]
        self.ingredients = ingredients.split('\t')
        amounts = nom_lines[2]
        self.amounts = amounts.split('\t')
        units = nom_lines[3]
        self.units = units.split('\t')
        self.tasty_rating = str(nom_lines[4])
        self.pretty_tasty_rating = self.tasty_rating + " of 10"
        self.prep_time = nom_lines[5]
        self.cook_time = nom_lines[6]
        self.match_counter = int(nom_lines[7])
        self.main_ingredient = nom_lines[8]
        instructions = nom_lines[9]
        self.instructions = instructions.replace('`', '\n\n')

        nom.close()

        # make dictionaries so that the amts and units are with their ings
        ing_amt_dict = {}
        ing_unit_dict = {}
        counter = 0        
        for ingredient in self.ingredients:
            ing_amt_dict[ingredient] = self.amounts[counter]
            ing_unit_dict[ingredient] = self.units[counter]
            counter +=1

        # use those dictionaries to make nice looking summaries of ingredient
        #  info, so it can be displayed as (ing, amt unit)
        counter = 0
        ingredient_info = []
        for ingredient in self.ingredients:
            ingredient_info.append("%s, %s %s" % (ingredient,
                                                  ing_amt_dict[ingredient],
                                                  ing_unit_dict[ingredient]))
            counter += 1

        #make the pretty summary an attribute of the object
        self.ingredient_info = ingredient_info

        #make a simple printable description of the recipe
        self.description = '%s is rated %s. It takes %s to prepare and %s to ' \
                           'cook.' % (self.name, self.pretty_tasty_rating, \
                                      self.prep_time, self.cook_time)

    
    def __str__(self):
        return str("Recipe Object: " + str(self.name))

    def display(self):    
        print(self.name)
        print(self.description)
        print("This recipe requires:")
        print(self.ingredient_info)
        print(self.instructions)
    
##    def edit(self, filename):
##        # overwrite/save
##        # print each thing in the file in order
##        ### allow user to change things, gui needed
##        filename = open(filename, "w")
##        print(self.name)
##        # put ingredients back in a tabbed list
##        edited_ingredients = []
##        for ingredient in self.ingredients:
##           edited_ingredients.append(str(ingredient) + '\t')
##        print(edited_ingredients)
##        # make the list a string so it can be written
##        edited_ingredients = "".join(edited_ingredients)
##        # and amounts
##        edited_amounts = ""
##        for amount in self.amounts:
##            edited_amounts += (str(amount) + '\t')
##        edited_amounts = "".join(edited_amounts)
##        print(edited_amounts)
##        # and units
##        edited_units = []
##        for unit in self.units:
##            edited_units.append(str(unit) + '\t')
##        edited_units = "".join(edited_units)
##        print(edited_units)
##        print(self.tasty_rating)
##        print(self.prep_time)
##        print(self.cook_time)
##        print(0)
##        print(self.main_ingredient)
##        print(self.instructions)
##        filename.write(self.name)
##        filename.write("\n")
##        filename.write(edited_ingredients)
##        filename.write("\n")
##        filename.write(edited_amounts)
##        filename.write("\n")
##        filename.write(edited_units)
##        filename.write("\n")
##        filename.write(self.tasty_rating)
##        filename.write("\n")
##        filename.write(self.prep_time)
##        filename.write("\n")
##        filename.write(self.cook_time)
##        filename.write("\n")
##        filename.write("0")
##        filename.write("\n")
##        filename.write(self.main_ingredient)
##        filename.write("\n")
##        filename.write(self.instructions)
##        filename.close()
##
##    def add(self, filename):
##        #Recipe.edit(filename)
##        cookbook = cookbook.create_cookbook
##        
##    def delete(self, filename):
##        yn = input("Are you sure you want to delete this recipe? y/n ")
##        if yn == 'y':
##            os.remove(self.filename)
##        else:
##            None

    def print(self, filename):
        os.startfile(filename, "print")
        ##adjust so it prints something pretty, not raw file
        


class Menu(object):

    def __init__(self):
        self.meal_list = []
        self.recipe_list = {}

    def __str__(self):
        print("This menu contains the following recipes:")
        recipes = ""
        for each in self.meal_list:
            recipes += (str(each) + "\n")
        return recipes

    def wipe(self):
        self.meal_list = []

    def create_cookbook(self):
        self.meal_list = []
        
        # find program files' current folder
        path1 = os.getcwd()
        # add strings to get the subfolder
        path2 = "\\recipes\\"
        folder_path = str(path1) + str(path2)
        self.folder_path = folder_path

        recipe_list = os.listdir(folder_path)
        for each in recipe_list:
            recipe = Recipe(each)
            self.meal_list.append(recipe)
            self.recipe_list[recipe.name] = recipe
        return self


    def match_recipes(self, user):

        ingredients_to_match = user.ingredients_to_match
        meal_list = user.menu.meal_list
        required_matches = user.required_matches


        similar_recipes = Menu()

        # sift ingredients from existing menu, remove staples, add to ingredients_to_match
        for each in user.menu.meal_list:
            for ing in each.ingredients:
                if ing in STAPLES:
                    None
                else:
                    if ing in ingredients_to_match:
                        None
                    else:
                        ingredients_to_match.append(ing)
        

        # check every ingredient
        for ing in ingredients_to_match:
            # against every recipe
            for each in cookbook.meal_list:
                # if they have a match
                if ing in each.ingredients:
                    # increase match counter
                    each.match_counter += 1
                    # if counter is high enough
                    if each.match_counter >= required_matches:
                        # add to list of matches
                        similar_recipes.add_recipe(each)
                        

        for recipe in similar_recipes.meal_list:
            if recipe in meal_list:
                similar_recipes.meal_list.remove(recipe)


        return similar_recipes                    





    def add_recipe(self, recipe_object): 
        if recipe_object not in self.meal_list:
            self.meal_list.append(recipe_object)
        else:
            print("This recipe is already on your menu.")

##    def sort_alpha(self):
##        return self.meal_list.sort()
##
##    def sort_matches(self):
##        sorted_contents = []
##        for recipe_object in self.meal_list:
##            # we need both the match number and the name of the recipe
##                # tuple time!
##            sorted_contents.append((recipe_object.match_counter, recipe_object))
##        return sorted_contents.sort()
##
##    def sort_main_ing(self):
##        sorted_contents = []
##        for recipe_object in self.meal_list:
##            sorted_contents.append((recipe_object.main_ingredient,
##                                    recipe_object))
##        return sorted_contents.sort()

    def load_menu(self, filename):
        None #meal_list = saved meal_list

    def save_menu(self, filename):
        filename = None

    def print(self):
        None #print the list



class Make_Shopping_List(object):

    def __init__(self, user):

        meal_list = user.menu.meal_list


        # recipe.ingredient_info contains ing_amt_unt sep by spaces
        # recipe.ingredients, recipe.amounts, and recipe.units have these alone
        # let's create a dictionary of {ingredient: amount to buy}        
        # a dictionary to hold the final values for the shopping list
        supplies_needed = {}

        # ing:amt and ing:unit lists
        ing = []
        amt = []
        unit = []

        # right now we're going to add every ing from every recipe to these lists
        for recipe_object in meal_list:
            counter = 0            
            for ingredient in recipe_object.ingredients:
                ing.append(ingredient)                  #list of ings
                amt.append(recipe_object.amounts[counter])   #list of amts
                unit.append(recipe_object.units[counter])    #list of units
                counter += 1


        # now we have long lists that, together, have all the info we need
        # let's make a dictionary with ing:(amt,unit)
        ingred_dict = {}
        counter = 0
        for ingredient in ing:
            # whether ingredient is there or not, we can append to the list of
            # values contained in a key with multiple values
            ingred_dict.setdefault(ingredient, []).append(str(amt[counter]) + str(" ") +
                                                           str(unit[counter]))
            counter += 1
            #ingred_dict is now a dictionary of amt/unit that can be called with keys from list ing


##        print("debug: ingred_dict")
##        for ingred_name in ingred_dict:
##            amt_unit_list = ingred_dict[ingred_name]
##            string_list = ", ".join(amt_unit_list)
##            print(ingred_name, string_list)



        for ingred_name in ingred_dict:
            amt_unit_list = ingred_dict[ingred_name]
            sums_dict = {}                            ## key is a unit type, value is the sum of ingred needed in that unit
            for pair in amt_unit_list: 
                pair_list = pair.split(" ")
                this_amt = eval(pair_list[0])
                this_unit = pair_list[1]
                if this_unit in sums_dict:
                    sums_dict[this_unit] += this_amt
                else:
                    sums_dict[this_unit] = this_amt
                         
            amounts = ""
            for each in sums_dict:
                amounts += str(sums_dict[each])
                amounts += " "
                amounts += str(each)
                supplies_needed[ingred_name] = amounts






        print("debug: supplies_needed")
        for each in supplies_needed:
            print(each, supplies_needed[each])
        if supplies_needed == {}:
            print("supplies_needed is empty")

        user.shopping_list = supplies_needed
        self.supplies_needed = supplies_needed


    def __str__(self):
        string = ""
        for each in self.supplies_needed:
            string += str(each) + "\n"
        return string


    def display(self, user):
        print("Shopping List:")
        for each in supplies_needed:
            print(each, supplies_needed[each])
        if supplies_needed == {}:
            print("supplies_needed is empty")

    def staples(self, user):
        self.supplies_needed.append(user.missing_staples)

    def save(self): ##save to file
        None


##    def print(self):
####      save to file first, then print the file (os.startfile(filename, "print")
##        print("Shopping List:")
##        for ingredient, [amt, unit] in self.supplies_needed:
##            print(str(ingredient) + "," + str(amt) + " " + str(unit))
##        ##### print to printer

#####    def sort(self):
        ##### what is the best way to sort for shopping
        # maybe best not to sort

        

class User(object):

    def __init__(self, supplies_needed = {}, menu = None, 
                 ingredients_to_match = [], on_hand_staples = [],
                 missing_staples = [], required_matches = 3):
        self.supplies_needed = supplies_needed
        self.menu = Menu()
        self.ingredients_to_match = ingredients_to_match
        self.on_hand_staples = on_hand_staples
        self.missing_staples = missing_staples
        self.required_matches = required_matches

    def __str__(self):
        print("You are here!")

#####    def load(self):
        ##### ask for file and pull those attributes
	##### set them to be this object's attributes like when reading recipes

#####    def save(self):
        ##### print those attributes to file and ask for name to save
        ##### maybe saving should be automatic when an attribute is changed
        # not optional
        ##### could save to temp file and create an official file when user
        # chooses to User.save()?


class Main_menu(tkinter.Frame):

    def __init__(self, container, root, user):
        tkinter.Frame.__init__(self, container)
        self.root = root
        self.grid(sticky = 'nsew')
        label = tkinter.Label(self, text = "Main Menu")
        label.grid(sticky = 'n', pady = 40)        

        button1 = tkinter.Button(self, text = "Create a menu by matching.",
                                 command = lambda: Main_menu.match(self, container, root, user)).grid(sticky = 'e')
        button2 = tkinter.Button(self, text = "Browse through the cookbook.",
                                 command = lambda: Main_menu.browse(self, container, root, user)).grid(sticky = 'e')
        button3 = tkinter.Button(self, text = "Take a kitchen inventory.",
                                 command = lambda: Main_menu.inventory(self, container, root, user)).grid(sticky = 'e')
        button4 = tkinter.Button(self, text = "View your menu.",
                                 command = lambda: Main_menu.view_menu(self, container, root, user)).grid(sticky = 'e')
        button5 = tkinter.Button(self, text = "Save or load user data.",
                                 command = lambda: Main_menu.user_load_save(self, container, root, user)).grid(sticky = 'e')
        button6 = tkinter.Button(self, text = "Quit.", command = quit).grid(sticky = 'e')

                                 
    def match(self, container, root, user):
        self.grid_forget()
        Match(container, root, user)
    def browse(self, container, root, user):
        self.grid_forget()
        Browse(container, root, user)
    def inventory(self, container, root, user):
        self.grid_forget()
        Inventory(container, root, user)
    def view_menu(self, container, root, user):
        self.grid_forget()
        View_menu(container, root, user)
    def user_load_save(self, container, root, user):
        self.grid_forget()
        User_load_save(container, root, user)



class Inventory(tkinter.Frame):

    def __init__(self, container, root, user):
        tkinter.Frame.__init__(self, container, bg = 'green')
        self.root = root
        self.grid()
        self.grid_columnconfigure(0, weight = 2)
        label = tkinter.Label(self, text = "Inventory")
        label.grid(sticky = 'n', pady = 40, row = 0, column = 2)

        left_frame = tkinter.Frame(self, width = 300, height = 300, bg = 'orange')
        left_frame.grid(row = 2, column = 1)

        text_frame = tkinter.Frame(left_frame, bg = 'yellow')
        text_frame.grid()

        box = tkinter.Text(text_frame, wrap = 'word', height = 12, width = 15)
        box.grid(row = 2, column = 0)
        scroll = tkinter.Scrollbar(text_frame)
        scroll.grid(row = 2, column = 1)
        box.config(yscrollcommand = scroll.set)
        scroll.config(command = box.yview)
        
        box2 = tkinter.Text(text_frame, wrap = 'word', height = 12, width = 15)
        box2.grid(row = 2, column = 2)
        scroll2 = tkinter.Scrollbar(text_frame)
        scroll2.grid(row = 2, column = 3)
        box2.config(yscrollcommand = scroll2.set)
        scroll2.config(command = box2.yview)

        self.missing_checked_dict = {}
        self.on_hand_checked_dict = {}


        button0 = tkinter.Button(self, text = "Reset", command = lambda: Inventory.wipe(self, container, root, user))
        button0.grid(row = 1, column = 1)
        button0a = tkinter.Button(self, text = "Set", command = lambda: Inventory.done_inner(self, container, root, user))
        button0a.grid(row = 3, column = 1)


        dont_have = tkinter.Label(text_frame, text = "I don't have...")
        dont_have.grid(row = 1, column = 0)
        do_have = tkinter.Label(text_frame, text = "I do have...")
        do_have.grid(row = 1, column = 2)
        
        for each in user.missing_staples:
            var = tkinter.IntVar()
            check = tkinter.Checkbutton(left_frame, text = each, variable = var)
            self.missing_checked_dict[each] = var
            box.window_create('end', window = check)
            box.insert('end', '\n')

        for each in user.on_hand_staples:
            var = tkinter.IntVar()
            check = tkinter.Checkbutton(left_frame, text = each, variable = var)
            self.on_hand_checked_dict[each] = var
            box2.window_create('end', window = check)
            box2.insert('end', '\n')

        box.config(state = 'disabled')
        box2.config(state = 'disabled')

            
        right_frame = tkinter.Frame(self, width = 200, bg = 'blue')
        right_frame.grid(row = 2, column = 3)
        

        button1 = tkinter.Button(right_frame, text = "Create a menu by matching ingredients or recipes.",
                                 command = lambda: Inventory.match(self, container, root, user)).grid(sticky = 'e')
        button2 = tkinter.Button(right_frame, text = "Create a shopping list from your existing menu.",
                                 command = lambda: Inventory.shopping_list(self, container, root, user)).grid(sticky = 'e')
        button3 = tkinter.Button(right_frame, text = "Go back to the main menu.",
                                 command = lambda: Inventory.main_menu(self, container, root, user)).grid(sticky = 'e')






    def wipe(self, container, root, user):
        user.on_hand_staples = []
        user.missing_staples = STAPLES
        self.grid_forget()
        Inventory(container, root, user)

    def done_inner(self, container, root, user):
        for each in STAPLES:
            if each in self.missing_checked_dict:
                if self.missing_checked_dict[each].get() == 1:
                    if each not in user.on_hand_staples:
                        user.on_hand_staples.append(each)
                        user.missing_staples.remove(each)
                    else:
                        None
                else:
                    None
            else:
                None

            if each in self.on_hand_checked_dict:
                if self.on_hand_checked_dict[each].get() == 1:
                    if each not in user.missing_staples:
                        user.missing_staples.append(each)
                        user.on_hand_staples.remove(each)
                    else:
                        None
                else:
                    None
        self.grid_forget()
        Inventory(container, root, user)

    def done_outer(self, container, root, user):
        for each in STAPLES:
            if each in self.missing_checked_dict:
                if self.missing_checked_dict[each].get() == 1:
                    if each not in user.on_hand_staples:
                        user.on_hand_staples.append(each)
                        user.missing_staples.remove(each)
                    else:
                        None
                else:
                    None
            else:
                None

            if each in self.on_hand_checked_dict:
                if self.on_hand_checked_dict[each].get() == 1:
                    if each not in user.missing_staples:
                        user.missing_staples.append(each)
                        user.on_hand_staples.remove(each)
                    else:
                        None
                else:
                    None      

    def match(self, container, root, user):
        Inventory.done_outer(self, container, root, user)
        self.grid_forget()
        Match(container, root, user)
        
    def shopping_list(self, container, root, user):
        Inventory.done_outer(self, container, root, user)        
        self.grid_forget()
        Make_Shopping_List(user)
        Shopping_list(container, root, user)
        
    def main_menu(self, container, root, user):
        Inventory.done_outer(self, container, root, user)
        self.grid_forget()
        Main_menu(container, root, user)


class User_load_save(tkinter.Frame):

    def __init__(self, container, root, user):
        
        tkinter.Frame.__init__(self, container)
        self.root = root
        self.grid()
        label = tkinter.Label(self, text = "Load or Save User")
        label.grid(sticky = 'n', pady = 40, row = 0, column = 1)

        frame = tkinter.Frame(self, bg = 'yellow')
        frame.grid()

        load_label = tkinter.Label(frame, text = "Filename :").grid(row = 0, column = 0)
        load_entry = tkinter.Entry(frame, width = 15)
        load_entry.grid(row = 0, column = 1)
        button1 = tkinter.Button(frame, text = "Load.",
                                 command = lambda: User_load_save.load(self, user, frame, load_entry))
        button1.grid(row = 0, column = 2)

        save_label = tkinter.Label(frame, text = "Filename: ").grid(row = 1, column = 0)
        save_entry = tkinter.Entry(frame, width = 15)
        save_entry.grid(row = 1, column = 1)
        button2 = tkinter.Button(frame, text = "Save.",
                                 command = lambda: User_load_save.save(self, user, frame, save_entry))
        button2.grid(row = 1, column = 2) 
        button3 = tkinter.Button(frame, text = "Done.",
                                 command = lambda: User_load_save.main_menu(self, container, root, user))
        button3.grid(row = 2, column = 2)






    def load(self, user, frame, load_entry):
        filename = load_entry.get()
        path1 = os.getcwd()
        path2 = '\\users\\'
        path = str(path1) + str(path2)
        file = str(path) + str(filename)
        file = open(file, 'r')
        contents = file.read()
        contents = contents.split('\n')

        user.shopping_list = []
        shopping_list = contents[0]
        shopping_list = shopping_list.split(',')
        shopping_list.remove("")
        for each in shopping_list:
            each.strip()
            user.shopping_list.append(each)
        print(user.shopping_list)

        user.menu.meal_list = []
        meal_list = contents[1]
        meal_list = meal_list.split(',')
        meal_list.remove("")
        for each in meal_list:
            each.strip()
            each = cookbook.recipe_list[each]
            user.menu.meal_list.append(each)
        print(user.menu.meal_list)
        
        user.ingredients_to_match = []
        ingredients_to_match = contents[2]
        ingredients_to_match = ingredients_to_match.split(',')
        ingredients_to_match.remove("")
        for each in ingredients_to_match:
            each.strip()
            user.ingredients_to_match.append(each)
        print(user.ingredients_to_match)

        user.on_hand_staples = []
        on_hand_staples = contents[3]
        on_hand_staples = on_hand_staples.split(',')
        on_hand_staples.remove("")
        for each in on_hand_staples:
            each.strip()
            user.on_hand_staples.append(each)
        print(user.on_hand_staples)

        user.missing_staples = []
        missing_staples = contents[4]
        missing_staples = missing_staples.split(',')
        missing_staples.remove("")
        for each in missing_staples:
            each.strip()
            user.missing_staples.append(each)
        print(user.missing_staples)
        
        user.required_matches = int(contents[5])
        print(user.required_matches)

        file.close()
        success_label = tkinter.Label(frame, text = "Loaded.").grid(row = 0, column = 3)


        

    def save(self, user, frame, save_entry):
        filename = save_entry.get()
        path1 = os.getcwd()
        path2 = '\\users\\'
        path = str(path1) + str(path2)
        file = str(path) + str(filename)
        file = open(file, 'w')
        for each in user.shopping_list:
            file.write(each)
            file.write(',')
        file.write('\n')
        for each in user.menu.meal_list:
            file.write(each.name)
            file.write(',')
        file.write('\n')
        for each in user.ingredients_to_match:
            file.write(each)
            file.write(',')
        file.write('\n')
        for each in user.on_hand_staples:
            file.write(each)
            file.write(',')
        file.write('\n')
        for each in user.missing_staples:
            file.write(each)
            file.write(',')
        file.write('\n')
        file.write(str(user.required_matches))
        file.close()
        success_label = tkinter.Label(frame, text = "Saved.").grid(row = 1, column = 3)
        


    def main_menu(self, container, root, user):
        self.grid_forget()
        Main_menu(container, root, user)



class View_menu(tkinter.Frame):

    def __init__(self, container, root, user):
        tkinter.Frame.__init__(self, container)
        self.root = root
        self.grid(row = 0, column = 0, sticky = 'nsew')
        label = tkinter.Label(self, text = "Your Menu")
        label.grid(sticky = 'n', pady = 40, row = 0, column = 2)



        left_frame = tkinter.Frame(self, width = 300, height = 300, bg = 'orange')
        left_frame.grid(row = 1, column = 0)
        left_frame.grid_propagate(False)

        text = tkinter.Text(left_frame, wrap = 'word', width = 30, height = 15)
        text.grid(row = 0, column= 0)

        

        counter = 0
        for each in user.menu.meal_list:
            display_button = tkinter.Button(left_frame, text = each, # text = recipe.name
                                            command = lambda n = each: View_menu.display_recipe(self, n))
            text.window_create('end', window = display_button)
            text.insert('end', '\t')
            del_button = tkinter.Button(left_frame, text = "X",
                                        command = lambda n = each: user.menu.meal_list.remove(n))
            text.window_create('end', window = del_button)
            text.insert('end', '\n')
            counter += 1

        text.config(state = 'disabled')
        scroll = tkinter.Scrollbar(left_frame)
        scroll.grid(row = 0, column = 1)
        text.config(yscrollcommand = scroll.set)
        scroll.config(command = text.yview)
        


        right_frame = tkinter.Frame(self, width = 200, bg = 'blue')
        right_frame.grid(row = 1, column = 3)

        button1 = tkinter.Button(right_frame, text = "Make your shopping list.",
                                 command = lambda: View_menu.shopping_list(self, container, root, user)).grid(sticky = 'e')
        button2 = tkinter.Button(right_frame, text = "Print this menu.",
                                 command = None).grid(sticky = 'e') ## Menu.print()
        button3 = tkinter.Button(right_frame, text = "Browse the cookbook for recipes to add.",
                                 command = lambda: View_menu.browse(self, container, root, user)).grid(sticky = 'e')
        button4 = tkinter.Button(right_frame, text = "Narrow down the list by matching again.",
                                 command = lambda: View_menu.match(self, container, root, user)).grid(sticky = 'e')
        button5 = tkinter.Button(right_frame, text = "Load or save a menu.",
                                 command = lambda: View_menu.menu_load_save(self, container, root, user)).grid(sticky = 'e')
        button6 = tkinter.Button(right_frame, text = "Go back to the main menu.",
                                 command = lambda: View_menu.main_menu(self, container, root, user)).grid(sticky = 'e')



    def shopping_list(self, container, root, user):
        self.grid_forget()
        Make_Shopping_List(user)
        Shopping_list(container, root, user)
    def browse(self, container, root, user):
        self.grid_forget()
        Browse(container, root, user)
    def match(self, container, root, user):
        self.grid_forget()
        Match(container, root, user)
    def menu_load_save(self, container, root, user):
        self.grid_forget()
        Menu_load_save(container, root, user)
    def main_menu(self, container, root, user):
        self.grid_forget()
        Main_menu(container, root, user)
    def display_recipe(self, recipe_object):
        Display_recipe(recipe_object)



class Menu_load_save(tkinter.Frame):


    def __init__(self, container, root, user):
        tkinter.Frame.__init__(self, container)
        self.root = root
        self.grid(row = 0, column = 0, sticky = 'nsew')
        label = tkinter.Label(self, text = "Load or Save Menu")
        label.grid(sticky = 'n', pady = 40, row = 0, column = 2)

        frame = tkinter.Frame(self, bg = 'blue')
        frame.grid()

        load_label = tkinter.Label(frame, text = "Filename: ").grid(row = 0, column = 0)
        load_entry = tkinter.Entry(frame, width = 15)
        load_entry.grid(row = 0, column = 1)
        button1 = tkinter.Button(frame, text = "Load.",
                                 command = lambda: Menu_load_save.load(self, user, frame, load_entry))
        button1.grid(row = 0, column = 2)
        
        save_label = tkinter.Label(frame, text = "Filename: ").grid(row = 1, column = 0)
        save_entry = tkinter.Entry(frame, width = 15)
        save_entry.grid(row = 1, column = 1)                                   
        button2 = tkinter.Button(frame, text = "Save.",
                                 command = lambda: Menu_load_save.save(self, user, frame, save_entry))
        button2.grid(row = 1, column = 2)
        button3 = tkinter.Button(frame, text = "Done.",
                                 command = lambda: Menu_load_save.view_menu(self, container, root, user))
        button3.grid(row = 2, column = 2)
        



    def load(self, user, frame, load_entry):
        filename = load_entry.get()
        path1 = os.getcwd()
        path2 = '\\menus\\'
        path = str(path1) + str(path2)
        file = str(path) + str(filename)
        file = open(file, 'r')
        recipe_list = file.read()
        recipe_list = recipe_list.split('\n')
        recipe_list.remove("")
        new_list = []
        for each in recipe_list:
            each.strip()
            new_list.append(cookbook.recipe_list[each])
        user.menu.meal_list = new_list
        success_label = tkinter.Label(frame, text = "Loaded.").grid(row = 0, column = 4)

        
    def save(self, user, frame, save_entry):
        filename = save_entry.get()
        path1 = os.getcwd()
        path2 = '\\menus\\'
        path = str(path1) + str(path2)
        file = str(path) + str(filename)
        file = open(file, 'w')
        for each in user.menu.meal_list:
            file.write(each.name)
            file.write('\n')
        file.close()
        success_label = tkinter.Label(frame, text = "Saved.").grid(row = 1, column = 4)
        
    def view_menu(self, container, root, user):
        self.grid_forget()
        View_menu(container, root, user)



class Match(tkinter.Frame):

    def __init__(self, container, root, user):
        
        tkinter.Frame.__init__(self, container)
        self.root = root
        self.grid(row = 0, column = 0, sticky = 'nsew')
        label = tkinter.Label(self, text = "Recipe Match Settings")
        label.grid(sticky = 'n', pady = 40, row = 0, column = 0)


        left_frame = tkinter.Frame(self, width = 350, bg = 'red')
        left_frame.grid(row = 1, column = 0)


        
        how_many = tkinter.Label(left_frame, text = "How many ingredients need to match? ")
        how_many.grid(row = 1, sticky = 'w')
        required_matches = tkinter.Entry(left_frame, width = 3, text = 1)
        required_matches.delete(0)
        required_matches.insert('end', int(user.required_matches))
        required_matches.grid(row = 1, column = 2)

        which_ones = tkinter.Label(left_frame, text = "Which ingredients would you like to use? ")
        which_ones.grid(row = 2, sticky = 'w')

        box = tkinter.Text(left_frame, wrap = 'word', height = 12, width = 15)
        box.grid(row = 3, column = 0, columnspan = 2)
        scroll = tkinter.Scrollbar(left_frame)
        scroll.grid(row = 3, column = 1)
        box.config(yscrollcommand = scroll.set)
        scroll.config(command = box.yview)

        some_ingredients = ["chicken", "beans", "white wine", "shrimp"]
        check_dict = {}
        for each in some_ingredients:
            var = tkinter.IntVar()
            check = tkinter.Checkbutton(left_frame, text = each, variable = var)
            check_dict[each] = var
            box.window_create('end', window = check)
            box.insert('end', '\n')



        right_frame = tkinter.Frame(self, width = 200, bg = 'orange')
        right_frame.grid(row = 2, column = 4)


        button1 = tkinter.Button(right_frame, text = "Browse the cookbook for recipes to build from.",
                                 command = lambda: Match.browse(self, container, root, user)).grid(sticky = 'e')
        button3 = tkinter.Button(right_frame, text = "See the matches!",
                                 command = lambda: Match.select_matches(self, container, root, user, required_matches, some_ingredients, check_dict)).grid(sticky = 'e')
        button4 = tkinter.Button(right_frame, text = "Go back to the main menu.",
                                 command = lambda: Match.main_menu(self, container, root, user)).grid(sticky = 'e')



        upper_right_frame = tkinter.Frame(self, width = 200, bg = 'purple')
        upper_right_frame.grid(row = 1, column = 4)

        scroll = tkinter.Scrollbar(upper_right_frame)
        scroll.grid(row = 1, column = 2, ipady = 50)
        text = tkinter.Text(upper_right_frame, width = 30, wrap = 'word', height = 10)
        text.insert('end', "You're set to match with:")
        text.grid(row = 1)
        for each in user.menu.meal_list:
            text.insert('end', "\n")
            text.insert('end', each.name)
        for each in user.ingredients_to_match:
            text.insert('end', '\n')
            text.insert('end', each)
        #text.insert('end', user.menu.meal_list, checked_recipes)
        text.config(state = 'disabled')

        text.config(yscrollcommand = scroll.set)
        scroll.config(command = text.yview)


    def check_button_states(user, some_ingredients, check_dict):
        for each in some_ingredients:
            if check_dict[each].get() == 1:
                if each in user.ingredients_to_match:
                    None
                else:
                    user.ingredients_to_match.append(each)
            else:
                None

    def browse(self, container, root, user):
        self.grid_forget()
        Browse(container, root, user)
        
    def select_matches(self, container, root, user, required_matches, some_ingredients, check_dict):
        #find out how many in common for a match
        #find out which ingredients the user chose
        #run match_recipes, which will add meal_list ingredients to ingredients_to_match
        #this returns similar_recipes, which can be sent to be displayed in match select
        user.required_matches = int(required_matches.get())
        Match.check_button_states(user, some_ingredients, check_dict)
        similar_recipes = Menu.match_recipes(self, user)
        self.grid_forget()
        Select_matches(container, root, user, similar_recipes)
        
    def main_menu(self, container, root, user):
        self.grid_forget()
        Main_menu(container, root, user)




class Select_matches(tkinter.Frame):

    def __init__(self, container, root, user, similar_recipes = Menu()):
        tkinter.Frame.__init__(self, container)
        self.root = root
        self.grid(row = 0, column = 0, sticky = 'nsew')
        label = tkinter.Label(self, text = "Choose What You Like")
        label.grid(sticky = 'n', pady = 40, row = 0, column = 2)


        left_frame = tkinter.Frame(self, bg = 'purple')
        left_frame.grid(row = 1, column = 0)
        text = tkinter.Text(left_frame, wrap = 'word', width = 30, height = 15)
        text.grid(row = 0, column = 0)


        check_dict = {}
        
        for each in similar_recipes.meal_list:
            var = tkinter.IntVar()
            check = tkinter.Checkbutton(left_frame, text = each, variable = var)
            check_dict[each.name] = var
            text.window_create('end', window = check)
            view_button = tkinter.Button(left_frame, text = "O",
                                         command = lambda: Select_matches.display_recipe(self, each))
            text.insert('end', '\t')
            text.window_create('end', window = view_button)
            text.insert('end', '\n')

        text.config(state = 'disabled')
        scroll = tkinter.Scrollbar(left_frame)
        scroll.grid(row = 0, column = 1)
        text.config(yscrollcommand = scroll.set)
        scroll.config(command = text.yview)

            
        done_button = tkinter.Button(left_frame, text = "Add to my menu.").grid()




        right_frame = tkinter.Frame(self, bg = 'green')
        right_frame.grid(row = 1, column = 3)

        button1 = tkinter.Button(right_frame, text = "View your menu.",
                                 command = lambda: Select_matches.view_menu(self, container, root, user, check_dict, similar_recipes)).grid(sticky = 'e')
        button2 = tkinter.Button(right_frame, text = "Browse the cookbook to add more.",
                                 command = lambda: Select_matches.browse(self, container, root, user)).grid(sticky = 'e')
        button3 = tkinter.Button(right_frame, text = "Take a kitchen inventory to make your shopping list.",
                                 command = lambda: Select_matches.inventory(self, container, root, user)).grid(sticky = 'e')
        button5 = tkinter.Button(right_frame, text = "Match again.",
                                 command = lambda: Select_matches.match(self, container, root, user)).grid(sticky = 'e')


    def check_button_states(user, check_dict, similar_recipes):
        for each in similar_recipes.meal_list:
            if check_dict[each.name].get() == 1:
                if each in user.menu.meal_list:
                    None
                else:
                    user.menu.meal_list.append(each)

    def view_menu(self, container, root, user, check_dict, similar_recipes):
        Select_matches.check_button_states(user, check_dict, similar_recipes)
        self.grid_forget()
        View_menu(container, root, user)
    def browse(self, container, root, user):
        self.grid_forget()
        Browse(container, root, user)
    def inventory(self, container, root, user):
        self.grid_forget()
        Inventory(container, root, user)
    def match(self, container, root, user):
        self.grid_forget()
        Match(container, root, user)
    def display_recipe(self, recipe_object):
        Display_recipe(recipe_object)  ## parameter recipe_object



class Shopping_list(tkinter.Frame):

    def __init__(self, container, root, user):
        tkinter.Frame.__init__(self, container)
        self.root = root
        self.grid(row = 0, column = 0, sticky = 'nsew')
        label = tkinter.Label(self, text = "Shopping List")
        label.grid(sticky = 'n', pady = 40, row = 0, column = 2)


        left_frame = tkinter.Frame(self, width = 300, bg = 'purple')
        left_frame.grid(row = 1, column = 0)

        for each in user.shopping_list:
            label = str(each) + ", " + str(user.shopping_list[each])
            tkinter.Label(left_frame, text = label).grid(sticky = 'w')

        if user.shopping_list == []:
            tkinter.Label(left_frame, text = "empty shopping list").grid(sticky = 'w')


        right_frame = tkinter.Frame(self, width = 200, bg = 'blue')
        right_frame.grid(row = 1, column = 3)

        button0 = tkinter.Button(right_frame, text = "Print your list.",
                                 command = lambda: Shopping_list.print()).grid(sticky = 'e')
        button1 = tkinter.Button(right_frame, text = "Narrow down your list with a kitchen inventory.",
                                 command = lambda: Shopping_list.inventory(self, container, root, user)).grid(sticky = 'e')
        button2 = tkinter.Button(right_frame, text = "View your menu.",
                                 command = lambda: Shopping_list.view_menu(self, container, root, user)).grid(sticky = 'e')



    def print():
        None
        #Shopping_list.print()
    def inventory(self, container, root, user):
        self.grid_forget()
        Inventory(container, root, user)
    def view_menu(self, container, root, user):
        self.grid_forget()
        View_menu(container, root, user)



class Display_recipe(tkinter.Frame):

    def __init__(self, recipe):  ## parameter recipe_object

        self = tkinter.Tk()
        self.minsize(width = 500, height = 500)
        self.title("Recipe Details")
        label = tkinter.Label(self, text = recipe.name)  
        label.grid(sticky = 'n', pady = 40, row = 0, column = 0)


        
        left_frame = tkinter.Frame(self, bg = 'green', width = 600)
        left_frame.grid(row = 1, column = 0, sticky = 'w')

        for each in recipe.ingredient_info:
            tkinter.Label(left_frame, text = each).grid(sticky = 'w')

        lower_left_frame = tkinter.Frame(self, bg = 'red')
        lower_left_frame.grid(row = 2, column = 0)
        instruct_text = tkinter.Text(lower_left_frame, wrap = 'word', width = 50)
        instruct_text.insert('end', recipe.instructions)
        instruct_text.config(state = 'disabled')
        instruct_text.grid(sticky = 'w')
        scroll = tkinter.Scrollbar(lower_left_frame)
        scroll.grid(row = 0, column = 1)
        instruct_text.config(yscrollcommand = scroll.set)
        scroll.config(command = instruct_text.yview)


        middle_frame = tkinter.Frame(self, bg = 'blue', width = 100)
        middle_frame.grid(row = 1, column = 2, sticky = 'n')

        tkinter.Label(middle_frame, text = ("Rating:", recipe.tasty_rating, "yums")).grid(sticky = 'w')

        tkinter.Label(middle_frame, text = ("Prep Time: " + str(recipe.prep_time))).grid(sticky = 'w')

        tkinter.Label(middle_frame, text = ("Cook Time: " + str(recipe.cook_time))).grid(sticky = 'w')
        




        right_frame = tkinter.Frame(self, bg = 'yellow')
        right_frame.grid(row = 3, column = 3)


        button1 = tkinter.Button(right_frame, text = "Print.",
                                 command = None).grid()    ## Recipe.print()
        button2 = tkinter.Button(right_frame, text = "Done.",
                                 command = lambda: Display_recipe.done(self)).grid()



    def done(self):
        self.destroy()



class Browse(tkinter.Frame):

    def __init__(self, container, root, user):
        tkinter.Frame.__init__(self, container)
        self.root = root
        self.grid(row = 0, column = 0, sticky = 'nsew')
        label = tkinter.Label(self, text = "Cookbook")
        label.grid(sticky = 'n', pady = 40, row = 0, column = 2)


        left_frame = tkinter.Frame(self, bg = 'yellow')
        left_frame.grid(row = 1, column = 0)

        box = tkinter.Text(left_frame, wrap = 'word', height = 10, width = 35)
        box.grid(row = 0, column = 0)

        scroll = tkinter.Scrollbar(left_frame)
        scroll.grid(row = 0, column = 1)

        box.config(yscrollcommand = scroll.set)
        scroll.config(command = box.yview)


        self.check_dict = {}
        
        counter = 0
        for each in cookbook.meal_list:
            var = tkinter.IntVar()
            check = tkinter.Checkbutton(left_frame, text = each.name, variable = var)
            self.check_dict[each.name] = var
            box.window_create('end', window = check)
            view_button = tkinter.Button(left_frame, text = "O",
                                         command = lambda n = counter: Browse.display_recipe(self, cookbook.meal_list[n]))
            box.insert('end', '\t')
            box.window_create('end', window = view_button)
            box.insert('end', '\n')
            counter += 1
            

        ## ideally these are sorted by expanding category
            ## i guess for now let's settle for alphabetical

        right_frame = tkinter.Frame(self, bg = 'red')
        right_frame.grid(row = 1, column = 3)


        button2 = tkinter.Button(right_frame, text = "Add these recipes to my menu.",
                                 command = lambda: Browse.view_menu(self, container, root, user)).grid(sticky = 'e')
        button3 = tkinter.Button(right_frame, text = "Match to these recipes.",
                                 command = lambda: Browse.match(self, container, root, user)).grid(sticky = 'e')
        button4 = tkinter.Button(right_frame, text = "Go back to the main menu.",
                                 command = lambda: Browse.main_menu(self, container, root, user)).grid(sticky = 'e')


    def check_button_states(check_dict):
        on_list = []
        for each in cookbook.meal_list:
            if check_dict[each.name].get() == 1:
                if each in on_list:
                    None
                else:
                    on_list.append(each)
            elif check_dict[each.name].get() == 0:
                if each in on_list:
                    on_list.remove(each)
                else:
                    None
            else:
                print("dictionary's intvar value is not 0 or 1 wut")
        return on_list



    def display_recipe(self, recipe_object):
        Display_recipe(recipe_object)
        
    def view_menu(self, container, root, user):
        self.grid_forget()
        on_list = Browse.check_button_states(self.check_dict)
        for each in on_list:
            if each in user.menu.meal_list:
                None
            elif each not in user.menu.meal_list:
                user.menu.add_recipe(each)
            else:
                print("Browse.display_menu error!")
        View_menu(container, root, user)
        
    def match(self, container, root, user):
        for each in Browse.check_button_states(self.check_dict):
            for ing in each.ingredients:
                if ing in user.ingredients_to_match:
                    None
                else:
                    if ing in STAPLES:
                        None
                    else:
                        user.ingredients_to_match.append(ing)
        self.grid_forget()
        Match(container, root, user)
        
    def main_menu(self, container, root, user):
        self.grid_forget()
        Main_menu(container, root, user)




def main():

    global STAPLES
    STAPLES = ["milk", "bread", "butter", "flour", "sugar", "beans", "water", "brown sugar",
               "baking powder", "baking soda", "salt", "pepper", "basil", "garlic", "marjoram",
               "cinnamon", "cumin", "dill", "fennel", "cloves", "oregano", "chives", "paprika",
               "salt", "cayenne"]

    global cookbook
    cookbook = Menu()
    cookbook = cookbook.create_cookbook()
    user = User(missing_staples = STAPLES)

    root = tkinter.Tk()
    root.resizable()
    root.grid()
    root.minsize(width = 500, height = 500)
    root.grid_rowconfigure(0, weight = 1)
    root.grid_columnconfigure(0, weight = 1)
    root.title("Recipe Match")
    container = tkinter.Frame(root)
    container.grid(sticky = 'n')
    container.grid_rowconfigure(0, weight = 1)
    container.grid_columnconfigure(0, weight = 1)
    main_menu = Main_menu(container, root, user)
    tkinter.mainloop()


main()




















