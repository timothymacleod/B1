import streamlit as st
import pandas as pd

st.title('Alzheimer’s Diagnostic Billing Pathfinder (Enhanced Prototype)')

st.sidebar.header('Provider Type')
provider = st.sidebar.selectbox('Select Provider Type:', ['Primary Care Physician (PCP)', 'Nurse Practitioner (NP)', 'Psychologist', 'Technician'])

st.header('Step 1: Initial Visit Type')
visit_type = st.radio('Choose Initial Visit Type:', ['Annual Wellness Visit (G0438/G0439)', 'Moderate complexity E/M Visit (99214)'])
brief_test = st.checkbox('Include Brief Cognitive Screening (96127 - MMSE/MoCA)')

st.header('Step 2: In-depth Cognitive Assessment')
assessment_options = []

if provider in ['Primary Care Physician (PCP)', 'Nurse Practitioner (NP)']:
    assessment_options.append('Cognitive Care Planning (99483)')
assessment_options.append('Standard E/M Visit (99214/99215)')

assessment_choice = st.selectbox('Select Cognitive Assessment Method:', assessment_options)

if assessment_choice == 'Cognitive Care Planning (99483)':
    st.warning('99483 Requirements: Caregiver present, comprehensive cognitive testing, functional status, safety assessment, medication review, care plan documented, ~50 mins face-to-face.')

st.header('Step 3: Labs & Imaging (optional)')
cmp = st.checkbox('Comprehensive Metabolic Panel (CMP - 80053)')
mri = st.checkbox('Brain MRI (70551 - requires documentation of cognitive decline)')

st.header('Step 4: Follow-up and Advance Care Planning')
follow_up_acp = st.checkbox('Advance Care Planning (99497 - requires min. 16 mins documented discussion)')

st.header('Generated CPT Code Bundle and Requirements')
cpt_data = []

if 'Annual Wellness' in visit_type:
    cpt_data.append(['Annual Wellness Visit', 'G0438/G0439', 'PCP, NP', 'N/A', 'Standard AWV components documented'])
else:
    cpt_data.append(['Moderate complexity E/M', '99214', 'PCP, NP', '30-39 mins or moderate MDM', 'MDM or time clearly documented'])

if brief_test:
    cpt_data.append(['Brief Cognitive Screening', '96127', 'PCP, NP, Psychologist', 'Brief (~5 mins)', 'Standard cognitive screening instruments (e.g., MMSE, MoCA)'])

if assessment_choice == 'Cognitive Care Planning (99483)':
    cpt_data.append(['Cognitive Care Planning', '99483', 'PCP, NP', '50 mins', 'Caregiver presence, comprehensive cognitive testing, functional & safety assessment, medication review, detailed care plan'])
else:
    cpt_data.append(['Standard E/M Visit', '99214/99215', 'PCP, NP', '30-54 mins or moderate/high MDM', 'MDM or total time clearly documented'])

if cmp:
    cpt_data.append(['Comprehensive Metabolic Panel', '80053', 'PCP, NP', 'N/A', 'Lab order documented'])

if mri:
    cpt_data.append(['Brain MRI', '70551', 'PCP, NP', 'N/A', 'Clear documentation of cognitive decline for medical necessity'])

if follow_up_acp:
    cpt_data.append(['Advance Care Planning', '99497', 'PCP, NP', '16 mins minimum', 'Discussion of care goals, patient consent clearly documented'])

cpt_df = pd.DataFrame(cpt_data, columns=['Service', 'CPT Code', 'Who Can Bill', 'Time/MDM Requirements', 'Documentation & Instruments'])

if st.button('Show CPT Codes & Requirements Chart'):
    st.subheader('Recommended CPT Codes and Billing Requirements:')
    st.table(cpt_df)
