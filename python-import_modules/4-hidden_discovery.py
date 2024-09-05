#!/usr/bin/python3
import importlib.util

# Charger le fichier compilé .pyc
spec = importlib.util.spec_from_file_location("hidden_4", "/tmp/hidden_4.pyc")
hidden_4 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hidden_4)

# Lister les noms définis dans le module
names = dir(hidden_4)

# Filtrer et afficher les noms qui ne commencent pas par __
for name in sorted(names):
    if not name.startswith("__"):
        print(name)
