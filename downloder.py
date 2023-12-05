import os
import requests
import dropbox

import pandas as pd

data_path = os.path.dirname(os.path.dirname(os.path.realpath("__file__")))


class Downloader:
    """
    This class downloads the data.
    """

    def data_downloader(from_folder: str, to_folder: str):
        data_folder = data_path + '/' + to_folder
        os.makedirs(name=data_folder, exist_ok=True)
        dbx = dropbox.Dropbox(oauth2_access_token='cDmk_VMavxMAAAAAAAAAAY4WdOJCz-A3uqPu2Ekes2xCMqcfx90hRkkPc7hFDFmW')
        dbx_path = None
        for entry in dbx.files_list_folder(path='').entries:
            if entry.name == 'ativizig-project':
                dbx_path = entry.path_display
        for entry in dbx.files_list_folder(path=dbx_path + f"/{from_folder}").entries:
            if isinstance(entry, dropbox.files.FolderMetadata):
                data_downloader(from_folder + '/' + entry.name, to_folder + '/' + entry.name)
            elif isinstance(entry, dropbox.files.FileMetadata):
                dbx.files_download_to_file(download_path=os.path.join(data_folder, entry.name),
                                           path=dbx_path + f"/{from_folder}/" + entry.name)


if __name__ == '__main__':
    print(PROJECT_PATH)
    Downloader(gdrive_id="1zJ0VQhM9umBPfqUlfoyq46z5kT1KPHfB", file_name="Geo_starting_row_CSV.csv", pumf=False)
    Downloader(gdrive_id="1hTdKSKHSN1Cwi47wHMyx9cnHbq9lkUU8", file_name="98-401-X2016044_English_CSV_data.csv", pumf=True)
    Downloader(gdrive_id="1EHOARdwSu2FwfBbdfBzeJ9gkI8N2xaO8", file_name="lookup.csv", pumf=False)
    Downloader(gdrive_id="120UzaIy4gEX0J1M3STX3U3zAiCFQxjd7", file_name="Census_2016_Individual_PUMF.dta", pumf=True)
