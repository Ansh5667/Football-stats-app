from flask import Flask, render_template, request
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['football_stats']