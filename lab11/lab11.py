postalProvince = {'A':'Newfoundland',
                  'B':'Nova Scotia',
                  'C':'Prince Edward Island',
                  'E':'New Brunswick',
                  'H':'Quebec',
                  'G':'Quebec',
                  'J':'Quebec',
                  'K':'Ontario',
                  'L':'Ontario',
                  'M':'Ontario',
                  'N':'Ontario',
                  'P':'Ontario',
                  'R':'Manitoba',
                  'S':'Saskatchewan',
                  'T':'Alberta',
                  'V':'British Columbia',
                  'X':'Nunavut or Northwest Territories',
                  'Y': 'Yukon'}

def readProgram(post):
    users = input("Enter a Canadian postalCode: ")
    if users[0] in postalProvince:
        if users[1] == "0":
            address = 'rural address'
        else:
            address = 'urban address'
        print('The postalcode in a', address, "in", postalProvince[users[0]])
    else:
        print ("What's a pity! Your postalcode does not exist. Let's try another one")


readProgram(postalProvince);
