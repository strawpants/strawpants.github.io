#Makefile to build the website using hugo
all:build

build:
	hugo -t HugoMDL
	
publish:
	@echo 'Publishing website to http://strawpants.github.io'
	#git subtree push --prefix=public publish master
show:
	@echo 'running test server, visit http://localhost:1313 to preview the page'
	hugo server --baseURL public/

clean:
	rm -rf public/*
