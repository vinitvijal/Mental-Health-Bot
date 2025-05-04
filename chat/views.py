from openai import OpenAI
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@csrf_exempt
def chat_with_bot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')

        if 'chat_history' not in request.session:
            request.session['chat_history'] = [
                {"role": "system", "content": "You are a friendly mental health assistant. Be kind, gentle, and helpful."}
            ]

        request.session['chat_history'].append({"role": "user", "content": user_message})

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=request.session['chat_history']
            )

            reply = response.choices[0].message.content.strip()

            request.session['chat_history'].append({"role": "assistant", "content": reply})
            request.session.modified = True 

            return JsonResponse({'response': reply})
        except Exception as e:
            return JsonResponse({'response': str(e)}, status=500)


from django.shortcuts import render

def chat_page(request):
    return render(request, "chat.html")

def home(request):
    return render(request, 'home.html')