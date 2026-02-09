"""
Verifieringsskript för ML-miljön
Kollar att alla paket är installerade och fungerar
"""

import sys

print("=" * 50)
print("Kontrollerar ML-miljön...")
print("=" * 50)
print()

# Kolla Python-version
print(f"Python version: {sys.version}")
print()

# Kolla PyTorch
print("--- PyTorch ---")
try:
    import torch
    print(f"PyTorch version: {torch.__version__}")
    
    # Kolla GPU/accelerator
    if torch.cuda.is_available():
        # Hanterar både NVIDIA (CUDA) och AMD (ROCm)
        device = "cuda"
        backend = "ROCm" if torch.version.hip else "CUDA"
        gpu_name = torch.cuda.get_device_name(0)
        print(f"GPU hittad: {gpu_name}")
    elif torch.backends.mps.is_available():
        # Hanterar Apple Silicon 
        device = "mps"
        backend = "MPS"
        gpu_name = "Apple Silicon"
        print(f"GPU hittad: {gpu_name}")
    else:
        device = "cpu"
        backend = "CPU"
        print("Ingen GPU hittad, använder CPU")
    
    print(f"Använder: {device} ({backend} backend)")
    
    # Gör en enkel tensor-beräkning för att testa
    print()
    print("Testar tensor-beräkning...")
    x = torch.tensor([1.0, 2.0, 3.0], device=device)
    y = torch.tensor([4.0, 5.0, 6.0], device=device)
    z = x + y
    print(f"  x = {x.tolist()}")
    print(f"  y = {y.tolist()}")
    print(f"  x + y = {z.tolist()}")
    print("Tensor-beräkning OK!")
    
except ImportError as e:
    print(f"FEL: Kunde inte importera PyTorch: {e}")
except Exception as e:
    print(f"FEL: {e}")

print()

# Kolla Scikit-learn
print("--- Scikit-learn ---")
try:
    import sklearn
    print(f"Scikit-learn version: {sklearn.__version__}")
except ImportError as e:
    print(f"FEL: Kunde inte importera Scikit-learn: {e}")

print()

# Kolla Pandas
print("--- Pandas ---")
try:
    import pandas as pd
    print(f"Pandas version: {pd.__version__}")
except ImportError as e:
    print(f"FEL: Kunde inte importera Pandas: {e}")

print()

# Kolla Jupyter
print("--- Jupyter ---")
try:
    import jupyter
    # Jupyter har inte __version__ så vi kollar notebook istället
    import notebook
    print(f"Jupyter notebook version: {notebook.__version__}")
except ImportError as e:
    print(f"FEL: Kunde inte importera Jupyter: {e}")

print()
print("=" * 50)
print("Kontroll klar!")
print("=" * 50)
