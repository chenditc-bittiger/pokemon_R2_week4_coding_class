#!/bin/bash
pip freeze > requirements.txt
eb deploy
