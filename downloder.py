import os
import requests
import dropbox
import urllib.request

import pandas as pd

data_path = os.path.dirname(os.path.dirname(os.path.realpath("__file__")))


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
        os.makedirs(name=data_folder, exist_ok=True)
        dbx = dropbox.Dropbox(oauth2_access_token='cDmk_VMavxMAAAAAAAAAAY4WdOJCz-A3uqPu2Ekes2xCMqcfx90hRkkPc7hFDFmW')
        dbx_path = None
        for entry in dbx.files_list_folder(path='./synthpop/lookup.csv').entries:
            if entry.name == 'lookup.csv':
                dbx_path = entry.path_display
        for entry in dbx.files_list_folder(path=dbx_path).entries:
            dbx.files_download_to_file(download_path=os.path.join(data_folder, entry.name),
                                       path=dbx_path + entry.name)

    def get_dropbox_client(self):
        return dropbox.Dropbox(
            oauth2_refresh_token="cDmk_VMavxMAAAAAAAAAAY4WdOJCz-A3uqPu2Ekes2xCMqcfx90hRkkPc7hFDFmW"
        )

    def download_file(self, remote_path: str, local_path: str):
        """
        Downloads a file at a `remote_path` in Dropbox
        to a `local_path` on the local machine.
        """
        print(f"Dropbox: downloading {remote_path}")
        dbx = self.get_dropbox_client()
        dbx.files_download_to_file(local_path, remote_path)
        print(f"Dropbox: successfully downloaded to {local_path}")


if __name__ == '__main__':
    print(data_path)
    # Downloader().download_file(remote_path="nrms1t8sdraat0le1k7ge", local_path="./census_2016")
    url = "https://www.dropbox.com/scl/fo/nrms1t8sdraat0le1k7ge/h?rlkey=45l9zkq459o5nipuc5vbntz65&dl=0/lookup.csv?dl=1"  # dl=1 is important

    u = urllib.request.urlopen(url)
    data = u.read()
    u.close()

    with open("lookup.csv", "wb") as f:
        f.write(data)
