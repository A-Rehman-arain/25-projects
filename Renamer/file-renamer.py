import os
import streamlit as st

st.title("Bulk File Renamer")

# File upload widget
uploaded_files = st.file_uploader("Upload Files", accept_multiple_files=True)

# Prefix input
prefix = st.text_input("Enter Prefix for Renaming:")

# Temporary directory to store uploaded files and renamed files
temp_dir = "tmp_renamed_files"
os.makedirs(temp_dir, exist_ok=True)

# Renaming process
if uploaded_files and prefix:
    for uploaded_file in uploaded_files:
        # Save the uploaded file to a temporary path
        file_path = os.path.join(temp_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Extract the file name without the prefix (if it was added previously)
        # Remove the old prefix if it exists
        old_prefix = "old_prefix_"  # Replace this with the actual prefix you want to remove
        file_name_without_old_prefix = uploaded_file.name
        if file_name_without_old_prefix.startswith(old_prefix):
            file_name_without_old_prefix = file_name_without_old_prefix[len(old_prefix):]

        # Now, add the new prefix
        new_file_name = prefix + file_name_without_old_prefix
        new_file_path = os.path.join(temp_dir, new_file_name)

        # Check if the new file name already exists, and if so, append a number
        counter = 1
        while os.path.exists(new_file_path):
            name, ext = os.path.splitext(new_file_name)
            new_file_name = f"{prefix}_{name}_{counter}{ext}"
            new_file_path = os.path.join(temp_dir, new_file_name)
            counter += 1

        # Rename the file
        os.rename(file_path, new_file_path)

        # Display the renaming result
        st.write(f"Renamed {uploaded_file.name} to {new_file_name}")

        # Provide a download link for the renamed file
        with open(new_file_path, "rb") as f:
            st.download_button(
                label=f"Download {new_file_name}",
                data=f,
                file_name=new_file_name,
                mime="application/octet-stream"
            )

# Handle cases where no files are uploaded or no prefix is provided
elif not uploaded_files:
    st.warning("Please upload some files.")
elif not prefix:
    st.warning("Please provide a prefix for renaming.")
