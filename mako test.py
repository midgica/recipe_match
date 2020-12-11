from mako.template import Template


template1 = Template("Your shopping list includes ${items}.")

shopping_str = "milk"
print(template1.render(items = shopping_str))

shopping_list = ["milk", "eggs", "cheese", "yogurt"]
print(template1.render(items = shopping_list))

shopping_dict = {"milk":"1 gal", "eggs":"18", "cheese":"1 lb", "yogurt":"32 oz"}
print(template1.render(items = shopping_dict))



template2 = Template(filename = "mako test template.txt")
print(template2.render(name = "Monica"))

for each in shopping_list:
    print(template2.render(name = each))



template3 = Template("Your shopping list includes ${item0}, ${item1}," + 
                     " ${item2}, and ${item3}.")
print(template3.render(item0 = shopping_list[0], item1 = shopping_list[1],
                       item2 = shopping_list[2], item3 = shopping_list[3]))



from mako.lookup import TemplateLookup
from mako import exceptions

try:
    lookup = TemplateLookup(directories = ['/recipe_match'])
    template4 = Template("""<%include file = "mako test template.txt"/>""",
                         lookup = lookup)
    print(template4.render(name = "Monica"))
except:
    print(exceptions.text_error_template().render())
