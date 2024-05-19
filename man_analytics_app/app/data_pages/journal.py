import streamlit as st
import yaml


def write_journal(message):
    with open('journal.txt', 'a') as f:
        f.write(message + '\n')

def read_journal(message):
    with open('journal.txt', 'r') as f:
        return f