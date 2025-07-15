import streamlit as st
import requests 
import typing_extensions 
def get_random_jokes():
    """Fetch the jokes from api"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data = response.json()
            # Return formatted joke with setup and punchline (dictionary keys)
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        else:
            # Return error message if API call fails
            return "Failed to fetch a joke. Please try again later."
    except Exception as e:
        return "Searching a good joke for you"
    

def main():
    """Main function to run the Streamlit app"""
    # Set page title
    st.title("Random Joke Generator")
    # Add instruction text
    st.write("Click the button below to generate a random Joke")

    # Create button and handle click
    if st.button("Generate Joke"):
        # Get random joke when button clicked
        joke = get_random_jokes()
        # Display joke with success styling
        st.success(joke)
st.markdown("---")

st.markdown(
    """
    <div style='text-align:center;'>
        <p>Joke from Official Joke API</p>
        <p>Build with ❤️ by <a href='https://github.com/Abdullahkhan'>Abdullah khan</a> using Streamlit</p>
    </div>
    """, 
    unsafe_allow_html=True
)










if __name__ == "__main__":
    main()
