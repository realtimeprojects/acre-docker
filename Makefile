
wd?=$(shell pwd)

volume_mapping=-v $(wd):/data

dopts=$(volume_mapping)

dockername=Pleiades1
dockerimage=pleiades
dockerrun=docker run -h $(dockername) $(dopts)

default: tests


tests:
	@docker build -t $(dockerimage) etc/docker/$(dockerimage)
	$(dockerrun) -it $(dockerimage) bin/testagent
