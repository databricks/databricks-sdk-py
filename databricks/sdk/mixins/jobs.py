from typing import Optional

from databricks.sdk.service import jobs


class JobsExt(jobs.JobsAPI):

    def get_run(self,
                run_id: int,
                *,
                include_history: Optional[bool] = None,
                include_resolved_values: Optional[bool] = None,
                page_token: Optional[str] = None) -> jobs.Run:
        """Get a single job run.

        Retrieve the metadata of a run. If a run has multiple pages of tasks, it will paginate through all pages of tasks, iterations, job_clusters, job_parameters, and repair history.

        :param run_id: int
          The canonical identifier of the run for which to retrieve the metadata. This field is required.
        :param include_history: bool (optional)
          Whether to include the repair history in the response.
        :param include_resolved_values: bool (optional)
          Whether to include resolved parameter values in the response.
        :param page_token: str (optional)
          To list the next page of job tasks, set this field to the value of the `next_page_token` returned in
          the GetJob response.

        :returns: :class:`Run`
        """
        run = super().get_run(run_id,
                              include_history=include_history,
                              include_resolved_values=include_resolved_values,
                              page_token=page_token)

        # When querying a Job run, a page token is returned when there are more than 100 tasks. No iterations are defined for a Job run. Therefore, the next page in the response only includes the next page of tasks.
        # When querying a ForEach task run, a page token is returned when there are more than 100 iterations. Only a single task is returned, corresponding to the ForEach task itself. Therefore, the client only reads the iterations from the next page and not the tasks.
        is_paginating_iterations = run.iterations is not None and len(run.iterations) > 0

        # runs/get response includes next_page_token as long as there are more pages to fetch.
        while run.next_page_token is not None:
            next_run = super().get_run(run_id,
                                       include_history=include_history,
                                       include_resolved_values=include_resolved_values,
                                       page_token=run.next_page_token)
            if is_paginating_iterations:
                run.iterations.extend(next_run.iterations)
            else:
                run.tasks.extend(next_run.tasks)
            # Each new page of runs/get response includes the next page of the job_clusters, job_parameters, and repair history.
            run.job_clusters.extend(next_run.job_clusters)
            run.job_parameters.extend(next_run.job_parameters)
            run.repair_history.extend(next_run.repair_history)
            run.next_page_token = next_run.next_page_token

        return run