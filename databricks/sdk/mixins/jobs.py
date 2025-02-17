from typing import Iterator, Optional

from databricks.sdk.service import jobs
from databricks.sdk.service.jobs import BaseJob, Job


class JobsExt(jobs.JobsAPI):

    def list(self,
             *,
             expand_tasks: Optional[bool] = None,
             limit: Optional[int] = None,
             name: Optional[str] = None,
             offset: Optional[int] = None,
             page_token: Optional[str] = None) -> Iterator[BaseJob]:
        """List jobs.

        Retrieves a list of jobs. If the job has multiple pages of tasks, job_clusters, parameters or environments,
        it will paginate through all pages and aggregate the results.

        :param expand_tasks: bool (optional)
          Whether to include task and cluster details in the response. Note that in API 2.2, only the first
          100 elements will be shown. Use :method:jobs/get to paginate through all tasks and clusters.
        :param limit: int (optional)
          The number of jobs to return. This value must be greater than 0 and less or equal to 100. The
          default value is 20.
        :param name: str (optional)
          A filter on the list based on the exact (case insensitive) job name.
        :param offset: int (optional)
          The offset of the first job to return, relative to the most recently created job. Deprecated since
          June 2023. Use `page_token` to iterate through the pages instead.
        :param page_token: str (optional)
          Use `next_page_token` or `prev_page_token` returned from the previous request to list the next or
          previous page of jobs respectively.

        :returns: Iterator over :class:`BaseJob`
        """
        # fetch jobs with limited elements in top level arrays
        jobs_list = super().list(expand_tasks=expand_tasks,
                                 limit=limit,
                                 name=name,
                                 offset=offset,
                                 page_token=page_token)
        if not expand_tasks:
            yield from jobs_list

        # fully fetch all top level arrays for each job in the list
        for job in jobs_list:
            if job.has_more:
                job_from_get_call = self.get(job.job_id)
                job.settings.tasks = job_from_get_call.settings.tasks
                job.settings.job_clusters = job_from_get_call.settings.job_clusters
                job.settings.parameters = job_from_get_call.settings.parameters
                job.settings.environments = job_from_get_call.settings.environments
            # Remove has_more fields for each job in the list.
            # This field in Jobs API 2.2 is useful for pagination. It indicates if there are more than 100 tasks or job_clusters in the job.
            # This function hides pagination details from the user. So the field does not play useful role here.
            if hasattr(job, 'has_more'):
                delattr(job, 'has_more')
            yield job

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

    def get(self, job_id: int, *, page_token: Optional[str] = None) -> Job:
        """Get a single job.

        Retrieves the details for a single job. If the job has multiple pages of tasks, job_clusters, parameters or environments,
        it will paginate through all pages and aggregate the results.

        :param job_id: int
          The canonical identifier of the job to retrieve information about. This field is required.
        :param page_token: str (optional)
          Use `next_page_token` returned from the previous GetJob to request the next page of the job's
          sub-resources.

        :returns: :class:`Job`
        """
        job = super().get(job_id, page_token=page_token)

        # jobs/get response includes next_page_token as long as there are more pages to fetch.
        while job.next_page_token is not None:
            next_job = super().get(job_id, page_token=job.next_page_token)
            # Each new page of jobs/get response includes the next page of the tasks, job_clusters, job_parameters, and environments.
            job.settings.tasks.extend(next_job.settings.tasks)
            job.settings.job_clusters.extend(next_job.settings.job_clusters)
            job.settings.parameters.extend(next_job.settings.parameters)
            job.settings.environments.extend(next_job.settings.environments)
            job.next_page_token = next_job.next_page_token

        return job