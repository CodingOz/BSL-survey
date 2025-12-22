from flask import render_template, redirect, request
from app import app
from app.forms import make_video_upload_form
import os
import uuid
from app.r2 import upload_video


submission_id = str(uuid.uuid4())

@app.route('/', methods=['GET', 'POST'])
def All():
    video_tutorials = {"A": "https://www.youtube-nocookie.com/embed/9yCOlhrrzsw",
                       "E": "https://www.youtube-nocookie.com/embed/QseQeoaF2Mo",
                       "I": "https://www.youtube-nocookie.com/embed/z8Itt63yfzk",
                       "O": "https://www.youtube-nocookie.com/embed/1OlieaP6YV0",
                       "U": "https://www.youtube-nocookie.com/embed/VDM_Aq-tb8s",
                       "J": "https://www.youtube-nocookie.com/embed/vnw1VnjA0tA",
                       "N": "https://www.youtube-nocookie.com/embed/iajFQ6DNsLE",
                       "S": "https://www.youtube-nocookie.com/embed/D-oT_KzUR4w",
                       "T": "https://www.youtube-nocookie.com/embed/KX0WranAw7k",
                       "B": "https://www.youtube-nocookie.com/embed/kihkw6yWxJw",
                       "P": "https://www.youtube-nocookie.com/embed/KlqyJ8DV3Hs",
                       "tea": "https://www.youtube-nocookie.com/embed/6iNUX3kTsTg",
                       "coffee": "https://www.youtube-nocookie.com/embed/NqsPtlg3lG4",
                       "and": "https://www.youtube-nocookie.com/embed/gQvE_kfjxpA",
                       "or": "https://www.youtube-nocookie.com/embed/HrpHw4SUq-o"
    }
    letters = ["A","E","I","O","U","J","N","S","T","B","P", "tea", "coffee", "and", "or"]
    VideoUploadForm = make_video_upload_form(letters)
    form = VideoUploadForm()


    if form.validate_on_submit():
        submission_id = str(uuid.uuid4())

        for letter in letters:
            video = getattr(form, f"video_{letter}").data
            if video:
                object_key = f"submissions/{submission_id}/{letter}.mp4"
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

