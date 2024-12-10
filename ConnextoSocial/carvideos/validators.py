import tempfile
from django.core.exceptions import ValidationError
from moviepy.video.io.VideoFileClip import VideoFileClip


def validate_video_length(file):
    try:
        # Save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            for chunk in file.chunks():
                temp_file.write(chunk)
            temp_file_path = temp_file.name

        # Open the temporary file with MoviePy
        clip = VideoFileClip(temp_file_path)
        duration = clip.duration
        clip.close()

        # Check duration
        if duration > 120:  # Increased limit to 2 minutes (120 seconds)
            raise ValidationError("Video duration cannot exceed 2 minutes.")
    except Exception as e:
        raise ValidationError(f"Invalid video file or unsupported format: {str(e)}")
