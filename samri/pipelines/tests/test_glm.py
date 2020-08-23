from samri.pipelines.glm import l1, l1_physio, seed
import tempfile
import shutil

#PREPROCESS_BASE = '/usr/share/samri_bidsdata/preprocessing'
PREPROCESS_BASE = '/home/vivian/samri_bidsdata/rs_preprocessing/prep/'

def test_l1():
	#tmp_out_base = tempfile.mkdtemp(dir ='/var/tmp/samri_testing/pytest/')
        l1(PREPROCESS_BASE,
		mask='mouse',
		match={'session': ['ofMaF'], 'acq':['EPIlowcov']},
		out_base='/home/vivian/samri_bidsdata/rs_l1',
		workflow_name='l1',
		keep_work=True,
                )
        #shutil.rmtree(tmp_out_base)

# Takes too long or hangs
def test_physio():
	tmp_out_base = tempfile.mkdtemp(dir ='/var/tmp/samri_testing/pytest/')
        l1_physio(PREPROCESS_BASE, 'astrocytes',
		highpass_sigma=180,
		convolution=False,
		mask='mouse',
		n_jobs_percentage=.33,
		match={
			'modality':['bold'],
			'session':['ofM'],
			},
		invert=False,
		workflow_name='l1_astrocytes',
		out_base=tmp_out_base,
		)
        shutil.rmtree(tmp_out_base)

# Takes too long or hangs
def test_seed():
	tmp_out_base = tempfile.mkdtemp(dir ='/var/tmp/samri_testing/pytest/')
        seed(PREPROCESS_BASE,'/usr/share/mouse-brain-atlases/dsurqec_200micron_roi-dr.nii',
		match={"acq":["EPIlowcov"]},
		out_base=tmp_out_base,
		workflow_name='dr_fc',
		)
        shutil.rmtree(tmp_out_base)

