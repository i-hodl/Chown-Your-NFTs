from init_dir import CID_LIST, ORIGINAL_MEDIA_DIR, ORIGINAL_META_DIR, RARIBLE_META_DIR
from shared_utils import sanitize_filename
import requests
import json
import os
import subprocess
from urllib.request import urlretrieve


def download_original_meta_and_media():
    print("Let's kick this off! 🚀")
    for filename in os.listdir(RARIBLE_META_DIR):
        print(f"Groovin' with {filename}...")
        with open(f"{RARIBLE_META_DIR}/{filename}", 'r') as f:
            nft = json.load(f)

        originalMetaUri = nft['meta']['originalMetaUri']

        try:
            if originalMetaUri.startswith("ipfs://"):
                originalMetaUri = originalMetaUri.replace('ipfs://ipfs/', '')
                cat_output = subprocess.check_output(["ipfs", "cat", originalMetaUri]).decode('utf-8')
                original_meta = json.loads(cat_output)

                # Save original metadata to Original_Metadata folder
                with open(f"{ORIGINAL_META_DIR}/{sanitize_filename(nft['meta']['name'])}.json", 'w') as meta_file:
                    json.dump(original_meta, meta_file)

                # Your existing logic for IPFS here...

            else:
                print(f"Fetching from non-IPFS: {originalMetaUri}...")
                response = requests.get(originalMetaUri)
                original_meta = response.json()

                # Save original metadata to Original_Metadata folder
                with open(f"{ORIGINAL_META_DIR}/{sanitize_filename(nft['meta']['name'])}.json", 'w') as meta_file:
                    json.dump(original_meta, meta_file)

                image_url = original_meta.get('image', '')

                if image_url.startswith('http') or image_url.startswith('https'):
                    print(f"Downloading from Arweave or other HTTP sources: {image_url}...")
                    urlretrieve(image_url, f"{ORIGINAL_MEDIA_DIR}/{sanitize_filename(nft['meta']['name'])}.png")

            CID_LIST.append({"name": sanitize_filename(nft['meta']['name']), "cid": originalMetaUri})

        except Exception as e:
            print(f"Oops! Couldn't fetch {originalMetaUri}: {e}")