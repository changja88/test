sale = 289000
fee = 16588
hitomi = 220000


def run():
    sale_tax1 = (sale / 11) * 10
    sale_tax2 = (sale / 11)

    fee_tax1 = (fee / 11) * 10
    fee_tax2 = (fee / 11)

    hitomi_tax1 = (hitomi / 11) * 10
    hitomi_tax2 = (hitomi / 11)

    margin = round(sale - fee - hitomi)
    tax1 = round(sale_tax1 - fee_tax1 - hitomi_tax1)
    tax2 = round(sale_tax2 - fee_tax2 - hitomi_tax2)

    print(margin)
    print(tax1)
    print(tax2)

    total = margin - (tax1*0.06) - tax2
    print(total)


run()
