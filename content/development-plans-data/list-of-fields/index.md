---
title: "Development plans data fields"
---

When publishing your development plan data, follow this guidance on how to format each field in each data file.

## development-plan-document

Field  | Description
------------- | -------------
development-plan-document  | a unique identifier for the document
description  | an optional description of the document
development-plan-types | a list of document types e.g. local-plans
development-policies | a list of references for all the policies in the document
document-url | a URL to the document
geographies | a list of references to the areas covered in the document. Use the statistical geography code if the document covers the whole local authority area. If it is a small area use references for each shape from your GIS
name | the name of the document
notes | an optional notes field
organisation | a list of organisation identifiers
entry-date | the date you add the record in the format `YYYY-MM-DD`
start-date | the beginning of the period the document covers. Can be an estimated date in the future. Format `YYYY-MM-DD`
end-date | the end of the period the document covers. Can be an estimated date in the future. Format `YYYY-MM-DD`

## development-plan-timetable

Field  | Description
------------- | -------------
development-plan-status | the status of the document. Allowable values are: `emerging`, `examination` or `adopted`
development-plan-document | the identifier for the document the status applies to
notes | an optional notes field
entry-date | the date you add the record in the format `YYYY-MM-DD`
start-date | the date the document entered the status. Format `YYYY-MM-DD`
end-date | the date the document finished having the status. Format `YYYY-MM-DD`

