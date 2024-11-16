import streamlit as st
from poka import research_task, generate_use_cases, search_datasets_based_on_use_cases

# Streamlit UI
st.title("Smart Data Navigator")
st.write("Unlock valuable insights and datasets tailored to your company's needs, all powered by smart research and strategic use cases.")


# Input for the company name
company_name = st.text_input("Enter Company Name", "")

if company_name:
    # Research for the company
    st.write(f"Performing research for {company_name}...")
    research_results = research_task(company_name)

    if research_results:
        # Generate use cases based on the research
        st.write(f"Generating use cases for {company_name}...")
        use_case_results = generate_use_cases(company_name, research_results)

        if use_case_results:
            # Display use case results
            st.subheader("Generated Use Cases")
            st.write(use_case_results)

            # Search for relevant datasets based on the use cases
            st.write(f"Searching for relevant datasets based on the generated use cases...")
            dataset_message = search_datasets_based_on_use_cases(use_case_results, company_name)  # Returns status message

            # Display the message about datasets in Streamlit
            st.subheader("Relevant Datasets")
            if dataset_message and "Relevant datasets have been saved" in dataset_message:
                st.write(dataset_message)
            else:
                st.write(dataset_message)
        else:
            st.write("No use cases generated.")
    else:
        st.write("Research failed. Unable to retrieve information.")
else:
    st.write("Please enter a company name to proceed.")
