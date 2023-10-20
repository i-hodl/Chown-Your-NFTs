import os
import json
from init_dir import CID_LIST, ORIGINAL_MEDIA_DIR, ORIGINAL_META_DIR, RARIBLE_META_DIR
from fetch_rarible_meta import fetch_rarible_meta
from shared_utils import sanitize_filename
from fetch_rarible_meta import fetch_rarible_meta
from shared_utils import sanitize_filename
from download_original_meta_and_media import download_original_meta_and_media

if __name__ == "__main__":
    os.makedirs(RARIBLE_META_DIR, exist_ok=True)
    os.makedirs(ORIGINAL_META_DIR, exist_ok=True)
    os.makedirs(ORIGINAL_MEDIA_DIR, exist_ok=True)
    print("Let's get this party started! 🎉")
    fetch_rarible_meta()
    download_original_meta_and_media()
    print("Saving the CID list...")
    with open("cid_list.json", "w") as f:
        json.dump(CID_LIST, f)
    print("Done! You have succesfully chowned your data! Decentralze 🐙")
