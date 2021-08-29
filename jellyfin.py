import re
from pathlib import Path
from typing import List

import dateutil.parser

from _config import SERVER_ADDRESS, API_KEY
from anime.kitsu_helper import inquire_kitsu_data, inquire_kitsu_data_by_id
from data_classes import BaseItemDto, UserDto, ReportIncludeItemTypes, SortOrder, MetadataField
from query_classes import Jellyfin

jellyfin = Jellyfin(SERVER_ADDRESS, API_KEY)
TAG = "vsapi"


def get_media_folder(name) -> BaseItemDto:
    for media_folder in jellyfin.library.get_media_folders().items:
        if media_folder.name == name:
            return media_folder

    raise Exception(f'Media Folder Not Found: "{name}"')


def get_user(username) -> UserDto:
    global jellyfin
    for user in jellyfin.users.get_users(is_disabled=False):
        if user.name == username:
            return user
    raise Exception(f'User Not Found: "{username}"')


def list_missing_episodes(user, parent, special=False):
    all_items = jellyfin.users.get_items_by_user_id(
        sort_by=["SeriesSortName", "SortName"],
        sort_order=SortOrder.ASCENDING,
        include_item_types=[ReportIncludeItemTypes.EPISODE],
        recursive=True,
        is_missing=True,
        is_unaired=False,
        user_id=user.id,
        parent_id=parent.id,
    )
    for item in all_items.items:
        if not special and "special" in item.season_name.lower():
            continue
        print(f"{item.series_name} {item.season_name} Episode {item.index_number} - {item.name}")


def get_all_items(user, parent):
    result: List[BaseItemDto] = []
    items = jellyfin.users.get_items_by_user_id(
        user_id=user.id,
        parent_id=parent.id,
        sort_by=["SortName"],
        enable_images=False,
        enable_user_data=False,
        enable_image_types=False,
        enable_total_record_count=False
    ).items
    for i in items:
        try:
            result.append(jellyfin.users.get_item(user_id=user.id, item_id=i.id))
        except:
            pass

    return result


def set_kitsu_season_data(user, parent, inquire=True, force=False):
    shows = get_all_items(user, parent)
    for show in shows:
        seasons = get_all_items(user, show)
        for season in seasons:
            if TAG in season.tags and "Kitsu" in season.provider_ids:
                if force:
                    kitsu_data = inquire_kitsu_data_by_id(season.provider_ids["Kitsu"])
                else:
                    continue
            elif inquire is True:
                if season.location_type == 'FileSystem':
                    kitsu_data = inquire_kitsu_data(Path(season.path).name, "TV")
                else:
                    kitsu_data = inquire_kitsu_data(Path(show.path).name, "TV")
            else:
                continue

            if kitsu_data.anime is None:
                continue
            new_season_info = BaseItemDto.from_dict(season.to_dict())
            new_season_info.name = kitsu_data.anime.title
            new_season_info.overview = kitsu_data.anime.synopsis
            new_season_info.index_number = None
            new_season_info.provider_ids["Kitsu"] = kitsu_data.anime.id
            if kitsu_data.anime.status == "finished":
                new_season_info.status = "Ended"
            if kitsu_data.anime.status == "current":
                new_season_info.status = 'Continuing'
            new_season_info.official_rating = kitsu_data.anime.age_rating
            new_season_info.community_rating = float(kitsu_data.anime.average_rating) / 10
            if TAG not in new_season_info.tags:
                new_season_info.tags.append(TAG)
            new_season_info.tags = list(set(new_season_info.tags))
            new_season_info.locked_fields = [
                MetadataField.NAME,
                MetadataField.OVERVIEW,
                MetadataField.OFFICIAL_RATING,
                MetadataField.TAGS
            ]
            new_season_info.production_year = int(kitsu_data.anime.started_at.split("-")[0])
            new_season_info.start_date = dateutil.parser.parse(kitsu_data.anime.started_at)
            new_season_info.end_date = dateutil.parser.parse(kitsu_data.anime.ended_at)

            # new_season_info.lock_data = True
            jellyfin.items.update_item(season.id, new_season_info)


def set_kitsu_season_index(user, parent):
    shows = get_all_items(user, parent)
    for show in shows:
        seasons = get_all_items(user, show)
        for season in seasons:
            if season.production_year is None:
                season.production_year = 9999999

        sorted_seasons = sorted(seasons, key=lambda k: k.production_year)

        for index, season in enumerate(sorted_seasons):
            if season.production_year == 9999999:
                continue
            new_season_info = BaseItemDto.from_dict(season.to_dict())
            new_season_info.index_number = index + 1
            print(f"{season.name} -- {new_season_info.index_number}")
            jellyfin.items.update_item(season.id, new_season_info)


def set_kitsu_episode_data(user, parent, force=False):
    shows = get_all_items(user, parent)
    for show in shows:
        seasons = get_all_items(user, show)
        for season in seasons:
            if TAG not in season.tags or "Kitsu" not in season.provider_ids:
                continue
            kitsu_data = inquire_kitsu_data_by_id(season.provider_ids["Kitsu"])
            episodes = get_all_items(user, season)
            for episode in episodes:
                if TAG in episode.tags and "Kitsu" in episode.provider_ids and not force:
                    continue

                name = Path(episode.path).name.split(".")[0]
                episode_number = int(re.findall("[0-9]+", name)[-1])

                kitsu_episode = None
                if kitsu_data.episodes[episode_number - 1] == episode_number:
                    kitsu_episode = kitsu_data.episodes[episode_number - 1]
                else:
                    for ke in kitsu_data.episodes:
                        if ke.number == episode_number:
                            kitsu_episode = ke
                            break
                if kitsu_episode is None:
                    raise Exception(f"Episode not found: {name}")

                new_episode_info = BaseItemDto.from_dict(episode.to_dict())
                new_episode_info.name = kitsu_episode.canonical_title if kitsu_episode.canonical_title is not None else name
                new_episode_info.overview = kitsu_episode.synopsis if kitsu_episode.synopsis != "" else None
                new_episode_info.index_number = kitsu_episode.number
                new_episode_info.provider_ids = {"Kitsu": kitsu_episode.id}
                if TAG not in new_episode_info.tags:
                    new_episode_info.tags.append(TAG)
                new_episode_info.tags = list(set(new_episode_info.tags))
                new_episode_info.locked_fields = [
                    MetadataField.NAME,
                    MetadataField.OVERVIEW,
                    MetadataField.TAGS
                ]
                new_episode_info.production_year = int(kitsu_episode.created_at.split("-")[0])
                new_episode_info.premiere_date = dateutil.parser.parse(kitsu_episode.created_at)

                # new_season_info.lock_data = True
                print(f"{show.name} -- {season.name} -- {new_episode_info.name}")
                jellyfin.items.update_item(episode.id, new_episode_info)



if __name__ == '__main__':
    jellyfin_user = get_user("jellyfin")
    # list_missing_episodes(jellyfin_user, get_media_folder("TV Shows"))
    set_kitsu_season_data(jellyfin_user, get_media_folder("Anime"), inquire=True)
    set_kitsu_season_index(jellyfin_user, get_media_folder("Anime"))
    set_kitsu_episode_data(jellyfin_user, get_media_folder("Anime"))
