import tempfile
from django.core.exceptions import ValidationError
from moviepy.video.io.VideoFileClip import VideoFileClip


def validate_video_length(file):
    try:
        # Save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(suffix='.mp4', delete=False) as temp_file:
            for chunk in file.chunks():
                temp_file.write(chunk)
            temp_file_path = temp_file.name

        # Open the temporary file with MoviePy
        clip = VideoFileClip(temp_file_path)
        duration = clip.duration
        clip.close()

        # Check duration
        if duration > 60:
            raise ValidationError("Video duration cannot exceed 1 minute.")
    except Exception as e:
        raise ValidationError(f"Invalid video file: {str(e)}")
