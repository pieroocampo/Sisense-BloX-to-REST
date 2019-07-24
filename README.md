# Sisense-BloX-to-REST
A simple pass through service built on Bottle to call the Sisense REST API from BloX widgets

## Why, Though?
Sisense BloX widgets are a simple way to make Sisense dashboards actionable. I thought it would make a cool demo to call the Sisense REST API directly from a BloX widget. This small service deals with the challenges of converting the BloX form input to a payload usable by the REST API:

* BloX only supports POST actions, but I'd like to demo other methods (GET, PUT, DELETE, etcetera)
* BloX sends data as a form. The service encapsulates taking the json from the form, cleaning it up, and dumping it into a JSON object ready to send to the REST API
* Most calls require previous authentication. The service provides a single call to perform both the authentication and the desired operation

## Dependencies
This tiny service uses Bottle, so you'll need that :) 

`pip install json`
`pip install bottle`

## Use
Run the script. Test by going to /hello on a browser
