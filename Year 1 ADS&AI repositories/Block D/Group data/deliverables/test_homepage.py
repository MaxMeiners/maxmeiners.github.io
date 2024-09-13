from Homepage import show_member_details


def test_show_member_details():
    member = {
        "name": "Max Meiners",
        "image_path": "team_pictures\picture_max.png",
        "description": "Max is an experienced software engineer with expertise in web development and machine learning.",
        "Personal GitHub page": "https://github.com/MaxMeiners",
        "Group 10 GitHub page": "https://github.com/BredaUniversityADSAI/2022-23d-1fcmgt-reg-ai-01-group-team10",
    }

    result = show_member_details(member)

    assert result == True
