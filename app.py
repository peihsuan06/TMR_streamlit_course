import streamlit as st

my_variable = "app.py Page"

def main():
    st.title("Streamlit Multi-Page")
    st.subheader("Main Page")
    st.write(my_variable)

    choice = st.sidebar.selectbox("SubMenu",["Pandas","Tensforflow"])
    if choice == "Pandas":
        st.subheader("Pandas")

if __name__ == '__main__':
    main()
