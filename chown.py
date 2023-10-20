import os
import json
import requests
import subprocess
from CONTRACT_ADDRESS import CONTRACT_ADDRESS
from HEADERS import HEADERS


# Initialize directories
RARIBLE_META_DIR = "test/Rarible_Meta"
ORIGINAL_META_DIR = "test/Original_Metadata"
ORIGINAL_MEDIA_DIR = "test/Original_Media"
CID_LIST = []

# Your Rarible API details
BASE_URL = 'https://api.rarible.org/v0.1/'
def sanitize_filename(filename):
    return "".join([c for c in filename if c.isalpha() or c.isdigit() or c in (' ', '-', '_')]).rstrip()

# Fetch initial metadata from Rarible
def fetch_rarible_meta():
    print("Fetching initial Rarible metadata...")
    url = f"{BASE_URL}items/byCollection?collection=ETHEREUM:{CONTRACT_ADDRESS}"
    response = requests.get(url, headers=HEADERS)
    all_nfts = response.json()
    for nft in all_nfts['items']:
        meta_name = sanitize_filename(nft['meta']['name'])
        with open(f"{RARIBLE_META_DIR}/{meta_name}.json", 'w') as f:
            json.dump(nft, f)

import requests

def download_original_meta_and_media():
    print("Starting download_original_meta_and_media...")
    for filename in os.listdir(RARIBLE_META_DIR):
        print(f"Processing {filename}...")
        with open(f"{RARIBLE_META_DIR}/{filename}", 'r') as f:
            nft = json.load(f)
        
        originalMetaUri = nft['meta']['originalMetaUri'].replace('ipfs://ipfs/', '')
        print(f"Original Meta URI: {originalMetaUri}")

        try:
            print("Fetching metadata with ipfs cat...")
            cat_output = subprocess.check_output(["ipfs", "cat", originalMetaUri]).decode('utf-8')
            original_meta = json.loads(cat_output)
            
            image_url = original_meta.get('image', '')
            animation_url = original_meta.get('animation_url', '')
            
            def download_and_pin(url, file_type, extension):
                if url.startswith("ipfs://ipfs/"):
                    cid = url.replace('ipfs://ipfs/', '')
                    print(f"Downloading and pinning {file_type} {cid}...")
                    subprocess.run(["ipfs", "get", cid, f"--output={ORIGINAL_MEDIA_DIR}/{sanitize_filename(nft['meta']['name'])}{extension}"])
                    subprocess.run(["ipfs", "pin", "add", cid])
                else:
                    print(f"Downloading {file_type} from external URL...")
                    response = requests.get(url)
                    with open(f"{ORIGINAL_MEDIA_DIR}/{sanitize_filename(nft['meta']['name'])}{extension}", 'wb') as f:
                        f.write(response.content)

            if image_url:
                download_and_pin(image_url, "image", ".gif")
            if animation_url:
                download_and_pin(animation_url, "animation", ".mp4")
            
            CID_LIST.append({"name": sanitize_filename(nft['meta']['name']), "cid": originalMetaUri})
        except Exception as e:
            print(f"Could not fetch data for CID {originalMetaUri}: {e}")

def download_original_meta_json():
    print("Downloading original metadata as JSON files...")
    for item in CID_LIST:
        name = item['name']
        cid = item['cid']
        try:
            print(f"Fetching JSON for {name}...")
            subprocess.run(["ipfs", "get", cid, f"--output={ORIGINAL_META_DIR}/{name}.json"])
        except Exception as e:
            print(f"Could not fetch JSON for {name}: {e}")

if __name__ == "__main__":
    os.makedirs(RARIBLE_META_DIR, exist_ok=True)
    os.makedirs(ORIGINAL_META_DIR, exist_ok=True)
    os.makedirs(ORIGINAL_MEDIA_DIR, exist_ok=True)
    print("Let's get this party started! 🎉")
    fetch_rarible_meta()
    download_original_meta_and_media()
    download_original_meta_json()
    print("Saving the CID list...")
    with open("cid_list.json", "w") as f:
        json.dump(CID_LIST, f)
    print("Done! If you see this message, we've hopefully succeeded. 🌟")
