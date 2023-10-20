import subprocess
import json
import os
import urllib.request

# Initialize directories
RARIBLE_META_DIR = "./Rarible_Meta"
ORIGINAL_META_DIR = "./Original_Metadata"
ORIGINAL_MEDIA_DIR = "./Original_Media"
CID_LIST = []

# Sanitize filenames
def sanitize_filename(filename):
    return "".join([c for c in filename if c.isalpha() or c.isdigit() or c in (' ', '-', '_')]).rstrip()

def download_original_meta_and_media():
    print("Starting download_original_meta_and_media...")
    for filename in os.listdir(RARIBLE_META_DIR):
        print(f"Processing {filename}...")
        with open(f"{RARIBLE_META_DIR}/{filename}", 'r') as f:
            nft = json.load(f)
            
        originalMetaUri = nft['meta']['originalMetaUri']
        print(f"Original Meta URI: {originalMetaUri}")

        try:
            if originalMetaUri.startswith("ipfs://"):
                # Use IPFS commands
                originalMetaUri = originalMetaUri.replace('ipfs://ipfs/', '')
                print("Fetching metadata with ipfs cat...")
                cat_output = subprocess.check_output(["ipfs", "cat", originalMetaUri]).decode('utf-8')
                original_meta = json.loads(cat_output)
            else:
                # Fetch from other URLs like Arweave
                print("Fetching metadata from non-IPFS URI...")
                with urllib.request.urlopen(originalMetaUri) as u:
                    cat_output = u.read().decode('utf-8')
                    original_meta = json.loads(cat_output)

            # Your existing logic for downloading and pinning media files can be inserted here.
            
            CID_LIST.append({"name": sanitize_filename(nft['meta']['name']), "cid": originalMetaUri})
        except Exception as e:
            print(f"Could not fetch data for URI {originalMetaUri}: {e}")

# Additional code for testing the function
if __name__ == "__main__":
    download_original_meta_and_media()
    # Save CID list to a JSON file
    with open("cid_list.json", "w") as f:
        json.dump(CID_LIST, f)
