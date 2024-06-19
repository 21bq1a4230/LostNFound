from .models import LostItems,FoundItems


def SearchItems(data):
    item = None
    type = data.split('_')[0]
    if type == 'lost':
        item = LostItems.objects.get(submissionID = data)
        print(item)
    return True