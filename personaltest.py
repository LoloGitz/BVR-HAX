import random

def noise(dataset, min_valid_value, max_valid_value, percent_noise):
    # Assuming percent_noise is a float between 0 and 1
    num_noise_values = round(len(dataset) * percent_noise, 0)
    noise_indices = []
    for _ in range(num_noise_values):
        random_index = random.randint(0, len(dataset) - 1)
        # Ensure each index is unique, no repeats
        while random_index in noise_indices:
            random_index = random.randint(0, len(dataset) - 1)
        noise_indices.append(random_index)

    for noise_index in noise_indices:
        dataset[noise_index] = random.randint(min_valid_value, max_valid_value)

    return dataset


noisecomplexity = 100
noiselist = []
for i in range(noisecomplexity):
    noiselist.append(random.uniform(0, 100))

newnoise = noise(noiselist, 0, 100, 1)
print(newnoise)
