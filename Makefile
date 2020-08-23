IMAGE_NAME = "opsani/servo-connector-templates:latest"

.PHONY: build
build:
	echo "building container image ${IMAGE_NAME}..."
	docker build -t ${IMAGE_NAME} .

.PHONY: run
run: build
	echo "generating connector to ./build"
	mkdir -p ./build
	cd ./build && docker run -it -v $(pwd):/connector ${IMAGE_NAME}

.PHONY: push
push: build
	docker push ${IMAGE_NAME}
