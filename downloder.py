import os
import requests
import dropbox
import urllib.request

from pathlib import Path
global_path = Path(__file__).parent.parent.absolute()

import pandas as pd

data_path = os.path.dirname(os.path.realpath("__file__"))


class Downloader:
    """
    This class downloads the data.
    """

    def data_downloader(self, from_folder: str, to_folder: str):
        data_folder = data_path + '/' + to_folder
        os.makedirs(name=data_folder, exist_ok=True)
        dbx = dropbox.Dropbox(oauth2_access_token='cDmk_VMavxMAAAAAAAAAAY4WdOJCz-A3uqPu2Ekes2xCMqcfx90hRkkPc7hFDFmW')
        dbx_path = None
        for entry in dbx.files_list_folder(path='').entries:
            if entry.name == 'synthpop':
                dbx_path = entry.path_display
        for entry in dbx.files_list_folder(path=dbx_path + f"/{from_folder}").entries:
            if isinstance(entry, dropbox.files.FolderMetadata):
                self.data_downloader(from_folder + '/' + entry.name, to_folder + '/' + entry.name)
            elif isinstance(entry, dropbox.files.FileMetadata):
                dbx.files_download_to_file(download_path=os.path.join(data_folder, entry.name),
                                           path=dbx_path + f"/{from_folder}/" + entry.name)

    def download(self):
        data_folder = "./census_2016"
        path = os.path.join(data_path, "synpopCanada")
        os.makedirs(os.path.join(path, "data"), exist_ok=True)
        dbx = dropbox.Dropbox(oauth2_access_token='cDmk_VMavxMAAAAAAAAAAY4WdOJCz-A3uqPu2Ekes2xCMqcfx90hRkkPc7hFDFmW')
        dbx_path = None
        for entry in dbx.files_list_folder(path='/lookup.csv').entries:
            if entry.name == 'lookup.csv':
                dbx_path = entry.path_display
        for entry in dbx.files_list_folder(path=dbx_path).entries:
            dbx.files_download_to_file(download_path=os.path.join(data_folder, entry.name),
                                       path=dbx_path + entry.name)


if __name__ == '__main__':
    PROJECT_PATH = os.path.dirname(os.path.realpath("__file__"))
    print(PROJECT_PATH)
    downl = Downloader()
    downl.data_downloader(from_folder="synthpop", to_folder="census_2016")

