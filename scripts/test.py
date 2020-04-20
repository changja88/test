from margin.models import Margin


def run():
    a = Margin.objects.all()

    total = 0
    for abc in a:
        total+=abc.margin

    print(total)