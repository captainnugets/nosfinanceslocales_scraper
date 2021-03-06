Localgouv
=========

This project aims at scraping financial data of cities (="communes"), EPCI
(group of cities Cf. [wikipedia](http://fr.wikipedia.org/wiki/%C3%89tablissement_public_de_coop%C3%A9ration_intercommunale)), department and regions from the website
http://www.collectivites-locales.gouv.fr/.

We used scrapy lib to crawl the page and xpaths stuff to scrap data.

To check the quality of the crawling and to analyze data, we use ipython
notebooks:
 * [analysis of data from cities in 2012](http://nbviewer.ipython.org/urls/raw.github.com/fmassot/localgouv_scraper/master/notebooks/localgouvdata_analysis.ipynb)
 * [analysis of data from epci from 2007 to 2012](http://nbviewer.ipython.org/urls/raw.github.com/fmassot/localgouv_scraper/master/notebooks/epcidata_analysis.ipynb)
 * [analysis of data from departments from 2008 to 2012](http://nbviewer.ipython.org/urls/raw.github.com/fmassot/localgouv_scraper/master/notebooks/department_analysis.ipynb)
 * [analysis of data from regions from 2008 to 2012](http://nbviewer.ipython.org/urls/raw.github.com/fmassot/localgouv_scraper/master/notebooks/region_analysis.ipynb)


All the data scraped for the regions is committed as an example here:
 * with variable names as header: [scraped_data/region_all.csv](scraped_data/region_all.csv)
 * with french header: [nosdonnees/region_all.csv](nosdonnees/region_all.csv)


Usage
=====

To scrap data of a give zone type (city, epci, department or region) on a given fiscal
year YYYY, run in the root dir:

`scrapy crawl localgouv -o scraped_data_dir/zonetype_YYYY.json -t csv -a year=YYYY`

To scrap data for all available fiscal years for a given zone type:

`source bin/crawl_all_years.sh zonetype`

To generate a csv file with all data for a given zonetype and with french
header, run:

`source bin/bundle_data.sh zonetype`

This command will generate a file in nosdonnees/zonetype_all.csv which you can
upload on [nosdonnees.fr](http://www.nosdonnees.fr) website.



Requirements
===========
[See requirements.txt file.](requirements.txt)


Tests
=====

`unit2 discover`

TODO
====
 * Add some docs, especially indicate the mapping between variable names and
   fields in html pages.
 * Get simple stats on scraped data to check its quality (partly made for
   cities and epci).
 * Add some tests on different fiscal years.


