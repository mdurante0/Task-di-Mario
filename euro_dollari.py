def converti_euro_dollari(euro, tasso_di_cambio):
    dollari = euro * tasso_di_cambio
    return f"{euro:.2f} euro corrispondono a {dollari:.2f} dollari al tasso di cambio di {tasso_di_cambio:.2f}."

euro = 50
tasso_di_cambio = 1.12
output = converti_euro_dollari(euro, tasso_di_cambio)
print(output)
