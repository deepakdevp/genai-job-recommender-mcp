from mcp.server.fastmcp import FastMCP
from mcp.types import Response
from src.jobs_api import fetch_linkedin_jobs, fetch_naukri_jobs
mcp = FastMCP()

@mcp.tool()
async def get_linkedin_job_recommendations(job_description: str) -> Response:
    return fetch_linkedin_jobs(job_description)

@mcp.tool()
async def get_naukri_job_recommendations(job_description: str) -> Response:
    return fetch_naukri_jobs(job_description)

if __name__ == "__main__":
    mcp.run(transport="stdio")