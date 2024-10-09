from ...models.pipeline import Pipeline
from .steps import StepStarted, StepAdding, StepDone
from typing import Any, List

class BusinessProcess:

    STARTED = "Started"
    ADDING = "Adding"
    #TODO: Implement the other steps
    DONE = "Done"

    @staticmethod
    def forward(pipeline: Pipeline):
        steps = BusinessProcess.get_steps()
        index = steps.index(pipeline.step)
        pipeline.step = steps[min(index+1, len(steps)-1)]

    @staticmethod
    def get_steps() -> List[str]:
        return [
            BusinessProcess.STARTED,
            BusinessProcess.ADDING,
            #TODO: Implement the other steps
            BusinessProcess.DONE,
        ]
    
    @staticmethod
    def run(orchestrator, pipeline: Pipeline):
        if pipeline.step == BusinessProcess.STARTED:
            StepStarted.run(orchestrator, pipeline)
            BusinessProcess.forward(pipeline)
        if pipeline.step == BusinessProcess.ADDING:
            StepAdding.run(orchestrator, pipeline)
            BusinessProcess.forward(pipeline)
        #TODO: Implement the other steps
        if pipeline.step == BusinessProcess.DONE:
            StepDone.run(orchestrator, pipeline)