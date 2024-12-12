import requests

from twitch_clips.settings import TWITCH_TOKEN


def get_data_clip(url):
    client_id = 'xjma95j2bcwulwsc3dxe4bshmp7bzu'
    headers = {
        'Authorization': f'Bearer {TWITCH_TOKEN}',
        'Client-ID': client_id
    }

    id_clip = url.split('/')[-1]
    response = requests.get(f'https://api.twitch.tv/helix/clips?id={id_clip}',
                            headers=headers)
    data = response.json()['data'][0]
    print(data)
    slug = data['id']
    title = data['title']
    url = data['url']
    image = data['thumbnail_url']
    embed = data['embed_url']
    streamer_name = data['broadcaster_name']
    streamer_id = data['broadcaster_id']

    return slug, title, url, image, embed, streamer_name, streamer_id


def get_data_user(user_id):
    client_id = 'xjma95j2bcwulwsc3dxe4bshmp7bzu'
    headers = {
        'Authorization': f'Bearer {TWITCH_TOKEN}',
        'Client-ID': client_id
    }

    response = requests.get(f'https://api.twitch.tv/helix/users?id={user_id}',
                            headers=headers)
    data = response.json()['data'][0]
    logo = data['profile_image_url']

    return logo
