from pytube import YouTube


def get_video(obj, user_id):
    obj.streams.filter(progressive=True,
                       file_extension="mp4"
                       ).order_by('resolution').desc().first().download(
        filename=f"video_{user_id}.mp4"
    )