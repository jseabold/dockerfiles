FROM debian:jessie
MAINTAINER Skipper Seabold 

RUN apt-get update -q && \
    apt-get -y --no-install-recommends install \
        texlive-base texlive-bibtex-extra texlive-extra-utils \
        texlive-generic-recommended texlive-latex-base \
        texlive-latex-recommended \
        texlive-fonts-recommended texlive-font-utils \
        texlive-fonts-extra \
        texlive-latex-extra texlive-math-extra texlive-pictures \
        texlive-pstricks texlive-science \
        perl-tk purifyeps chktex latexmk dvipng dvidvi \
        fragmaster lacheck latexdiff libfile-which-perl dot2tex \
        tipa latex-xcolor latex-beamer prosper pgf \
        python-pygments gnuplot

RUN apt-get -y --no-install-recommends install \
        lmodern

VOLUME ["/output"]
WORKDIR /output
ENTRYPOINT ["/usr/bin/pdflatex"]
CMD []
