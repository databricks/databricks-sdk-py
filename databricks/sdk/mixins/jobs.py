from typing import Optional

from databricks.sdk.service import jobs


class JobsExt(jobs.JobsAPI):

    def get_run(self,
                run_id: int,
                *,
                include_history: Optional[bool] = None,
                include_resolved_values: Optional[bool] = None,
                page_token: Optional[str] = None) -> jobs.Run:
        """
        This method fetches the details of a run identified by `run_id`. If the run has multiple pages of tasks or iterations,
        it will paginate through all pages and aggregate the results.

        :param run_id: int
          The canonical identifier of the run for which to retrieve the metadata. This field is required.
        :param include_history: bool (optional)
          Whether to include the repair history in the response.
        :param include_resolved_values: bool (optional)
          Whether to include resolved parameter values in the response.
        :param page_token: str (optional)
          To list the next page or the previous page of job tasks, set this field to the value of the
          `next_page_token` or `prev_page_token` returned in the GetJob response.

        :returns: :class:`Run`
        """
        run = super().get_run(run_id,
                              include_history=include_history,
                              include_resolved_values=include_resolved_values,
                              page_token=page_token)

        isPaginatingIterations = run.iterations is not None and len(run.iterations) > 0

        while run.next_page_token is not None:
            next_run = super().get_run(run_id,
                                       include_history=include_history,
                                       include_resolved_values=include_resolved_values,
                                       page_token=run.next_page_token)
            if isPaginatingIterations:
                run.iterations.extend(next_run.iterations)
            else:
                run.tasks.extend(next_run.tasks)
            run.next_page_token = next_run.next_page_token

        run.prev_page_token = None
        return run
