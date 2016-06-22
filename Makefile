#Makefile to build the website using hugo
all:build

build:
	hugo -t HugoMDL

publish:
	echo publishing website

show:
	hugo server --baseURL public/
