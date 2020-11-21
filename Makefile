
wd?=$(shell pwd)

volume_mapping=-v $(wd)/tests:/pantest/tests -v $(wd)/steps:/pantest/radish

dopts=$(volume_mapping)

dockername=pantest-run
image=pantest
dockerrun=docker run -h $(dockername) $(dopts)

default: idock

testrun: pantest.image
	$(dockerrun) -it $(image) testrun

idock: pantest.image
	$(dockerrun) -it $(image) idock
	
run: $(image).image


%.image: docker/%
	@docker build -t $*  docker/$*
