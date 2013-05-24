# application verison
VERSION = nightly

# generally the prefix to the directory
PREFIX = /ms4w/apps/geomoose2/

# output directory for scripts
TEMP = /ms4w/tmp/ms_tmp/

# url path is the root of the installation
URLPATH = /geomoose2/

# default projection
PROJECTION = EPSG:900913

# root path to mapfiles
MAPFILE_ROOT = /ms4w/apps/geomoose2/maps/


all:
	@echo "*****************************************************************"
	@echo "There is no code to compile for GeoMOOSE, please run 'make install'"
	@echo "to install geomoose to /ms4w/apps/geomoose2/"
	@echo "*****************************************************************"

install:
	mkdir -p /ms4w/apps/geomoose2//htdocs
	mkdir -p /ms4w/apps/geomoose2//conf

	mkdir -p /ms4w/apps/geomoose2/maps/

	cp -r maps/* /ms4w/apps/geomoose2/maps/
	cp -r htdocs/* /ms4w/apps/geomoose2//htdocs
	cp -r conf/* /ms4w/apps/geomoose2//conf

	cp geomoose2_httpd.conf /ms4w/apps/geomoose2/

	@echo "To finish installation you much include /ms4w/apps/geomoose2//geomoose2_httpd.conf in your Apache configuration"

MS4W_APP_DIR = ms4w_pkg_build/ms4w/apps/geomoose2

ms4w-prep:
	mkdir -p ms4w_pkg_build
	cp -r ms4w ms4w_pkg_build

	cp -r maps $(MS4W_APP_DIR)
	cp -r htdocs $(MS4W_APP_DIR)
	cp -r conf $(MS4W_APP_DIR)

	# Fix for ticket #76
	cp $(MS4W_APP_DIR)/conf/ms4w_local_settings.ini $(MS4W_APP_DIR)/conf/local_settings.ini

	# include some more of the info in the ms4w package
	cp README.txt $(MS4W_APP_DIR)
	cp LICENSE $(MS4W_APP_DIR)
ifeq ("$(VERSION)","nightly")
	cp NIGHTLY_VERSION.txt $(MS4W_APP_DIR) 2>&1 >/dev/null
endif

	cp -r art $(MS4W_APP_DIR)
	cp -r sphinx-docs $(MS4W_APP_DIR)
	cp -r tools $(MS4W_APP_DIR)
	rm -rf `find ./ms4w_pkg_build -name .svn`

ms4w-webmerc-prep: ms4w-prep
	grep -v "webmerc-lib" $(MS4W_APP_DIR)/htdocs/geomoose.html > $(MS4W_APP_DIR)/htdocs/geomoose_webmerc.html
	mv $(MS4W_APP_DIR)/htdocs/geomoose_webmerc.html $(MS4W_APP_DIR)/htdocs/geomoose.html

ms4w-package:
	find ./ms4w_pkg_build -name "*.in" -exec rm {} \;
	cd ms4w_pkg_build ; zip GeoMOOSE-$(VERSION)-MS4W.zip -r ms4w ; mv GeoMOOSE-$(VERSION)-MS4W.zip .. 
	rm -rf ms4w_pkg_build

ms4w-dist: ms4w-prep ms4w-package

ms4w-webmerc-dist: ms4w-webmerc-prep ms4w-package
