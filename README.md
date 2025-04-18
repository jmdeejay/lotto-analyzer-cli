# Lotto Analyzer CLI 🎰📊

A Python command-line tool for scraping, analyzing, and forecasting lottery games draw data — covering every draw since their respective launch.

This tool offers hot/cold number analytics, draw forecasts based on recurrence, full graph generation, and historical insights — all from your terminal.

---

## 🎯 Purpose

Originally built as a fun learning project with Python, this application explores the statistical patterns in Lotto 6/49 & Extra draws over more than 40 years of data.

While predicting lottery outcomes is inherently futile in a fair system, this project aims to surface **non-random behavior**, **recurring patterns**, or **potential statistical biases**, if they exist — inspired by real-world anomalies like [Joan R. Ginther](https://en.wikipedia.org/wiki/Joan_R._Ginther)'s improbable winning streaks.

---

## ⚙️ Features

### 🔢 Forecast Generator
Generate draw suggestions based on historical trends:
- Top recurring numbers
- Coldest (least drawn) numbers
- Position-based recurrence (1st ball, 2nd ball, etc.)
- Completely random sets
- Hybrid sets (e.g. top 12 from hot/cold pools)

### 📈 Graph Generation
- Graph number frequencies ordered by **number**
- Graph number frequencies ordered by **occurrence count**
- Auto-generate and export graphs as PNG files

---

## 🧰 Tech Stack
- Python 3.7+
- requests — Web scraping
- pandas — Data processing
- matplotlib — Visualization

---

## 📦 Installation
```bash
pip install -r requirements.txt
python 649.py
or
python extra.py
```

---

## 🔒 Disclaimer
This project is for educational and entertainment purposes only.
It does not increase your odds of winning the lottery. Always play responsibly.
