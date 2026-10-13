"""Vercel serverless entrypoint.

Vercel's Python runtime looks for a WSGI callable named ``app`` in this file.
All routes are rewritten here by vercel.json, and Flask handles routing/static files.
"""
import os
import sys

# Make the project root importable (app/, wsgi.py) from inside /api.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app  # noqa: E402

app = create_app()
