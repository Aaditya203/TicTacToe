import streamlit as st
import numpy as np

# Original game logic (UNCHANGED)
board = np.zeros((3, 3), dtype=int)

def check_winner(board):
    if 3 in np.sum(board, axis=0) or 3 in np.sum(board, axis=1) or np.trace(board) == 3 or np.trace(np.fliplr(board)) == 3:
        return 'X won the game'
    if -3 in np.sum(board, axis=0) or -3 in np.sum(board, axis=1) or np.trace(np.fliplr(board)) == -3 or np.trace(board) == -3:
        return 'O won the game!'
    if not 0 in board:
        return "DRAW"
    else:
        return None

# Streamlit UI Setup
st.set_page_config(page_title="Tic Tac Toe", layout="centered", page_icon="🎮")

# Minimal Clean Theme
st.markdown(
    """
    <style>
/* FULL WHITE THEME */
body {background-color: #ffffff !important;}

.main {
    background-color: #ffffff !important;
    padding: 30px;
    border-radius: 16px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.04);
}

/* Main Buttons */
.stButton>button {
    background-color: #1a73e8 !important;
    color: #ffffff !important;
    border-radius: 10px !important;
    padding: 14px 0 !important;
    font-size: 20px !important;
    font-weight: 600 !important;
    width: 100% !important;
}

/* Game Cell Buttons */
.stButton>button[kind="primary"], .cell-btn>button {
    background-color: #f7f7f7 !important;
    border: 1px solid #e0e0e0 !important;
    border-radius: 14px !important;
    font-size: 36px !important;
    height: 95px !important;
    color: #2c3e50 !important;
}
</style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align:center;color:#2c3e50;'>Tic Tac Toe</h1>", unsafe_allow_html=True)


# Session State
if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)
if "current" not in st.session_state:
    st.session_state.current = 1
if "result" not in st.session_state:
    st.session_state.result = None

# Handle Click

def handle_click(i, j):
    if st.session_state.result is not None:
        return
    current_val = 1 if st.session_state.current == 1 else -1
    if st.session_state.board[i, j] == 0:
        st.session_state.board[i, j] = current_val
        result = check_winner(st.session_state.board)
        if result is not None:
            st.session_state.result = result
        else:
            st.session_state.current = 0 if st.session_state.current == 1 else 1

# Board Rendering

def render_board():
    grid = st.columns(3)
    for i in range(3):
        row_cols = st.columns(3)
        for j in range(3):
            cell = st.session_state.board[i, j]
            symbol = "❌" if cell == 1 else "⭕" if cell == -1 else " "
            with row_cols[j]:
                st.button(symbol, key=f"{i}{j}", on_click=lambda i=i, j=j: handle_click(i, j), help=f"Click to place {symbol}", kwargs=None, use_container_width=True, type="primary", disabled=(cell != 0),)

# Player Status
if st.session_state.result is None:
    turn = "❌ X" if st.session_state.current == 1 else "⭕ O"
    st.markdown(f"<h3 style='text-align:center;color:#34495e;'>Turn: {turn}</h3>", unsafe_allow_html=True)
else:
    st.markdown(f"<h2 style='text-align:center;color:#27ae60;'>{st.session_state.result}</h2>", unsafe_allow_html=True)

render_board()

# Reset Button
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🔄 Restart Game"):
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.session_state.result = None
