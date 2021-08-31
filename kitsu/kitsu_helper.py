import json
import os
from pathlib import Path
from typing import List, Union, Dict
from urllib.error import HTTPError

import requests

from kitsu.kitsu_anime import Anime
from kitsu.kitsu_episode import KitsuEpisode
from util.path_functions import remove_illegal_char

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
    return Anime(get_request(f'{kitsu_base_url}/kitsu/{media_id}')['data'])


def kitsu_anime_search(query, subtype=None, slug=False) -> List[Anime]:
    params = {
        "page[limit]": 10
    }
    if subtype is not None:
        params["filter[subtype]"] = subtype
    if slug:
        params["filter[slug]"] = query
    else:
        params["filter[text]"] = query

    return [Anime(data) for data in get_request(f'{kitsu_base_url}/kitsu', params=params)["data"]]


def kitsu_anime_inquire(query, subtype=None, slug=False) -> Union[None, Anime]:
    json_list = kitsu_anime_search(query, subtype=subtype, slug=slug)
    if len(json_list) == 0:
        return None

    print()
    for i, v in enumerate(reversed(json_list)):
        print(f"{len(json_list) - i}. {v.title} ({v.id}) - {v.subtype} - https://kitsu.io/anime/{v.id}")

    print(f"Select for '{query}'")
    print()

    answer = input("Which Series? [1]: ") or "1"
    if answer.startswith("*"):
        answer = answer[1:]
        return kitsu_anime_inquire(answer, subtype=subtype, slug=True)
    answer = int(answer) - 1

    if answer < 0 or answer > len(json_list):
        print("skipping....")
        return None

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


def kitsu_anime_get_all_episodes(anime: Anime) -> List[KitsuEpisode]:
    episodes = []
    if anime.episode_count is None:
        anime.episode_count = get_request(f'{kitsu_base_url}/episodes', params={
            'filter[mediaType]': "Anime",
            'page[limit]': 10,
            'page[offset]': 0,
            'filter[media_id]': anime.id,
            'sort': 'number'
        })["meta"]["count"]
        pass
    while len(episodes) < anime.episode_count:
        episodes += kitsu_anime_get_episodes(anime, limit=10, offset=len(episodes))

    return episodes


class KitsuData:
    anime: Union[None, Anime]
    episodes: Union[None, List[KitsuEpisode]]
    parameters: Dict
    save_folder: Union[None, Path]

    def __init__(self, anime=None, episodes=None, parameters=None, save_folder=None):
        if episodes is None:
            episodes = []
        if parameters is None:
            parameters = {}
        self.anime = anime
        self.episodes = episodes
        self.parameters = parameters
        self.save_folder = save_folder if save_folder is not None else Path(__file__).parent.parent.joinpath(
            "data_kitsu")
        if isinstance(self.save_folder, str):
            self.save_folder = Path(self.save_folder)
        if not self.save_folder.exists():
            os.mkdir(self.save_folder)

    def set_anime_by_id(self, media_id):
        if self.load_by_id(media_id) is False:
            self.anime = kitsu_anime(media_id)
        return self

    def set_anime_by_inquire(self, query, subtype=None):
        self.anime = kitsu_anime_inquire(query, subtype)
        return self

    def fill_episodes(self):
        if self.anime is not None:
            if self.load_by_id(self.anime.id) is False:
                print(f"Downloading episodes {self.anime.id} - {self.anime.title}...")
                self.episodes = kitsu_anime_get_all_episodes(self.anime)
            self.save()
        return self

    def set_parameter(self, name, value):
        self.parameters[name] = value
        return self

    def to_json(self):
        result = {
            "kitsu": None,
            "episodes": [],
            "parameters": self.parameters
        }
        if self.anime is not None:
            result["kitsu"] = self.anime.to_json()

        if self.episodes is not None:
            for episode in self.episodes:
                result["episodes"].append(episode.to_dict())
        return result

    def save(self, filepath=None):
        if filepath is None:
            filepath = self.save_folder.joinpath(f"{self.anime.id} - {remove_illegal_char(self.anime.title)}.json")

        with open(filepath, "w") as file:
            file.write(json.dumps(self.to_json(), indent=4))

        return self

    def load(self, filepath):
        with open(filepath, "r") as file:
            json_data = json.loads(file.read())

            self.anime = Anime(json_data["kitsu"])
            self.episodes = []
            for episode in json_data["episodes"]:
                self.episodes.append(KitsuEpisode.from_dict(episode))
            self.parameters = json_data["parameters"]

        return self

    def load_by_id(self, media_id):
        for filename in os.listdir(self.save_folder):
            if filename.startswith(f"{media_id} -"):
                return self.load(self.save_folder.joinpath(filename))
        return False


def inquire_kitsu_data(query, subtype=None):
    return KitsuData().set_anime_by_inquire(query, subtype).fill_episodes()


def inquire_kitsu_data_by_id(media_id):
    return KitsuData().set_anime_by_id(media_id).fill_episodes()


if __name__ == '__main__':
    data = kitsu_anime_inquire("id-invaded")
    print(data)
