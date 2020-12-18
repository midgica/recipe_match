

def ingred_list(recipe):
    ingred_list = {}
    ingred_list.append(recipe.ingred1)
    ingred_list.append(recipe.ingred2)
    ingred_list.append(recipe.ingred3)
    if recipe.ingred4:
        ingred_list.append(recipe.ingred4)
    if recipe.ingred5:
        ingred_list.append(recipe.ingred5)
    if recipe.ingred6:
        ingred_list.append(recipe.ingred6)
    if recipe.ingred7:
        ingred_list.append(recipe.ingred7)
    if recipe.ingred8:
        ingred_list.append(recipe.ingred8)
    if recipe.ingred9:
        ingred_list.append(recipe.ingred9)
    if recipe.ingred10:
        ingred_list.append(recipe.ingred10)
    if recipe.ingred11:
        ingred_list.append(recipe.ingred11)
    if recipe.ingred12:
        ingred_list.append(recipe.ingred12)
    if recipe.ingred13:
        ingred_list.append(recipe.ingred13)
    if recipe.ingred14:
        ingred_list.append(recipe.ingred14)
    if recipe.ingred15:
        ingred_list.append(recipe.ingred15)
    if recipe.ingred16:
        ingred_list.append(recipe.ingred16)
    if recipe.ingred17:
        ingred_list.append(recipe.ingred17)
    if recipe.ingred18:
        ingred_list.append(recipe.ingred18)
    if recipe.ingred19:
        ingred_list.append(recipe.ingred19)
    if recipe.ingred20:
        ingred_list.append(recipe.ingred20)
    return ingred_list


def ingred_dict(recipe, ingred_list):
    ingred_dict = {}
    counter = 0
    for ing in ingred_list:
        ingred_dict[ing] = recipe.amt[counter]
