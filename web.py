import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    # "new_todo" is the key of text_input, so it will get the text which we write on the text_input
    todo = st.session_state["new_todo"]
    todos.append(todo + '\n')
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.write_todos(todos)
        del st.session_state[todo]  # delete the key and corresponding value in the session_state dictionary
        st.experimental_rerun()  # rerun the code is necessary

# label is a required argument
st.text_input(label="", placeholder="Add a new todo...", on_change=add_todo, key="new_todo")

# it displays in the terminal
print("Hello")

# we can keep track how it changes in session_state dictionary
# st.session_state