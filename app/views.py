from flask import render_template
from app import app
from app.forms import VideoUploadForm
import os

@app.route('/', methods=['GET', 'POST'])
def All():
    video_tutorials = []
    letters = ["A","E","I","O","U","J","N","S","T","B","P", "tea", "coffee", "and", "or"]
    form = VideoUploadForm(letters=letters)


    if form.validate_on_submit():
        for letter in letters:
            video = getattr(form, f"video_{letter}").data
            if video:
                save_path = os.path.join(app.config["UPLOAD_FOLDER"], f"{letter}.mp4")
                video.save(save_path)

        return "Upload successful!"
    return render_template('main.html', 
                           title='survey page', 
                           form=form, 
                           letters=letters, 
                           video_tutorials=video_tutorials)


