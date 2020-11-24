
wd?=$(shell pwd)
PP?=$(wd)

volume_mapping=-v $(PP)/features:/acre/features -v $(wd)/steps:/acre/radish/acre -v $(PP)/steps:/acre/radish/project -v $(PP)/reports:/acre/reports
port_mapping=-p 9900:9900

dopts=$(volume_mapping) \
	  $(port_mapping)


dockername=acre-run
image=acre
dockerrun=docker run -h $(dockername) $(dopts) -it $(image) 
TAGS?=regression

FEATURES?=features/

default: userrun

userrun: prepare
	$(dockerrun) bash -c "FEATURES=$(FEATURES) TAGS=$(TAGS) userrun"

idock: prepare
	$(dockerrun) idock
	
selftest: prepare
	$(dockerrun) selftest

prepare: $(image).image
	mkdir -p reports/


acre.image: docker/Dockerfile
	@docker build -t acre docker/
