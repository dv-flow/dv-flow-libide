
import os
import pytest
from pytest_dfm import dvflow
import dv_flow.libide as ide
from dv_flow.mgr import TaskGraphBuilder, PackageLoader, TaskSetRunner

def test_smoke(dvflow, tmpdir):

    data_dir = os.path.join(os.path.dirname(__file__), "data/defines")
    runner = TaskSetRunner(os.path.join(tmpdir, 'rundir'))

    def marker_listener(marker):
        raise Exception("marker")

    builder = TaskGraphBuilder(
        PackageLoader(marker_listeners=[marker_listener]).load_rgy(['std', 'ide']),
        os.path.join(tmpdir, 'rundir'))

    top = builder.mkTaskNode(
        'std.FileSet',
        name="top",  
        type="systemVerilogSource", 
        base=os.path.join(data_dir),
        include="top_mod1.v",
        defines=["SPECIAL_DEFINE"])
#    dvflow.mk

    pass
