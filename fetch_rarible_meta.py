from BASE_URL import BASE_URL
from CONTRACT_ADDRESS import CONTRACT_ADDRESS
from HEADERS import HEADERS
from init_dir import RARIBLE_META_DIR
from shared_utils import sanitize_filename
import requests
import json


def fetch_rarible_meta():
    print("Fetching initial Rarible metadata...")
    url = f"{BASE_URL}items/byCollection?collection=ETHEREUM:{CONTRACT_ADDRESS}"
    response = requests.get(url, headers=HEADERS)
    all_nfts = response.json()
    for nft in all_nfts['items']:
        meta_name = sanitize_filename(nft['meta']['name'])
        with open(f"{RARIBLE_META_DIR}/{meta_name}.json", 'w') as f:
            json.dump(nft, f)