import numpy as np

def calculate_uncertain_cuboid_statistics(n_sample, mean_length, mean_width, mean_height, range_length=0, range_width=0, range_height=0):
    '''
    Calculate the mean and standard deviation of the volume of a cuboid with uncertain dimensions.
    :param n_sample: int, The number of samples to take.
    :param mean_length: float, The mean length of the cuboid.
    :param mean_width: float, The mean width of the cuboid.
    :param mean_height: float, The mean height of the cuboid.
    :param range_length: float, The range of the length of the cuboid.
    :param range_width: float, The range of the width of the cuboid.
    :param range_height: float, The range of the height of the cuboid.
    :return: tuple, The mean volume and standard deviation of the volume of the cuboid.
    '''

    if (range_length == 0) and (range_width == 0) and (range_height == 0):
        return mean_length * mean_width * mean_height, 0
    
    # Generate random dimensions for the cuboids
    if range_length == 0:
        dist_length = 0.0
    else: 
        dist_length = (range_length / 2) * np.random.uniform(-1, 1, n_sample)

    if range_width == 0:
        dist_width = 0.0
    else: 
        dist_width = (range_width / 2) * np.random.uniform(-1, 1, n_sample)

    if range_height == 0:
        dist_height = 0.0
    else: 
        dist_height = (range_height / 2) * np.random.uniform(-1, 1, n_sample)

    lengths = mean_length + dist_length
    widths = mean_width + dist_width
    heights = mean_height + dist_height
    # Calculate the volumes of the cuboids
    volumes = lengths * widths * heights

    # Calculate the mean and standard deviation of the volumes
    mean_volume = np.mean(volumes)
    std_volume = np.std(volumes)

    # Return the mean and standard deviation of the volumes
    return mean_volume, std_volume