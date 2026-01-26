from rgbmatrix import RGBMatrix, RGBMatrixOptions

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 2
options.gpio_slowdown = 4
options.hardware_mapping = 'adafruit-hat'
options.drop_privileges = False

matrix = RGBMatrix(options=options)
matrix.Clear()
print("Display cleared")
