import streamlit as st

st.title('Alzheimer’s Diagnostic Billing Pathfinder (Prototype)')

st.header('Step 1: Initial Encounter')
annual_wellness = st.checkbox('Annual Wellness Visit (Cognitive Screen)')
concern_em = st.checkbox('Concern-based Visit (E/M)')
brieftest = st.checkbox('Brief Cognitive Assessment (MMSE/MoCA)')

st.header('Step 2: In-depth Cognitive Assessment')
care_plan = st.checkbox('Cognitive Care Planning (99483)')
neuropsych_test = st.checkbox('Neuropsych Testing (provider or tech-administered)')
digital_tool = st.checkbox('Digital Cognitive Tool')

st.header('Step 3: Rule-Out Labs')
cmp = st.checkbox('Comprehensive Metabolic Panel (CMP)')
tsh = st.checkbox('TSH Test')
b12 = st.checkbox('Vitamin B12 Test')

st.header('Step 4: Imaging')
mri = st.checkbox('Brain MRI')

st.header('Step 5: Follow-up and Referrals')
follow_up = st.checkbox('PCP Follow-up Visit')
advance_care_plan = st.checkbox('Advance Care Planning')

st.header('Generated CPT Code Bundle')
codes = []

if annual_wellness:
    codes.append('G0438/G0439')
if concern_em:
    codes.append('99213/99214')
if brieftest:
    codes.append('96127')
if care_plan:
    codes.append('99483')
if neuropsych_test:
    codes.append('96136/96138')
if digital_tool:
    codes.append('99453/99454 or unlisted')
if cmp:
    codes.append('80053')
if tsh:
    codes.append('84443')
if b12:
    codes.append('82607')
if mri:
    codes.append('70551')
if follow_up:
    codes.append('99214')
if advance_care_plan:
    codes.append('99497')

if st.button('Show CPT Codes'):
    st.subheader('Recommended CPT Codes:')
    for code in codes:
        st.write(f'- {code}')

    st.subheader('Documentation Tips & Notes:')
    if '99483' in codes:
        st.write('- 99483 requires detailed documentation including caregiver involvement and care planning.')
    if '99497' in codes:
        st.write('- 99497 (Advance Care Planning) requires documentation of at least 16 min of discussion.')
    if '99214' in codes and (annual_wellness or concern_em):
        st.write('- Add modifier -25 to 99214 if billed alongside wellness or cognitive planning visits.')
