import matplotlib.pyplot as plt
from flyr import unpack
from numpy import unique
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Reading and rendering a thermal image
thermogram = unpack('termico.png')
images = [thermogram.optical, thermogram.celsius]

# Plotting the thermal image with different emissivities
fig, axs = plt.subplots(1, 2, figsize=(20, 7))
for value in range(2):
    ax = axs[value]
    ax.set_axis_off()
    image = images[value]
    im = ax.imshow(image, cmap='inferno')
    if value == 0:
        continue
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='4%', pad=0.05)
    cb = plt.colorbar(im, cax=cax)
    cb.set_label(label=f'Temperatura (°C)', size='large')
plt.show()