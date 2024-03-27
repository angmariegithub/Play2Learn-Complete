import json
from leaderboard.models import Leaderboard
from .models import Category
from django.http import JsonResponse


def SaveData(request):
    username = request.user # The logged-in user (or AnonymousUser).
    data = json.loads(request.body) # Data from the JavaScript.

    # Set simple variables.
    fs = data['score'] 
    cat = data['operation']
    print('made it here')
    if username.is_anonymous: # User not logged in. Can't vote.
        msg = 'Sorry, you have to be logged in to track games'
        response = {'msg':msg}
        return JsonResponse(response)
    else:
        category = Category.objects.get(category=cat)
        category_id = category.id
        game_data = Leaderboard(username=username, final_score=fs, 
                                category_id=category_id)
        game_data.save()
    print('made it here')
    



    


