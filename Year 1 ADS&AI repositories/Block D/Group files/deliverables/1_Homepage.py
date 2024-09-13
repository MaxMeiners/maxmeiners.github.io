import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

def set_page_configuration():
    """
    Sets the configuration for the homepage of Streamlit.
    """
    st.set_page_config(
        page_title="Welcome on the homepage of group 10!",
        page_icon="🏠",
        layout="wide",
    )

# Call the function to set the page configuration
set_page_configuration()

def main():
    """
    The main function that sets up the Streamlit app and displays the homepage of group 10.
    """
    st.title("Our research question")
    st.markdown("What factors should Breda municipality consider for resource allocation to prevent public nuisance? Can an algorithm help predict the risk of public nuisance in specific areas?")
    st.subheader("The Problem")
    st.markdown("In the context of our school project, we have taken up the task of creating a machine learning model to address the issue of public nuisance in the municipality of Breda. Our motivation for choosing this research question stems from the desire to contribute to the improvement of the local community and enhance the overall quality of life for its residents.")
    st.markdown("Recognizing that resource allocation plays a crucial role in combating public nuisance effectively, we aim to identify the most important factors that the municipality of Breda should consider. By analyzing relevant data and exploring various variables, we seek to provide valuable insights and recommendations to assist the municipality in making informed decisions about resource allocation.")
    st.image("deliverables/aicanvas.png")
    st.markdown("---")

    st.title("Team Members")
    st.markdown("Our team consists of four members with diverse backgrounds and skill sets. We are all students at Breda University of Applied Sciences, enrolled in the Data Science and Artificial Intelligence program. We are passionate about data science and machine learning and are excited to apply our knowledge and skills to solve real-world problems.")
    st.markdown("---")
    
    # Create a list of dictionaries containing the member data
    member_data = [
        {
            "name": "Max Meiners",
            "image_path": "team_pictures/picture_max.png",
            "description": "Max is an experienced software engineer with expertise in web development and machine learning.",
            "Personal GitHub page": "https://github.com/MaxMeiners",
            "Group 10 GitHub page": "https://github.com/BredaUniversityADSAI/2022-23d-1fcmgt-reg-ai-01-group-team10",
        },
        {
            "name": "Michal Dziechciarz",
            "image_path": "team_pictures/picture_michal.png",
            "description": "Michal is a talented designer who specializes in user interface and user experience design.",
            "Personal GitHub page": "https://github.com/MichalDziechciarz225484",
            "Group 10 GitHub page": "https://github.com/BredaUniversityADSAI/2022-23d-1fcmgt-reg-ai-01-group-team10",
        },
        {
            "name": "Marwa Rouah",
            "image_path": "team_pictures/picture_marwa.png",
            "description": "Marwa is a Data Science and AI student at BUAS with a passion for machine learning and data analysis.",
            "Personal GitHub page": "https://github.com/IsavanderMierde224299",
            "Group 10 GitHub page": "https://github.com/BredaUniversityADSAI/2022-23d-1fcmgt-reg-ai-01-group-team10",
        },
        {
            "name": "Isa van der Mierde",
            "image_path": "team_pictures/picture_isa.png",
            "description": "Isa is a full stack developer who specializes in creating delightful, user-friendly software.",
            "Personal GitHub page": "https://github.com/IsavanderMierde224299",
            "Group 10 GitHub page": "https://github.com/BredaUniversityADSAI/2022-23d-1fcmgt-reg-ai-01-group-team10",
        }
    ]
    
    col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the column widths as needed
    
    selected_member = None
    
    for i, member in enumerate(member_data):
        if i % 2 == 0:
            column = col1
        else:
            column = col3
            
        with column:
            image = Image.open(member["image_path"])
            st.image(image, caption=member["name"], width=150)
            
            if st.button(f"Select {member['name']}"):
                selected_member = member
            
            st.markdown("---")

    with col2:
        if selected_member is not None:
            show_member_details(selected_member)

# Function to show the member details
def show_member_details(member):
    """
    Function to show the details of a team member.

    Args:
        member (dict): A dictionary containing the details of a team member.

    Returns:
        None
    """
    st.write(f"**Name:** {member['name']}")
    st.write(f"**Description:** {member['description']}")
    st.write(f"**Personal GitHub page:** {member['Personal GitHub page']}")
    st.write(f"**Group 10 GitHub page:** {member['Group 10 GitHub page']}")
    image = Image.open(member["image_path"])
    st.image(image, caption=member["name"], width=300)

if __name__ == "__main__":
    main()