---
title: "Publish your conservation area data"
slug: "publish-conservation-area-data"
summary: Follow our guidance on publishing conservation area data.
---

This guidance sets out what you need to do to standardise conservation area data. It provides details on what data should be provided with each conservation area, and how they should be made available online.

Most conservation areas will be made up of two elements, the boundary of the designation (the geography) and one or more area appraisals (the document).  This guidance is focused on the standardisation and publishing of the boundary only.

Conservation area boundaries should be created using [Geographic information system (GIS)](https://en.wikipedia.org/wiki/Geographic_information_system) software. This will make it easier to add the relevant data and make it available online.

<details class="govuk-details" data-module="govuk-details">
  <summary class="govuk-details__summary">
    <span class="govuk-details__summary-text">
      Why is conservation area data important?
    </span>
  </summary>
  <div class="govuk-details__text">
    Conservation area designation provides a basis for planning policies whose objective is to conserve the historic character of an area. They impact on the general permitted development rights of the public, so knowing where they are is essential for anyone undertaking any form of development.
  </div>
</details>

## What information do you need to provide for each conservation area?

#### Reference

A unique number or code used to identify the conservation area. The code should be unique within your organisation, for example, CA01.

If a reference code has been used to refer to a different conservation area in the past, you should add something to the reference to make it unique.

For example, if `CA01` has been used in the past to refer to another conservation area, add something (such as `XYZ`) to make a new reference for the new conservation area. In this case you would have the reference `CA01-XYZ`.

Or, if you have inherited conservation areas defined by old organisations you could prefix the references with the organisation code. For example, `WYO-CA01` and `AYL-CA01`.

#### Name

The name of the conservation area. This will be used as the name that users see and refer to. For example, `South Bank`.

#### Documentation-url

A link to the documentation which contains the authoritative boundary. This may be the appraisal document, or separate PDF containing the map and “red line” boundary.

#### Organisation

An identifier of the organisation that created the conservation area. Use an organisation identifier. This will allow machines to link the conservation record to the publishing organisation. For example, `local-authority-eng:NFK` is the identifier for Norfolk County Council.

[Find your organisation identifier](https://digital-land.github.io/organisation/).

#### Entry-date

The date you created or updated the data record in your GIS system or in the CSV. Use the `YYYY-MM-DD` for dates. For example, `2021-02-26`.

#### Start date

The date the designation for the conservation area was created. Use the `YYYY-MM-DD` for dates. For example, `1982-07-26`.

#### End-date

The date the conservation area stopped being a conservation area. Use the `YYYY-MM-DD` for dates. This date can be in the future if the date it will stop being a conservation area is known. For example, `2022-09-01`.

::: highlight-box--cta
    Dates should follow the [GOV.UK standard on dates in data](https://www.gov.uk/government/publications/open-standards-for-government/date-times-and-time-stamps-standard)

## How you make your conservation areas available online?

Make your geospatial data available online.

There are multiple ways to do this:

* you can expose a WFS endpoint
* or publish the geojson on your website.

<div class="govuk-warning-text">
  <span class="govuk-warning-text__icon" aria-hidden="true">!</span>
  <strong class="govuk-warning-text__text">
    <span class="govuk-warning-text__assistive">Warning</span>
    Do not put the geospatial data behind a login.
  </strong>
</div>

Once the geospatial data is available online, [email the URL to the Digital Land team](mailto:digitalland@communities.gov.uk?subject=Link+to+conservation+area+data).

