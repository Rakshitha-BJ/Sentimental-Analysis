import re
from googleapiclient.discovery import build

def extract_video_id(url):
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex, url)
    return match.group(1) if match else None

def get_comments(api_key, video_id, max_comments=100):
    comments = []
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=100,
            textFormat="plainText"
        )
        while request and len(comments) < max_comments:
            response = request.execute()
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']
                comments.append({
                    'author': comment['authorDisplayName'],
                    'text': comment['textDisplay'],
                    'likes': comment['likeCount']
                })
            request = youtube.commentThreads().list_next(request, response)
    except Exception as e:
        return []
    return comments
