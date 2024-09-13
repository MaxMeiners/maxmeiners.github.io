def covid_flowchart():
    symptoms = input("\nPlease answer with Yes or No. Do you have one of the following symptoms: Symptoms of a cold such as a stuffy or runny nose, sneezing o a sore throat; shortness of breath; a cough; a temperature above 38 degrees Celsius of a fever; sudden loss of smell or taste (without having a blocked nose)")
    if symptoms == "Yes":
        results_1 = input("\nDo the results of the test indicate that you carry the coronavirus?")
        if results_1 == "Yes":
            print("You may only return to the campus/your internship If you have been symptom-free 24 hours and Is at least 7 days since you first got sick.")
        else:
            breath = input("\nIs someone in your household experiencing shortness of breath?")
            if breath == "Yes":
                results_fam = input("\nDo the results indicate your family member carries the virus?")
                if results_fam == "Yes":
                    print("Stay at home for 10 days and follow the GGD instructions")
                else:
                    contact = input("\nDo you know that you have been in close contact with someone who tested positive: ")
                    if contact == "Yes":
                        print("Stay at home and go into quarantine for 10 days")
                    else:
                        print("You can come to the office")
            else:
                contact = input("\nDo you know that you have been in close contact with someone who tested positive: ")
                if contact == "Yes":
                    print("Stay at home and go into quarantine for 10 days")
                else:
                        print("You can come to the office")
    else:
        breath = input("\nDoes someone in your household have a fever and/or is experiencing shortness of breath?")
        if breath == "Yes":
            results_fam = input("\nDo the result of the test indicate that the household member carries the coronavirus?")
            if results_fam == "Yes":
                 print("Stay at home for 10 days and follow the GGD instructions")
            else:
                contact = input("\nDo you know that you have been in close contact with someone who has tested positive for the coronavirus")
                if contact == "Yes":
                    print("Stay at home for 10 days and follow the instructions issued by the GGD.")
                else:
                    print("You can come to the office.")
        else:
            contact_2 = input("\nDo you know that you have been in close contact with someone who tested positive: ")
            if contact_2 == "Yes":
                print("Stay at home for 10 days and follow the instructions issued by the GGD.")
            else:
                print("You can come to the office.")
    

            

covid_flowchart()