from samri.manipulations import flip_axis
import tempfile, shutil

def test_flip_axis():
        nii_path = '/usr/share/samri_bidsdata/bids_collapsed/sub-4007/ses-ofM/func/sub-4007_ses-ofM_task-JogB_acq-EPIlowcov_run-0_bold.nii.gz'
        tmp_out_base = tempfile.mkdtemp(dir = '/var/tmp/samri_testing/pytest/')
        flip_axis(nii_path,out_path = tmp_out_base)
        shutil.rmtree(tmp_out_base)
