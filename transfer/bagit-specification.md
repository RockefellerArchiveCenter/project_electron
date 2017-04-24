# Rockefeller Archive Center BagIt Specification

```
{
     "BagIt-Profile-Info":{
      "BagIt-Profile-Identifier":"http://rockarch.org/standards/bagit/transfer.json",
      "Source-Organization":"Rockarch.org",
      "Contact-Name":"Hillel Arnold",
      "Contact-Email":"harnold@rockarch.org",
      "External-Description":"BagIt profile for transfering content from donors to the RAC",
      "Version":"1.0"
   },
   "Bag-Info":{
      "Source-Organization":{
         "required":true,
         "values":[
            "Ford Foundation"
         ]
      },
      "External-Identifier":{
        "required":true,
        "values":[
          "8a8efcc33e364c8eab03191ff66f8d26"
        ]
      },
      "Internal-Sender-Description":{
         "required":true,
         "values":[
           "Administrative records from 1990-1995."
         ]
      },
      "title":{
        "required":true,
        "values":[
          "Administrative Records"
        ]
      },
      "date-start":{
        "required":true,
        "values":[
          "1990-01-01"
        ]
      },
      "date-end":{
        "required":true,
        "values":[
          "1995-12-31"
        ]
      },
      "record-creators":{
        "required":true,
        "values":[
        "Ford Foundation",
        "Ford Foundation - Office of Administrative Affairs"
        ]
      },
      "record-type":{
        "required":true,
        "values":[
          "administrative records",
          "board materials"
        ]
      },
      "language":{
        "required":true,
        "values":[
          "http://id.loc.gov/vocabulary/iso639-2/eng.html",
          "http://id.loc.gov/vocabulary/iso639-2/ger.html"
        ]
      },
      "restrictions":{
        "required":false,
        "values":[
          "All materials are restricted for 10 years from date of creation."
        ]
      },
      "Bagging-Date":{
         "required":true
      },
      "Payload-Oxum":{
         "required":true
      }
   },
   "Manifests-Required":[
      "md5"
   ],
   "Allow-Fetch.txt":false,
   "Serialization":"optional",
   "Accept-Serialization":[
      "application/zip"
   ],
   "Accept-BagIt-Version":[
      "0.96"
   ]
}
```
