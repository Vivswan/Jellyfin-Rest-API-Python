from jellyfin_kitsu import *

jellyfin = Jellyfin(SERVER_ADDRESS, API_KEY)
TAG = "vsapi"


def set_all_episode(user, parent, show_name):
    shows = get_all_items(user, parent)
    show = None
    for i in shows:
        if i.name.lower().replace("(dub)", "") == show_name.lower():
            show = i
            print(show.name)
            break

    if show is None:
        print("Show not found")
        return

    seasons = get_all_items(user, show)
    for season in seasons:
        if season.index_number == 1:
            main_season = season
            break

    for season in seasons:
        # if TAG not in season.tags or "Kitsu" not in season.provider_ids:
        #     continue
        # kitsu_data = inquire_kitsu_data_by_id(season.provider_ids["Kitsu"])
        episodes = get_all_items(user, season)

        for episode in episodes:
            name = Path(episode.path).name.split(".")[0]
            new_episode_info = BaseItemDto.from_dict(episode.to_dict())
            new_episode_info.parent_index_number = 1
            new_episode_info.parent_id = main_season.id
            new_episode_info.index_number = int(re.findall("[0-9]+", name)[-1])
            print(name)
            jellyfin.items.update_item(episode.id, new_episode_info)

    # for season in seasons:
    #     if season.index_number != 1:
    #         jellyfin.items.delete_items(season.id)
    #         print(f"Deleting season: {season.name}")


if __name__ == '__main__':
    jellyfin_user = get_user("jellyfin")
    media_folder = "Anime (Dub)"
    set_all_episode(jellyfin_user, get_media_folder(media_folder), "Bleach")
    set_all_episode(jellyfin_user, get_media_folder(media_folder), "Black Clover")
    set_all_episode(jellyfin_user, get_media_folder(media_folder), "Fairy Tail")
    # set_all_episode(jellyfin_user, get_media_folder(media_folder), "")
    # set_all_episode(jellyfin_user, get_media_folder(media_folder), "")
    # set_all_episode(jellyfin_user, get_media_folder(media_folder), "")
    # set_all_episode(jellyfin_user, get_media_folder(media_folder), "")
