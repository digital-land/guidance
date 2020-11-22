---
title: "Development plan documents data standard"
---

This guidance sets out a data format and approach that you can follow in order to publish data about your development plan documents.

Publishing is a 3 step process:

1. Collect the information (Column headers in each sample data file)
2. Record the information and create 2 development plan documents schema CSV files to store the data
3. Upload each of these files to your organisation’s website and give them a URL that won’t change in the future so we can rely on it when collecting data.

## 1. Collect the information

## 2. Record the information and create two CSV files

[[scene setting]]

We’ve created a sample CSV file for each of the 2 files:

- `development-plan-document.csv`
- `development-plan-timetable.csv`

If it helps, you can use the above sample files and enter your development plan documents data. You must follow the guidelines below, then ‘save as .csv file’. You can work on the files using Excel, however you need to save it as a .csv file when you are ready to upload them for publication.

Each of the CSV files must:

* be named using the convention specified in each section below
* contain all the expected column headers (written exactly as shown, in lowercase and only contain entries that conform to the constraints described below

[Find out more about creating a CSV file](https://w3c.github.io/csvw/primer/).

Important considerations:

* The first row of data in each sample data file is prepopulated with an example. Once you’ve added your rows you can delete these example rows.
* If you don’t have information for any fields, you can leave them blank. You can add more data at a later date.
* `end-dates` can be estimated dates in the future.

Below is some guidance for specific fields of the schemas:

### Development plan document

#### development-plan-document
Create a unique identifier for the document. By ‘unique’ this means it should not be used for anything else in your organisation.

[[example]]

#### development-plan-document-type
Local-plan - (your local plan doc, or core strategy, site allocations)
SPD
Neighbourhood-plan
AAP
Other

#### Organisation
[Find your organisation in this list](https://digital-land.github.io/organisation/) (in most cases this will be a local planning authority). Text must follow the same letter casing, with no spaces. Norfolk’s local planning authority, for example, would be: local-authority-eng:NFK

#### Geographies
Enter the ONS statistical reference if the document’s boundary has one.
 Enter or create the reference your GIS team has associated to each shape file.


### Development plan timetable

#### Development-plan-status
Enter one of the following status:

* Emerging
* Currently under review by PINS
* Adopted

## 3. Update your development plan documents web page

To complete this process you will need to upload the files to your local planning authority’s website and edit (or create) your development plan documents web page. If you are not able or authorised to do this, speak to someone who is.

Upload each CSV file to your local planning authority’s website. Make sure the URL for each CSV file won’t change over time.

If have any questions or feedback, please fill out this feedback form or email DigitalLand@communities.gov.uk
