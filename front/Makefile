# +----------------------------------------------------------------------+
# | Alert Logic LRAT User Interface |
# +----------------------------------------------------------------------+
# | Copyright (c) 2015 AlertLogic, Inc. |
# +----------------------------------------------------------------------+
# | Author: John Diaz <jdiaz@alertlogic.com> |
# +----------------------------------------------------------------------+
#
# Usage examples:
#
# make clean
# make package
# make all
# make rpm

NAME = soc_ui_template
NAME_PRE =
NAME_POST =
LOCATION = /var/alertlogic/soc/soc_ui_template
LOCATION_PRE =
LOCATION_POST =

all: clean package

clean:
	rm -f ./*.deb

package:
	fakeroot dpkg-deb --build ./build ./

rpm:
	rm -f ./*.rpm

	mkdir -p rpmbuild/BUILD
	mkdir -p rpmbuild/RPMS
	mkdir -p rpmbuild/SOURCES
	mkdir -p rpmbuild/SPECS
	mkdir -p rpmbuild/SRPMS
	mkdir -p rpmbuild/tmp


	npm -v
	node -v
	which npm
	which node
	echo $PATH
	rm -rf node_modules
	npm install
	npm run build:prod
	mv build.spec rpmbuild/SPECS/build.spec
	mv package.json rpmbuild/BUILD/
	mv run.sh rpmbuild/BUILD/
	mv dist rpmbuild/BUILD/
	mv src/index.html rpmbuild/BUILD/

	tar czf rpmbuild/SOURCES/build.tar.gz --exclude='node_modules' rpmbuild/BUILD
	rpmbuild -ba --define "_topdir `pwd`/rpmbuild" \
					--define "_version $(RPM_VERSION)" \
					--define "_NAME $(NAME_PRE)$(NAME)$(NAME_POST)" \
					--define "_LOCATION $(LOCATION_PRE)$(LOCATION)$(LOCATION_POST)" \
					--define "_release $(RPM_RELEASE)" \
					rpmbuild/SPECS/build.spec

	mkdir final
	rm -rf final/*

	cp rpmbuild/RPMS/x86_64/* final
