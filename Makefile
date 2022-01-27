
wd?=$(shell pwd)
PP?=$(wd)

volume_mapping=-v $(PP)/features:/acre/features -v $(PP)/etc:/acre/etc -v $(wd)/steps:/acre/acre-steps -v $(PP)/steps:/acre/project-steps -v $(PP)/reports:/acre/reports -v $(PP)/lib:/acre/project-lib -v $(wd)/lib:/acre/acre-lib

port_mapping=-p 9900:9900

dopts=$(volume_mapping) \
	  $(port_mapping)


dockername=acre-run
image=acre
dockerrun=docker run -e TERM -it -h $(dockername) $(dopts) $(image) 
TAGS?=regression

FEATURES?=features/

default: userrun

userrun: prepare
	$(dockerrun) bash -c "FEATURES=$(FEATURES) TAGS='--tags $(TAGS)' userrun"

idock: prepare
	$(dockerrun) idock
	
selftest: prepare
	$(dockerrun) selftest

prepare: $(image).image
	mkdir -p reports/


acre.image: docker/Dockerfile
	@docker build -t acre docker/
