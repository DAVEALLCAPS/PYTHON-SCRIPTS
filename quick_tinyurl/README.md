# Quick TinyURL

This Python script provides a quick and easy way to shorten URLs using TinyURL service and copy the resulting short URL directly to your clipboard.

## Prerequisites

Make sure you have installed the following Python packages:

- `pyshorteners` for interfacing with the TinyURL service.
- `pyperclip` for accessing the clipboard to copy URLs.

You can install these using pip:

```bash
pip install pyshorteners pyperclip
```

## Usage

To use the script, simply run it from your terminal and provide the URL you want to shorten as an argument:

```bash
python quick_tinyurl.py https://www.example.com
```

The script will print the shortened URL to the console and also copy it directly to your clipboard. After running the script, you will see a success message like this:

```
http://tinyurl.com/example
Copied short URL to clipboard!
```

## Error Handling

If no URL is provided as an argument when running the script, you will see the following error message:

```
Please provide a URL
```


That's it! Now you have a tool that allows you to quickly shorten URLs and copy them to your clipboard. Enjoy!