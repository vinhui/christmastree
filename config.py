NO_PI = False

HTML_FILE = "WebFiles/index.html"
PORT = 8000

SEQUENCE_DIR = "Sequences/"

LED_COUNT = 30
LED_DATA_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

if not NO_PI:
    from neopixel import ws
    LED_STRIP = ws.WS2811_STRIP_GRB
