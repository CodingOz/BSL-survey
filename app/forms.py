from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_wtf.file import FileAllowed

def make_video_upload_form(letters):
    class VideoUploadForm(FlaskForm):
        submit = SubmitField("Submit")

    for letter in letters:
        setattr(
            VideoUploadForm,
            f"video_{letter}",
            FileField(
                f"Upload video for {letter}",
                validators=[FileAllowed(["mp4", "mov", "avi"])]
            )
        )

    return VideoUploadForm
