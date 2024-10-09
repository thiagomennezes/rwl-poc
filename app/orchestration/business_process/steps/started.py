class StepStarted:
    
    @staticmethod
    def run(orchestrator, pipeline) -> None:
        output = StepStarted.__format_output(pipeline)
        orchestrator.bots.printer.print_output(output)

    def __format_output(pipeline):
        return f"{pipeline.step} > Input: {pipeline.lhs}, {pipeline.rhs}"