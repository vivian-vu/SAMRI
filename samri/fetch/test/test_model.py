def test_abi_connectivity_map():
	import tempfile, shutil
        from samri.fetch.model import abi_connectivity_map
	tmp_out_base = tempfile.mkdtemp(dir = '/var/tmp/samri_testing/pytest/')
        abi_connectivity_map('ventral_tegmental_area',
		invert_lr_experiments=[
			"127651139",
			"127796728",
			"127798146",
			"127867804",
			"156314762",
			"160539283",
			"160540751",
			"165975096",
			"166054222",
			"171021829",
			"175736945",
			"278178382",
			"292958638",
			"301062306",
			"304337288",
			],
		exclude_experiments=['175736945','301062306'],
		save_as_zstat='{}/vta_zstat.nii.gz'.format(tmp_out_base),
		save_as_tstat='{}/vta_tstat.nii.gz'.format(tmp_out_base),
		save_as_cope='{}/vta_cope.nii.gz'.format(tmp_out_base),
		)
        shutil.rmtree(tmp_out_base)
