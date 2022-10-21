import streamlit as st

# title
st.markdown("# Portfolio WebApp")
st.sidebar.markdown("# Portfolio WebApp")
st.sidebar.subheader('Full project on [GitHub](https://github.com/aaAbdulkadir/DevOps/tree/main/project)')

# caption
caption = '''
    A cloud based CI/CD pipeline of my portfolio webapp created using Streamlit.
'''
st.caption(caption)

overview, technologies, architectures = st.tabs(["Overview", "Technologies", "Architecture"])

with overview:
    overview_string = """
        This project consisted of creating a CI/CD pipeline using Jenkins 
        for a portfolio web application created on Streamlit. Jenkins was 
        provisioned on an Azure virtual machine. The Jenkins pipeline 
        consists of a webhook to the GitHub repo which contains the files 
        and pulls it into Jenkins The pipeline builds a docker image of the 
        portfolio webapp and pushes it into Azure Container Registry, where 
        the image uploaded is pulled to Azure Kubernetes Service to create a 
        cluster of the application and deploy it.
    """
    outcome_string = """
        From this project, I learnt how to use Jenkins to create a CI/CD pipeline, 
        how to deploy an application using Kubernetes and how to do these things on 
        Azure, i.e. provising a Jenkins server, creating an Azure Container Registry and 
        creating an Azure Kubernetes Service which deployed the cluster.
    """
    st.subheader('Outline')
    st.markdown(overview_string)
    st.subheader('Learning Outcome')
    st.markdown(outcome_string)
with technologies:
    st.subheader('Technologies Implemented')
    with st.expander("Jenkins"):
        st.write('Created a CI/CD pipeline to build and deploy the web app.')
    with st.expander("Kubernetes"):
        st.write('Created a Kubernetes cluster on Azure Kubernetes Service using the webapp docker image.')
    with st.expander("Terraform"):
        st.write('Provisioned Infrastructure as Code on Azure for a resource group that contained a virtual machine, a container registry and kubernetes service.')
    with st.expander("Azure"):
        st.write('Provisioned a virtual machine for the jenkins pipeline to run on, which built a docker image of the web app and pushed it into the container registry, which was pulled to the kubernetes service for deployment.')
with architectures:
    st.subheader('Architectural Diagram')
    st.image('pages/plan.png')
