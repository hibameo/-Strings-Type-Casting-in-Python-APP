import streamlit as st
import pandas as pd

st.set_page_config(page_title="Strings & Type Casting in Python", layout="centered")
st.title("🔤 Strings & 🔄 Type Casting in Python")
st.markdown("### 👩‍💻 By Hiba's Python Learning App")

# ----- Strings Section -----
st.header("1️⃣ Strings in Python")
st.markdown("""
Strings are a sequence of characters enclosed in quotes (`' '` or `" "`).  
They are **immutable** and support **indexing**, **slicing**, and various methods.
""")

example = '''name = "Hiba"
print(name[0])     # H
print(name[1:3])   # ib
print(name + " Khan")  # Hiba Khan
print(len(name))   # 4
'''
st.code(example, language='python')

# ----- Analyze Your String -----
st.subheader("🧪 Analyze Your String")
user_string = st.text_input("Enter a string to analyze:", "Hiba")
if user_string:
    st.write(f"Length: {len(user_string)}")
    st.write(f"Uppercase: {user_string.upper()}")
    st.write(f"Reversed: {user_string[::-1]}")
    st.write(f"First Character: {user_string[0] if len(user_string) > 0 else 'N/A'}")

    df = pd.DataFrame({
        "Character": list(user_string),
        "Index": list(range(len(user_string)))
    })
    st.dataframe(df)

# ----- String Methods -----
st.subheader("🧰 Try String Methods")
method = st.selectbox("Choose a method to apply:", ["upper", "lower", "capitalize", "title", "replace", "split"])
replacement = None

if method == "replace":
    old = st.text_input("Old text", "a")
    new = st.text_input("New text", "@")
    replacement = user_string.replace(old, new)
elif method == "split":
    replacement = user_string.split()
else:
    replacement = getattr(user_string, method)()

st.write(f"Result using `{method}()`:", replacement)

# ----- Type Casting Section -----
st.header("2️⃣ Type Casting in Python")
st.markdown("""
Type casting means converting one data type into another using functions like:

- `int()`
- `float()`
- `str()`
- `bool()`
""")

cast_input = st.text_input("🔢 Enter a value to cast:", "123")
if cast_input:
    try:
        st.success(f"int: {int(float(cast_input))}")
        st.success(f"float: {float(cast_input)}")
        st.success(f"str: '{str(cast_input)}'")
        st.success(f"bool: {bool(cast_input)}")
    except:
        st.error("⚠️ Invalid input for numeric casting.")

# ----- Quiz Section -----
st.header("🧠 Mini Quiz: Check Your Understanding!")
q1 = st.radio("1. What is the result of 'hello'.upper()?", ["HELLO", "hello", "Hello"])
q2 = st.radio("2. Which function converts string to integer?", ["str()", "int()", "float()"])

score = 0
if q1 == "HELLO":
    score += 1
if q2 == "int()":
    score += 1

if st.button("Submit Quiz"):
    st.success(f"Your Score: {score}/2")
    if score == 2:
        st.balloons()
    else:
        st.info("Try again! You can do better 😊")

st.markdown("---")
st.info("Made with ❤️ using Streamlit by Hiba")
