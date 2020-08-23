from samri.pipelines.reposit import bru2bids
import tempfile
import shutil

BRU_DIR = '/usr/share/samri_bindata/'
tmp_out_base = tempfile.mkdtemp(dir = '/var/tmp/samri_testing/pytest/')
# The `20180730_053743_6587_1_1` measurement is acquired with the (incorrect) Bruker ParaVision Prone (i.e. supine) orientation.
# This is relevant for testing the flip_if_needed function

def test_bru2bids():
        bru2bids(BRU_DIR,
                inflated_size=False,
                functional_match={"acquisition":["EPI"]},
                structural_match={"acquisition":["TurboRARE"]},
                out_base=tmp_out_base,
                #keep_crashdump=True,
                keep_work=True,
                )
        shutil.rmtree(tmp_out_base)
