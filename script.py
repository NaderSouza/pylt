#!/usr/bin/env python3
"""
SCRIPT test for study purposes - 
"""

# Metadata
__version__ = "0.1.0"
__author__ = "nadin"
__license__ = "MIT"


# Imports
import os

# Language detection and greeting message
current_language = os.getenv("LANG" "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt-BR":
    msg = "Olá, Mundo!"
elif current_language == "fr-FR":
    msg = "Bonjour, le monde!"
print(msg)

# Main function execution
# print("Mashallah mesmo!")
