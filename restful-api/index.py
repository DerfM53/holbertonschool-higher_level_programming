#!/usr/bin/python3

import cgi

print("Content-type: text/html; charset=utf-8\n")

html  = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>La page web de Fred avec Python et HTML !</title>
</head>
<body>
    <h1>Bienvenue Fred</h1>
</body>
</html>
"""

print(html)