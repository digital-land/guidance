---
title: "Publish your design code data"
slug: "publish-your-design-code-data"
phase: "prototype"
summary: Follow our guidance for publishing your design code data.
---

The [Levelling-up and Regeneration Act 2023](https://www.legislation.gov.uk/ukpga/2023/55/enacted) requires local planning authorities to publish their design codes data on their website and that it must be kept up to date.

You must make sure your data is:

* published in the agreed format and contains the required data
* kept up to date
* easily found online

Make your data findable, usable and trustworthy.

Design codes are an important part of sustainable local planning and development. Data on  design codes has a wide range of uses, including:

* planning for housing-led development
* creating new digital services
* giving community members insight into local development

But for data to be useful it must be easy to find, use, understand and trust. You should ensure that your design codes data is all of these by following this guidance on the data format and the publication process.

### What you need to publish

There are 3 datasets you must provide for development plans:

* [design code](#design-code-dataset)
* [design code rule](#design-code-rule-dataset)
* [design code area](#design-code-area-dataset)

The design code and design code rule datasets should be provided as a CSV file. You can provide the design code area data in one of these formats:

* CSV
* GeoJSON
* GML
* Geopackage

For more information, see how to provide your data.

## Design code dataset

This dataset is about your design code. A design code is the body of work that contains a set of design requirements for the physical development of a site or area.

A design code is usually published as a website or pdf. For example, [`Healthy Streets for Surrey`](https://healthystreets.surreycc.gov.uk/). 

The dataset must contain at least one entry (row) for each design code.
It must contain the following fields (columns):

#### reference

A unique identifier for your design code that is:

* unique within your dataset
* permanent - it doesn't change when the dataset is updated

If you don't use a reference already, you’ll need to create one. This can be a short set of letters or numbers. It should not contain spaces. Example: `healthy-streets-for-surrey`

#### name

This will be the title of the design code publication.

Example: `Healthy Streets for Surrey`

#### description

A brief description of the design code.

#### design-code-status

This is the status of the design code publication. For example, `draft`.

The [design-code-status dataset](https://dluhc-datasets.planning-data.dev/dataset/design-code-status) contains the set of allowable statuses. You should use the value included in the reference field.

#### documentation-url

The URL of the web page where you can find information about the design code.

On GOV.UK these pages are called publication cover pages - the document itself is an HTML document or PDF and the cover page lists the document title and a short summary of what the document is about.

Example: `http://www.LPAwebsite.org.uk/design-code-for-bigtown`

#### document-url

The URL of the web page where you can find the design code publication. This can be an HTML document or PDF.

Example: `http://www.LPAwebsite.org.uk/design-code-for-bigtown/designcode.pdf`

#### notes

Optional notes.

#### entry-date 

The date this information has been entered as a record.

Example: `2024-01-20`

#### start-date

The date the validity of the record starts.

Example: `2024-01-20`

#### end-date

The date the validity of the record ends.

Example: `2035-01-20`

## Design code rule dataset

This dataset is about your design code rules. A design code rule is clear, specific and unambiguous, and it should normally include extensive graphical illustrations

The dataset must contain at least one entry (row) for each design code rule.

It must contain the following fields (columns):

#### reference

A unique identifier for your design code rule that is:

* unique within your dataset
* permanent - it doesn't change when the dataset is updated

If you don't use a reference already, you’ll need to create one. This can be a short set of letters or numbers. Example: `hsfs-20-minute-neighbourhoods`

#### name

This will be the name of the design code rule.

Example: `20-minute neighbourhoods`

#### design-code

The reference for the design code which this rule is part of.

Example: `healthy-streets-for-surrey`

#### description

A description of the design code rule.

If the rule is short enough you can include the whole rule. For example, `Proposals should avoid coniferous screen planting. Deciduous tree planting to mitigate developments is encouraged.`

#### documentation-url

The URL of the web page where you can find information about the design code rule.

On GOV.UK these pages are called publication cover pages - the document itself is an HTML document or PDF and the cover page lists the document title and a short summary of what the document is about.

Example: `http://www.LPAwebsite.org.uk/built-form`

#### document-url

The URL of the web page where you can find the design code rule.

If the design code publication is a PDF then include the URL to the PDF.

If the design code publication is a digital design code then include a URL to the specific rule. For example, `https://healthystreets.surreycc.gov.uk/requirements-and-guidance/section?id=12.6`

#### design-code-rule-categories

A list of one or more [design-code-rule-categories references](https://dluhc-datasets.planning-data.dev/dataset/design-code-rule-category), separated by a semi-colon `;` character.

For example, `accessibility;facade-design`

#### notes

Optional notes.

#### entry-date 

The date this information has been entered as a record.

Example: `2024-01-20`

#### start-date

The date the validity of the record starts.

Example: `2024-01-20`

#### end-date

The date the validity of the record ends.

Example: `2035-01-20`

## Design code area dataset

This dataset is about your design code areas. A design code area defines the area covered by a design code or specific design code rules.

The dataset must contain at least one entry (row) for each design code area.

It must contain the following fields (columns):

#### reference

A unique identifier for your design code area that is:

* unique within your dataset
* permanent - it doesn't change when the dataset is updated

If you don't use a reference already, you’ll need to create one. This can be a short set of letters or numbers. Example: `chatham-centre-industrial-areas`

#### name

This will be the name of the design code area.

If it is a specific area then use that name. For example, `Lye Town Centre`

Or if it is a set of areas, all of the same type then use that in the name. For example, `Chatham Centre Industrial Areas`

#### geometry

The boundary for the design code area as a single polygon or multipolygon value. All points in the polygon should be in the WGS84 coordinate reference system if possible. If you can’t do this, give us what you have and then we can transform it into WGS84. However, this could mean there’s a small loss of precision when we do the transformation. If you’re providing geometry in a CSV, geometry should be in well-known text (WKT).

Example: `MULTIPOLYGON (((1.188829 51.23478,1.188376 51.234909,1.188381 51.234917,1.187912 51.235022...`

If you’re providing geometry in a GeoJSON, GML or Geopackage, use the associated geometry format.

#### design-code

The reference for the design code publication that includes this area.
Example: `healthy-streets-for-surrey`

#### design-code-rules

A list of one or more references for the design code rules that apply to this area.

They should be separated by a semi-colon `;` character.

For example, `trafford-design-code-LNL-5;trafford-design-code-TBSM-2;trafford-design-code-APG-1;trafford-design-code-TBET-3`

#### design-code-area-type

The classification of the design code area, for example, rural settlement or urban neighbourhood. 

The area types are defined in the [design code area type dataset](https://dluhc-datasets.planning-data.dev/dataset/design-code-area-type).

You should use the reference value for the area type you want to use. For example, for Rural settlements you should use `rural‑settlements`

#### documentation-url

The URL of the web page where you can find information about the design code area.

On GOV.UK these pages are called publication cover pages - the document itself is an HTML document or PDF and the cover page lists the document title and a short summary of what the document is about.

Example: `http://www.LPAwebsite.org.uk/design-code-area-newpark`

#### notes

Optional notes.

#### entry-date 

The date this information has been entered as a record.

Example: `2024-01-20`

#### start-date

The date the validity of the record starts.

Example: `2024-01-20`

#### end-date

The date the validity of the record ends.

Example: `2035-01-20`
