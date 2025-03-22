import csv
from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["indeed"],
    search_term="remote",
    location="Manchester",
    results_wanted=100,
    hours_old=72, # (only Linkedin/Indeed is hour specific, others round up to days old)
    country_indeed='UK',  # only needed for indeed / glassdoor
    
    # linkedin_fetch_description=True # get full description , direct job url , company industry and job level (seniority level) for linkedin (slower)
    # proxies=["208.195.175.46:65095", "208.195.175.45:65095", "localhost"],
    
)
print(f"Found {len(jobs)} jobs")
print(jobs.head())
jobs.to_csv("samples/Manch_test.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False) # to_excel