# Laboration - Robust Miljöhantering

Detta projekt är en laboration för att sätta upp en ML-utvecklingsmiljö.

## Vad projektet innehåller

- PyTorch (med CUDA-stöd för GPU)
- Scikit-learn
- Pandas
- Jupyter

## Hur man använder

Först måste du ha `uv` installerat. Sedan kör du:

```bash
uv sync
```

Detta installerar alla paket.

## Köra verifieringsskriptet

För att kolla att allt fungerar:

```bash
uv run check_env.py
```

Skriptet kollar:
- Python-version
- PyTorch-version och GPU-status
- Scikit-learn version
- Pandas version
- Jupyter version

Det gör också en enkel tensorberäkning för att testa att GPU:n funkar.
