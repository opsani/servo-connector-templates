IMAGE_NAME = "opsani/servo-templates:latest"

.PHONY: build
build:
	docker build -t $(IMAGE_NAME) .

.PHONY: clean
clean:
	@rm -rf ./build/*

.PHONY: run
run: build
	@mkdir -p ./build
	docker run -it -v $(CURDIR)/build:/build \
		-e SERVO_SKIP_DEPS=true \
		$(IMAGE_NAME) $(COOKIECUTTER_ARGS)

.PHONY: push
push: build
	docker push $(IMAGE_NAME)

# Convenience targets

.PHONY: assembly
assembly: export COOKIECUTTER_ARGS += "--directory=assembly"
assembly:
	@$(MAKE) run

.PHONY: connector
connector: export COOKIECUTTER_ARGS += "--directory=connector"
connector:
	@$(MAKE) run

.PHONY: all
all: clean
	# TODO: Should be a standard recursive make invocation
	@$(MAKE) assembly
	@$(MAKE) connector

.PHONY: all
test: export COOKIECUTTER_ARGS += "--no-input"
test: all
