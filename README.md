# Arachnida :spider_web: :computer: [![slegaris's 42 arachnida Score](https://badge42.vercel.app/api/v2/cle3f3fm900060fjx7kw7tghw/project/3070894)](https://github.com/JaeSeoKim/badge42)

Arachnida is a powerful Python-based tool that offers web scraping and image EXIF data reading functionalities. It has two main scripts, `spider.py` and `scorpion.py`.

## :spider: Spider

The `spider.py` script is a robust web scraper designed to download images and documents from any specified URL. It provides options for recursive scraping with customizable depth and allows the user to specify the directory to save images and documents.

## :scorpion: Scorpion

The `scorpion.py` script is an EXIF data viewer. It allows you to view the metadata (EXIF data) for each image in a directory, which can be specified on the command line.

## :floppy_disk: Files

This repo contains:

- `spider.py`: A powerful web scraper.
- `scorpion.py`: An EXIF data viewer.

## :wrench: How to Use

### :spider: Spider

You can use spider by providing a URL as a mandatory argument, and optional parameters such as whether to scrape recursively (-r), maximum depth to scrape to (-l), and the directory to save images and documents to (-p).

Example:
```bash
python3 spider.py <URL> -r -l 5 -p data
```

### :scorpion: Scorpion

You can use scorpion by running the script with the directory containing the images as the argument. 

Example:
```bash
python3 scorpion.py <Directory_Path>
```
If no directory is provided, it will read the EXIF data for each image in the current directory.

## :gear: Dependencies

- urllib
- bs4 (BeautifulSoup)
- os
- argparse
- exifread
- getkey

Please ensure you have these installed before running the scripts.

## :pencil: Note on Code Aesthetics

Arachnida represents my first journey into Python programming. As such, while I'm proud of what Arachnida accomplishes, I'd like to acknowledge upfront that you might not find it to be the most beautiful or elegantly structured code. Nonetheless, my focus has been on functionality and robustness. This project has been a learning curve, and I strongly believe in the saying, "First make it work, then make it beautiful." :blush:

Remember, the beauty of a tool lies in its effectiveness and ability to get the job done. And Arachnida does its job well. As I grow in my Python journey, I hope to improve the aesthetics of the code without compromising its functionality. 

If you have any suggestions for improving the code design or structure, I'm all ears! Please feel free to contribute. After all, code beauty is often found in the eye of the beholder. :heart:
