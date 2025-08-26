import streamlit as st
import math

# Custom CSS for styling
st.markdown("""
<style>
    body {
        background-color: #f0f0f0;
    }
    .calculator {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        margin: 20px;
    }
    .button {
        padding: 20px;
        font-size: 24px;
        border: none;
        border-radius: 5px;
        background-color: #007BFF;
        color: white;
        cursor: pointer;
        transition: background-color 0.3s;
        text-align: center;
    }
    .button:hover {
        background-color: #0056b3;
    }
    .display {
        font-size: 32px;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        margin-bottom: 20px;
        text-align: right;
        background-color: white;
    }
    .clear {
        background-color: #dc3545;
    }
    .clear:hover {
        background-color: #c82333;
    }
</style>
""", unsafe_allow_html=True)

# Title of the app
st.title("Scientific Calculator")

# Initialize the expression
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# Function to evaluate the expression
def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)

# Function to update the expression
def update_expression(value):
    st.session_state.expression += value

# Function to clear the expression
def clear_expression():
    st.session_state.expression = ""

# Display the current expression
st.markdown('<div class="display">{}</div>'.format(st.session_state.expression), unsafe_allow_html=True)

# Create a grid layout for the calculator buttons
button_layout = [
    ['7', '8', '9', '÷'],
    ['4', '5', '6', '×'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['sin', 'cos', 'tan', 'C'],
    ['log', 'exp', 'sqrt', '('],
    [')', 'π', 'e', 'x^y']
]

# Create buttons for the calculator layout
for row in button_layout:
    cols = st.columns(len(row))
    for i, button in enumerate(row):
        with cols[i]:
            if button == 'C':
                if st.button(button, key=button, help=button, css_class="button clear"):
                    clear_expression()
            else:
                if st.button(button, key=button, help=button):
                    if button in ['+', '-', '×', '÷', 'x^y']:
                        update_expression(button.replace('×', '*').replace('÷', '/'))
                    elif button == '=':
                        result = calculate(st.session_state.expression)
                        st.success(f"Result: {result}")
                    elif button in ['sin', 'cos', 'tan', 'log', 'exp', 'sqrt']:
                        update_expression(f"math.{button}(")
                    elif button in ['π', 'e']:
                        update_expression(str(math.pi) if button == 'π' else str(math.e))
                    else:
                        update_expression(button)

# Display the final expression
st.markdown('<div class="display">{}</div>'.format(st.session_state.expression), unsafe_allow_html=True)