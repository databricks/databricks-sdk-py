from databricks.sdk.service import jobs


class JobsExt(jobs.JobsAPI):

    def get_run(self,
                run_id: int,
                *,
                include_history: bool | None = None,
                include_resolved_values: bool | None = None,
                page_token: str | None = None) -> jobs.Run:
        run = super().get_run(run_id,
                              include_history=include_history,
                              include_resolved_values=include_resolved_values,
                              page_token=page_token)

        isPaginatingIterations = run.iterations is not None and len(run.iterations) > 0

        while run.next_page_token:
            next_run = super().get_run(run_id,
                                       include_history=include_history,
                                       include_resolved_values=include_resolved_values,
                                       page_token=run.next_page_token)
            if (isPaginatingIterations):
                run.iterations.extend(next_run.iterations)
            else:
                run.tasks.extend(next_run.tasks)
            run.next_page_token = next_run.next_page_token

        return run
