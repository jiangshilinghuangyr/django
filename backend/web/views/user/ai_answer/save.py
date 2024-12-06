from django.http import JsonResponse
from web.models.user.user import UserQuesSaved, UserDefined


def save_ai_answer(request):
    data = request.GET
    userid = data.get('userid')
    user = UserDefined.objects.get(user_id=userid)
    question = data.get('question')
    answer = data.get('answer')
    print(userid, question, answer)
    UserQuesSaved.objects.create(user=user, ques=question, ai_answer=answer)
    return JsonResponse({
        'message': 'ok',
    })