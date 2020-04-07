printer-pdf:
	cd printer \
	; ls  | grep [.]md$$ \
	| xargs -I% bash -x -c "\
	docker run --rm --volume `pwd`:/data \
	--user `id -u`:`id -g` pandoc/latex \
	% -o %.pdf '-fmarkdown-implicit_figures -o' \
	--from=markdown \
	-V geometry:margin=.4in \
	--toc --highlight-style=espresso"
