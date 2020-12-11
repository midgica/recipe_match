import tkinter


class Main_menu(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = root
        self.grid(sticky = 'nsew')
        label = tkinter.Label(self, text = "Main Menu")
        label.grid(sticky = 'n', pady = 40)        

        button1 = tkinter.Button(self, text = "Create a menu by matching.",
                                 command = lambda: Main_menu.match(self)).grid(sticky = 'e')
        button2 = tkinter.Button(self, text = "Browse through the cookbook.",
                                 command = lambda: Main_menu.browse(self)).grid(sticky = 'e')
        button3 = tkinter.Button(self, text = "Take a kitchen inventory.",
                                 command = lambda: Main_menu.inventory(self)).grid(sticky = 'e')
        button4 = tkinter.Button(self, text = "View your menu.",
                                 command = lambda: Main_menu.view_menu(self)).grid(sticky = 'e')
        button5 = tkinter.Button(self, text = "Save or load user data.",
                                 command = lambda: Main_menu.user_load_save(self)).grid(sticky = 'e')
        button6 = tkinter.Button(self, text = "Quit.", command = quit).grid(sticky = 'e')

                                 
    def match(self):
        self.grid_forget()
        Match(container, root)
    def browse(self):
        self.grid_forget()
        Browse(container, root)
    def inventory(self):
        self.grid_forget()
        Inventory(container, root)
    def view_menu(self):
        self.grid_forget()
        View_menu(container, root)
    def user_load_save(self):
        self.grid_forget()
        User_load_save(container, root)



class Inventory(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent, bg = 'green')
        self.controller = root
        self.grid()
        self.grid_columnconfigure(0, weight = 2)
        label = tkinter.Label(self, text = "Inventory")
        label.grid(sticky = 'n', pady = 40, row = 0, column = 2)



        left_frame = tkinter.Frame(self, width = 300, height = 300, bg = 'orange')
        left_frame.grid(row = 1, column = 0)
        left_frame.grid_propagate(False)

        box = tkinter.Text(left_frame, wrap = 'word', height = 10, width = 15)
        box.grid(row = 0, column = 0)

        scroll = tkinter.Scrollbar(left_frame)
        scroll.grid(row = 0, column = 1)
        
        box.config(yscrollcommand = scroll.set)
        scroll.config(command = box.yview)

        staples = ["milk", "bread", "butter", "flour", "sugar", "beans", "water", "brown sugar",
                   "baking powder", "baking soda", "salt", "pepper", "basil", "garlic", "marjoram",
                   "cinnamon", "cumin", "dill", "fennel", "cloves", "oregano", "chives", "paprika"]

        for each in staples:
            check = tkinter.Checkbutton(left_frame, text = each)
            box.window_create('end', window = check)
            box.insert('end', '\n')

        box.config(state = 'disabled')
        

            
        right_frame = tkinter.Frame(self, width = 200, bg = 'blue')
        right_frame.grid(row = 1, column = 3)
        

        button1 = tkinter.Button(right_frame, text = "Create a menu by matching ingredients or recipes.",
                                 command = lambda: Inventory.match(self)).grid(sticky = 'e')
        button2 = tkinter.Button(right_frame, text = "Create a shopping list from your existing menu.",
                                 command = lambda: Inventory.shopping_list(self)).grid(sticky = 'e')
        button3 = tkinter.Button(right_frame, text = "Go back to the main menu.",
                                 command = lambda: Inventory.main_menu(self)).grid(sticky = 'e')







        

    def match(self):
        self.grid_forget()
        Match(container, root)
    def shopping_list(self):
        self.grid_forget()
        Shopping_list(container, root)
    def main_menu(self):
        self.grid_forget()
        Main_menu(container, root)


class User_load_save(tkinter.Frame):

    def __init__(self, parent, controller):
        
        tkinter.Frame.__init__(self, parent)
        self.controller = root
        self.grid()
        label = tkinter.Label(self, text = "Load or Save User")
        label.grid(sticky = 'n', pady = 40, row = 0, column = 1)

        frame = tkinter.Frame(self, bg = 'yellow')
        frame.grid(row = 1)

        button1 = tkinter.Button(frame, text = "Load.",
                                 command = None).grid()  ## load user data function
        button2 = tkinter.Button(frame, text = "Save.",
                                 command = None).grid()  ## save user data function
        button3 = tkinter.Button(frame, text = "Done.",
                                 command = lambda: User_load_save.main_menu(self)).grid()



    def main_menu(self):
        self.grid_forget()
        Main_menu(container, root)



class View_menu(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = root
        self.grid(row = 0, column = 0, sticky = 'nsew')
        label = tkinter.Label(self, text = "Your Menu")
        label.grid(sticky = 'n', pady = 40, row = 0, column = 2)



        left_frame = tkinter.Frame(self, width = 300, height = 300, bg = 'orange')
        left_frame.grid(row = 1, column = 0)
        left_frame.grid_propagate(False)

        text = tkinter.Text(left_frame, wrap = 'word', width = 30, height = 15)
        text.grid(row = 0, column= 0)

        
        sample_menu = ['Chicken Marsala', 'Eggs Benedict', 'Eggs Florentine', 'Steak Diane',
                       'Steak au Poivre', 'Baba Ghanoush', 'Goulash', 'Chocolate Cake']
        ### this list should contain recipe objects 

        for each in sample_menu:
            display_button = tkinter.Button(left_frame, text = each, # text = recipe.name
                                            command = lambda: View_menu.display_recipe(self))
            text.window_create('end', window = display_button)
            text.insert('end', '\t')
            del_button = tkinter.Button(left_frame, text = "X",
                                        command = None) ##meal_list.remove(each)
            text.window_create('end', window = del_button)
            text.insert('end', '\n')

        text.config(state = 'disabled')
        scroll = tkinter.Scrollbar(left_frame)
        scroll.grid(row = 0, column = 1)
        text.config(yscrollcommand = scroll.set)
        scroll.config(command = text.yview)


        right_frame = tkinter.Frame(self, width = 200, bg = 'blue')
        right_frame.grid(row = 1, column = 3)

        button1 = tkinter.Button(right_frame, text = "Make your shopping list.",
                                 command = lambda: View_menu.shopping_list(self)).grid(sticky = 'e')
        button2 = tkinter.Button(right_frame, text = "Print this menu.",
                                 command = None).grid(sticky = 'e') ## Menu.print()
        button3 = tkinter.Button(right_frame, text = "Browse the cookbook for recipes to add.",
                                 command = lambda: View_menu.browse(self)).grid(sticky = 'e')
        button4 = tkinter.Button(right_frame, text = "Narrow down the list by matching again.",
                                 command = lambda: View_menu.match(self)).grid(sticky = 'e')
        button5 = tkinter.Button(right_frame, text = "Load or save a menu.",
                                 command = lambda: View_menu.menu_load_save(self)).grid(sticky = 'e')
        button6 = tkinter.Button(right_frame, text = "Go back to the main menu.",
                                 command = lambda: View_menu.main_menu(self)).grid(sticky = 'e')



    def shopping_list(self):
        self.grid_forget()
        Shopping_list(container, root)
    def browse(self):
        self.grid_forget()
        Browse(container, root)
    def match(self):
        self.grid_forget()
        Match(container, root)
    def menu_load_save(self):
        self.grid_forget()
        Menu_load_save(container, root)
    def main_menu(self):
        self.grid_forget()
        Main_menu(container, root)
    def display_recipe(self):
        Display_recipe(container, root)  ## parameter recipe_object



class Menu_load_save(tkinter.Frame):


    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = root
        self.grid(row = 0, column = 0, sticky = 'nsew')
        label = tkinter.Label(self, text = "Load or Save Menu")
        label.grid(sticky = 'n', pady = 40, row = 0, column = 2)

        button1 = tkinter.Button(self, text = "Load.",
                                 command = None).grid()    ## load menu function
        button2 = tkinter.Button(self, text = "Save.",
                                 command = None).grid()    ## save menu function
        button3 = tkinter.Button(self, text = "Done.",
                                 command = lambda: Menu_load_save.view_menu(self)).grid()


    def view_menu(self):
        self.grid_forget()
        View_menu(container, root)



class Match(tkinter.Frame):

    def __init__(self, parent, controller):
        
        tkinter.Frame.__init__(self, parent)
        self.controller = root
        self.grid(row = 0, column = 0, sticky = 'nsew')
        label = tkinter.Label(self, text = "Recipe Match Settings")
        label.grid(sticky = 'n', pady = 40, row = 0, column = 0)


        left_frame = tkinter.Frame(self, width = 350, bg = 'red')
        left_frame.grid(row = 1, column = 0)


        #enter ingredients
        #required matches



        
        how_many = tkinter.Label(left_frame, text = "How many ingredients need to match? ")
        how_many.grid(row = 1, sticky = 'w')
        ingredients_to_match = tkinter.Entry(left_frame, width = 3).grid(row = 1, column = 2)
        #user.ingredients_to_match = int(ingredients_to_match.get())


        which_ones = tkinter.Label(left_frame, text = "Which ingredients would you like to use? ")
        which_ones.grid(row = 2, sticky = 'w')

        some_ingredients = ["chicken", "coconut milk", "apple", "green onion", "yam", "turkey"]
        for each in some_ingredients:
            check = tkinter.Checkbutton(left_frame, text = each).grid(sticky = 'w')



        right_frame = tkinter.Frame(self, width = 200, bg = 'orange')
        right_frame.grid(row = 2, column = 4)


        button1 = tkinter.Button(right_frame, text = "Browse the cookbook for recipes to build from.",
                                 command = lambda: Match.browse(self)).grid(sticky = 'e')
##        button2 = tkinter.Button(right_frame, text = "Find recipes that match your ingredients.",
##                                 command = lambda: Match.enter_ingredients(self)).grid(sticky = 'e')
        button3 = tkinter.Button(right_frame, text = "See the matches!",
                                 command = lambda: Match.select_matches(self)).grid(sticky = 'e')
        button4 = tkinter.Button(right_frame, text = "Go back to the main menu.",
                                 command = lambda: Match.main_menu(self)).grid(sticky = 'e')



        upper_right_frame = tkinter.Frame(self, width = 200, bg = 'purple')
        upper_right_frame.grid(row = 1, column = 4)

        scroll = tkinter.Scrollbar(upper_right_frame)
        scroll.grid(row = 1, column = 2, ipady = 50)
        text = tkinter.Text(upper_right_frame, width = 30, wrap = 'word', height = 10)
        text.insert('end', "You're set to match with:")
        text.grid(row = 1)
        #text.insert('end', user.meal_list, checked_recipes)
        text.config(state = 'disabled')

        text.config(yscrollcommand = scroll.set)
        scroll.config(command = text.yview) #we're assuming this is working, can't test yet



    def browse(self):
        self.grid_forget()
        Browse(container, root)
    def select_matches(self):
        self.grid_forget()
        Select_matches(container, root)
    def main_menu(self):
        self.grid_forget()
        Main_menu(container, root)




class Select_matches(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = root
        self.grid(row = 0, column = 0, sticky = 'nsew')
        label = tkinter.Label(self, text = "Choose What You Like")
        label.grid(sticky = 'n', pady = 40, row = 0, column = 2)


        left_frame = tkinter.Frame(self, bg = 'purple')
        left_frame.grid(row = 1, column = 0)
        text = tkinter.Text(left_frame, wrap = 'word', width = 30, height = 15)
        text.grid(row = 0, column = 0)

        sample_matches = ['recipe1', 'recipe2', 'recipe3', 'recipe4', 'recipe5', 'recipe6', 'recipe7']
        for each in sample_matches:
            check = tkinter.Checkbutton(left_frame, text = each)
            text.window_create('end', window = check)
            view_button = tkinter.Button(left_frame, text = "O",
                                         command = lambda: Select_matches.display_recipe(self))
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
                                 command = lambda: Select_matches.view_menu(self)).grid(sticky = 'e')
        button2 = tkinter.Button(right_frame, text = "Browse the cookbook to add more.",
                                 command = lambda: Select_matches.browse(self)).grid(sticky = 'e')
        button3 = tkinter.Button(right_frame, text = "Take a kitchen inventory to make your shopping list.",
                                 command = lambda: Select_matches.inventory(self)).grid(sticky = 'e')
        button4 = tkinter.Button(right_frame, text = "Display this recipe.",
                                 command = lambda: Select_matches.display_recipe(self)).grid(sticky = 'e')
                                 ## interactable checklist  #### parameter recipe_object
        button5 = tkinter.Button(right_frame, text = "Match again.",
                                 command = lambda: Select_matches.match(self)).grid(sticky = 'e')



    def view_menu(self):
        self.grid_forget()
        View_menu(container, root)
    def browse(self):
        self.grid_forget()
        Browse(container, root)
    def inventory(self):
        self.grid_forget()
        Inventory(container, root)
    def match(self):
        self.grid_forget()
        Match(container, root)
    def display_recipe(self):
        Display_recipe(container, root)  ## parameter recipe_object



class Shopping_list(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = root
        self.grid(row = 0, column = 0, sticky = 'nsew')
        label = tkinter.Label(self, text = "Shopping List")
        label.grid(sticky = 'n', pady = 40, row = 0, column = 2)


        left_frame = tkinter.Frame(self, width = 300, bg = 'purple')
        left_frame.grid(row = 1, column = 0)
        sample_list = ['coriander', 'green pepper', 'cucumber', 'strawberry', 'ground beef']
        
        for each in sample_list:
            tkinter.Label(left_frame, text = each).grid(sticky = 'w')


        right_frame = tkinter.Frame(self, width = 200, bg = 'blue')
        right_frame.grid(row = 1, column = 3)

        buttonA = tkinter.Button(right_frame, text = "Print your list.",
                                 command = lambda: Shopping_list.print()).grid(sticky = 'e')
        button1 = tkinter.Button(right_frame, text = "Narrow down your list with a kitchen inventory.",
                                 command = lambda: Shopping_list.inventory(self)).grid(sticky = 'e')
        button2 = tkinter.Button(right_frame, text = "View your menu.",
                                 command = lambda: Shopping_list.view_menu(self)).grid(sticky = 'e')



    def print():
        None
        #Shopping_list.print()
    def inventory(self):
        self.grid_forget()
        Inventory(container, root)
    def view_menu(self):
        self.grid_forget()
        View_menu(container, root)



class Display_recipe(tkinter.Frame):

    def __init__(self, parent, controller):  ## parameter recipe_object

        self = tkinter.Tk()
        self.minsize(width = 500, height = 500)
        self.title("Recipe Details")
        label = tkinter.Label(self, text = "Recipe Name")   ## recipe.name
        label.grid(sticky = 'n', pady = 40, row = 0, column = 0)


        
        left_frame = tkinter.Frame(self, bg = 'green', width = 600)
        left_frame.grid(row = 1, column = 0, sticky = 'w')

        ingredients = ["flour, 3 cups", "salt, 2 tsp", "baking soda, 2 tbsp",
                       "water, 1 cup", "yeast, 1 tbsp", "egg, 1"] ##recipe.ingredient_info
        for each in ingredients:
            tkinter.Label(left_frame, text = each).grid(sticky = 'w')

        lower_left_frame = tkinter.Frame(self, bg = 'red')
        lower_left_frame.grid(row = 2, column = 0)
        instructions = "Mix together a rough dough and let it rise. Form into balls and bake."
        ## recipe.instructions
        instruct_text = tkinter.Text(lower_left_frame, wrap = 'word', width = 50)
        instruct_text.insert('end', instructions)
        instruct_text.config(state = 'disabled')
        instruct_text.grid(sticky = 'w')
        scroll = tkinter.Scrollbar(lower_left_frame)
        scroll.grid(row = 0, column = 1)
        instruct_text.config(yscrollcommand = scroll.set)
        scroll.config(command = instruct_text.yview)


        middle_frame = tkinter.Frame(self, bg = 'blue', width = 100)
        middle_frame.grid(row = 1, column = 2, sticky = 'n')

        rating = 8  ## recipe.tasty_rating
        tkinter.Label(middle_frame, text = ("Rating:", rating, "yums")).grid(sticky = 'w')

        prep_time = "30 minutes" ##recipe.prep_time
        tkinter.Label(middle_frame, text = ("Prep Time: " + str(prep_time))).grid(sticky = 'w')

        cook_time = "60 minutes" ##recipe.cook_time
        tkinter.Label(middle_frame, text = ("Cook Time: " + str(cook_time))).grid(sticky = 'w')
        




        right_frame = tkinter.Frame(self, bg = 'yellow')
        right_frame.grid(row = 3, column = 3)


        button0 = tkinter.Button(right_frame, text = "Edit.",
                                 command = lambda: Display_recipe.edit(self)).grid()
        button1 = tkinter.Button(right_frame, text = "Print.",
                                 command = None).grid()    ## Recipe.print()
        button2 = tkinter.Button(right_frame, text = "Done.",
                                 command = lambda: Display_recipe.done(self)).grid()



    def edit(self):
        None  ## maybe this feature is super not critical 
    def done(self):
        self.destroy()



class Browse(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = root
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
        
        cookbook = ['recipe1', 'recipe2', 'recipe3', 'recipe4', 'recipe5', 'recipe6', 'recipe7', 'recipe8']
        for each in cookbook:
            check = tkinter.Checkbutton(left_frame, text = each)
            box.window_create('end', window = check)
            box.insert('end', '\n')

        ## ideally these are sorted by expanding category
            ## i guess for now let's settle for alphabetical

        right_frame = tkinter.Frame(self, bg = 'red')
        right_frame.grid(row = 1, column = 3)

        button1 = tkinter.Button(right_frame, text = "Display recipe.",
                                 command = lambda: Browse.display_recipe(self)).grid(sticky = 'e') ## parameter recipe_object
        button2 = tkinter.Button(right_frame, text = "Add these recipes to my menu.",
                                 command = lambda: Browse.view_menu(self)).grid(sticky = 'e')
        button3 = tkinter.Button(right_frame, text = "Match to these recipes.",
                                 command = lambda: Browse.match(self)).grid(sticky = 'e')
        button4 = tkinter.Button(right_frame, text = "Go back to the main menu.",
                                 command = lambda: Browse.main_menu(self)).grid(sticky = 'e')






    def display_recipe(self):
        Display_recipe(container, root)  ## parameter recipe_object
    def view_menu(self):
        self.grid_forget()
        View_menu(container, root)
    def match(self):
        self.grid_forget()
        Match(container, root)
    def main_menu(self):
        self.grid_forget()
        Main_menu(container, root)



    
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
main_menu = Main_menu(container, root)
tkinter.mainloop() 






















