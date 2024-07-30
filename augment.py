# 数据增强
import random

def time_slicing(sequence, slice_length):
    return [sequence[i:i + slice_length] for i in range(0, len(sequence), slice_length)]

def masking(sequence, mask_ratio=0.1):
    num_to_mask = int(len(sequence) * mask_ratio)
    masked_sequence = sequence.copy()
    mask_indices = random.sample(range(len(sequence)), num_to_mask)
    for idx in mask_indices:
        masked_sequence[idx] = 0
    return masked_sequence

def noise_injection(sequence, all_items):
    negative_samples = list(set(all_items) - set(sequence))
    if not negative_samples:
        return sequence
    negative_sample = random.choice(negative_samples)
    insert_position = random.randint(0, len(sequence))
    augmented_sequence = sequence[:insert_position] + [negative_sample] + sequence[insert_position:]
    return augmented_sequence

def redundancy_injection(sequence):
    if not sequence:
        return sequence
    positive_sample = random.choice(sequence)
    insert_position = random.randint(0, len(sequence))
    augmented_sequence = sequence[:insert_position] + [positive_sample] + sequence[insert_position:]
    return augmented_sequence

def augment_sequence(sequence, all_items, num_iterations):
    augmentation_methods = [time_slicing, masking, noise_injection, redundancy_injection]
    augmented_sequences = [sequence]

    for _ in range(num_iterations):
        new_augmented_sequences = []
        for seq in augmented_sequences:
          method = random.choice(augmentation_methods)
          if method == time_slicing:
            new_augmented_sequences.extend(method(seq, slice_length=5))
          elif method == noise_injection:
            new_augmented_sequences.append(method(seq, all_items))
          else:
            new_augmented_sequences.append(method(seq))
        augmented_sequences = new_augmented_sequences
    
    return augmented_sequences
