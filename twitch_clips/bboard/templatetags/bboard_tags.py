from django import template
import requests
from twitch_clips.settings import TWITCH_TOKEN

register = template.Library()


@register.simple_tag()
def get_preview(url):
    client_id = 'xjma95j2bcwulwsc3dxe4bshmp7bzu'
    headers = {
        'Authorization': f'Bearer {TWITCH_TOKEN}',
        'Client-ID': client_id
    }

    id_clip = url.split('/')[-1]
    response = requests.get(f'https://api.twitch.tv/helix/clips?id={id_clip}',
                            headers=headers)
    print(response.json())
    return response.json()['data'][0]['thumbnail_url']


@register.simple_tag()
def get_count_clips(streamer):
    posts = streamer.post_set.all()
    return len(posts)
