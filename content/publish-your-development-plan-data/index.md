---
title: "Publish your development plan data"
slug: "publish-development-plan-data"
phase: "prototype"
summary: Follow our guidance for publishing your development plan data.
---

The [Levelling-up and Regeneration Act 2023](https://www.legislation.gov.uk/ukpga/2023/55/enacted) requires local planning authorities to publish their data on the status of emerging development plans on their website and that it must be kept up to date.

You must make sure your data is:

* published in the agreed format and contains the required data
* kept up to date
* easily found online

### Make your data findable, usable and trustworthy

Development plans are an important part of sustainable local planning and development. Data on development plans has a wide range of uses, including:

* planning for housing-led development
* creating new digital services
* giving community members insight into local development

But for data to be useful it must be easy to find, use, understand and trust. You should ensure that your development plan data is all of these by following this guidance on the data format and the publication process.

### What you need to publish

There are 4 datasets you must provide for development plans:

* development plan
* development plan boundary 
* development plan timetable 
* development plan document

The development plan, development plan timetable and development plan document datasets should be provided as a CSV file. You can provide the development plan boundary data in one of these formats:

* CSV
* GeoJSON
* GML
* Geopackage

## Development plan dataset

This dataset is about your development plan. A development plan sets out a vision and a framework for the future development of the area.

The dataset must contain at least one entry (row) for each development plan. Don’t worry if you don’t have all the data we’ve asked for available right now. If you give us what you’ve got, we can help you fill in the gaps later.

A complete record should contain the following fields (columns):

#### reference

A unique identifier for your development plan that is:

* unique within your dataset
* permanent - it doesn't change when the dataset is updated

If you don't use a reference already, you’ll need to create one. This can be a short set of letters or numbers.
Example: `DPO1`

#### name

This will be the title of the page hosting data about the name of the development plan on our website.

Example: `adopted-local-plan-for-leeds`

#### description

A brief description of the development plan.

#### development-plan-type

The reference to the type of plan this is. This should be one of the options [listed here](https://dluhc-datasets.planning-data.dev/dataset/development-plan-document-type).

#### period-start-date

The start date of the period the plan covers. The more precise you can be the better, but if you only have a month or year just give us that.

Example: `2019-01-20`

With dates, some data is better than no data, so:

<ul class="govuk-list govuk-list--bullet">
<li><code class="dl-code">2019</code> is fine</li>
<li><code class="dl-code">2019-01</code> is better</li>
<li><code class="dl-code">2019-01-20</code> is brilliant</li>

#### period-end-date

The end date of the period the plan covers.

Example: `2035-01-20`

With dates, some data is better than no data, so:

<ul class="govuk-list govuk-list--bullet">
<li><code class="dl-code">2035</code> is fine</li>
<li><code class="dl-code">2035-01</code> is better</li>
<li><code class="dl-code">2035-01-20</code> is brilliant</li>

#### development-plan-boundary

The reference code for the boundary of the area the plan covers.

Example: `DPGO1`

#### documentation-url 

The URL of the web page where you can find information about the plan.

On GOV.UK these pages are called publication cover pages - the document itself is an HTML document or PDF and the cover page lists the document title and a short summary of what the document is about.

Example: `http://www.LPAwebsite.org.uk/local-plan-for-leeds`

#### adopted-date

The date a plan is officially adopted.

Example: `2023-01-20`

With dates, some data is better than no data, so:

<ul class="govuk-list govuk-list--bullet">
<li><code class="dl-code">2023</code> is fine</li>
<li><code class="dl-code">2023-01</code> is better</li>
<li><code class="dl-code">2023-01-20</code> is brilliant</li>

#### organisations

The code for the organisations, or organisation, that created the plan.

Example: `local-authority:BUC`

Create this code by using the relevant prefix, a colon (:), and the reference for your organisation from this <a href="https://www.planning.data.gov.uk/organisation/">list of organisations</a>. If it's a single organisation responsible, just enter one code. If more than one organisation is responsible, separate the codes with a semicolon (;) 

#### entry-date 

The date this information has been entered as a record.

Example: `2024-01-20`

With dates, some data is better than no data, so:

<ul class="govuk-list govuk-list--bullet">
<li><code class="dl-code">2024</code> is fine</li>
<li><code class="dl-code">2024-01</code> is better</li>
<li><code class="dl-code">2024-01-20</code> is brilliant</li>

#### start-date

The date the validity of the record starts.

Example: `2024-01-20`

With dates, some data is better than no data, so:

<ul class="govuk-list govuk-list--bullet">
<li><code class="dl-code">2024</code> is fine</li>
<li><code class="dl-code">2024-01</code> is better</li>
<li><code class="dl-code">2024-01-20</code> is brilliant</li>

#### end-date

The date the validity of the record ends.

Example: `2035-01-20`

With dates, some data is better than no data, so:

<ul class="govuk-list govuk-list--bullet">
<li><code class="dl-code">2035</code> is fine</li>
<li><code class="dl-code">2035-01</code> is better</li>
<li><code class="dl-code">2035-01-20</code> is brilliant</li>

---

## Development plan boundary dataset

This dataset is about the development plan boundary. This shows the boundary of the area covered by the development plan.
The dataset must contain at least one entry (row) for each development plan. Don’t worry if you don’t have all the data we’ve asked for available right now. If you give us what you’ve got, we can help you fill in the gaps later.

A complete record should contain the following fields (columns):

#### reference

A unique identifier for your development plan boundary that is:

* unique within your dataset
* permanent - it doesn't change when the dataset is updated

If you don't use a reference already, you will need to create one. This can be a short set of letters or numbers.

Example: `DPGO1`

#### name

This is the name of the development plan boundary.

Example: `Leeds local plan boundary`

#### geometry

The boundary for the development plan area as a single polygon or multipolygon value. All points in the polygon should be in the WGS84 coordinate reference system if possible. If you can’t do this, give us what you have and then we can transform it into WGS84. However, this could mean there’s a small loss of precision when we do the transformation.
If you’re providing geometry in a CSV, geometry should be in well-known text (WKT).

Example: `MULTIPOLYGON (((1.188829 51.23478,1.188376 51.234909,1.188381 51.234917,1.187912 51.235022...`

If you’re providing geometry in a GeoJSON, GML or Geopackage, use the associated geometry format.

#### development-plan-boundary-type

What sort of boundary type this is.

This should be one of these 3 options:

* `planning-authority-district` (the boundary of the planning authority)
* `combined-planning-authority-district` (when there's a joint plan and the boundary covers 2 or more authority boundaries)
* `designated-plan-area` (when the plan covers an alternative area)

#### description

A description of your development plan boundary.

Examples: `The boundary of Leeds planning authority`
`Tower Hamlets authority area minus the site covered by the Olympic Development Corporation area`

#### entry-date

The date the entity was last updated.

If the entity has never been updated, enter the same date as start-date.

Write in `YYYY-MM-DD` format.

Example: `2024-02-20`

With dates, some data is better than no data, so:

<ul class="govuk-list govuk-list--bullet">
<li><code class="dl-code">2024</code> is fine</li>
<li><code class="dl-code">2024-02</code> is better</li>
<li><code class="dl-code">2024-02-20</code> is brilliant</li>

#### start-date

The date that the development plan boundary was first announced, written in YYYY-MM-DD format. Don’t worry if you don’t know the exact date, just the month and year is fine.

Example: `1984-03-28`

With dates, some data is better than no data, so:

<ul class="govuk-list govuk-list--bullet">
<li><code class="dl-code">1984</code> is fine</li>
<li><code class="dl-code">1984-03</code> is better</li>
<li><code class="dl-code">1984-03-28</code> is brilliant</li>

#### end-date

If applicable, the date that the boundary for the plan was no longer in effect, written in YYYY-MM-DD format. If it's still current, leave the cell blank.

Example: `1999-01-20`

With dates, some data is better than no data, so:

<ul class="govuk-list govuk-list--bullet">
<li><code class="dl-code">1999</code> is fine</li>
<li><code class="dl-code">1999-01</code> is better</li>
<li><code class="dl-code">1999-01-20</code> is brilliant</li>

---

## Development plan timetable

This dataset is about your development plan timetable. A development plan timetable sets out the approximate timing for preparing a new development plan and supporting documents.

The data must contain at least one record for each event in the plan-making process.

Each record must contain the following fields:

#### reference

A unique identifier for your development plan that is:

* unique within your dataset
* permanent - it doesn't change when the dataset is updated

If you don't use a reference already, you will need to create one. This can be a short set of letters or numbers.

Example: `DPTO1-consultation-start`

#### name

This is the name of the event in the plan-making process.

Example: `Leeds local plan consultation start`

#### development-plan

The reference for a particular development plan.

Example: `adopted-local-plan-for-leeds`

#### development-plan-event

The reference for a development plan event. This should be one of the options [listed here](https://dluhc-datasets.planning-data.dev/dataset/development-plan-event)

Example: `plan-adopted`

#### event-date

The date this event happened.

Example: `2024-01-20`

With dates, some data is better than no data, so:

<ul class="govuk-list govuk-list--bullet">
<li><code class="dl-code">2024</code> is fine</li>
<li><code class="dl-code">2024-01</code> is better</li>
<li><code class="dl-code">2024-01-20</code> is brilliant</li>

#### notes

Optional notes

#### organisations

The code for the organisations, or organisation, that created the plan.

Example: `local-authority:BUC`

Create this code by using the relevant prefix, a colon (:), and the reference for your organisation from this <a href="https://www.planning.data.gov.uk/organisation/">list of organisations</a>. If it's a single organisation responsible, just enter one code. If more than one organisation is responsible, separate the codes with a semicolon (;) 

#### entry-date

The date this information has been entered as a record.

Example: `2024-01-20`

With dates, some data is better than no data, so:

<ul class="govuk-list govuk-list--bullet">
<li><code class="dl-code">2024</code> is fine</li>
<li><code class="dl-code">2024-01</code> is better</li>
<li><code class="dl-code">2024-01-20</code> is brilliant</li>

#### start-date

The date the validity of the record starts.

Example: `2024-01-20`

With dates, some data is better than no data, so:

<ul class="govuk-list govuk-list--bullet">
<li><code class="dl-code">2024</code> is fine</li>
<li><code class="dl-code">2024-01</code> is better</li>
<li><code class="dl-code">2024-01-20</code> is brilliant</li>

#### end-date

The date the validity of the record ends.

Example: `2035-01-20`

With dates, some data is better than no data, so:

<ul class="govuk-list govuk-list--bullet">
<li><code class="dl-code">2024</code> is fine</li>
<li><code class="dl-code">2024-01</code> is better</li>
<li><code class="dl-code">2024-01-20</code> is brilliant</li>

---

## Development plan document dataset

This dataset is about your development plan documents. Development plan documents are planning policy documents which make up the development plan.

The dataset must contain at least one entry (row) for each development plan document.

It must contain the following fields (columns):

#### reference

A unique reference for each development plan document that is:

* unique within your dataset
* permanent - it doesn't change when the dataset is updated

If you don't use a reference already, you will need to create one. This can be a short set of letters or numbers.

Example: `DPDO1-adoption-statement`

#### name

The name of this document. 

Example: `Leeds adoption statement`

#### description

Brief description of this document.

Example: `Adoption statement document 2024`

#### development-plan

The reference for your development plan that these documents relate to.

Example: `adopted-local-plan-for-leeds`

#### document-type

The [reference for this document type](https://dluhc-datasets.planning-data.dev/dataset/development-plan-document-type)

Example: `policies‑map`

#### documentation-url 

The URL of the web page where you can find information about the plan.

On GOV.UK these pages are called publication cover pages - the document itself is an HTML document or PDF and the cover page lists the document title and a short summary of what the document is about.

Example: `http://www.LPAwebsite.org.uk/local-plan-for-leeds`

#### document-url

The URL of the document file (HTML or PDF) for the plan.

Example: `http://www.LPAwebsite.org.uk/local-plan-for-leeds/newlocalplan.pdf`

#### organisations

The code for the organisations, or organisation, that created the plan.

Example: `local-authority:BUC`

Create this code by using the relevant prefix, a colon (:), and the reference for your organisation from this <a href="https://www.planning.data.gov.uk/organisation/">list of organisations</a>. If it's a single organisation responsible, just enter one code. If more than one organisation is responsible, separate the codes with a semicolon (;) 

#### entry-date

The date this information has been entered as a record.

Example: `2024-01-20`

With dates, some data is better than no data, so:

<ul class="govuk-list govuk-list--bullet">
<li><code class="dl-code">2024</code> is fine</li>
<li><code class="dl-code">2024-01</code> is better</li>
<li><code class="dl-code">2024-01-20</code> is brilliant</li>

#### start-date

The date the validity of the record starts.

Example: `2024-01-20`

With dates, some data is better than no data, so:

<ul class="govuk-list govuk-list--bullet">
<li><code class="dl-code">2024</code> is fine</li>
<li><code class="dl-code">2024-01</code> is better</li>
<li><code class="dl-code">2024-01-20</code> is brilliant</li>

#### end-date

The date the validity of the record ends.

Example: `2035-01-20`

>With dates, some data is better than no data, so:

<ul class="govuk-list govuk-list--bullet">
<li><code class="dl-code">2035</code> is fine</li>
<li><code class="dl-code">2035-01</code> is better</li>
<li><code class="dl-code">2035-01-20</code> is brilliant</li>
