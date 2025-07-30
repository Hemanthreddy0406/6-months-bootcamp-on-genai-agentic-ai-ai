import streamlit as st
import chess
import chess.svg
from io import StringIO
import base64

st.title("Minimal Chess Game")

# Initialize session state
if 'board' not in st.session_state:
    st.session_state.board = chess.Board()
if 'selected_square' not in st.session_state:
    st.session_state.selected_square = None

board = st.session_state.board
selected_square = st.session_state.selected_square

# Helper to render SVG in Streamlit
def render_svg(svg):
    b64 = base64.b64encode(svg.encode('utf-8')).decode('utf-8')
    html = f'<img src="data:image/svg+xml;base64,{b64}"/>'
    st.markdown(html, unsafe_allow_html=True)

# Display board
svg_board = chess.svg.board(board=board, lastmove=board.peek() if board.move_stack else None)
render_svg(svg_board)

# User input for move
st.write("Select a piece to move:")
from_square = st.selectbox("From", [chess.square_name(sq) for sq in chess.SQUARES], key="from_square")
st.write("Select destination square:")
to_square = st.selectbox("To", [chess.square_name(sq) for sq in chess.SQUARES], key="to_square")

if st.button("Make Move"):
    move_uci = from_square + to_square
    move = chess.Move.from_uci(move_uci)
    if move in board.legal_moves:
        board.push(move)
        st.success(f"Moved {from_square} to {to_square}")
    else:
        st.error("Illegal move!")

if st.button("Reset Game"):
    st.session_state.board = chess.Board()
    st.experimental_rerun()

# Show game status
if board.is_checkmate():
    st.warning("Checkmate!")
elif board.is_stalemate():
    st.info("Stalemate!")
elif board.is_check():
    st.info("Check!")