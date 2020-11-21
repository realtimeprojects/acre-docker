
wd?=$(shell pwd)

volume_mapping=-v $(wd)/tests:/pantest/tests -v $(wd)/steps:/pantest/radish -v $(wd)/reports:/pantest/reports

dopts=$(volume_mapping)

dockername=pantest-run
image=pantest
dockerrun=docker run -h $(dockername) $(dopts) -it $(image) 

FEATURES=tests/basic/helloworld.feature

default: userrun

userrun: prepare
	$(dockerrun) bash -c "FEATURES=$(FEATURES) userrun"

idock: prepare
	$(dockerrun) idock
	
selftest: prepare
	$(dockerrun) selftest

prepare: $(image).image
	mkdir -p reports/


%.image: docker/%
	@docker build -t $*  docker/$*
