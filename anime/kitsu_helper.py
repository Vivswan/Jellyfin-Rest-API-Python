from typing import List
from urllib.error import HTTPError

import requests
from kitsu.models import Anime

from anime.kitsu_episode import KitsuEpisode

kitsu_base_url = "https://kitsu.io/api/edge/"


def get_request(url, params=None) -> object:
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise HTTPError(
            url=response.url,
            code=response.status_code,
            msg=f"<{response.reason}> :{response.text}",
            hdrs=response.headers,
            fp=None
        )
    return response.json()


def kitsu_anime(media_id) -> Anime:
    return Anime('anime', get_request(f'{kitsu_base_url}/anime/{media_id}')['data'])


def kitsu_anime_search(query, subtype=None) -> List[Anime]:
    params = {
        "filter[text]": query,
        "page[limit]": 10
    }
    if subtype is not None:
        params["filter[subtype]"] = subtype

    return [Anime('anime', data) for data in get_request(f'{kitsu_base_url}/anime', params=params)["data"]]


def kitsu_anime_inquire(query, subtype=None):
    json_list = kitsu_anime_search(query, subtype=subtype)
    print()
    for i, v in enumerate(reversed(json_list)):
        print(f"{len(json_list) - i}. {v.title} ({v.id}) - {v.subtype} - https://kitsu.io/anime/{v.id}")

    print(f"Select for '{query}'")
    print()

    answer = input("Which Series? [1]: ") or "1"
    answer = int(answer) - 1

    if answer < 0 or answer > len(json_list):
        print("skipping....")
        return False

    return json_list[answer]


def kitsu_anime_get_episodes(anime: Anime, limit: int = 10, offset: int = 0) -> List[KitsuEpisode]:
    episodes = []
    response = get_request(f'{kitsu_base_url}/episodes', params={
        'filter[mediaType]': "Anime",
        'page[limit]': limit,
        'page[offset]': offset,
        'filter[media_id]': anime.id,
        'sort': 'number'
    })
    for episode in response["data"]:
        attributes = episode['attributes']
        attributes['id'] = episode['id']
        attributes['type'] = episode['type']
        episodes.append(attributes)

    return [KitsuEpisode.from_dict(episode) for episode in episodes]


def kitsu_anime_all_episodes(anime: Anime) -> List[KitsuEpisode]:
    episodes = []
    while len(episodes) < anime.episode_count:
        episodes += kitsu_anime_get_episodes(anime, limit=10, offset=len(episodes))

    return episodes


if __name__ == '__main__':
    anime = kitsu_anime_inquire("Ansatsu Kyoushitsu", "TV")
    episode = kitsu_anime_get_episodes(anime, 1)[0]
    print(episode.canonical_title)
