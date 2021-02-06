from decimal import Decimal


def unconvert_fractions(amt_str):
    #amt_str = (str(whole) + " " + str(frac))
    amt_str = str(amt_str)
    amt_list = amt_str.split(" ")

    if len(amt_list) == 2:
    #start with first thing in list
        whole = Decimal(amt_list[0])
        frac = amt_list[1]
        frac_list = frac.split("/")
        frac = (Decimal(frac_list[0]) / Decimal(frac_list[1]))
        amount = (whole + frac)

    elif len(amt_list) == 1:
        #find if it's a whole or frac
        if '/' in amt_list[0]:
            frac_list = amt_list[0].split("/")
            amount = (Decimal(frac_list[0]) / Decimal(frac_list[1]))
        else:
            print(amt_list) #debug
            amount = Decimal(amt_list[0])

    else:
##        raise Exception("amt_list didn't have 1 or 2 values")
        amount = amt_list


    return amount
