import fractions

def convert_fractions(amount):

    if int(amount) == amount: #already an integer
        amt_str = str(int(amount))
        return amt_str

    else:
        if amount < 1: #a fraction less than 1
            frac = fractions.Fraction(amount).limit_denominator(8)
            amt_str = str(frac)
            return amt_str
        
        else: #a fraction over 1, i.e. a mixed number
            whole = int(amount)
            portion = amount - whole
            frac = fractions.Fraction(portion).limit_denominator(8)
            if int(frac) == frac:
                amt_str = str(whole + frac)
            else:
                amt_str = (str(whole) + " " + str(frac))
            return amt_str
