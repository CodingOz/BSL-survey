from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, BooleanField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

class VideoUploadForm(FlaskForm):
    # Consent checkboxes
    consent_video_deletion = BooleanField(
        'I understand that my videos will be used only for key-point extraction and that the original video will be permanently deleted afterwards.',
        validators=[DataRequired(message="You must agree to this consent statement.")]
    )
    
    consent_data_usage = BooleanField(
        'I consent to the key-point tracking data extracted from my video being used to train and evaluate machine-learning models.',
        validators=[DataRequired(message="You must agree to this consent statement.")]
    )
    
    submit = SubmitField("Submit")

    def __init__(self, letters=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if letters:
            for letter in letters:
                field_name = f"video_{letter}"
                # Create an unbound field
                unbound_field = FileField(
                    f"Upload video for {letter}",
                    validators=[FileAllowed(['mp4', 'mov', 'avi'])]
                )
                # Bind the field to this form instance
                bound_field = unbound_field.bind(form=self, name=field_name)
                # Set the bound field on the form
                setattr(self, field_name, bound_field)