from flask import Flask, jsonify, request,Response, redirect;
import json

app = Flask(__name__);

if __name__ == __name__:
    @app.route('/')
    def  main():
        return {
            "status": 200,
            "base-url": "sisula welgamage"
        }
