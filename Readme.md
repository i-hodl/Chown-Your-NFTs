### README.md


# Chown Your NFTs

## About

Chown Your NFTs is a Python script to download and archive your Rarible NFTs. It fetches the metadata and media files associated with your NFTs and saves them to your local machine.

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



