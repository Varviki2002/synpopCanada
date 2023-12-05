import os
import requests
import dropbox
import urllib.request

from pathlib import Path
global_path = Path(__file__).parent.parent.absolute()

import pandas as pd

data_path = os.path.dirname(os.path.dirname(os.path.realpath("__file__")))


class Downloader:
    """
    This class downloads the data.
    """

    def download_data(self):
        """
        This method downloads the data.
        """
        path = os.path.join(data_path, "synpopCanada")
        os.makedirs(os.path.join(path, "data"), exist_ok=True)
        if not os.listdir(os.path.join(path, "data")):
            dbx = dropbox.Dropbox(oauth2_refresh_token='cDmk_VMavxMAAAAAAAAAAY4WdOJCz-A3uqPu2Ekes2xCMqcfx90hRkkPc7hFDFmW')
            for entry in dbx.files_list_folder("").entries:
                dbx.files_download_to_file(os.path.join(path, "census_2016/" + entry.name),
                                           entry.path_display)
            print("The data has been successfully downloaded!")


if __name__ == '__main__':
    print(global_path)
    downl = Downloader()
    downl.download_data()

