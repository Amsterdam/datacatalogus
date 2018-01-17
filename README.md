# datacatalogus

Amsterdams eigen implementatie van het [datacatalog-core](https://github.com/Amsterdam/datacatalog-core) project, 
alle code en configuratie specifiek voor Amsterdam en Datapunt is terug te vinden in dit project

### datacatalog-core als submodule

Het datacatalog-core project is als een git [submodule](https://github.com/blog/2104-working-with-submodules)
bijgesloten. Dat vereist bij checkout de `--recursvie` vlag:

	$ git clone --recursive git@github.com:Amsterdam/datacatalogus.git
	
Wijzigingen in het datacatalog-core project komen niet automatisch in dit project, die moet je expliciet meenemen:

	$ git submodule update --recursive --remote
	
### import legacy data

Bij startup downloadt de docker meteen de legacy data van de huidige datapunt implementatie.

(Zie `Dockerfile` in de root van dit project, en `import/get_packages`)
