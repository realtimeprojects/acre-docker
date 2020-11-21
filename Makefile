
wd?=$(shell pwd)

volume_mapping=-v $(wd)/tests:/pantest/tests -v $(wd)/steps:/pantest/radish

dopts=$(volume_mapping)

dockername=pantest
dockerimage=pantest
dockerrun=docker run -h $(dockername) $(dopts)

default: idock

idock:
	@docker build -t $(dockerimage) docker/$(dockerimage)
	$(dockerrun) -it $(dockerimage) interactive
