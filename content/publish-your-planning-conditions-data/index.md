---
title: "Publish your planning conditions data"
slug: "publish-your-planning-conditions-data"
phase: "prototype"
summary: Follow our guidance for publishing your planning conidtions data.
---

<div class="govuk-notification-banner" aria-label="Notice" role="region">
    <p class="govuk-notification-banner__content">This guidance is a working draft which means we will be updating it based our research and your feedback</p>
</div>

There are 2 datasets you must provide for planning conditions data:

* [planning condition dataset](#planning-condition-dataset)
* [planning application condition dataset](#planning-application-condition-dataset)

  
## Format

You should provide data as a CSV.

## Planning condition dataset

This dataset is about planning conditions. Planning conditions are applied to the decision notice of planning applications, to limit and control how the planning permission is implemented. 

Don’t worry if you don’t have all the data we’ve asked for available right now. If you give us what you’ve got, we can help you fill in the gaps later.

A complete record should contain the following fields (columns):

### reference

A reference or ID for each planning condition that is:

* unique within your dataset
* permanent - it doesn't change when the dataset is updated

If you don't use a reference already, you will need to create one that makes sense for this planning condition.

Example: `PC01-drawings`

### name

The official name of the planning condition.

Example: `Old Market approved drawings`

### description

The text of the condition.

Example: `The development hereby permitted must be begun not later than the end of three years from the date of this permission`.

### reason

The text of the reason for the condition.

Example: `In order to comply with the provisions of Section 91 of the Town and Country Planning Act 1990 (as amended)`.

### organisation

The code for the organisation that created the condition that applies to the application.

Example: `local-authority:BUC`

Create this code by using the relevant prefix, a colon (:), and the reference for your organisation from this [list of organisations](https://www.planning.data.gov.uk/organisation/). 

### notes

Optional additional notes on this planning condition

### entry-date

The date the entity was last updated.

If the entity has never been updated, enter the same date as start-date.

Write in YYYY-MM-DD format.

Example:  

`2022-12-20`

With dates, some data is better than no data, so:  

* `2022` is fine
* `2022-12` is better
* `2022-12-20` is brilliant

### start-date

The date the validity of the record starts, written in YYYY-MM-DD format. This is likely to be the decision date or if anything about the relationship between the application and the condition has changed. For example, with updated approved drawings via a Section 73, it should be the date of that change.

Example: `2024-04-25`

With dates, some data is better than no data, so:

* `2024` is fine
* `2024-04` is better
* `2024-04-25` is brilliant

### end-date

Where the planning condition is no longer valid, this should be the date that it was no longer in effect, written in YYYY-MM-DD format. If this does not apply, leave the cell blank.

Example: `2024-01-20`

With dates, some data is better than no data, so:

* `2024` is fine
* `2024-01` is better
* `2024-01-20` is brilliant

*This could refer to ‘the expiry date’ of a condition due to time limits, or if the condition has been varied or removed via a Section 73 application. Therefore, the original conditions end date would be the date the Section 73 decision was issued.* 


## Planning application condition dataset

This dataset is about linking planning applications to the planning conditions set.

A complete record should contain the following fields (columns):

### reference

A reference or ID for the connection between the planning application and the planning condition that is:

* unique within your dataset
* permanent - it doesn't change when the dataset is updated

This could be a combination of the planning application reference and the planning condition reference.
Example: `2021/3734/P-4`

### planning-application

This is the reference for the planning application the conditions are attached to.

Example: `2021/3734/P`

### planning-condition

This is the reference for the planning condition that is attached to the planning application. This can be a standard planning condition, or something unique to this application.

Example: `PC01-time-limit`

### description 

A description of the condition that is applied to the application.

Example: `A commencement date condition for this planning application`

### organisation

The code for the organisation that created the condition that applies to the application.

Example: `local-authority:BUC`

Create this code by using the relevant prefix, a colon (:), and the reference for your organisation from this [list of organisations](https://www.planning.data.gov.uk/organisation/). 

### document-url

A link to the decision notice where the conditions are laid out.

### document-type

The type of document. This must be one of the following values, or left blank:

* area-appraisal
* notice

### notes

Optional additional notes on the connection between the planning condition and the planning application 

### entry-date

The date the record was last updated.

If the record has never been updated since it was created, enter the same date as start-date.

Write in YYYY-MM-DD format.

Example:  

`2022-12-20`

With dates, some data is better than no data, so:

* `2022` is fine
* `2022-12` is better
* `2022-12-20` is brilliant

### start-date

The date the validity of the record starts, written in YYYY-MM-DD format. This is likely to be the decision date or if anything about the relationship between the application and the condition has changed, for example, with updated approved drawings via a Section 73, it should be the date of that change.

Example: `2024-04-25`

With dates, some data is better than no data, so:

* `2024` is fine
* `2024-04` is better
* `2024-04-25` is brilliant

### end-date

Where the planning condition is no longer valid, this should be the date that it was no longer in effect, written in YYYY-MM-DD format. If this does not apply, leave the cell blank.

Example: `2024-01-20`

With dates, some data is better than no data, so:

* `2024` is fine
* `2024-01` is better
* `2024-01-20` is brilliant

*This could refer to ‘the expiry date’ of a condition due to time limits, or if the condition has been varied or removed via a Section 73 application. Therefore, the original conditions end date would be the date the Section 73 decision was issued.* 

<hr class="govuk-section-break govuk-section-break--l govuk-section-break--visible">

## Template and examples

To help you build your dataset correctly, we have created [a template CSV](https://docs.google.com/spreadsheets/d/1vv9Tz92gKgK4llHGpxeO4w29qEGf8xBMxQfFhSbU4F0/edit?usp=sharing) with the column names you’ll need, plus some example data.
