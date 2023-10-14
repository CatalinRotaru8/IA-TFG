PYTHON_FILES := $(shell find . -name '*.py')

all: format check-format run clean

.PHONY: check-format format run clean

check-format:
	python3 -m black --check $(PYTHON_FILES)

format:
	python3 -m black $(PYTHON_FILES)

run:
	python3 -m src

clean:
	# rm -rf ./data/original_Data/*