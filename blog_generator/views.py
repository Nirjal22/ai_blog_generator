import json
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from pytube import YouTube
import assemblyai as aai

@login_required
def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        usernameInput = request.POST['username']
        passwordInput = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=usernameInput, password=passwordInput)
        if user is not None:
            # Log the user in
            login(request, user)
            return redirect('/')  # Redirect to the home page
        else:
            # Handle invalid credentials
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        # Match the 'name' attributes from the HTML form
        usernameInput = request.POST['username']  # Use the corrected field name
        passwordInput = request.POST['password']

        # Check if both fields are filled
        if usernameInput and passwordInput:
            try:
                # Create the user
                user = User.objects.create_user(username=usernameInput, password=passwordInput)
                user.save()
                # Log the user in and redirect to the signout page
                login(request, user)
                return redirect('/')  # Ensure 'signout' is defined in urls.py
            except Exception as e:
                # Capture and display any errors during user creation
                error_message = f"Error creating the account: {str(e)}"
                return render(request, 'register.html', {'error_message': error_message})
        else:
            # If fields are missing, return an error message
            error_message = 'Enter valid input'
            return render(request, 'register.html', {'error_message': error_message})

    # Render the registration form if the request is GET
    return render(request, 'register.html')

def signout(request):
    logout(request)
    return redirect('/')  # Redirect to home page after logout


def generate_blog(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # Parse the JSON body
        link = data.get('link')  # Extract the YouTube link

        if not link:
            return JsonResponse({'success': False, 'message': 'No link provided.'}, status=400)

        try:
            youtube_object = YouTube(link)
            audio_stream = youtube_object.streams.filter(only_audio=True).first()
            if not audio_stream:
                return JsonResponse({'success': False, 'message': 'No audio streams available.'}, status=400)

            file_path = audio_stream.download(output_path="./Downloads", filename="audio.mp4")
            return JsonResponse({'success': True, 'file_path': file_path}, status=200)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)


# def transcribe_audio(audio_path):
#     aai.settings.api_key = "b69dd0549a064009946dd88ba6e923ea" 

#     transcriber = aai.Transcriber()

#     # You can use a local filepath:
#     # audio_file = "./example.mp3"

#     # Or use a publicly-accessible URL:
#     audio_file = (
#         "https://assembly.ai/sports_injuries.mp3"
#     )

#     config = aai.TranscriptionConfig(speaker_labels=True)

#     transcript = transcriber.transcribe(audio_file, config)

#     if transcript.status == aai.TranscriptStatus.error:
#         print(f"Transcription failed: {transcript.error}")
#         exit(1)

#     print(transcript.text)

#     for utterance in transcript.utterances:
#         print(f"Speaker {utterance.speaker}: {utterance.text}")

# def generate_blog(request):
#     link = request.GET.get('link')
#     if not link:
#         return JsonResponse({"error": "No link provided."}, status=400)

#     # Step 1: Download audio
#     audio_path, error = download_audio(link)
#     if error:
#         return JsonResponse({"error": f"Audio download failed: {error}"}, status=400)

#     # Step 2: Transcribe audio
#     transcription, error = transcribe_audio(audio_path)
#     if error:
#         return JsonResponse({"error": f"Transcription failed: {error}"}, status=400)

#     # Clean up the downloaded file
#     if os.path.exists(audio_path):
#         os.remove(audio_path)

#     return JsonResponse({"blog": transcription})
