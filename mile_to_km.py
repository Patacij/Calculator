convert = True
while convert:

    x_km = float(raw_input("Vnesi kilometre za pretvorbo v milje:" ) )
    p = 1.609
    x_mil = x_km / p

    # .format ti pove da pretvoris vrednost v string. najprej dolocis prvo spremenljivko {0} in potem drugo {1} v odgovoru
    print("{0} km je {1} mil".format(x_km, x_mil))

    answer = raw_input(("Vtipkaj 'da' za novo pretvorbo in 'ne' za zakljucek"))

    if answer == 'da':
        continue
    elif answer =='ne':
        convert = False
    else:
        raise ValueError ("Go F...CK yourself you sick bastard!!!")