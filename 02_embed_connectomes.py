import numpy as np

# Load affinitity matrix
aff = np.load('gradient_data/conn_matrices/cosine_affinity.npy')


import sys
sys.path.append("../mapalign")
from mapalign import embed

emb, res = embed.compute_diffusion_map(aff, alpha = 0.5)

