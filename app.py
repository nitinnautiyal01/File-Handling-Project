# CRUD Operation in UI using Streamlit

import streamlit as st
from pathlib import Path

# PAGE SETUP 
st.set_page_config(page_title="File CRUD Operations", page_icon="📝", layout="centered")
st.title(" File CRUD Operations")
st.caption("Create, Read, Update, and Delete files easily via this dashboard.")

# NAVIGATION
# Using a sidebar for a clean interface
operation = st.sidebar.radio(
    "Choose an Operation",
    ["Create File", "Read File", "Update File", "Delete File"]
)

st.subheader(f"{operation}")
st.divider()

# CREATE FILE
if operation == "Create File":
    file_name = st.text_input("Enter new file name (e.g., notes.txt):")
    data = st.text_area("Write content:")
    
    if st.button("Create File", type="primary"):
        if file_name:
            path = Path(file_name)
            if not path.exists():
                try:
                    with open(path, "w") as file:
                        file.write(data)
                    st.success(f" File '{file_name}' created successfully!")
                except Exception as error:
                    st.error(f"Error: {error}")
            else:
                st.warning("File already exists!")
        else:
            st.error("Please provide a valid file name.")

# READ FILE
elif operation == "Read File":
    file_name = st.text_input("Enter file name to read:")
    
    if st.button("Read File", type="primary"):
        if file_name:
            path = Path(file_name)
            if path.exists():
                try:
                    with open(path, "r") as file:
                        content = file.read()
                    st.info("**File Content:**")
                    st.text_area("Content", value=content, height=200, disabled=True)
                except Exception as error:
                    st.error(f"Error: {error}")
            else:
                st.warning("File does not exist!")
        else:
            st.error("Please provide a file name.")

# UPDATE FILE
elif operation == "Update File":
    file_name = st.text_input("Enter file name to update:")
    
    if file_name:
        path = Path(file_name)
        if path.exists():
            update_action = st.radio(
                "What action would you like to take?",
                ["Rename File", "Append Content", "Overwrite Content"]
            )
            
            # Rename
            if update_action == "Rename File":
                new_name = st.text_input("Enter new file name:")
                if st.button("Rename", type="primary"):
                    if new_name:
                        new_path = Path(new_name)
                        if not new_path.exists():
                            try:
                                path.rename(new_path)
                                st.success(f"🔄 File renamed to '{new_name}' successfully!")
                            except Exception as error:
                                st.error(f"Error: {error}")
                        else:
                            st.warning("A file with that name already exists!")
                    else:
                        st.error("Please provide a new file name.")
            
            # Append
            elif update_action == "Append Content":
                append_data = st.text_area("Enter content to add:")
                if st.button("Append", type="primary"):
                    try:
                        with open(path, "a") as file:
                            file.write("\n" + append_data)
                        st.success(" Content successfully appended!")
                    except Exception as error:
                        st.error(f"Error: {error}")
            
            # Overwrite
            elif update_action == "Overwrite Content":
                overwrite_data = st.text_area("Enter new content:")
                if st.button("Overwrite", type="primary"):
                    try:
                        with open(path, "w") as file:
                            file.write(overwrite_data)
                        st.success("Content successfully overwritten!")
                    except Exception as error:
                        st.error(f"Error: {error}")
        else:
            st.warning("File does not exist!")

# DELETE FILE 
elif operation == "Delete File":
    file_name = st.text_input("Enter file name to delete:")
    
    if st.button("Delete File", type="primary"):
        if file_name:
            path = Path(file_name)
            if path.exists():
                try:
                    path.unlink()
                    st.success(f"File '{file_name}' deleted successfully!")
                except Exception as error:
                    st.error(f"Error: {error}")
            else:
                st.warning("File does not exist!")
        else:
            st.error("Please provide a file name.")
