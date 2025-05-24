import streamlit as st
import pandas as pd

st.title('Alzheimer’s Diagnostic Billing Pathfinder (Enhanced Prototype)')

provider_options = ['Primary Care Physician (PCP)', 'Nurse Practitioner (NP)', 'Psychologist', 'Technician']

st.header('Step 1: Initial Visit Type')
initial_provider = st.selectbox('Select Provider for Initial Visit:', ['PCP', 'NP'])
visit_type = st.radio('Choose Initial Visit Type:', ['Annual Wellness Visit (G0438/G0439)', 'Moderate complexity E/M Visit (99214)'])
brief_test = st.checkbox('Include Brief Cognitive Screening (96127 - MMSE/MoCA)')
brief_provider = None
if brief_test:
    brief_provider = st.selectbox('Provider for Brief Cognitive Screening:', ['PCP', 'NP', 'Psychologist'])

st.header('Step 2: In-depth Cognitive Assessment')
assessment_choice = st.selectbox('Select Cognitive Assessment Method:', ['Cognitive Care Planning (99483)', 'Standard E/M Visit (99214/99215)'])
assessment_provider = st.selectbox('Provider for In-depth Assessment:', ['PCP', 'NP', 'Psychologist'])

if assessment_choice == 'Cognitive Care Planning (99483)':
    st.warning('99483 Requirements: Caregiver present, comprehensive cognitive testing, functional status, safety assessment, medication review, care plan documented, ~50 mins face-to-face.')

st.header('Step 3: Labs & Imaging (optional)')
labs_provider = st.selectbox('Provider ordering Labs:', ['PCP', 'NP'])
cmp = st.checkbox('Comprehensive Metabolic Panel (CMP - 80053)')
imaging_provider = st.selectbox('Provider ordering Imaging:', ['PCP', 'NP'])
mri = st.checkbox('Brain MRI (70551 - requires documentation of cognitive decline)')

st.header('Step 4: Follow-up and Advance Care Planning')
followup_provider = st.selectbox('Provider for Follow-up/ACP:', ['PCP', 'NP'])
follow_up_acp = st.checkbox('Advance Care Planning (99497 - requires min. 16 mins documented discussion)')

st.header('Generated CPT Code Bundle and Requirements')
cpt_data = []

cpt_data.append(['Initial Visit', visit_type.split(' ')[-1], initial_provider, '30-39 mins or moderate MDM', 'MDM or time clearly documented'])

if brief_test:
    cpt_data.append(['Brief Cognitive Screening', '96127', brief_provider, 'Brief (~5 mins)', 'Standard cognitive screening instruments (e.g., MMSE, MoCA)'])

if assessment_choice == 'Cognitive Care Planning (99483)':
    cpt_data.append(['Cognitive Care Planning', '99483', assessment_provider, '50 mins', 'Caregiver presence, comprehensive cognitive testing, functional & safety assessment, medication review, detailed care plan'])
else:
    cpt_data.append(['Standard E/M Visit', '99214/99215', assessment_provider, '30-54 mins or moderate/high MDM', 'MDM or total time clearly documented'])

if cmp:
    cpt_data.append(['Comprehensive Metabolic Panel', '80053', labs_provider, 'N/A', 'Lab order documented'])

if mri:
    cpt_data.append(['Brain MRI', '70551', imaging_provider, 'N/A', 'Clear documentation of cognitive decline for medical necessity'])

if follow_up_acp:
    cpt_data.append(['Advance Care Planning', '99497', followup_provider, '16 mins minimum', 'Discussion of care goals, patient consent clearly documented'])

cpt_df = pd.DataFrame(cpt_data, columns=['Service', 'CPT Code', 'Who Can Bill', 'Time/MDM Requirements', 'Documentation & Instruments'])

if st.button('Show CPT Codes & Requirements Chart'):
    st.subheader('Recommended CPT Codes and Billing Requirements:')
    st.table(cpt_df)
