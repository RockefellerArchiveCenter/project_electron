## Rockefeller Archive Center Data Modeling Bibliography

Compiled by Patrick Galligan

February 10, 2017

**Introduction**

On August 23rd, 2016, the Rockefeller Archive Center announced its partnership with Marist College to develop and implement a sustainable platform capable of supporting and integrating archival management systems that help us care for digitized and born-digital materials. It is our firm belief that there is no magic bullet for managing digital records in archives and that our best bet would be to create a system that can connect our disparate systems into a single workflow. The systems implemented as part of the project will be compatible with existing archival standards and best practices, and will be built using well-documented, open-source technologies and user-centered design methodologies, so that components can be widely shared and deployed by other institutions.

We quickly realized that we would have to model archival data as part of our systems integration process, but none of us had any experience with data modeling before. To aid us, we performed a broad review of readings about data modeling, linked data, and archival data. I am sure we have missed some readings, but we feel confident that we have gained enough background information to make the right modeling decisions for our institution. This bibliography is also available as a [Zotero library](https://www.zotero.org/groups/d-team_readings/items/collectionKey/C487VG6E).

**Bibliography**

**Database Normalization**

Hillyer, Mike. &quot;An Introduction to Database Normalization.&quot; Retrieved from [http://mikehillyer.com/articles/an-introduction-to-database-normalization/](http://mikehillyer.com/articles/an-introduction-to-database-normalization/) on 6 February 2017.

- A nice, basic overview on normalizing databases and best practices for relational modeling of shared data. Originally published in 2003, but updated for 2016. Uses a simple example of a bookstore to talk about relational theory, keys, and defining relationships. It is somewhat entry-level, and you may know all of this if you have already worked with relational databases, but it is helpful for beginners.

Kent, William. &quot;A Simple Guide to Five Normal Forms in Relational Database Theory&quot;, Communications of the ACM 26(2), Feb. 1983, 120-125. Also, IBM Technical Report TR03.159, Aug. 1981. Also presented at SHARE 62, March 1984, Anaheim, California. Also in A.R. Hurson, L.L. Miller and S.H. Pakzad, Parallel Architectures for Database Systems, IEEE Computer Society Press, 1989.&quot;

[http://www.bkent.net/Doc/simple5.htm](http://www.bkent.net/Doc/simple5.htm)

- This article is apparently the original introduction to relational database theory and represents a guideline for relational database systems. Thinking about modeling in relational databases helps us with designing our model because the model will take the place of a database, but many of the underlying rules still apply. The article presents a simple and easy to understand explanation of different types of database normalization and redundancy.

**Existing Standards/Models**

Coyle, Karen. _FRBR, Before and After: A Look at Our Bibliographic Models_. Chicago: ALA Editions, an imprint of the American Library Association, 2016. Chapter 10.

[http://kcoyle.net/beforeAndAfter/c10-978-0-8389-1364-2.pdf](http://kcoyle.net/beforeAndAfter/c10-978-0-8389-1364-2.pdf)

- This is a broad chapter about bibliographic description in the semantic web in a larger book that frames the conversation around FRBR (Functional Requirements for Bibliographic Records) which was a 1998 recommendation from the IFLA. It starts talking about how we used to store data in databases, and then switches to how FRBR is represented in RDF. The article then gives a brief overview of the BIBFRAME model and other models with FRBR concepts. It may be too specific to FRBR for many of our needs, but there are many helpful graphs and diagrams to illustrate how the data model works and helps me think more abstractly about our records.

Europeana Data Model and Primer. 2013.

[http://pro.europeana.eu/files/Europeana\_Professional/Share\_your\_data/Technical\_requirements/EDM\_Documentation//EDM\_Primer\_130714.pdf](http://pro.europeana.eu/files/Europeana_Professional/Share_your_data/Technical_requirements/EDM_Documentation//EDM_Primer_130714.pdf)

- This document acts as a primer to the Europeana Data Model. It outlines the structured data model that Europeana uses for ingesting, managing, and publishing materials. It includes detailed RDF graphs for description, as well as rules for syntax and URL abbreviations. Ultimately, the EDM Primer is an in-depth look at the EDM, and could be super helpful to crib from when building a data model.

Ferro, Nicola and Silvello, Gianmaria. &quot;NESTOR: A Formal Model for Digital Archives.&quot; _Information Processing &amp; Management_. Vol. 49, Issue 6, November 2013. pp 1206-1240.

- This document details the NESTOR (Nested Sets Model) of digital archives. It is a pretty dry and detailed technical look at conceptual models for libraries and archives, and I sometimes found myself struggling to follow the terminology. While based in archival theory, this article was excessively technical and mathematic for me to make much sense of, but some might find this interesting. The end had some interesting points about the OAI-ORE data model explaining the metadata and associated digital object especially some OAI-ORE models that give examples of an archive comprised of descriptive metadata and related objects.

International Council on Archives Experts Group on Archival Description. _Records in Contexts: A Conceptual Model for Archival Description_. Consultation Draft v.0.1. September 2016.

[http://www.ica.org/sites/default/files/RiC-CM-0.1.pdf](http://www.ica.org/sites/default/files/RiC-CM-0.1.pdf)

- This document is the most recent draft of the Records in Context model that identifies and defines the primary descriptive entities of archival description and their relationships. The RiC conceptual model currently covers all core descriptive models except for control. This standard lists every entity, its description, scope, data type, and examples, and then lists its relation number, domain, name, and inverse for all RiC ontological elements.

Murray, Ronald J. &quot;The FRBR-Theoretic Library: The Role of Conceptual Data Modeling in Cultural Heritage Information System Design.&quot; 2008. [https://www.bl.uk/ipres2008/presentations\_day1/26\_Murray.pdf](https://www.bl.uk/ipres2008/presentations_day1/26_Murray.pdf)

- This paper deals less with the actual act of data modeling, or the data models themselves, and explores the role of data modeling in cultural heritage institutions. While this may seem unrelated at first, the author goes into detail on what makes a good data model, defines some basic types of data models, and offers critiques on past models, especially FRBR. While I could not draw a lot of information from this one, I did find the discussion on what makes a good data model interesting, as many other articles did not clearly lay that information out like Murray does.

PCDM. _Portland Common Data Model_. 2016. [https://github.com/duraspace/pcdm/wiki](https://github.com/duraspace/pcdm/wiki)

- We plan to draw heavily from the Portland Common Data Model for our data modeling efforts, so understanding its underlying model is essential for our process. PCDM is a general model designed for customization and generalizability by archives and libraries, which makes it perfect for our purposes. The Github wiki page includes domain model graphs, core classes, and everything else you would need to understand the model. This wiki is a must-read for anyone working with data models in archives.

**For Beginners**

Allemang, Dean and Hendler, Jim. _Semantic Web for the Working Ontologist: Effective Modeling in RDFS and OWL._ Burlington, MA: Morgan Kaufmann Publishers. 2008.

- Like the RDF book on this list, this is a top-to-bottom approach to data modeling with RDF. I found this the most in-depth and easy to understand explanation of ontological modeling that I read for this bibliography. The entire book is helpful, however for those that are just starting out with modeling, chapter 12, &quot;Good and Bad Modeling Practices&quot;, is a must-read to help avoid problems later down the line. The whole book is a lot to take in over one read, so it is definitely helpful to have handy as a reference for when modeling starts.

Bizer, Chris, Cyganiak, Richard, and Heath, Tom. &quot;How to Publish Linked Data on the Web.&quot; Retrieved from [http://wifo5-03.informatik.uni-mannheim.de/bizer/pub/LinkedDataTutorial/20070727/](http://wifo5-03.informatik.uni-mannheim.de/bizer/pub/LinkedDataTutorial/20070727/) on 6 February 2017.

- This tutorial offers a quick but in-depth look at the semantic web and RDF. After a general overview of the concept of Linked Data, it describes several practical ways to publishing information as Linked Data on the Web. I found this helpful in understanding RDF, how it works, and how to help it interact with relational databases and other systems.

Feigenbaum, Lee and Prud&#39;hommeaux, Eric. &quot;SPARQL by Example: A Tutorial.&quot; 2013. Retrieved from [http://www.cambridgesemantics.com/semantic-university/sparql-by-example](http://www.cambridgesemantics.com/semantic-university/sparql-by-example) on 6 February 2017.

- A short introduction to SPARQL and queries created by W3C SPARQL Working Group co-chair Lee Feigenbaum and W3C team member Eric Prud&#39;hommeaux. Great introduction to RDF and RDF datasets for anyone. Understanding the SPARQL query syntax helped me better understand how linked data actually works, and how data models affects those queries.

McGuinness, Deborah L. and Noy, Natalya F. ``Ontology Development 101: A Guide to Creating Your First Ontology&#39;&#39;. Stanford Knowledge Systems Laboratory Technical Report KSL-01-05 and Stanford Medical Informatics Technical Report SMI-2001-0880, March 2001.

  [http://www.ksl.stanford.edu/people/dlm/papers/ontology-tutorial-noy-mcguinness.pdf](http://www.ksl.stanford.edu/people/dlm/papers/ontology-tutorial-noy-mcguinness.pdf)

- This Stanford University-generated document provides a general overview to creating an ontology for the first time. It is a great resource for background information on ontologies, how they work, and how to create them in a standardized manner. According to EGAD, this is required reading for anyone looking to work with conceptual model, especially for newcomers.

Powers, Shelley. _Practical RDF_. Sebastopol, CA: O&#39;Reilly &amp; Associates, Inc. 2003.

- This book is a top-to-bottom exploration of RDF. The first half of the book focuses on the uses of RDF, how to structure triples, namespaces, and the other technical elements that make up RDF, and the last half talks about how to query RDF, different specifications, making your own ontology, and current examples of RDF in commercial products (Mozilla, etc.). I have always found the O&#39;Reilly books well written and easy to understand, and this one is no exception. While not strictly about data modeling, the information about RDF is extremely helpful in thinking about our ontological work, especially the chapter on ontologies.

Tillman, Ruth Kitchin. &quot;An Introduction to RDF for Librarians (of a Metadata Bent).&quot; 20 March 2016. Retrieved from: [http://ruthtillman.com/introduction-rdf-librarians-metadata/](http://ruthtillman.com/introduction-rdf-librarians-metadata/)

- This post is a great introduction to RDF structure, Turtle, and ontologies by a librarian working with linked data. This was the first article about RDF that I ever read, and it served as a great jumping off point for further reading. Well laid out and explained in an understandable way. I would recommend this post for any RDF newbies.

**Linked Data in Archives and Libraries**

Angjeli, Anila. &quot;Archives and Linked Open Data: Are Our Tools Ready to Complete the Picture?&quot; Presented at the Society of American Archivists Annual Meeting 2012.

[http://files.archivists.org/conference/sandiego2012/401-Angjeli.pdf](http://files.archivists.org/conference/sandiego2012/401-Angjeli.pdf)

- This presentation provides an agent-focused look at linked data, specifically EAC-CPF and SNAC. It is a bit tough to tell what the presenter was talking about in each case because I do not have the script to the presentation, but there are examples of data models inspired by FRBR, as well as the presenter&#39;s data represented in RDF.

CBPS. &quot;Relationship in archival descriptive systems&quot;. 2012.

[http://www.ica.org/en/cbps-relationship-archival-descriptive-systems](http://www.ica.org/en/cbps-relationship-archival-descriptive-systems)

- This brief document outlines the ICA&#39;s best practices and standards regarding descriptive relationships in archival systems. This document lays out examples of relationships, mandatory elements, relationship areas, and more. It could be extremely helpful while attempting to visualize your data modeling.

Frew, James, Janée, Greg and Mathena, Justin. &quot;A Data Model and Architecture for Long-term Preservation.&quot; Pittsburgh, PA: JCDL &#39;08 Proceedings of the 8th ACM/IEEE-CS joint conference on Digital libraries. 2008

        [http://www.ngda.org/research/Tech%20Arch/jcdl-paper.pdf](http://www.ngda.org/research/Tech%20Arch/jcdl-paper.pdf)

- In this paper the authors describe an archive architecture that provides a minimal approach to the long-term preservation of digital objects based on co-archiving of object semantics, uniform representation of objects and semantics, explicit storage of all objects and semantics as files, and abstraction of the underlying storage system. While the article and project primarily deals with extremely large datasets (geospatial data), I think many of the lessons are important, specifically the preservation of context. The authors also include various data model diagrams, which are helpful in thinking about the archival object model.

Gueguen, Gretchen, Manoel Marques da Fonseca, Vitor, Pitti, Daniel and Sibille-de Grimouard, Claire. &quot;Toward an International Conceptual Model for Archival Description: A Preliminary Report from the International Council on Archives&#39; Experts Group on Archival Description.&quot; _The American Archivist_. Vol. 76, No. 2, 2013. pp 566-583.

[http://americanarchivist.org/doi/pdf/10.17723/aarc.76.2.p071x02401282qx2](http://americanarchivist.org/doi/pdf/10.17723/aarc.76.2.p071x02401282qx2)

- While not particularly in-depth regarding conceptual models, this paper gives background information about the creation of EGAD from ICA and the context in which it exists.

Linked Data for Archives Focus Group Report (DRAFT). 2016

[https://docs.google.com/document/d/1N7UYAbFeoSY-vt8FfKZEMBiDcIjeunHUV73pmGT6WhE/edit#heading=h.dpge4oe7yhez](https://docs.google.com/document/d/1N7UYAbFeoSY-vt8FfKZEMBiDcIjeunHUV73pmGT6WhE/edit#heading=h.dpge4oe7yhez)

- Report based on surveys and conversations conducted by Zepheira and Atlas Systems. This report provides an overview of findings, along with a summary of the next steps that arose from the focus group discussions. The major findings seem a bit suspect, and don&#39;t have much depth to them at this point in time, however, there was some good information about more support for EAC-CPF, which we also definitely want to be able to incorporate into our description going forward.

Morgan, Eric Lease. &quot;Linked Archival Metadata.&quot; 2014.

[http://infomotions.com/sandbox/liam/tmp/guidebook.pdf](http://infomotions.com/sandbox/liam/tmp/guidebook.pdf)

- This is more of a handbook than an article or chapter in a book because it covers so much information. It is hard to talk about everything, but the sections I found most interesting where the strategies for putting linked data into practice because they provide practical steps for multiple sizes of institutions with different levels of knowledge. Morgan also provides some handy links to linked data tools, like Mass RDF editors, and scripts that helped him with his work that may be worth checking out. Definitely worth a read.

Park, Ok Nam. &quot;Development for Linked Data for Archives in Korea.&quot; _D-Lib Magazine._ Vol. 21, Number 3 of 4, March/April 2015. [http://www.dlib.org/dlib/march15/park/03park.print.html](http://www.dlib.org/dlib/march15/park/03park.print.html)

- This research analyzed the data structure of the National Archives of Korea and how they created ontologies and turned their data into linked data. It includes some good points on data model principles and approaches into three &quot;stages&quot;. The authors started with an ISADG descriptive record, and then modeled to create _Record_ as a main class, with collection, series, file, and item as super or subclasses. They then include the structure for each section, its property type, the vocabulary they used, the level, and any notes. All this info is helpful for us in thinking about what vocabularies we want to use, and how they are connected in the overall data model. I found the proliferance of graphs and modeling images useful, as it is often hard to visualize the models when they are just text on a page.

Rubinstein, Aaron. _An RDF vocabulary for describing archival collections and the names associated with them_.

[https://github.com/rubinsztajn/archival/blob/master/arch.rdf](https://github.com/rubinsztajn/archival/blob/master/arch.rdf)

- This document is a Github repository that lays out common RDF properties used by libraries and archives. This could be a good resource to pull from when thinking about what ontologies to use in creating our data models. However, it hasn&#39;t been updated since 2017, so it&#39;s fairly out of date.

van Hooland, Seth and Verbough, Ruben. _Linked Data for Libraries, Archives, and Museums: How to clean, link and publish your metadata._ Facet Publishing, 2014. Chapter 2 &quot;Modelling&quot;.

[http://book.freeyourmetadata.org/chapters/1/modelling.pdf](http://book.freeyourmetadata.org/chapters/1/modelling.pdf)

- This article starts by putting linked data into context and explaining why data modeling is important to linked data. It then gives a brief history of data modeling efforts up to 2014, while reviewing different serialization formats as well as their pros and cons. The authors also cover relational database methodology and how that methodology applies to data models. They even address markup languages like HTML and CSS to explain what metadata is, and then pivot to namespaces. They also give a broad overview of RDF, how it uses URLs, and how important serialization is to linked data. Finally, the chapter ends with a lengthy case study of DBpedia data, and explores the possibilities and limitations of different linked data sources. This chapter is definitely worth a read because it gives a more in-depth look at the history of linked data, data models, and linked data in the context of libraries.
