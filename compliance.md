# OpenEO API Compliance Notes

## General
 - add to 'conformsTo': 'https://api.openeo.org/1.2.0' (specification downloadable)

## Capabilities Microservice

 - GET / - lists general information about the back-end
   - needs api_version (1.2.0 for openEO)
   - needs backend_version for back-end implementation [?]
   - got stack version [OK]
   - needs endpoints (all supported endpoints) (list subpaths and methods)
   - got links [OK]

 - GET /.well-known/openeo
   - list of versions pointing to resources, dict entries include `url`, `api_version`. Can also have `production`:`false` if needed.

 - GET /file_formats
   - input: Backend can read from files
   - output: Backend can write to.
   - can specify a title for the format (shorthand)
   - aligns with GDAL codes (zarr support but no Kerchunk or CFA)

 - GET /conformance [OK]
   - conformsTo return specifically.

 - GET /udf_runtimes
   - Supported runtimes for user-defined functions, including programming languages with environments or docker containers.
   - can use openeo known docker containers.
   - requires all options to include `type`, `default` (version), `versions`

 - GET /service_types
   - List supported secondary web service protocols (e.g OGC WMS)
   - `service name` has `configuration` and `process parameters` required properties.

## EO Data Discovery

 - GET /collections [OK]

 - GET /collections/{collection_id}
   - missing required parameter `cube:dimensions` for data cube.

 - GET /collections/{collection_id}/queryables [OK]

## Process Discovery

 - GET /processes
   - Predefined processes available at the backend (which we would need to implement somehow?)

 - GET /process_graphs
   - User defined processes of the authenticated user stored at the backend (describes inputs/outputs to the process, not how that process works.)

 - GET /process_graphs/{graph_id}
   - id and process graph returned, displays steps to the process in more detail.

 - GET /result

### Server-side processing
See the following repositories which should assist with setting up server-side processing.
 - Process graph parsing: https://github.com/Open-EO/openeo-pg-parser-networkx
 - Dask-friendly process registry: https://github.com/Open-EO/openeo-processes-dask/tree/main

## L1 Minimal Compliance
Ensures that the openEO implementation has a minimal set of functionality which allow users to execute basic use-cases.

https://openeo.org/documentation/1.0/developers/profiles/api.html#requirements-per-profile

https://openeo.org/documentation/1.0/developers/api/reference.html#tag/Capabilities/operation/capabilities

## Possible Approaches

### DataPoint Integration
 - compliant STAC API with openEO minimal requirements.
 - load an openEO datacube and perform any and all selections/filterings.
 - openEO cube records processes to act on the data.

Options:
 - give the openEO cube to DataPoint (clientside), applying all selections and returning an xarray dataset. Would be able to open the dataset remotely and perform client-side processes. (BELOW MINIMAL FUNCTIONALITY)
 - set up server-side architecture to handle process functions and tasks computed on the data before sending data to the user. (How to send the data once processed?) - can use DataPoint functionality or otherwise to open specific formats.


## Questions for ESA

 - Is it a strict requirement for an openEO-compliant API endpoint to provide server-side processing and parallel/job deployments?
 - 