
import streamlit as st

# Define the questions for the ISI assessment
questions = [
    "1. Difficulty falling asleep",
    "2. Difficulty staying asleep",
    "3. Problems waking up too early",
    "4. Satisfaction with current sleep pattern",
    "5. Interference of sleep problems with daily functioning",
    "6. Noticeability of sleep problems to others",
    "7. Distress caused by sleep problems"
]

# Define severity interpretation based on total score
def interpret_score(score):
