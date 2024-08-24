import matplotlib.pyplot as plt
import numpy as np

def display_images_side_by_side(images, titles=None, max_images_per_row=4):
    # %matplotlib inline
    num_images = len(images)
    
    if num_images == 0:
        print("Нет изображений для отображения.")
        return
    
    num_rows = (num_images + max_images_per_row - 1) // max_images_per_row  # округление вверх
    num_cols = min(num_images, max_images_per_row)
    
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 5 * num_rows))
    
    if num_rows == 1:
        axes = np.array([axes])
    if num_cols == 1:
        axes = np.array([[ax] for ax in axes])
    
    axes = axes.reshape(num_rows, num_cols)
    
    for i, (ax, image) in enumerate(zip(axes.flat, images)):
        if image.ndim == 2:  # grayscale image
            ax.imshow(image, cmap='gray')
        else:  # RGB image
            ax.imshow(image)
        ax.axis('off')
        if titles is not None and i < len(titles):
            ax.set_title(titles[i])
    
    # Удаление лишних осей
    for j in range(i + 1, num_rows * num_cols):
        fig.delaxes(axes.flat[j])
    
    plt.tight_layout()
    plt.show()