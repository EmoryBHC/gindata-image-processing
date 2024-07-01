import os
def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes
def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where
    allowed template fields - follow python string module:
    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """
    t1w_3d = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_run-{item:01d}_acq-3d_T1w')
    t1w_ax = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_run-{item:01d}_acq-ax_T1w')
    t1w_sag = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_run-{item:01d}_acq-sag_T1w')
    t1w_cor = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_run-{item:01d}_acq-cor_T1w')

    t2w_3d = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_run-{item:01d}_acq-3d_T2w')
    t2w_2d = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_run-{item:01d}_acq-2d_T2w')

    flair_3d = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_run-{item:01d}_acq-3d_FLAIR')
    flair_ax = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_run-{item:01d}_acq-ax_FLAIR')
    flair_sag = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_run-{item:01d}_acq-sag_FLAIR')
    flair_cor = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_run-{item:01d}_acq-cor_FLAIR')

    dwi = create_key('{bids_subject_session_dir}/dwi/{bids_subject_session_prefix}_run-{item:01d}_dwi')
    rest = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-rest_rec-{rec}_run-{item:01d}_bold')
    ADC = create_key('{bids_subject_session_dir}/dwi/{bids_subject_session_prefix}_run-{item:01d}_ADC')

    info = {t1w_3d: [], t1w_ax: [], t1w_sag: [], t1w_cor: [],  t2w_3d: [], t2w_2d: []}

    for s in seqinfo:
        if (s.dim4 == 1) and ('ORIGINAL' in s.image_type) and ('loc' not in s.series_description.lower()) and ('tof' not in s.series_description.lower()) and ('3D' in s.AcquisitionType) and (('t1' in s.series_description.lower()) or ('mpr' in s.series_description.lower()) or ('mp-rage' in s.series_description.lower()) or ('flash' in s.series_description.lower())  or ('bravo' in s.series_description.lower()) or ('tfl' in s.sequence_name.lower()) or ('1 mm' in s.series_description)):
           info[t1w_3d].append(s.series_id) # append if multiple series meet criteria  
        if (s.dim4 == 1) and ('loc' not in s.series_description.lower()) and ('tof' not in s.series_description.lower()) and ('ax' in s.series_description.lower()) and ('t1' in s.series_description.lower()):
           info[t1w_ax].append(s.series_id) # append if multiple series meet criteria
        if (s.dim4 == 1) and ('loc' not in s.series_description.lower()) and ('tof' not in s.series_description.lower()) and ('sag' in s.series_description.lower()) and ('t1' in s.series_description.lower()):
           info[t1w_sag].append(s.series_id) # append if multiple series meet criteria 
        if (s.dim4 == 1) and ('loc' not in s.series_description.lower()) and ('tof' not in s.series_description.lower()) and ('cor' in s.series_description.lower()) and ('t1' in s.series_description.lower()):
           info[t1w_cor].append(s.series_id) # append if multiple series meet criteria 


        if (s.dim4 == 1) and ('ORIGINAL' in s.image_type) and ('loc' not in s.series_description.lower()) and ('tof' not in s.series_description.lower()) and ('3D' in s.AcquisitionType) and (('t2' in s.series_description.lower()) ):
           info[t2w_3d].append(s.series_id) # append if multiple series meet criteria 
        if (s.dim4 == 1) and ('ORIGINAL' in s.image_type) and ('loc' not in s.series_description.lower()) and ('tof' not in s.series_description.lower()) and ('2D' in s.AcquisitionType) and (('t2' in s.series_description.lower()) ):
           info[t2w_2d].append(s.series_id)    

        if (s.dim4 == 1) and ('ORIGINAL' in s.image_type) and ('loc' not in s.series_description.lower()) and ('tof' not in s.series_description.lower()) and ('post' not in s.series_description.lower()) and ('repeat' not in s.series_description.lower()) and ('3D' in s.AcquisitionType) and ('flair' in s.series_description.lower()):
           info[flair_3d].append(s.series_id) # append if multiple series meet criteria
        if (s.dim4 == 1) and ('ORIGINAL' in s.image_type) and ('loc' not in s.series_description.lower()) and ('tof' not in s.series_description.lower()) and ('post' not in s.series_description.lower()) and ('repeat' not in s.series_description.lower()) and  ('ax' in s.AcquisitionType) and ('flair' in s.series_description.lower()):
           info[flair_ax].append(s.series_id) # append if multiple series meet criteria
        if (s.dim4 == 1) and ('ORIGINAL' in s.image_type) and ('loc' not in s.series_description.lower()) and ('tof' not in s.series_description.lower()) and ('post' not in s.series_description.lower()) and ('repeat' not in s.series_description.lower()) and ('sag' in s.AcquisitionType) and ('flair' in s.series_description.lower()):
           info[flair_sag].append(s.series_id) # append if multiple series meet criteria
        if (s.dim4 == 1) and ('ORIGINAL' in s.image_type) and ('loc' not in s.series_description.lower()) and ('tof' not in s.series_description.lower()) and ('post' not in s.series_description.lower()) and ('repeat' not in s.series_description.lower()) and ('cor' in s.AcquisitionType) and ('flair' in s.series_description.lower()):
           info[flair_cor].append(s.series_id) # append if multiple series meet criteria  

    return info


        # if (s.dim3 == 72) and (s.dim4 == 1) and ('diffusion' in s.protocol_name):
        #   info[dwi].append(s.series_id) # append if multiple series meet criteria
        # if (s.dim3 <= 25) and ('ADC' in s.series_description):
        #     info[ADC].append(s.series_id) # append if multiple series meet criteria
        # if (s.dim4 > 10) and ('taskrest' in s.protocol_name):
        #     if not s.is_motion_corrected:
        #         info[rest].append({'item': s.series_id[0], 'rec': 'uncorrected'})


