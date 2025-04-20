import os
from dv_flow.mgr import TaskDataInput, TaskDataResult, TaskRunCtxt

async def UpdateFileList(ctxt : TaskRunCtxt, input : TaskDataInput) -> TaskDataResult:
    """Update the file list in the IDE"""
    changed = input.changed

    fp = open(os.path.join(ctxt.root_pkgdir, "verible.filelist"), "w")

    for fs in input.inputs:
        if hasattr(fs, "incdirs"):
            for d in fs.incdirs:
                fp.write("+incdir+%s\n" % os.path.join(fs.basedir, d))

        if hasattr(fs, "files"):
            for f in fs.files:
                fp.write("%s\n" % os.path.join(fs.basedir, f))


