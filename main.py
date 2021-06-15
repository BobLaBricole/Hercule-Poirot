from model import locusIn

class Main:
    listLocusIn = []

    for i in range(3):
        locus = locusIn.LocusIn(input('Marqueur ? : '), input('valeur Allele 1 : '), input('valeur Allele 2 : '))
        listLocusIn.append(locus)

    print(listLocusIn)
