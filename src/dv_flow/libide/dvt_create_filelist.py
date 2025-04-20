
from dv_flow.mgr import TaskDataInput, TaskRunCtxt

async def CreateFilelist(ctxt : TaskRunCtxt, input : TaskDataInput):

    fp = open(ctxt.roo)

    for fs in input.inputs:
        pass



