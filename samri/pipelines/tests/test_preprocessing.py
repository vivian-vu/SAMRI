from samri.pipelines.preprocess import generic, legacy
from samri.pipelines import manipulations

BIDS_BASE = '/home/vivian/samri_bidsdata/bids_rs'

# Takes too long
def test_generic():
	generic(BIDS_BASE,
		'/usr/share/mouse-brain-atlases/dsurqec_200micron.nii',
		registration_mask='/usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii',
		functional_match={'acquisition':['EPIlowcov'],},
		structural_match={'acquisition':['TurboRARElowcov'],},
		out_base='/home/vivian/samri_bidsdata/rs_preprocessing/',
		workflow_name='prep',
		)
