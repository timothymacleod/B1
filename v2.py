import streamlit as st

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

st.header('Generated CPT Code Bundle')
codes = []

if 'Annual Wellness' in visit_type:
    codes.append('G0438/G0439')
else:
    codes.append('99214')

if brief_test:
    codes.append('96127')

if assessment_choice == 'Cognitive Care Planning (99483)':
    codes.append('99483')
else:
    codes.append('99214/99215')

if cmp:
    codes.append('80053')

if mri:
    codes.append('70551')

if follow_up_acp:
    codes.append('99497')

if st.button('Show CPT Codes & Documentation Notes'):
    st.subheader('Recommended CPT Codes:')
    for code in codes:
        st.write(f'- {code}')

    st.subheader('Important Documentation Tips & Constraints:')
    if '99483' in codes:
        st.write('- 99483: Caregiver must be present; document cognitive testing, functional & safety assessment, medication review, detailed care plan.')
    if '70551' in codes:
        st.write('- 70551 (MRI): Must clearly document cognitive decline to justify imaging.')
    if '99497' in codes:
        st.write('- 99497 (Advance Care Planning): Document at least 16 min discussion with patient consent.')
    if '99214' in codes and 'Annual Wellness' not in visit_type:
        st.write('- 99214: Document moderate complexity medical decision making or 30-39 minutes of total time spent.')
