
wd?=$(shell pwd)

volume_mapping=-v $(wd)/docker/pantest:/pantest

dopts=
# $(volume_mapping)

dockername=pantest
dockerimage=pantest
dockerrun=docker run -h $(dockername) $(dopts)

default: idock

idock:
	@docker build -t $(dockerimage) docker/$(dockerimage)
	$(dockerrun) -it $(dockerimage) interactive
