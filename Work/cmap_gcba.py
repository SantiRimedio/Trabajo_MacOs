from matplotlib.colors import LinearSegmentedColormap

cmap_gcba =  LinearSegmentedColormap.from_list('gcba', (
    # Edit this gradient at https://eltos.github.io/gradient/#gcba=EC607E-F08372-FFD500-EEEDA6-29BDEF
    (0.000, (0.925, 0.376, 0.494)),
    (0.250, (0.941, 0.514, 0.447)),
    (0.500, (1.000, 0.835, 0.000)),
    (0.750, (0.933, 0.929, 0.651)),
    (1.000, (0.161, 0.741, 0.937))))