from pathlib import Path
import sys
sys.dont_write_bytecode = True

ROOT = Path(__file__).parent

DATA = ROOT / "data"
AUDIO = DATA / "audio"
IMAGE = DATA / "image"
FONT = DATA / 'font'

SCREEN = ROOT / "screen"
COMPONENT = SCREEN / 'component'
SERVICE = SCREEN / 'service'