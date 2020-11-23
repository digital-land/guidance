---
title: "Publish your development plan data"
---

This guidance sets out a data format and approach that you can follow in order to publish data about your development plan documents.

Publishing is a 3 step process:

1. Collect the information (Column headers in each sample data file)
2. Record the information as data. In this step you need to create 2 CSV files for the data, these should match the [development-plan-document](https://digital-land.github.io/specification/schema/development-plan-document/) and [development-plan-timetable schemas](https://digital-land.github.io/specification/schema/development-plan-timetable/).
3. Upload each of these files to your organisation’s website and give them a URL that won’t change in the future so we can rely on it when collecting data.

![Image of the 3 step process for publishing development plans data](publishing-process.svg)

## 1. Collect the information

You should list out all your development plan documents, whether emerging or adopted. Your list should include all documents related to your Local plan, any Area action plans, Neighbourhood plans, SPDs and any other document you consider to be a development plan document.

For each document, where applicable, you need to provide the following information:

* The organisation or organisations who own the document.
* The area or areas the document covers. You should provide these as shapefiles.
* A link to where the document can be viewed online.
* The period the document covers. If the document is emerging provide your best estimate. You can update it if things change.
* The current (and any previous) statuses. For any previous statuses, where possible provide both a `start-date` and an `end-date`.

## 2. Record the information as data

You need to turn the development plan document information collected into data. There is a defined format to help you do this. The format follows our [data principles](https://digital-land.github.io/guidance/data-principles/) and will make sure the data is machine readable.

MHCLG will collect all the published data from Local authorities and use it to create a publicly available national dataset.

<div class="govuk-warning-text">
  <span class="govuk-warning-text__icon" aria-hidden="true">!</span>
  <strong class="govuk-warning-text__text">
    <span class="govuk-warning-text__assistive">Warning</span>
    All development plan data needs to be published in the same format.
  </strong>
</div>

You need to publish 2 CSV files containing data.

1 will include the list of development plan documents, 1 document per row and the other will include any statuses for each of the documents, 1 document status per row.

We’ve created sample CSV files for you to use as a guide:

- [development-plan-document.csv](sample-development-plan-document.csv)
- [development-plan-timetable.csv](sample-development-plan-timetable.csv)

You should name your files the same as those above.

If it helps, you can use the above sample files and enter your development plan documents data.

You can work on the files using Excel, however you need to save it as a .csv file when you are ready to upload them for publication.

<div class="govuk-warning-text">
  <span class="govuk-warning-text__icon" aria-hidden="true">!</span>
  <strong class="govuk-warning-text__text">
    <span class="govuk-warning-text__assistive">Warning</span>
    The first row of data in each sample data file is prepopulated with an example. Once you’ve added your rows you can delete these example rows.
  </strong>
</div>

For each of the CSV files:

* give them the same name as the sample files provided above
* include all the expected column headers (written exactly as shown, in lowercase and only contain entries that conform to the constraints described below).
* if you don’t have information for any fields, leave them blank. You can add more data at a later date.
* `end-dates` can be estimated dates in the future.

[Find out more about creating a CSV file](https://w3c.github.io/csvw/primer/).

## What data to enter

For the fields that require the values to be precise we have provided detailed guidance below.

[Read guidance for every field]().

### Development plan document data file

This file should contain a list of all your development plan documents. Key fields include:

#### development-plan-document
Create a unique identifier for the document. ‘Unique’ means it should not be used for anything else in your organisation. Once created you should not change it, even if other values in the row change, such as the name of the document changes.

`CAM-DPD3-APX12-123` is an example of an identifier which is likely to be unique.

#### development-plan-types
List all types the document belongs to. If listing more than one type, separate items in the list with a `;`. You can use the values *local-plan*, *spd*, *neighbourhood-plan*, *area-action-plan* and *other*.

For example, `local-plan`.

#### organisation
[Find your organisation in this list](https://digital-land.github.io/organisation/). Text must follow the same letter casing, with no spaces. Norfolk’s local planning authority, for example, would be: `local-authority-eng:NFK`

If you can not find an organisation, please let us know.

#### geographies
If the area covered is the whole of the local authority then enter the ONS statistical geography reference for the organisation.

For example, the reference for Harrogate Borough Council is `E07000165`. For joint plans list the reference from both local authorities.

If the area (or areas) covered is an area other than the whole of the local authority boundary then provide shapefiles for the area from your GIS system. The value you should enter is the reference associated with the area in your GIS system. If there are multiple areas covered, list all references separated by a `;`.

#### development-policies
List all the policies in the document. The values should be a reference (or identifier) for each policy. Separate each policy with a `;`.

<div class="govuk-warning-text">
  <span class="govuk-warning-text__icon" aria-hidden="true">!</span>
  <strong class="govuk-warning-text__text">
    <span class="govuk-warning-text__assistive">Warning</span>
    You do not need to complete the <code class="dl-code">development-policies</code> field at this stage.
  </strong>
</div>


### Development plan timetable data file

This file should contain a list of the statuses each development plan documents has had, including the current status. Key fields include:

#### development-plan-status
In this field enter one of the following statuses:

* `emerging` - currently working on the plan and it has not yet been formally adopted.
* `examination` - the plan is under examination by the planning inspectorate.
* `adopted` - the plan has been formally adopted.

## 3. Update your development plan documents web page

To complete this process you will need to upload the files to your local planning authority’s website. You should publish the 2 CSV files you created and any related shapefiles.

If you are not able or authorised to do this, please speak to someone who is able to do this.

Each file you upload should have a URL that won’t change over time. If you are updating a file, replace the old version with the new version.

When published email URLs for the data files and shapefiles to [DigitalLand@communities.gov.uk](mailto:DigitalLand@communities.gov.uk).

