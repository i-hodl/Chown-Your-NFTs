### README.md


# Chown Your NFTs

## About

Chown Your NFTs is a Python script to download and archive your NFTs. It fetches the metadata and media files associated with your NFTs and saves them to your local machine. Powered by the Rarible Protocol. 

## Requirements

- Python 3.x
- IPFS (Optional, but recommended)
- Rarible API key

## Installation

1. Clone this repo: `git clone https://github.com/i-hodl/Chown-Your-NFTs.git`
2. Navigate to the project directory: `cd Chown-Your-NFTs`
3. Install required packages: `pip install -r requirements.txt`

## Configuration

1. Add your Rarible API key to `HEADERS.py` (create this file if it doesn't exist). Example:

```python
HEADERS = {
    'x-api-key': 'YOUR_RARIBLE_API_KEY_HERE'
}
```

2. Specify a contract address in `CONTRACT_ADDRESS.py`. Example:

```python
CONTRACT_ADDRESS = '0xYourContractAddressHere'
```

## Usage

1. Run the script: `python chown.py`
2. Let the magic happen! 🎉

## Contributing

Feel free to fork, submit PRs, and report issues.

## License

cc0 v1.0

## What Does This Do?

Ever worry that your precious NFTs might go poof if the platform you minted them on suddenly decides to exit stage left? With this code, you can put those fears to bed, permanently. 🛌
Our script fetches the original metadata and media associated with your NFTs and pins them to IPFS, using the exact same CID as the original. So even if your minting platform decides to take an unplanned vacation, your NFTs will keep partying on, immortal and unstoppable. 🎉
In simpler terms: We make sure your NFTs are as resilient as a cockroach at a nuclear test site. 🪳

