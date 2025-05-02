import streamlit as st

st.title("Binary Search")

# Input: Sorted list and target number
arr_input = st.text_input("Enter a sorted list (comma separated):", "1,2,3,4,5")
try:
    arr = [int(x) for x in arr_input.split(",")]
    if arr != sorted(arr):
        st.warning("The list must be sorted in ascending order.")
except ValueError:
    st.error("Please enter a valid list of numbers.")
    arr = []

# Set the target number input bounds based on the list's values
if arr:
    target = st.number_input("Enter a number to search:", min_value=min(arr), max_value=max(arr))
else:
    target = None

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    steps = []  # To track search steps for visualization
    while low <= high:
        mid = (low + high) // 2
        steps.append(f"Low: {low}, Mid: {mid}, High: {high}, Comparing {arr[mid]} with {target}")
        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps

# Search when button is clicked
if st.button("Search"):
    if not arr:
        st.warning("Please provide a valid sorted list.")
    else:
        result, steps = binary_search(arr, target)
        if result != -1:
            st.success(f"Element {target} found at index {result}.")
        else:
            st.error("Element not found.")

        # Displaying the search steps
        st.subheader("Search Process:")
        for step in steps:
            st.write(step)
