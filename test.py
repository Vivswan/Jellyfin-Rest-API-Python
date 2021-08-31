import os
from pathlib import Path


def test(path):
    path = Path(path)
    for folder in os.listdir(path):
        folder_path = path.joinpath(folder)
        root, dirs, files = next(os.walk(folder_path))
        # if len(files) > 0:
        #     print(folder)
        for index, file in enumerate(sorted(files)):
            os.rename(folder_path.joinpath(file), folder_path.joinpath(
                " ".join(file.split(".")[0].split(" ")[:-1]) + f" {str(index + 1).zfill(2)}." + ".".join(
                    file.split(".")[1:])))
            print(" ".join(file.split(".")[0].split(" ")[:-1]) + f" {str(index + 1).zfill(2)}." + ".".join(
                file.split(".")[1:]))


if __name__ == '__main__':
    test("D:/encrypted/Media Server/Anime/Anime (Dub)/The Legend of Korra (Dub)")
