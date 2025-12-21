from flask import render_template, redirect, request
from app import app
from app.forms import make_video_upload_form
import os
import uuid
from app.r2 import upload_video


submission_id = str(uuid.uuid4())

@app.route('/', methods=['GET', 'POST'])
def All():
    video_tutorials = {"A": "https://www.youtube-nocookie.com/embed/mesL1xcYnuE",
                       "E": "https://www.youtube-nocookie.com/embed/mesL1xcYnuE",
                       "I": "https://www.youtube-nocookie.com/embed/mesL1xcYnuE",
                       "O": "https://www.youtube-nocookie.com/embed/mesL1xcYnuE",
                       "U": "https://www.youtube-nocookie.com/embed/mesL1xcYnuE",
                       "J": "https://www.youtube-nocookie.com/embed/mesL1xcYnuE",
                       "N": "https://www.youtube-nocookie.com/embed/mesL1xcYnuE",
                       "S": "https://www.youtube-nocookie.com/embed/mesL1xcYnuE",
                       "T": "https://www.youtube-nocookie.com/embed/mesL1xcYnuE",
                       "B": "https://www.youtube-nocookie.com/embed/mesL1xcYnuE",
                       "P": "https://www.youtube-nocookie.com/embed/mesL1xcYnuE",
                       "tea": "https://www.youtube-nocookie.com/embed/mesL1xcYnuE",
                       "coffee": "https://www.youtube-nocookie.com/embed/mesL1xcYnuE",
                       "and": "https://www.youtube-nocookie.com/embed/mesL1xcYnuE",
                       "or": "https://www.youtube-nocookie.com/embed/mesL1xcYnuE"
    }
    letters = ["A","E","I","O","U","J","N","S","T","B","P", "tea", "coffee", "and", "or"]
    VideoUploadForm = make_video_upload_form(letters)
    form = VideoUploadForm()


    if form.validate_on_submit():
        for letter in letters:
            video = getattr(form, f"video_{letter}").data
            if video:
                object_key = f"{uuid.uuid4()}/{letter}.mp4"
                upload_video(video, object_key)

        return redirect('/success')
    return render_template('main.html', 
                           title='survey page', 
                           form=form, 
                           letters=letters, 
                           video_tutorials=video_tutorials)

# page for successful submission
@app.route('/success')
def success():
    return render_template('success.html', title='Success')

