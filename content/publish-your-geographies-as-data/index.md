---
title: "Publish your geographies as data"
slug: "publish-your-geographies-as-data"
label: "guidance:geographies-data"
summary: Follow this guidance to help you publish your geographies as data.
---

This guidance sets out how to structure and publish site and other boundaries as geospatial data.

It details what information you should provide and how it should be made available online.

Geospatial data can be any area, location, site or boundary you have created. These two images show a visual representation of what the data might look like.

#### Boundary or polygon

<a href="https://res.cloudinary.com/digital-land/image/upload/v1626864208/digital-land.github.io_conservation-area_stonesfield_btkguo.png" title="Site boundary"><img class="dl-image" src="https://res.cloudinary.com/digital-land/image/upload/v1626864208/digital-land.github.io_conservation-area_stonesfield_btkguo.png" alt="An example of shape data shown on a map - in this case it is the boundary of a conservation area"></a>

[See complete record for this conservation area record](https://digital-land.github.io/conservation-area/local-authority-eng/WOX/48/).

#### Point

<a href="https://res.cloudinary.com/digital-land/image/upload/v1626864208/digital-land.github.io_listed-building_old-vicarage_osox8x.png" title="Site point"><img class="dl-image" src="https://res.cloudinary.com/digital-land/image/upload/v1626864208/digital-land.github.io_listed-building_old-vicarage_osox8x.png" alt="An example of point data shown on a map - in this case it is the location of a listed building"></a>

[See complete record for the listed building record](https://digital-land.github.io/listed-building/1021474/) shown as a point.

You can publish your geography data as [GeoJSON](https://geojson.org/), [ESRI shapefiles](https://www.esri.com/content/dam/esrisites/sitecore-archive/Files/Pdfs/library/whitepapers/pdfs/shapefile.pdf), [KML](https://developers.google.com/kml) or CSV containing the geometry as [WKT](https://www.ogc.org/standards/wkt-crs).

Each record must contain a boundary, polygon or site point.

## Publishing as GeoJSON, shapefiles or KML

GeoJson, a shapefile or KML consists of data for the shape or point, and a number of attributes containing data about the geography.

Each record should include the following attributes:

### name

The name of the area or boundary which your organisation uses. This will be used as the name that users see and refer to, for example, `Rawcliffe`.

### documentation-url

If available, a link to the documentation which contains the authoritative boundary. This may be the appraisal document, or separate PDF containing the map and “red line” boundary. A URL is a permanent link that doesn’t change.


### organisation

[Find your organisation in this list](https://digital-land.github.io/organisation/) (in most cases this will be a local planning authority). Text must follow the same letter casing, with no spaces. Norfolk’s local planning authority, for example, would be:

`local-authority-eng:NFK`

### reference

A unique number or code used to identify the geographical area. The code should be unique within your organisation, for example, `CA01`.

If a reference code has been used to refer to a different location in the past, you should add something to the reference to make it unique and meaningful to your organisation.

### notes

Supplementary information related to the geographical data.

### entry-date

The date you created or updated the data record in your GIS system or in the CSV. Where possible, use the format YYYY-MM-DD for dates, for example, `2021-02-26`.

### start-date

The date the geographical data was first created. Use the format YYYY-MM-DD for dates where possible, for example, `1991-06-12`.

### end-date

The date the geographical area no longer existed due to a change like a boundary change. Where possible, use the format YYYY-MM-DD for dates. This date can be in the future if the date it will stop being a location or boundary is known, for example, `2025-10-11`.

If you don’t have a specific piece of data mentioned above such as an end date, please leave it blank rather than adding N/A or Not applicable.

## Publish in CSV format

If you prefer to publish your geography data in CSV format, you need to include all of the fields mentioned above as well as one of the following for each record:

### Geometry

WKT representing the shape/boundary/area.

### Point

Point data represents a particular item for example, listed buildings, points of interest or specific features like schools. Point data is based on a pair of coordinates.

## Keeping your data up to date

You will need to let Digital Land know where you have published your data so that it can be included in our [national collections](https://digital-land.github.io/dataset/). If you make any changes to your data these will be reflected in the national collection providing the URL hasn't changed. If updated data is published at a new URL or you are not sure whether it has changed please let us know via digitalland@communities.gov.uk
