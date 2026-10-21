# *** THIS PROJECT IS IN ACTIVE DEVELOPMENT ***
# PROJECT OVERVIEW

### Frustrated with over saturated job boards? Use programming to leverage OSINT techniques and Unix-like data transformation methods to gather and transform data into actionable intelligence. This intel aims to aid the IT professional in discovering work opportunities based on evidence of a business's physical presence in a region, as well as to help inform and organize their job search strategy.

# METHOD OVERVIEW

1. Identify available data sources
2. Perform recon/data ingestion
3. Transform data
- clean
- structure
- verify
- organize
- de-duplicate
4. Generate succinct business summaries/overviews
5. Populate final documents

# DATA SOURCES

- Open Street Map - utilizing Overpass API
- State business registries
- yellowpages.com
- County GIS and assessor records

# FINAL RESULTS

The final result of this recon and data transformation methodology should result in a series of documents organized by U.S. Postal zip codes. Each document will contain a list of entries that comprise the businesses identified in that boundary. Each entry will include (if available) the following data points:
- Business name
- Address
- estimated size (number of employees)
- Infrastructure footprint (if applicable, large scale enterprises will be identified and scored by IT infrastructure footprint. e.g, A company owns a verified dedicated IP range)
- about url
- generated summary about business
- careers url

User input will also be structured into the template as follows:
- Status (Applied:y/n, Date: , Application expiration:) *will attempt to structure as an event log rather than changing state
- Notes

# HOW TO USE THE RESULTS
Suggestions on how to strategically leverage results

### In summary, raw intel will be gathered on local businesses, transformed into a useable dataset and utilized to attempt an alternative approach to job seeking than standard modern job boards.
