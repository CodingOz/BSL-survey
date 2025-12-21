from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_wtf.file import FileAllowed

class VideoUploadForm(FlaskForm):
    submit = SubmitField("Submit")

    def __init__(self, *args, letters=None, **kwargs):
        # Add fields FIRST
        if letters:
            for letter in letters:
                field_name = f"video_{letter}"
                setattr(
                    self.__class__,
                    field_name,
                    FileField(
                        f"Upload video for {letter}",
                        validators=[FileAllowed(["mp4", "mov", "avi"])]
                    )
                )

        # THEN let WTForms bind request data
        super().__init__(*args, **kwargs)