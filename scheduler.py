from __future__ import division
'''
Scheduler
---------
Calculates the optimal processing order for a list of jobs, where each job has a priority (higher value = higher priority)
and a duration (higher value = job takes more time to complete)
'''
def schedule(jobs):
    jobs.sort(key=lambda job : job['priority'] / job['duration'], reverse=True)