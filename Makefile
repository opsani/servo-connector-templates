IMAGE_NAME = "opsani/servo-templates:latest"

.PHONY: build
build:
	docker build -t ${IMAGE_NAME} .

.PHONY: clean
clean:
	@rm -rf ./build/*

.PHONY: run
run: build
	@mkdir -p ./build
	docker run -it -v $(CURDIR)/build:/build ${IMAGE_NAME} --directory=${TEMPLATE_SUBDIR} --no-input

.PHONY: push
push: build
	docker push ${IMAGE_NAME}

# Convenience targets

.PHONY: assembly
assembly:
	@$(MAKE) -e TEMPLATE_SUBDIR="assembly" run

.PHONY: connector
connector:	
	@$(MAKE) -e TEMPLATE_SUBDIR="connector" run

.PHONY: all
SUBDIRS = $(shell ls -d */)
all: clean
	# TODO: Should be a standard recursive make invocation
	@$(MAKE) assembly
	@$(MAKE) connector
