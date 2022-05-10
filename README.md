# ezgif-essentials

Want to generate GIFs of the highest quality? Tired of having too many unecessary parameters? You also happen to be a motion graphic designer? `ezgif-essentials` is a pseudo-opinionated video/sequence to GIF CLI converter. It uses the same robust conversion pipeline as [ezGIF](https://ezgif.com/) without the frame rate limitations or involuntary compression. It is powered by [FFmpeg](https://github.com/kkroening/ffmpeg-python), [Gifsicle](https://github.com/kohler/gifsicle) and my frustration with all GIF converters.


Clone this repository
```bash
git clone https://github.com/ZacharyShaver/ezgif-essentials.git
cd ezgif-essentials
```

Install Python3 / Pip3
```bash
sudo apt update
sudo apt install python3
sudo apt install python3-pip
```

Install the `ffmpeg-python` module

```bash
pip3 install ffmpeg-python 
```

Install `gifsicle`

```bash
sudo apt install gifsicle
```

Test the script

```bash
python main.py -h
```

## Usage 

> Place Images into the folder named ImageInput make sure the images are labled in the _FRAMEX format

```bash
python main.py -i test.mp4 -z 3
```

```yaml
Optional arguments:
-h, --help              show this help message and exit
-z, --optimise          optimise GIF file size with zero quality penalty (1 - 3)
-l, --lossy             number of artefacts allowed for compression
-w, --transparent       enables transparency
```


