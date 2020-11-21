
wd?=$(shell pwd)

volume_mapping=-v $(wd)/tests:/pantest/tests -v $(wd)/steps:/pantest/radish -v $(wd)/reports:/pantest/reports

dopts=$(volume_mapping)

dockername=pantest-run
image=pantest
dockerrun=docker run -h $(dockername) $(dopts) -it $(image) 

features=tests/basic/helloworld.feature

default: user-run

user-run: prepare
	$(dockerrun) testrun radish $(features)

idock: prepare
	$(dockerrun) idock
	
selftest: prepare
	$(dockerrun) selftest

prepare: $(image).image
	mkdir -p reports/


%.image: docker/%
	@docker build -t $*  docker/$*
