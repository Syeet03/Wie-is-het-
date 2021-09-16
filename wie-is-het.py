# Lucas van Pelt, 99057303, Wie is het?

print('WORK IN PROGRESS!')
print('- - - - - - - - -')
print('Geef alleen antwoord met Jongen, Meisje en Ja of Nee!')
print('-----------------------------------------------------')
print('Kies je type:')
print('- - - - - - - - - - - ')
print('Jongen, bril, blond haar, blauw shirt')
print('Jongen, bril, blond haar, rood shirt' )
print('Jongen, bril, zwart haar, blauw shirt')
print('Jongen, bril, zwart haar, rood shirt' )
print('Jongen,       blond haar, blauw shirt')
print('Jongen,       blond haar, rood shirt' )
print('Jongen,       zwart haar, blauw shirt')
print('Jongen,       zwart haar, rood shirt ')
print('Meisje, bril, blond haar, blauw shirt')
print('Meisje, bril, blond haar, rood shirt ')
print('Meisje, bril, zwart haar, blauw shirt')
print('Meisje, bril, zwart haar, blauw shirt')
print('Meisje,       blond haar, blauw shirt')
print('Meisje,       blond haar, rood shirt ')
print('Meisje,       zwart haar, blauw shirt')
print('Meisje,       zwart haar, rood shirt ')

Geslacht = input('Ben jij een jongen of een meisje? ')

if Geslacht == "Jongen":

    BrilJongen = input('Draag je een bril? ')
    if BrilJongen == "Ja":
        BlondHaarJongen = input('Heb je blond haar? ')
        if BlondHaarJongen == "Ja":
            BlauwShirtJongen = input('Heb je een blauw shirt? ')
            if BlauwShirtJongen == "Ja":
                    print('Jij bent een jongen met een bril, blond haar met een blauw shirt')
            else: RoodShirtJongen = input('Heb je en rood shirt? ')
            if RoodShirtJongen == ("Ja"):
                print('Jij bent een jongen met een bril, blond haar met een rood shirt')

        else:
            ZwartHaarJongen = input('Heb je zwart haar? ')
            if ZwartHaarJongen == "Ja":
                BlauwShirtJongen = input('Heb je een blauw shirt? ')
                if BlauwShirtJongen == "Ja":
                    print('Jij bent een jongen met een bril, zwart haar met een blauw shirt')
                else: RoodShirtJongen = input('Heb je een rood shirt? ')
            if RoodShirtJongen == ("Ja"):
                print('Jij bent een jongen met een bril, zwart haar met een rood shirt')

    else:
        BlondHaarJongen = input('Heb je blond haar? ')
        if BlondHaarJongen == "Ja":
            BlauwShirtJongen = input('Heb je een blauw shirt? ')
            if BlauwShirtJongen == "Ja":
                    print('Jij bent een jongen zonder bril, blond haar met een blauw shirt')
            else: 
                RoodShirtJongen = input('Heb je een rood shirt? ')
                if RoodShirtJongen == ("Ja"):
                    print('Jij bent een jongen met een bril, blond haar met een rood shirt')
        else:
            ZwartHaarJongen = input('Heb je zwart haar? ')
            if ZwartHaarJongen == "Ja":
                BlauwShirtJongen = input('Heb je een blauw shirt? ')
                if BlauwShirtJongen == "Ja":
                    print('Jij bent een jongen zonder bril, zwart haar met een blauw shirt')
                else: RoodShirtJongen = input('Heb je een rood shirt? ')
            if RoodShirtJongen == ("Ja"):
                print('Jij bent een jongen met een bril, zwart haar met een rood shirt')

else:
    BrilMeisje = input('Draag je een bril? ')
    if BrilMeisje == "Ja":
        BlondHaarMeisje = input('Heb je blond haar? ')
        if BlondHaarMeisje == "Ja":
            BlauwShirtMeisje = input('Heb je een blauw shirt? ')
            if BlauwShirtMeisje == "Ja":
                    print('Jij bent een meisje met een bril, blond haar met een blauw shirt')
            else: RoodShirtMeisje = input('Heb je een rood shirt? ')
            if RoodShirtMeisje == ("Ja"):
                print('Jij bent een meisje met een bril, blond haar met een rood shirt')
        else:
            ZwartHaarMeisje = input('Heb je zwart haar? ')
            if ZwartHaarMeisje == "Ja":
                BlauwShirtMeisje = input('Heb je een blauw shirt? ')
                if BlauwShirtMeisje == "Ja":
                    print('Jij bent een meisje met een bril, zwart haar met een blauw shirt')
                else: RoodShirtMeisje = input('Heb je een rood shirt? ')
            if RoodShirtMeisje == ("Ja"):
                print('Jij bent een meisje met een bril, zwart haar met een rood shirt')

    else:
        BlondHaarMeisje = input('Heb je blond haar? ')
        if BlondHaarMeisje == "Ja":
            BlauwShirtMeisje = input('Heb je een blauw shirt? ')
            if BlauwShirtMeisje == "Ja":
                    print('Jij bent een meisje zonder bril, blond haar met een blauw shirt')
            else: 
                RoodShirtMeisje = input('Heb je een rood shirt? ')
                if RoodShirtMeisje == ("Ja"):
                    print('Jij bent een meisje zonder bril, zwart haar met een rood shirt')
        else:
            ZwartHaarMeisje = input('Heb je zwart haar? ')
            if ZwartHaarMeisje == "Ja":
                BlauwShirtMeisje = input('Heb je een blauw shirt? ')
                if BlauwShirtMeisje == "Ja":
                    print('Jij bent een zonder bril, zwart haar met een blauw shirt')
                else: RoodShirtMeisje = input('Heb je een rood shirt? ')
            if RoodShirtMeisje == ("Ja"):
                print('Jij bent een meisje met een bril, zwart haar met een rood shirt')