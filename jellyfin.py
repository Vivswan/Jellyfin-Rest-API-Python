from pathlib import Path

from _config import SERVER_ADDRESS, API_KEY
from data_classes import BaseItemDto
from data_classes.user_dto_class import UserDtoClass
from query_classes import Jellyfin

jellyfin = Jellyfin(SERVER_ADDRESS, API_KEY)


def get_media_folder(name) -> BaseItemDto:
    for media_folder in jellyfin.library.get_media_folders().items:
        if media_folder.name == name:
            return media_folder

    raise Exception(f'Media Folder Not Found: "{name}"')


def get_user(username) -> UserDtoClass:
    global jellyfin
    for user in jellyfin.users.get_users():
        if user.name == username:
            return user
    raise Exception(f'User Not Found: "{username}"')


def list_missing_episodes(user, parent, special=False):
    # http://localhost:8096/jellyfin/Users/44bfc03c10894f8383982a4651c45010/Items?SortBy=SeriesSortName%2CSortName&SortOrder=Ascending&IncludeItemTypes=Episode&Recursive=true&Fields=PrimaryImageAspectRatio%2CMediaSourceCount&IsMissing=true&ImageTypeLimit=1&EnableImageTypes=Primary%2CBackdrop%2CThumb&StartIndex=0&Limit=100&ParentId=767bffe4f11c93ef34b805451a696a4e
    pass


def check_item(user, parent):
    folder_items = jellyfin.users.get_items_by_user_id(
        user_id=user.id,
        parent_id=parent.id,
        sort_by=["SortName"],
    )
    for item in folder_items.items:
        if item.is_folder:
            check_item(user, item)
        else:
            # metadata = jellyfin.items.get_metadata_editor_info(item_id=item.id)
            item_data = jellyfin.users.get_item(user_id=user.id, item_id=item.id)
            if parent is not None:
                print(f"{item.name.rjust(50)} == {Path(item_data.path).name}")
            else:
                print(f"{item.name}")
            # print(to_json_str(metadata))
            exit()


if __name__ == '__main__':
    jellyfin_user = get_user("jellyfin")
    list_missing_episodes(jellyfin_user, get_media_folder("TV Shows"))
    # check_item(jellyfin_user, get_media_folder("Anime (Dub)"))
