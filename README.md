# 🎮 Tic Tac Toe – NumPy + Streamlit

A simple Tic Tac Toe game built with NumPy and Streamlit.

## 🚀 Features

- NumPy-based game logic
- Clean Streamlit UI
- Win, draw & invalid move detection
- Restart option

## ⚡ Installation

```bash
pip install streamlit numpy
```

## ▶️ Run

```bash
streamlit run app.py
```

## 🧩 How It Works

The board is a 3×3 NumPy array:
- `1` = X
- `-1` = O
- `0` = Empty

Winner detected by checking row, column, and diagonal sums.
