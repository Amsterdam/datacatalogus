# datacatalogus

Amsterdams eigen implementatie van het [datacatalog](https://github.com/Amsterdam/datacatalog) project, 
alle code en configuratie specifiek voor Amsterdam en Datapunt is terug te vinden in dit project

### datacatalog als submodule

Het datacatalog project is als een git [submodule](https://github.com/blog/2104-working-with-submodules) bijgesloten. 
Dat vereist bij checkout de `--recursvie` vlag:

	$ git clone --recursive git@github.com:Amsterdam/datacatalogus.git
	
Wijzigingen in het datacatalog project komen niet automatisch in dit project, die moet je expliciet meenemen:

	$ git pull --recurse-submodules
	
