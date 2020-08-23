from samri.pipelines.preprocess import generic, legacy
from samri.pipelines import manipulations
import tempfile
import shutil

BIDS_BASE = '/home/vivian/samri_bidsdata/bids_rs'
#tmp_out_base = tempfile.mkdtemp(dir = '/home/vivian/samri_bidsdata/')

# Takes too long
def test_generic():
        generic(BIDS_BASE,
                '/usr/share/mouse-brain-atlases/dsurqec_200micron.nii',
                registration_mask='/usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii',
                functional_match={'acquisition':['EPIlowcov'],},
                structural_match={'acquisition':['TurboRARElowcov'],},
                out_base='/home/vivian/samri_bidsdata/bids_rs_tmp',
                workflow_name='prep',
                )
        #shutil.rmtree(tmp_out_base)
